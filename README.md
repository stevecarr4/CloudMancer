CloudMancer - Multi-Cloud Management System

CloudMancer is a powerful multi-cloud management system, offering a unified and streamlined approach to managing resources across major cloud platforms - AWS, Google Cloud, and Azure. With CloudMancer, managing cloud instances and data storage becomes a breeze, as you can start/stop instances, upload/download files to/from storage, and perform an array of management tasks, all in one place.

Features 🎯

CloudMancer comes loaded with features to manage resources on the following cloud platforms:

AWS Management
Start and stop EC2 instances
Upload and download files to/from S3
Google Cloud Management
Start and stop Compute Engine instances
Upload and download files to/from Cloud Storage
Azure Management
Start and stop Virtual Machines
Upload and download files to/from Storage Accounts
Getting Started 🚀

Here's a quick guide on how to install and set up CloudMancer:

Prerequisites
Ensure you have Python installed on your machine. CloudMancer runs on Python 3.7 and above.

Installation
Clone the CloudMancer repository to your local machine.

git clone https://github.com/your-username/CloudMancer.git

Install the required dependencies.
pip install -r requirements.txt
Configure your cloud provider credentials in the respective config files (aws.py, google_cloud.py, azure.py). Make sure to replace the placeholder values with your actual credentials.
Usage 💻

After setting up CloudMancer, here's how to use it:

Run the main.py script.
python main.py

You'll be presented with options to choose a cloud platform to manage.
Welcome to the CloudMancer: Multi-Cloud Management System!
What cloud platform would you like to manage?
1. AWS
2. Google Cloud
3. Azure
Enter your choice (1-3):
Follow the on-screen prompts to perform various management tasks specific to your chosen cloud platform.
Contribution ✨

Contributions to CloudMancer are warmly welcomed! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Check out the CONTRIBUTING.md file for more details on how to contribute.

License 📝

This project is licensed under the MIT License - see the LICENSE file for more details.

Acknowledgements 👏

CloudMancer leverages the power of several libraries to deliver its functionality:

boto3 - AWS SDK for Python
google-cloud-storage - Google Cloud Storage Client Library
azure-storage-blob - Azure Blob Storage Client Library
We're immensely grateful to the developers of these libraries!
