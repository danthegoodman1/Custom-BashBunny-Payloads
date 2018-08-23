#!/usr/bin/env python

import subprocess
from time import sleep

# /usr/sbin/ioreg -c IOHIDSystem | /usr/bin/awk '/HIDIdleTime/ {print int($NF/1000000000); exit}'

def checkIdleTime():
    """
    """
    try:
        run_command = subprocess.check_output(
        "/usr/sbin/ioreg -c IOHIDSystem | /usr/bin/awk '/HIDIdleTime/ {print int($NF/1000000000); exit}'", shell=True)
    except subprocess.CalledProcessError:
        pass
    return int(run_command)

# print checkIdleTime()
