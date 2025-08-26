# 🚀 AWS DevOps CI/CD Pipeline Demo

[![GHCR Push](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions/workflows/ghcr-push.yml/badge.svg?branch=main)](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions/workflows/ghcr-push.yml)
[![CodeQL](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions/workflows/codeql.yml)
[![Trivy](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions/workflows/trivy.yml/badge.svg?branch=main)](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions/workflows/trivy.yml)
[![Build Status](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

## Pull the image

1. **Authenticate to GHCR (first time only)**  
   *Skip this if your package is public.* Create a Personal Access Token with `read:packages` and log in:
   ```bash
   echo "$GHCR_TOKEN" | docker login ghcr.io -u saiakhil-devops --password-stdin
   
    # Latest
   
    docker pull ghcr.io/saiakhil-devops/aws-devops-pipeline-demo/app:latest

    # Or a specific version
   
    docker pull ghcr.io/saiakhil-devops/aws-devops-pipeline-demo/app:v0.1.0
    
    docker run --rm -p 5000:5000 ghcr.io/saiakhil-devops/aws-devops-pipeline-demo/app:latest

A professionally structured DevOps project demonstrating a complete **CI/CD pipeline** using **GitHub Actions**, **Docker**, and **Python**. This repository showcases key DevOps practices including code validation, containerization, automated testing, and deployment readiness — ideal for production and real-world corporate environments.

## 📁 Project Directory Structure

<details>
<summary><b>Click to expand</b></summary>

```text
aws-devops-pipeline-demo/
├─ app/                     # Python web application
│  └─ app.py
├─ tests/                   # Unit tests
│  └─ test_sample.py
├─ .github/
│  └─ workflows/
│     ├─ main.yml          # CI build & test
│     ├─ codeql.yml        # CodeQL static analysis
│     └─ trivy.yml         # Trivy image scan
├─ Dockerfile               # Docker image definition
├─ requirements.txt         # Python dependencies
└─ README.md                # Project documentation
```
</details> 

---

## 🧰 Technology Stack

| Category         | Tools Used                       |
|------------------|----------------------------------|
| Language         | Python 3.9                       |
| Version Control  | Git + GitHub                    |
| CI/CD Pipeline   | GitHub Actions                   |
| Testing          | Pytest                           |
| Code Quality     | Flake8, Black                    |
| Containerization | Docker                           |
| IDE              | VS Code / PyCharm                |

---

## ⚙️ CI/CD Pipeline Workflow

This project uses **GitHub Actions** to automate the following:

1. 🧾 Code checkout and Python setup  
2. 📦 Dependency installation  
3. ✅ Unit testing using `pytest`  
4. 🔍 Linting with `flake8` and formatting check with `black`  
5. 🐳 Docker image build  
6. 🛠️ Future: Container push & AWS deployment (coming soon)

**Trigger**: On every push or pull request to the `main` branch.

---

## 💻 Run Locally

```bash
# Clone the repository
git clone https://github.com/saiakhil-devops/aws-devops-pipeline-demo.git
cd aws-devops-pipeline-demo

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app/app.py
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

Run all tests inside the `tests/` folder and check output. For code coverage:

```bash
pytest --cov=app
```

---

## 🐳 Docker Support

```bash
# Build the Docker image
docker build -t aws-devops-demo .

# Run the container
docker run -p 5000:5000 aws-devops-demo
```

---

## 🚀 Roadmap & Future Enhancements

- [ ] Add AWS EC2/Fargate deployment automation
- [ ] Integrate Terraform for Infrastructure as Code (IaC)
- [ ] Set up DockerHub auto-push
- [ ] Add SonarQube for code quality reports
- [ ] Configure Slack/MS Teams pipeline alerts
- [ ] Multi-environment staging (dev/stage/prod)

---

## 👨‍💻 Author

**Sai Akhil Perumalla**  
🔹 AWS Certified | DevOps & Cloud Enthusiast | QA Engineer  
📍 Scarborough, Ontario  
📧 saiakhilperumallaofficial@gmail.com  
🔗 [GitHub](https://github.com/saiakhil-devops) | [LinkedIn](https://www.linkedin.com/in/sai-akhil-perumalla-0b473819b)

---

## 📄 License


This project is licensed under the [MIT License](LICENSE).

---

> 🔥 *This repository is crafted to align with real-world DevOps job requirements, showcasing hands-on experience with CI/CD pipelines, Dockerization, automated testing, and scalable workflows.*
