# Craft Cloud asset sync

Python script for syncing AWS assets between Craft Cloud environments.

## Requirements

* python-dotenv

```sh
cp .env.example .env
```

## Setup

Obtain the AWS S3 CLI crendetials from Craft Console Projects > Access > Asset Storage > AWS CLI

These values are needed for the following environment variables:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION
* AWS_SESSION_TOKEN

The following path variables set the local and remote S3 paths for syncing

* S3_REMOTE_ASSETS_PATH - The S3 target e.g. s3://{asset_storage_uuid}/{environment_uuid}/assets/
* LOCAL_ASSETS_PATH - The local path to the folder of local assets usually this is the path to web/uploads

## Syncing

### Local sync (assets are synced from the remote S3 path to the LOCAL_ASSETS_PATH

```sh
python3 ./craft-cloud-aws-sync.py local
```

### Remote sync (assets are synced to the remote S3 path from the contents f the LOCAL_ASSETS_PATH

```sh
python3 ./craft-cloud-aws-sync.py remote
```