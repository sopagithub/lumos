from apscheduler.schedulers.blocking import BlockingScheduler
from lumos.lumos import Monitor
from time import time

sched = BlockingScheduler()

m = Monitor();

@sched.scheduled_job('interval', seconds=5)
#@sched.scheduled_job('cron', year='*', month='*', day='*', week='*', day_of_week='*', hour='*', minute='*', second=5)
def timed_job():
    print('The scheduling job is fired at ')
    Monitor.run(m)

sched.start()
