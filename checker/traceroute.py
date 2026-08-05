import subprocess
def traceroute(ip):
    try:
        result = subprocess.run(["tracert", ip], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Traceroute Failed\n{result.stderr}"
    except Exception as e:
        return f"Traceroute Error: {e}"