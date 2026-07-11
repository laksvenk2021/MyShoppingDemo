# MyShoppingDemo API

A Python REST API scaffold using FastAPI for AWS EC2 deployment.

## Features
- FastAPI application with CRUD endpoints for shopping items
- ASGI server support via Uvicorn/Gunicorn
- EC2 bootstrap script for deployment
- Simple configuration through environment variables

## Setup

1. SSH into your EC2 instance.
2. Update packages and install Python 3.11 (or later).
3. Clone this repository.
4. Create a Python virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run locally

```bash
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Production

Start with Gunicorn and Uvicorn workers:

```bash
./scripts/start_server.sh
```

## AWS EC2 Deployment

Use the provided EC2 bootstrap script to install dependencies, create a virtual environment, and start the API server:

```bash
sudo bash deploy/ec2_setup.sh
```

Then point your security group to allow inbound HTTP traffic on port 8000.
