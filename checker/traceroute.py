import subprocess
def traceroute(ip):
    result = subprocess.run(["traceroute", ip], capture_output=True, text=True)
    return result.stdout
#print(trace("8.8.8.8"))