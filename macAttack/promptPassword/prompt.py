import subprocess

def promptSystem():
    try:
        run_command = subprocess.check_output(
        "osascript system.applescript", shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command

def promptiCloud():
    try:
        run_command = subprocess.check_output(
        "osascript icloud.applescript", shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command

if __name__ == "__main__":
    print promptiCloud()