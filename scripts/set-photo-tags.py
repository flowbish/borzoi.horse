#!/usr/bin/env python3

import json
import os
import sys
import tomllib

from r2 import R2Client


if len(sys.argv) < 2:
    print('Update objects in r2 with tags contaings the description and fragment from a gallery toml.')
    print(f'Usage: {sys.argv[0]} <gallery_toml>')
    sys.exit(1)

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
bucket_name = 'assets-borzoi-horse'
gallery_toml = sys.argv[1]

with open(gallery_toml, 'rb') as toml_file:
    toml = tomllib.load(toml_file)

for image in toml['images']:
    url = image['url']
    fragment = image['fragment']
    description = image['description']

    local_metadata = {}
    if fragment:
        local_metadata['fragment'] = fragment

    if description:
        local_metadata['description'] = description

    if url.startswith(url_prefix):
        object_key = url[len(url_prefix):]

        user_metadata = client.get_user_metadata(bucket_name, object_key)
        if user_metadata != local_metadata:
            print(f'Updating {object_key}: remote metadata {user_metadata} does not match {local_metadata}')
            tmp_key = f'{object_key}.tmp'
            client.copy_object(bucket_name, tmp_key, object_key, local_metadata)
            client.copy_object(bucket_name, object_key, tmp_key, local_metadata)
            client.delete_object(bucket_name, tmp_key)