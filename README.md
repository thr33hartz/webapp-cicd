# Flask CI/CD WebApp

![Version](https://img.shields.io/badge/version-v1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-AWS%20ECR-blue?logo=docker)
[![CI/CD Pipeline](https://github.com/thr33hartz/webapp-cicd/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/thr33hartz/webapp-cicd/actions/workflows/ci_cd.yml)

This is a demo project built to practice DevOps skills:\
an **automated CI/CD pipeline** for a Flask application, with Docker image build, Amazon ECR push, and EKS deployment using GitHub Actions.

---

## Tech Stack

- **Backend**: Python 3.10, Flask 3.x, Gunicorn
- **CI/CD**: GitHub Actions (`workflow_call`, `buildx`, `modular workflows`)
- **Testing**: Manual or via local container health check
- **Infrastructure**: Docker, **AWS ECR**, **EKS**, Kubernetes, Helm
- **DevOps Practices**: multi-stage workflows, SHA-tagged images, health check

---

## Project Structure

```
├── webapp/              # Flask application
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt     # Production dependencies
├── helm-chart/          # Helm chart for K8s (EKS)
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
└── .github/workflows/   # CI/CD workflows (test, build-push, deploy, etc)
```

---

## CI/CD Workflows

The main pipeline is defined in `.github/workflows/ci.yml`.

### Flow:

1. **build-push** — builds Docker image with `buildx`, pushes to **ECR**
2. **health check** — checks container availability on port `5001`
3. **deploy** — deploys to **EKS** using Helm

---

## Docker

Base image:

```dockerfile
FROM python:3.10-slim
```

Highlights:

- Uses pip cache for faster builds
- Production server with Gunicorn:

```bash
CMD ["gunicorn", "-b", "0.0.0.0:5001", "webapp.app:app"]
```

`.dockerignore` excludes:

- `.git`, `.venv`, `__pycache__`, local/system files

---

## Helm Chart

Folder: `helm-chart/`

Templates:

- `deployment.yaml`, `service.yaml`, `ingress.yaml`
- Configured via `values.yaml`:

```yaml
 
```

---

## Commands

### Local development:

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
FLASK_DEBUG=true python webapp/app.py
```

### Docker:

```bash
docker build -t flask-app .
docker run -p 5001:5001 flask-app
```

---

## Triggering CI/CD

The `ci.yml` pipeline is triggered via:

- Manual dispatch (`workflow_dispatch`)
- Git tag push:

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

## Status

✔️ Fully working CI/CD with AWS ECR + EKS\
✔️ Health-checked container post-push\
✔️ Helm-based EKS deployment with image SHA tag\
✔️ Modular GitHub Actions pipeline\
✔️ Easy to test and extend