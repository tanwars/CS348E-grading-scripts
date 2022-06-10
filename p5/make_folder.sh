#!/bin/bash

mkdir $1
cp ../../../../Downloads/$1* ./$1

cd ./$1
unzip $1*

cd ..
python plot_logs.py $1