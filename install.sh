#!/bin/bash
clear
echo -e "\e[92mInstalling dependencies...\e[0m"
pkg install python -y
pip install -r requirements.txt
echo -e "\e[92mDone. Jalankan dengan:\e[0m python tracker.py"