#!/bin/bash

sudo apt-get install libfreetype6-dev libharfbuzz-dev libfribidi-dev gtk-doc-tools
wget -O raqm-0.7.0.tar.gz https://raw.githubusercontent.com/python-pillow/pillow-depends/master/raqm-0.7.0.tar.gz

tar -xzvf raqm-0.7.0.tar.gz
cd raqm-0.7.0
./configure --prefix=/usr && make -j4 && sudo make -j4 install

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
