import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://search-mydomain-l2if7ee4caz2wurlatk63yed4q.us-east-1.es.amazonaws.com/'
region = 'us-east-1'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository
path = '_snapshot/my-snapshot-repo' # the Elasticsearch API endpoint
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": "mo-manual-es-snaps-bkt-001",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::767397755561:role/TheSnapshotRole"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)