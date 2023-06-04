import boto3
from config import aws_access_key_id, aws_secret_access_key, aws_region

def aws_start_instance(instance_id):
    ec2 = boto3.client("ec2", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    ec2.start_instances(InstanceIds=[instance_id])

def aws_stop_instance(instance_id):
    ec2 = boto3.client("ec2", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    ec2.stop_instances(InstanceIds=[instance_id])

def aws_create_bucket(bucket_name):
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    s3.create_bucket(Bucket=bucket_name)

def aws_upload_to_s3(bucket_name, local_file_path, s3_file_name):
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    s3.upload_file(local_file_path, bucket_name, s3_file_name)

def aws_download_from_s3(bucket_name, s3_file_name, local_file_path):
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    s3.download_file(bucket_name, s3_file_name, local_file_path)

# Add other AWS-specific functions here
