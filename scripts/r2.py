import requests
import hmac
import hashlib
import datetime
import xml.etree.ElementTree as ET
import mimetypes
import urllib.parse

class R2Error(Exception):
    pass

class R2Client:
    """
    A client class for interacting with Cloudflare R2 storage with Python native packages.

    :param access_key: The access key for authentication.
    :param secret_key: The secret key for authentication.
    :param account_id: The account ID for the R2 storage.
    """

    def __init__(self, access_key, secret_key, endpoint):
        self.access_key = access_key
        self.secret_key = secret_key
        self.endpoint = endpoint

    def sign(self, key, msg):
        """
        Sign a message using the provided key.

        :param key: The key used for signing.
        :param msg: The message to be signed.
        :return: The signed message digest.
        """
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def get_signature_key(self, key, date_stamp, region_name, service_name):
        """
        Generate a signature key based on the provided parameters.

        :param key: The secret key.
        :param date_stamp: The date stamp in the format 'YYYYMMDD'.
        :param region_name: The region name.
        :param service_name: The service name.
        :return: The generated signature key.
        """
        k_date = self.sign(('AWS4' + key).encode('utf-8'), date_stamp)
        k_region = self.sign(k_date, region_name)
        k_service = self.sign(k_region, service_name)
        k_signing = self.sign(k_service, 'aws4_request')
        return k_signing

    def create_request_headers_upload(self, bucket_name, file_key=None, extra_headers=None, payload_hash=None, method='PUT', content_type=None):
        service = 's3'
        region = 'auto'
        host = self.endpoint.split("://")[-1]

        t = datetime.datetime.utcnow()
        amz_date = t.strftime('%Y%m%dT%H%M%SZ')
        date_stamp = t.strftime('%Y%m%d')

        canonical_uri = f'/{bucket_name}/{file_key}'
        canonical_querystring = ''
        

        amz_canonical_headers = {'x-amz-content-sha256': payload_hash, 'x-amz-date': amz_date,}

        if content_type:
            amz_canonical_headers['content-type'] = content_type

        for key, value in extra_headers.items():
            amz_canonical_headers[key] = value

        amz_canonical_headers_sorted = sorted([
            (key, value) for key, value in amz_canonical_headers.items()
        ])
        canonical_headers = [
            ('host', host),
            *amz_canonical_headers_sorted,
        ]
        canonical_headers_string = '\n'.join(f'{key}:{value}' for key, value in canonical_headers) + '\n'
        signed_headers_string = ';'.join(key for key, _ in canonical_headers)

        canonical_request = f"{method}\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers_string}\n{signed_headers_string}\n{payload_hash}"

        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"
        string_to_sign = f"{algorithm}\n{amz_date}\n{credential_scope}\n" + hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

        signing_key = self.get_signature_key(self.secret_key, date_stamp, region, service)
        signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

        authorization_header = f"{algorithm} Credential={self.access_key}/{credential_scope}, SignedHeaders={signed_headers_string}, Signature={signature}"

        headers = {
            'Authorization': authorization_header
        }

        if content_type:
            headers['Content-Type'] = content_type

        for key, value in amz_canonical_headers.items():
            headers[key] = value

        return headers

    def create_request_headers(self, method, bucket_name, copy_source=None, query_string=None, file_key=None, payload_hash=None, content_type=None):
        service = 's3'
        region = 'auto'
        host = self.endpoint.split("://")[-1]

        t = datetime.datetime.utcnow()
        amz_date = t.strftime('%Y%m%dT%H%M%SZ')
        date_stamp = t.strftime('%Y%m%d')

        canonical_uri = f'/{bucket_name}/' if file_key is None else f'/{bucket_name}/{file_key}'
        canonical_querystring = '' if query_string is None else query_string
        canonical_headers = f"host:{host}\nx-amz-date:{amz_date}\n"

        signed_headers = 'host;x-amz-date'
        if content_type:
            canonical_headers += f"content-type:{content_type}\n"
            signed_headers += ';content-type'

        if copy_source:
            signed_headers += ';x-amz-copy-source'

        payload_hash = payload_hash or hashlib.sha256(''.encode('utf-8')).hexdigest()
        canonical_request = f"{method}\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{payload_hash}"

        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"
        string_to_sign = f"{algorithm}\n{amz_date}\n{credential_scope}\n" + hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

        signing_key = self.get_signature_key(self.secret_key, date_stamp, region, service)
        signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

        authorization_header = f"{algorithm} Credential={self.access_key}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}"

        headers = {
            'x-amz-date': amz_date,
            'x-amz-content-sha256': payload_hash,
            'Authorization': authorization_header
        }

        if content_type:
            headers['Content-Type'] = content_type

        if copy_source:
            headers['x-amz-copy-source'] = copy_source

        return headers

    def get_content_type(self, path):
        mime_type, _ = mimetypes.guess_type(path)
        return mime_type if mime_type is not None else 'application/octet-stream'


    def upload_file(self, bucket_name, local_file_path, r2_file_key):
        file_url = f"{self.endpoint}/{bucket_name}/{r2_file_key}"

        with open(local_file_path, 'rb') as file:
            file_data = file.read()

        payload_hash = hashlib.sha256(file_data).hexdigest()
        mimetype = self.get_content_type(local_file_path)
        headers = self.create_request_headers_upload(bucket_name, r2_file_key, payload_hash, 'PUT', mimetype)

        response = requests.put(file_url, headers=headers, data=file_data)

        if response.ok:
            print(f"File {local_file_path} uploaded successfully as {r2_file_key}.")
        else:
            print(f"Failed to upload file {local_file_path}. Status code: {response.status_code}")
            print("Response Content:", response.text)


    def get_user_metadata(self, bucket, key):
        tags_url = f"{self.endpoint}/{bucket}/{key}"
        headers = self.create_request_headers('HEAD', bucket, file_key=key)

        response = requests.head(tags_url, headers=headers)

        if response.status_code != 200:
            raise R2Error(f'Failed to get tags for {bucket}/{key}: {response}')

        user_metadata = {}
        for header, value in response.headers.items():
            if header.startswith('x-amz-meta'):
                user_metadata[header.lstrip('x-amz-meta')] = value
        return user_metadata

    def copy_object(self, bucket, key, source, user_metadata=None):

        extra_headers = {}
        if user_metadata:
            for k, v in user_metadata.items():
                extra_headers[f'x-amz-meta-{k}'] = v

        extra_headers['x-amz-copy-source'] = f'{bucket}/{source}'
        extra_headers['x-amz-metadata-directive'] = 'MERGE'

        copy_url = f"{self.endpoint}/{bucket}/{key}"
        payload_hash = hashlib.sha256(b'').hexdigest()
        headers = self.create_request_headers_upload(bucket, file_key=key, extra_headers=extra_headers, payload_hash=payload_hash)

        response = requests.put(copy_url, headers=headers)

        if not response.ok:
            raise R2Error(f'Failed to copy to {bucket}/{key}: {response.text}')


    def delete_object(self, bucket, key):
        delete_url = f"{self.endpoint}/{bucket}/{key}"
        headers = self.create_request_headers('DELETE', bucket, file_key=key)

        response = requests.delete(delete_url, headers=headers)

        if not response.ok:
            raise R2Error(f'Failed to delete {bucket}/{key}: {response.text}')
        
    def download_file(self, bucket_name, file_key, local_file_name):
        """
        Download a file from the specified bucket.

        :param bucket_name: The name of the bucket.
        :param file_key: The key of the file to download.
        :param local_file_name: The local file name to save the downloaded file.
        """
        file_url = f"{self.endpoint}/{bucket_name}/{file_key}"
        headers = self.create_request_headers('GET', bucket_name, file_key=file_key)

        response = requests.get(file_url, headers=headers)

        if response.status_code == 200:
            with open(local_file_name, "wb") as file:
                file.write(response.content)
            print(f"File {file_key} downloaded successfully.")
        else:
            print(f"Failed to download file {file_key}. Status code: {response.status_code}")

    def list_objects(self, bucket_name, prefix=None):
        """
        List all files in the specified bucket.

        :param bucket_name: The name of the bucket.
        :return: A dictionary containing folder names as keys and lists of file names as values.
        """

        query_string = None
        quoted_query_string = None
        if prefix is not None:
            query_string = f"list-type=2&prefix={prefix}"
            quoted_prefix = urllib.parse.quote(prefix, safe='~')
            quoted_query_string = f"list-type=2&prefix={quoted_prefix}"

        headers = self.create_request_headers('GET', bucket_name, query_string=quoted_query_string)

        uri = f"{self.endpoint}/{bucket_name}/"
        if query_string is not None:
            uri += '?' + query_string

        response = requests.get(uri, headers=headers)

        if response.status_code == 200:
            root = ET.fromstring(response.content)
            objects = []
            for content in root.findall('{http://s3.amazonaws.com/doc/2006-03-01/}Contents'):
                key = content.find('{http://s3.amazonaws.com/doc/2006-03-01/}Key').text
                objects.append(key)

            return objects
        else:
            print(f"Failed to retrieve file list. Status code: {response.status_code}")
            return []
