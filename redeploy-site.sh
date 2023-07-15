#!/bin/bash

tmux kill-server

cd portfolio-site-mlh/

git fetch && git reset origin/main --hard

git pull

source python3-virtualenv/bin/activate

pip install -r requirements.txt

tmux new -d -s portfolio

tmux ls

tmux send-keys -t portfolio.0 "source python3-virtualenv/bin/activate" ENTER

tmux send-keys -t portfolio.0 "export FLASK_ENV=development" ENTER

tmux send-keys -t portfolio.0 "flask run --host=0.0.0.0" ENTER
