import paramiko
from loader.config_loader import load_config
config = load_config()
def ssh_connect(ip, command):
    client=None
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
        hostname=ip,
        username=config["ssh_username"],
        password=config["ssh_password"],
        port=config["ssh_port"],
        timeout=config["ssh_timeout"])
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        
        return output
    except Exception:
        return None
    finally:
        if client:
            client.close()