# AWS DevOps Pipeline Demo

This project demonstrates a simple cloud-native CI/CD pipeline using a python app, containerized with docker and automated with GitHub Actions. It's designed to showcase modern DevOps practices.

## Tech Stack

- **python 3.13**: Basic "Hello, Devops World!" app
- **Docker**: Containerize the python app
- **GitHub Actions**: Automate build & deploy pipelines
-**AWS**: For deployment targets

## Setup

```bash
# Clone the repo
git clone https://github.com/saiakhil-devops/aws-devops-pipeline-demo.git
cd aws-devops-pipeline-demo

# Run Python app locally
cd app
python app.py
