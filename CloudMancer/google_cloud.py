from google.cloud import storage
from google.auth import compute_v1
from config import google_service_account_key_path, google_project_id

def google_start_instance(instance_name):
    try:
        compute_client = compute_v1.InstancesClient.from_service_account_json(google_service_account_key_path)
        project = google_project_id
        zone = "us-central1-a"
        instance = instance_name
        operation = compute_client.start(project=project, zone=zone, instance=instance)
        operation.result()
    except Exception as e:
        print(f"Error occurred while starting Google Cloud instance: {str(e)}")

def google_stop_instance(instance_name):
    try:
        compute_client = compute_v1.InstancesClient.from_service_account_json(google_service_account_key_path)
        project = google_project_id
        zone = "us-central1-a"
        instance = instance_name
        operation = compute_client.stop(project=project, zone=zone, instance=instance)
        operation.result()
    except Exception as e:
        print(f"Error occurred while stopping Google Cloud instance: {str(e)}")

def google_upload_to_storage(bucket_name, local_file_path, storage_file_name):
    try:
        storage_client = storage.Client.from_service_account_json(google_service_account_key_path)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(storage_file_name)
        blob.upload_from_filename(local_file_path)
    except Exception as e:
        print(f"Error occurred while uploading to Google Cloud Storage: {str(e)}")

def google_download_from_storage(bucket_name, storage_file_name, local_file_path):
    try:
        storage_client = storage.Client.from_service_account_json(google_service_account_key_path)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(storage_file_name)
        blob.download_to_filename(local_file_path)
    except Exception as e:
        print(f"Error occurred while downloading from Google Cloud Storage: {str(e)}")

# Testing the functions
def test_functions():
    instance_name = "example-instance"
    bucket_name = "example-bucket"
    local_file_path = "example-file.txt"
    storage_file_name = "example-file.txt"

    # Test Google Cloud functions
    google_start_instance(instance_name)
    google_stop_instance(instance_name)
    google_upload_to_storage(bucket_name, local_file_path, storage_file_name)
    google_download_from_storage(bucket_name, storage_file_name, local_file_path)

if __name__ == "__main__":
    test_functions()
