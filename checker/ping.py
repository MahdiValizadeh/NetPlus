import subprocess
def ping(ip):
    result = subprocess.run(["ping", ip], capture_output=True, text=True)
    return result.returncode == 0
#print(ping("8.8.8.8"))

