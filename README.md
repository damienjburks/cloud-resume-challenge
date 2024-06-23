# Google Cloud - Cloud Resume API Challenge

![GitHub Actions](https://github.com/damienjburks/cloud-resume-challenge/actions/workflows/default.yml/badge.svg?style=flat)
![Terraform](https://img.shields.io/badge/Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

## Project Overview

This project is part of my GCP Cloud Resume Challenge, where I created and deployed a cloud-based resume using various Google
The Cloud Resume Challenge helped me demonstrate my skills in cloud computing and modern infrastructure as code practices. This project includes setting up a serverless function, a cloud storage bucket, and a NoSQL database to serve and manage my resume.

### Key Components and Google Cloud Services Used

1. **Google Cloud Storage**:
   - Used to store the static assets of the resume.
   - A bucket named `cloud-resume-src-bucket` is created to hold the source files.

2. **Google Cloud Functions**:
   - Serverless functions are used to manage backend logic.
   - A function named `cloud-resume` is created, with its source code located in the `serverless-src` directory and specified entry point `handler`.
   - The function uses the Python runtime version `python312`.

3. **Google Firestore**:
   - Firestore is used as a NoSQL database to store and manage resume data.
   - A Firestore database named `cloud-resume-nosql` is set up in the `nam5` location.

### Folder Structure

- `.github`: Contains GitHub-specific configurations.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `LICENSE`: Contains the project's license information.
- `README.md`: Provides an overview and instructions for the project.
- `main.tf`: Terraform configuration file defining the infrastructure setup.
- `outputs.tf`: Specifies the output values for the Terraform configuration.
- `provider.tf`: Configures the Google Cloud provider for Terraform.
- `serverless-src`: Contains the source code for the Google Cloud Function.
  - `assets`: Directory for static assets.
  - `main.py`: Main Python script for the serverless function.
  - `requirements.txt`: Lists the dependencies for the Python script.
- `tf-modules`: Directory containing Terraform modules used in the project.

### How to Get Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/damienjburks/cloud-resume-challenge.git
   ```

2. **Set Up Google Cloud Services**:
   - Ensure you have a Google Cloud account and the necessary permissions.
   - Configure your `gcloud` CLI with your project details.

3. **Deploy everything with Terraform**:
   - Initialize Terraform:

     ```bash
     terraform init
     ```

   - Apply the configuration:

     ```bash
     terraform apply
     ```

### Additional Resources

- [Cloud Resume API Challenge](https://cloudresumeapi.dev/)
- [JSON Resume](https://jsonresume.org/getting-started)
