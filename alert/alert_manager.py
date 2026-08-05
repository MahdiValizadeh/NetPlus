from alert.email_alert import send_email
from alert.telegram_alert import send_telegram
from logger import logger
def send_alerts(results):
    errors = []
    for device in results:
        if device["error"]:
            errors.append(f"{device['name']} - {device['error']}")
    if errors:
        message = "\n".join(errors)
        email_result=send_email(message)
        telegram_result=send_telegram(message)
        if email_result["success"]:
            print("Email Sent")
            logger.info("Email Alert Sent")
        else:
            print(email_result["error"])
            logger.error(email_result["error"])

        if telegram_result["success"]:
            print("Telegram Sent")
            logger.info("Telegram Alert Sent")
        else:
            print(telegram_result["error"])
            logger.error(telegram_result["error"])