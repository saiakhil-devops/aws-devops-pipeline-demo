# AWS DevOps Pipeline Demo

This project showcases a simple python app containerized with docker, illustrating modern Devops practices and automation readiness.

---

## Tech Stack
- **python 3.13**
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

----

## Continuous Integration

This project uses **GitHub Actions** to automatically build the docker image on every push to the `main` branch.
You can see the pipeline in action here: [Actions tab](https://github.com/saiakhil-devops/aws-devops-pipeline-demo/actions).


----

**Author**: [Sai Akhil Perumalla]
**GitHub**: [https://github.com/saiakhil-devops/aws-devops-pipeline-demo](https://github.com/saiakhil-devops/aws-devops-pipeline-demo)
