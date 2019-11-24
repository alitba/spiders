import schedule
import time
import schedule
import time

def job(message='stuff'):
    print("I'm working on:", message)

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
