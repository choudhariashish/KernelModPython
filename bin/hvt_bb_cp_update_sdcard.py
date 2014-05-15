#!/usr/bin/python

import sys
import os
import shutil
import fileinput

kernel_module=sys.argv[1]

script_bb_compile='hvt_bb_compile.sh '+kernel_module
script_cp_kmod_sdcard='hvt_cp_kmod_sdcard.py '+kernel_module
script_update_sdcard='hvt_update_sdcard.py '+kernel_module

os.system(script_bb_compile)
os.system(script_cp_kmod_sdcard)
os.system(script_update_sdcard)
