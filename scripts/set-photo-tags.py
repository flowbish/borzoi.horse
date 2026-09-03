#!/usr/bin/env python3

import json
import os
import sys

from r2 import R2Client


if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <prefix>')
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

bucket_name = 'assets-borzoi-horse'
prefix = sys.argv[1]

for key in client.list_objects(bucket_name, prefix):
    if not (key.endswith('.jpg') or key.endswith('.png')):
        continue

    print(f'replacing {key}')

    tmp_key = f'{key}.tmp'
    client.copy_object(bucket_name, tmp_key, key, user_metadata={'horse': 'true'})
    client.copy_object(bucket_name, key, tmp_key, user_metadata={'horse': 'true'})
    client.delete_object(bucket_name, tmp_key)

    tags = client.get_user_metadata(bucket_name, key)
    print(f'{key}: {tags}')