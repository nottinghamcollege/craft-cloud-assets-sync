#!/usr/bin/env python
import os
import argparse
import subprocess
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Sync assets between local and remote storage.')
    parser.add_argument('sync_direction', type=str, choices=['local', 'remote'], help='Sync direction for asset syncing. e.g. local or remote', default='local')
    args = parser.parse_args()

    # AWS client keys for Craft Cloud
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_default_region = os.getenv('AWS_DEFAULT_REGION')
    aws_session_token = os.getenv('AWS_SESSION_TOKEN')

    if not all([aws_access_key_id, aws_secret_access_key, aws_default_region, aws_session_token]):
        raise EnvironmentError("One or more AWS S3 client variables are missing or invalid")

    # Environment path variables
    s3_remote_assets_path = os.getenv('S3_REMOTE_ASSETS_PATH')
    local_assets_path = os.getenv('LOCAL_ASSETS_PATH')

    if not all([s3_remote_assets_path, local_assets_path]):
        raise EnvironmentError("Local or remote path variables are not set.")

    # Construct the sync command
    if args.sync_direction == 'remote':
        sync_command = f'aws s3 sync {local_assets_path} {s3_remote_assets_path}'
    else:
        sync_command = f'aws s3 sync --delete {s3_remote_assets_path} {local_assets_path}'

    # Run the sync command
    result = subprocess.run(sync_command, shell=True, capture_output=True, text=True)

    # Check the result
    if result.returncode == 0:
        print("Sync completed successfully")
    else:
        print(f"Error during sync: {result.stderr}")

if __name__ == '__main__':
    main()
