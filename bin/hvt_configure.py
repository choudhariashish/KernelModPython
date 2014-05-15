#!/usr/bin/python

import sys
import os
import shutil
import fileinput

curr_kmod_source='path_kmod="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/meta/recipes-kernel/"'
curr_ko_mod_path='compiled_mod_path="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/build_p4080ds_release/tmp/sysroots/p4080ds/lib/modules/3.0.34-rt55-02404-g1a39570/extra/"'
curr_mod_sdcard_path='mod_sdcard_path="/media/min_distro/lib/modules/3.0.34-rt55-02404-g1a39570/"'
curr_qoriq_path='qoriq_path="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/"'

# directory where the tool is installed
curr_dir="/home/hypervisor/ashish/pythonCodes/hvt/bin"

print "\nEnter 'help' for commands\n"
while (1):
    option = raw_input("hvt/> ")
    
    if option == 'help':
        print "\nAvailable commands:\n"
        print "1.'set_mod_path'              - Location of kernel modules source"
        print "2.'set_ko_mod_path'           - Location of compiled kernel module(*.ko)"
        print "3.'set_ko_mod_sdcard_path'    - Location of .ko file in sdcard"
        print "4.'set_qoriq_path'            - Location of QorIQ root directory"
        print "5.'print_config'              - Print configuration"
        print "6.'exit'                      - Close hvt configuration"
        
    if option == 'set_mod_path' or option == '1':
        os.chdir(curr_dir)
        option = raw_input("hvt/set_mod_path> ")
        for file in os.listdir(curr_dir):
            if file.find('hvt_') >= 0:
                for line in fileinput.input(file, inplace=True):
                    print line.replace(curr_kmod_source, 'path_kmod='+'"'+option+'/"'),        
        
    if option == 'set_ko_mod_path' or option == '2':
        os.chdir(curr_dir)
        option = raw_input("hvt/set_ko_mod_path> ")
        for file in os.listdir(curr_dir):
            if file.find('hvt_') >= 0:
                for line in fileinput.input(file, inplace=True):
                    print line.replace(curr_ko_mod_path, 'compiled_mod_path='+'"'+option+'/"'),

    if option == 'set_ko_mod_sdcard_path' or option == '3':
        os.chdir(curr_dir)        
        option = raw_input("hvt/set_ko_mod_sdcard_path> ")
        for file in os.listdir(curr_dir):
            if file.find('hvt_') >= 0:
                for line in fileinput.input(file, inplace=True):
                    print line.replace(curr_mod_sdcard_path, 'mod_sdcard_path='+'"'+option+'/"'),

    if option == 'set_qoriq_path' or option == '4':
        os.chdir(curr_dir)
        option = raw_input("hvt/set_qoriq_path> ")
        for file in os.listdir(curr_dir):
            if file.find('hvt_') >= 0:
                for line in fileinput.input(file, inplace=True):
                    print line.replace(curr_qoriq_path, 'qoriq_path='+'"'+option+'/"'),

    if option == 'print_config' or option == '5':
        print "\nCurrent configuration:\n"
        print curr_kmod_source
        print curr_ko_mod_path
        print curr_mod_sdcard_path
        print curr_qoriq_path
        
    if option == 'exit' or option == '6':
        break
