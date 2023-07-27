# Cloud Share - File Sharing System

Cloud Share is a file sharing system built using Vue.js and Django Rest Framework that allows users to easily upload and share files with others. It provides a simple and efficient way to upload multiple files to the server, which then generates a unique link for each file set. When another user accesses this link, the server compresses all the uploaded files into a zip folder and initiates the download process.

## Features

User-friendly interface for easy file uploading and sharing.

Multiple files can be uploaded simultaneously.

Automatic generation of unique download links for each uploaded file set.

Downloading files in a convenient zip format.

Secure and efficient file handling with Vue.js and Django Rest Framework.

## Requirements
Before running Cloud Share, ensure you have the following installed:

Vue.js (for front-end)

Python 3 (for Django backend)

Django Rest Framework

Django

Virtual environment (optional but recommended)

## Installation and Setup
Clone the repository:

git clone https://github.com/your-username/cloud-share.git

cd cloud-share

python -m venv env  # Optional: Create a virtual environment

source env/bin/activate  # Optional: Activate the virtual environment

pip install -r requirements.txt

Configure the Django settings:

Create a .env file in the back-end directory and set the necessary environment variables like database configuration, secret key, etc.

Apply migrations and start the server:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Build and run the Vue.js front-end:



## Access the Cloud Share application:

Open your web browser and go to: http://localhost:8080/ (or any other port specified by the Vue.js server)

## Usage
Home Page: Upon accessing the application, users can see an interface to upload files.

Upload: Click on the "Upload" button to select and upload one or multiple files to the server.

Generate Link: After uploading, the server will generate a unique link for the uploaded file set.

Share Link: Share the provided link with others who want to download the files.

Download: When a user accesses the link, the server will serve the files as a zip folder for easy downloading.

## Contributing
Contributions to Cloud Share are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request on GitHub.


## Acknowledgments
We would like to thank all the contributors and the open-source community for their valuable contributions and support in building Cloud Share.

