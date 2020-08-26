import schedule
import time
from app import integra

schedule.every(1).minutes.do(integra)

while True:
    schedule.run_pending()
    time.sleep(1)
