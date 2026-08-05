import smtplib
from email.message import EmailMessage
from loader.config_loader import load_config
config = load_config()
def send_email(message):
    try:
        email = EmailMessage()
        email["Subject"] = "NetPlus Alert"
        email["From"] = config["email_sender"]
        email["To"] = config["email_receiver"]
        email.set_content(message)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(
                config["email_sender"],
                config["email_password"]
            )
            server.send_message(email)
            return {"success": True}
    except Exception as e:
        return {
            "success": False,
            "error": f"Email Failed: {e}"
        }