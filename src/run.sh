#!/bin/bash

python3 -m venv quiz-venv
source quiz-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py