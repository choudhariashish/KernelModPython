#!/usr/bin/python

import sys
import os
import shutil
import fileinput

path_kmod="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/meta/recipes-kernel/"

def printDirTree(rootDir):
    for dirName, subdirList, fileList in os.walk(rootDir):
#     print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)

def renameFile(file, mod_old_name,  mod_new_name):
    # variable to hold new file names
    fname = file
    fname = fname.replace(mod_old_name, mod_new_name)
    print "\t\t\t\t\trename->", file, fname
    os.rename(file, fname)

def replaceModName(rootDir, mod_old_name, mod_new_name):
    # important
    os.chdir(mod_new_name)
    for dirName, subdirList, fileList in os.walk(rootDir):
#        print('Found directory: %s' % dirName)
        # important
        os.chdir(dirName)    
        for file in fileList:
            print('\t%s' % file)
            for line in fileinput.input(file, inplace=True):
                print line.replace(mod_old_name, mod_new_name),
            if file.find(mod_old_name) >= 0:
                print "\t\b\b*  \bmatch:", file
                renameFile(file, mod_old_name, mod_new_name)
            

arg_count = 0
# check for input parameters
if len(sys.argv) < 2:
    print "\nError: Not enough arguments"
    print "Usage: hvt_mk_Kmod <all_mod_director> <mod_old_name> <mod_new_name> <option>"
    print "option:"
    print "\t1. open -> to open the kernel module source folder\n"
    sys.exit()

# print all arguments
for a_it in sys.argv:
    print "arg:", arg_count, a_it
    arg_count += 1

if len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        cmd = 'ls '+path_kmod
        os.system(cmd)
        sys.exit()

# initialize input parameters
mod_old_name = sys.argv[1]
mod_new_name = sys.argv[2]

# check if path exists
if os.path.isdir(path_kmod) <= 0:
    print "Error: path does not exists", path_kmod
    sys.exit()

# check if old module exists
if os.path.isdir(path_kmod+mod_old_name) <= 0:
    print "Error: directory not found", path_kmod+mod_old_name
    sys.exit()

# change directory and make a copy of existing kernel module directory
# with a new name
os.chdir(path_kmod)
shutil.copytree(mod_old_name, mod_new_name)

mod_old_name = mod_old_name[:-1]
replaceModName(path_kmod+mod_new_name, mod_old_name, mod_new_name)
#printDirTree(path_kmod+mod_old_name)

if len(sys.argv)==4:
    open_source = sys.argv[3]
    if open_source == 'open':
        print open_source
        cmd = 'gnome-open '+path_kmod+mod_new_name+'/files'
        print cmd
        os.system(cmd)
        sys.exit()
