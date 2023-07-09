tmux kill-server
source venv/bin/activate
git fetch && git reset origin/main --hard
pip install --upgrade pip
pip install -r requirements.txt
tmux new-session -d -s my_session \; send-keys "flask run --host=0.0.0.0" Enter


