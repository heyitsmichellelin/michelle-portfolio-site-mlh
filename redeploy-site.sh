#!/bin/bash

# Step 1: Kill all existing tmux sessions
tmux kill-session -a

# Step 2: Change to the project folder
cd /path/to/project/folder

# Step 3: Fetch and reset the git repository
git fetch && git reset origin/main --hard

# Step 4: Enter the python virtual environment and install dependencies
source /path/to/virtualenv/bin/activate
pip install -r requirements.txt

# Step 5: Start a new detached Tmux session and run Flask server
tmux new-session -d -s flask-session 'cd /path/to/project/folder && source /path/to/virtualenv/bin/activate && flask run'
