#!/usr/bin/env bash
# Exit on error
echo " BUILD START"
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
python manage.py migrate
# Convert static asset files
python manage.py collectstatic --noinput --clear
echo " BUILD END"

# Apply any outstanding database migrations
