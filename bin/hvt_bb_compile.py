#!/usr/bin/python

import sys
import os
import shutil
import fileinput

qoriq_path="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/"

os.chdir(qoriq_path)
cmd='source ./fsl-setup-poky -m p4080ds -j 12 -t 12 -l'
os.system(cmd)

cmd='bitbake '+sys.argv[1]
os.system(cmd)
