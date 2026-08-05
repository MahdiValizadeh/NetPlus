import subprocess
def ping(ip):
    try:
        result = subprocess.run(["ping", ip], capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        return False

#print(ping("8.8.8.8"))

