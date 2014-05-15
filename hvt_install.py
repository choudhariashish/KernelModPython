#!/usr/bin/python

import sys
import os
import shutil
import fileinput

install_dir=os.getcwd()+'/bin'     

print install_dir

os.chdir(install_dir)

config_dir='curr_dir="/"'

for file in os.listdir(os.getcwd()):
    if file.find('hvt_') >= 0:
        for line in fileinput.input(file, inplace=True):
            print line.replace(config_dir, 'curr_dir='+'"'+install_dir+'"'),




cmd = 'echo "export PATH=$PATH:'+ install_dir +'" >> ~/.bashrc'
os.system(cmd)
