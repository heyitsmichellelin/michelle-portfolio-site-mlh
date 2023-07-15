#!/bin/bash

# Step1: Change to the project folder
cd ~/portfolio-site-mlh

# Step 2: Fetch and reset the git repository
git fetch && git reset origin/main --hard

# Step 3: Enter the python virtual environment and install dependencies
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step 4: restart my portfolio service
systemctl restart myportfolio