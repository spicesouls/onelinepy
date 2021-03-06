#!/bin/bash

echo 'Installing Requirements...'
sudo apt install python3
sudo apt install python3-pip
python3 -m pip install -r requirements.txt
echo 'Adding to Bin...'
sudo ln -s $PWD'/oneline.py' /usr/bin/onelinepy
chmod +x /usr/bin/onelinepy
echo "Done! Run 'onelinepy' anywhere to start!"
