import schedule
import time
from main import monitor
def run_monitoring():
    monitor()
schedule.every(5).minutes.do(run_monitoring)
print("NetPlus Scheduler Started...")
print("Monitoring interval: 5 minutes")
while True:
    schedule.run_pending()
    time.sleep(1)