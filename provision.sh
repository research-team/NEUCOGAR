#!/bin/sh

sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get -y install screen

# NEST dependencies
sudo apt-get -y install libtool libltdl-dev libgsl0-dev python-all-dev python-tk

# Downloading and installing NEST from sources
wget http://www.nest-simulator.org/downloads/gplreleases/nest-2.6.0.tar.gz
cd /tmp
tar xzf ~/nest-2.6.0.tar.gz
cd nest-2.6.0
mkdir build
cd build
../configure --prefix=/usr/local
make
sudo make install
cd
sudo rm -rf /tmp/nest-2.6.0
