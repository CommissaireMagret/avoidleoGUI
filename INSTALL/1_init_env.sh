#!/bin/sh
python3 -m venv ../venv
source ../venv/bin/activate
pip install wheel
pip install pypredict
pip install PyQt6
cd ..
