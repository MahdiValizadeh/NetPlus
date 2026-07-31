import paramiko
from loader.config_loader import load_config
config = load_config()
def ssh_connect(ip, commands):
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
        outputs={}
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            outputs[command] = stdout.read().decode()
        return outputs
    except Exception:
        return None
    finally:
        if client:
            client.close()