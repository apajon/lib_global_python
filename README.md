# lib_global_python

## add this repo as submodule into another git repo
```bash
git submodule add https://github.com/chaconinc/DbConnector
```

## clone repo with this submodule

```bash
git clone --recursive ####
```

or clone the repo in a classic way
```bash
git clone ####
```
after cloning 
```bash
git submodule update --init --recursive
```

git branch
git checkout ###

git pull --recurse-submodules



git add and commit in submodule repo
git add and commit in global repo
git push
or
git push --recurse-submodules=check

## Python module installation
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
