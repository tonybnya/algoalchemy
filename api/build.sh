#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Install gunicorn for production server
pip install gunicorn

# Create the database directory if it doesn't exist
mkdir -p instance

# Initialize the database (if needed)
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()" 