#!/usr/bin/python

import sys
import os

#/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/build_p4080ds_release/tmp/sysroots/p4080ds/lib/modules/3.0.34-rt55-02404-g1a39570/extra/
#/media/min_distro/lib/modules/3.0.34-rt55-02404-g1a39570/

compiled_mod_path="/home/hypervisor/QorIQ-SDK-V1.2-20120614-yocto/build_p4080ds_release/tmp/sysroots/p4080ds/lib/modules/3.0.34-rt55-02404-g1a39570/extra/"
mod_sdcard_path="/media/min_distro/lib/modules/3.0.34-rt55-02404-g1a39570/"
mod_name = sys.argv[1]
cmd='sudo cp '+compiled_mod_path+mod_name+'.ko'+' '+mod_sdcard_path
#print cmd
os.system(cmd)
