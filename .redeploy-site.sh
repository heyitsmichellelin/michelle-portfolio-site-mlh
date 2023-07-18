git fetch && git reset origin/main --hard
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
systemctl restart myportfolio