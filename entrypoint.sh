#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Apply database migrations
export PYTHONPATH="/app:/app/jobintel:$PYTHONPATH"
echo "Applying database migrations..."
python jobintel/manage.py migrate

# Then execute the command passed to this script (the CMD from Dockerfile or command from docker-compose.yml)
exec "$@"
