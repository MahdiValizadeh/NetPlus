import paramiko
from paramiko import AuthenticationException, SSHException
from paramiko.ssh_exception import IncompatiblePeer
from socket import timeout
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
        return {
        "success": True,
        "output": outputs
        }
    except AuthenticationException:
        return {
        "success": False,
        "error": "Authentication Failed"
        }
    except IncompatiblePeer:
        return {
            "success": False,
            "error": "Legacy SSH KEX Algorithm"
        }
    except SSHException:
        return {
        "success": False,
        "error": "SSH Connection Failed"
        } 
    except timeout:
        return {
        "success": False,
        "error": "SSH Timeout"
        }
    except Exception as e:
        return {
        "success": False,
        "error": f"Unknown Error: {e}"
        }
    finally:
        if client:
            client.close()