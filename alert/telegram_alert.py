import requests
from loader.config_loader import load_config
config = load_config()
def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{config['telegram_token']}/sendMessage"
        data = {
            "chat_id": config["telegram_chat_id"],
            "text": message
        }
        requests.post(url, data=data)
        return {"success": True}
    except Exception as e:
        return {
            "success": False,
            "error": f"Telegram Failed: {e}"
        }