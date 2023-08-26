#!/usr/bin/env bash

# Updating code
echo student | sudo -S apt update -y
echo student | sudo -S apt upgrade code -y

# Installing python
echo student | sudo -S apt install python3 -y

# Installing vscode extension
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension ms-toolsai.jupyter-keymap
code --install-extension ms-toolsai.jupyter-renderers
code --install-extension ms-toolsai.vscode-jupyter-cell-tags
code --install-extension ms-toolsai.vscode-jupyter-slideshow


# Installing libraries
pip3 install pandas
pip3 install qiskit
pip3 install numpy
pip3 install nbimporter
pip3 install nbformat
pip3 install pylatexenc
pip3 install matplotlib
pip3 install IPython
