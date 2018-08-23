import subprocess

def promptPass():
    try:
        run_command = subprocess.check_output(
        "osascript script.applescript", shell=True)
    except subprocess.CalledProcessError:
        pass
    return run_command

if __name__ == "__main__":
    print promptPass()
