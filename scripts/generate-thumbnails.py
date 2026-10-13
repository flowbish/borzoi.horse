#!/usr/bin/env python3

import argparse
import json
import os
import sys
import tomllib
import concurrent.futures

from typing import List, Set
from io import BytesIO

from r2 import R2Client, HeadObject
from PIL import Image, ImageOps

# Load credentials from "credentials.json" in the form
# {
#   "R2_ACCESS_KEY_ID": "xxxxxx",
#   "R2_SECRET_ACCESS_KEY": "xxxxxxxxxxxxx",
#   "R2_ENDPOINT": "https://xxx.r2.cloudflarestorage.com"
# }
with open(os.path.join(os.path.dirname(__file__), 'credentials.json'), 'r') as credentials_file:
    credentials = json.load(credentials_file)

access_key = credentials['R2_ACCESS_KEY_ID']
secret_key = credentials['R2_SECRET_ACCESS_KEY']
endpoint = credentials['R2_ENDPOINT']

url_prefix = 'https://assets.borzoi.horse/'
bucket = 'assets-borzoi-horse'

small_suffix = '-thumbnail'
small_size = (500, 500)

def is_image(head_object: HeadObject) -> bool:
    content_type = head_object.content_type()
    return content_type.startswith('image/')

def key_is_thumbnail(key: str) -> bool:
    return key.endswith(small_suffix)


def has_already_been_processed(head_object: HeadObject, all_objects: Set[str]) -> bool:
    # a small version of this object already exists
    small_key = f'{head_object.key}{small_suffix}'
    if small_key in all_objects:
        return True

    return False

def maybe_downscale(key: str, all_objects: Set[str]):
    if key_is_thumbnail(key):
        return None

    client = R2Client(access_key=access_key, secret_key=secret_key, endpoint=endpoint)

    head_object = client.head_object(bucket, key)
    if is_image(head_object) and not has_already_been_processed(head_object, all_objects):
        contents = client.get_object(bucket, key)
        io = BytesIO(contents)
        img = Image.open(io)

        img = ImageOps.exif_transpose(img)

        img = ImageOps.contain(img, small_size, method=Image.Resampling.BICUBIC)
        img = img.convert("RGB")

        img_io = BytesIO()
        img.save(img_io, 'jpeg')

        small_key = f'{head_object.key}{small_suffix}'

        user_metadata = {'exclude-from-gallery': 'true'}
        client.put_object(bucket, small_key, img_io.getvalue(), user_metadata=user_metadata)

        return key


def delete_thumbnail(key):
    if not key_is_thumbnail(key):
        return None

    client = R2Client(access_key=access_key, secret_key=secret_key, endpoint=endpoint)
    client.delete_object(bucket, key)
    return key

def main(args: List[str]) -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument('action', choices=['generate', 'delete'])
    parser.add_argument('--prefix', required=False)

    args = parser.parse_args(args)


    client = R2Client(access_key=access_key, secret_key=secret_key, endpoint=endpoint)
    all_objects = client.list_objects(bucket, prefix=args.prefix)


    if args.action =='generate':
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(lambda key: maybe_downscale(key, set(all_objects)), all_objects)

        for key in results:
            if key is not None:
                print(f'downscaled {key}')
    elif args.action == 'delete':
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(delete_thumbnail, all_objects)

        for key in results:
            if key is not None:
                print(f'deleted {key}')
    else:
        print(f'invalid action specified: {args.action}')

if __name__ == '__main__':
    main(sys.argv[1:])