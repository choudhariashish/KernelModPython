#!/usr/bin/python

import sys
import os
import shutil
import fileinput

path_kmod="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/meta/recipes-kernel/"
compiled_mod_path="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/build_p4080ds_release/tmp/sysroots/p4080ds/lib/modules/3.0.34-rt55-02404-g1a39570/extra/"

for file in os.listdir(compiled_mod_path):
	print file	
