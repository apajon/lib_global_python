# lib_global_python
____
# Table of content
- [Adding this submodule](#Adding-this-submodule)
- [Using repo with submodules](#Using-repo-with-submodules)
  - [Clone](#Clone)
  - [Pull](#Pull)
  - [Push](#Push)
- [Python module installation](#Python-module-installation)
____
# Add this submodule
add this repo as submodule into another git repo
```bash
git submodule add https://github.com/apajon/lib_global_python
```
____
# Using repo with submodules
## Clone
```bash
git clone --recursive ####
```

or clone the repo in a classic way
```bash
git clone ####
git submodule update --init --recursive
```
after any method
```bash
cd #SUBMODULE PATH#
git branch
git checkout #chosen branch#
```
## Pull
```bash
git pull --recurse-submodules
```
## Push
```bash
cd #submodule repo#
git add *
git commit -m "update submodule"
cd ..
git add #submodule repo#
git commit "update submodule"
```
```bash
git push
```
or
```bash
git push --recurse-submodules=check
```

____
# Python module installation
#### pexpect library in python needed to work with gaspard
```bash
pip install pexpect
```
or

```bash
pip3 install pexpect
```

#### paho.mqtt.client library in python
In a terminal run for Python3
```bash
pip3 install paho-mqtt
```
or for Python2
```bash
pip2 install paho-mqtt
```
source web
>http://www.steves-internet-guide.com/into-mqtt-python-client/

#### install numpy
```bash
pip3 install numpy
pip3 show numpy
pip3 install --upgrade numpy
```
and test
```bash
python3
import numpy as np
```

#### matplotlib installation
In a terminal run for Python3
```bash
sudo apt update
sudo apt install python3-matplotlib
```
or for Python2
```bash
sudo apt update
sudo apt-get install python-matplotlib
```
source web
>https://matplotlib.org/users/installing.html

#### CSV reader pandas
In a terminal run for Python3
```bash
sudo pip3 install pandas
```
or for Python2
```bash
sudo pip2 install pandas
```
source web
>https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
