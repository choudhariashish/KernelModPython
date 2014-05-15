#!/usr/bin/python

import sys
import os
import shutil
import fileinput

sd_card_file_path='/media/min_distro/home/hyper/Pcache/'

old_file = ' '

os.chdir(sd_card_file_path)
for file in os.listdir(sd_card_file_path):
    if file.find('cacheLocking') >= 0:
        old_file=file
        print old_file
        cmd='mv '+old_file+' '+sys.argv[1]+'.h'
        os.system(cmd)        

for file in os.listdir(sd_card_file_path):
    if file.find('testCache') >= 0:
        for line in fileinput.input(file, inplace=True):
            print line.replace(old_file[:-2], sys.argv[1]),
        
        
        
        




