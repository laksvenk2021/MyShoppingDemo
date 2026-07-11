#!/bin/bash
set -e

# Update system and install Python
if command -v yum >/dev/null 2>&1; then
  sudo yum update -y
  sudo yum install -y python3 python3-venv git
elif command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update -y
  sudo apt-get install -y python3 python3-venv python3-pip git
else
  echo "Unsupported package manager. Install Python 3 and git manually."
  exit 1
fi

# Clone repo if not present
if [ ! -d ".git" ]; then
  echo "Repository not found in current directory. Please clone the repository first."
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Start the API
nohup gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --log-level info \
  > /tmp/myshoppingdemo.log 2>&1 &

echo "API started on port 8000. Logs: /tmp/myshoppingdemo.log"
