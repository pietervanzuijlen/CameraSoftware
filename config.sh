#!/bin/bash

print(Installing Daheng software)
sudo ./CameraFilter/install.sh

print(Installing linux modules)
sudo apt-get install python-pip

print(Installing python packages)
pip install Pillow
pip install numpy

print(Compiling C++ software)
print(Installation completed)

