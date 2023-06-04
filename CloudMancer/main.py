from aws import aws_start_instance, aws_stop_instance, aws_upload_to_s3, aws_download_from_s3
from google_cloud import google_start_instance, google_stop_instance, google_upload_to_storage, google_download_from_storage
from azure import azure_start_vm, azure_stop_vm, azure_upload_to_storage, azure_download_from_storage

class CloudMancer:
    def __init__(self):
        pass

    def main(self):
        print("Welcome to the CloudMancer: Multi-Cloud Management System!")
        print("What cloud platform would you like to manage?")
        print("1. AWS")
        print("2. Google Cloud")
        print("3. Azure")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            self.aws_menu()
        elif choice == "2":
            self.google_cloud_menu()
        elif choice == "3":
            self.azure_menu()
        else:
            print("Invalid choice. Please try again.")

    def aws_menu(self):
        print("AWS Management Menu:")
        print("1. Start EC2 Instance")
        print("2. Stop EC2 Instance")
        print("3. Upload File to S3")
        print("4. Download File from S3")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            instance_id = input("Enter the EC2 instance ID to start: ")
            aws_start_instance(instance_id)
        elif choice == "2":
            instance_id = input("Enter the EC2 instance ID to stop: ")
            aws_stop_instance(instance_id)
        elif choice == "3":
            bucket_name = input("Enter the S3 bucket name: ")
            local_file_path = input("Enter the local file path: ")
            storage_file_name = input("Enter the storage file name: ")
            aws_upload_to_s3(bucket_name, local_file_path, storage_file_name)
        elif choice == "4":
            bucket_name = input("Enter the S3 bucket name: ")
            storage_file_name = input("Enter the storage file name: ")
            local_file_path = input("Enter the local file path: ")
            aws_download_from_s3(bucket_name, storage_file_name, local_file_path)
        else:
            print("Invalid choice. Please try again.")

    def google_cloud_menu(self):
        print("Google Cloud Management Menu:")
        print("1. Start Compute Engine Instance")
        print("2. Stop Compute Engine Instance")
        print("3. Upload File to Cloud Storage")
        print("4. Download File from Cloud Storage")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            instance_name = input("Enter the Compute Engine instance name to start: ")
            google_start_instance(instance_name)
        elif choice == "2":
            instance_name = input("Enter the Compute Engine instance name to stop: ")
            google_stop_instance(instance_name)
        elif choice == "3":
            bucket_name = input("Enter the Cloud Storage bucket name: ")
            local_file_path = input("Enter the local file path: ")
            storage_file_name = input("Enter the storage file name: ")
            google_upload_to_storage(bucket_name, local_file_path, storage_file_name)
        elif choice == "4":
            bucket_name = input("Enter the Cloud Storage bucket name: ")
            storage_file_name = input("Enter the storage file name: ")
            local_file_path = input("Enter the local file path: ")
            google_download_from_storage(bucket_name, storage_file_name, local_file_path)
        else:
            print("Invalid choice. Please try again.")

    def azure_menu(self):
        print("Azure Management Menu:")
        print("1. Start Virtual Machine")
        print("2. Stop Virtual Machine")
        print("3. Upload File to Storage Account")
        print("4. Download File from Storage Account")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            vm_name = input("Enter the virtual machine name to start: ")
            azure_start_vm(vm_name)
        elif choice == "2":
            vm_name = input("Enter the virtual machine name to stop: ")
            azure_stop_vm(vm_name)
        elif choice == "3":
            storage_account_name = input("Enter the Storage Account name: ")
            local_file_path = input("Enter the local file path: ")
            storage_file_name = input("Enter the storage file name: ")
            azure_upload_to_storage(storage_account_name, local_file_path, storage_file_name)
        elif choice == "4":
            storage_account_name = input("Enter the Storage Account name: ")
            storage_file_name = input("Enter the storage file name: ")
            local_file_path = input("Enter the local file path: ")
            azure_download_from_storage(storage_account_name, storage_file_name, local_file_path)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cloud_mancer = CloudMancer()
    cloud_mancer.main()
