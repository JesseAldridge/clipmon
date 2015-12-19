echo "installing requirements..."
pip install -r requirements.txt
echo "setting up launchctl..."
python setup_launchctl.py
