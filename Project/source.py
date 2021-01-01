from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler
from Automate import Reminders


scheduler = BlockingScheduler()

scheduler.add_job(Reminders,'interval',seconds=20)
scheduler.start()