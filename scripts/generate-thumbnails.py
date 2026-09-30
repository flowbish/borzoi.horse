#!/usr/bin/env python3

import json
import os
import sys
import tomllib

from typing import List
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

# Initialize the R2Client
client = R2Client(access_key=access_key, secret_key=secret_key, endpoint=endpoint)

url_prefix = 'https://assets.borzoi.horse/'
bucket = 'assets-borzoi-horse'

small_suffix = '-thumbnail'
small_size = (500, 500)

def is_image(head_object: HeadObject) -> bool:
    content_type = head_object.content_type()
    return content_type.startswith('image/')


def has_already_been_processed(head_object: HeadObject, all_objects: List[str]) -> bool:
    # this object is already small
    if head_object.key.endswith(f'{small_suffix}'):
        print(f'{head_object.key} is already small')
        return True

    # a small version of this object already exists
    small_key = f'{head_object.key}{small_suffix}'
    if small_key in all_objects:
        print(f'{small_key} already exists')
        return True

    return False

all_objects = client.list_objects(bucket)

for key in all_objects:
    head_object = client.head_object(bucket, key)
    if is_image(head_object) and not has_already_been_processed(head_object, set(all_objects)):
        contents = client.get_object(bucket, key)
        io = BytesIO(contents)
        img = Image.open(io)

        small_img = ImageOps.contain(img, small_size)
        small_io = BytesIO()
        small_img.save(small_io, 'jpeg')

        small_key = f'{head_object.key}{small_suffix}'

        print(f'Putting downscaled object {small_key}')
        user_metadata = {'exclude-from-gallery': 'true'}
        client.put_object(bucket, small_key, small_io.getvalue(), user_metadata=user_metadata)