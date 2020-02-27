from apscheduler.schedulers.blocking import BlockingScheduler
from lumos.lumos import Monitor

sched = BlockingScheduler()

m = Monitor();

#@sched.scheduled_job('cron', year='*', month='*', day='*', week='*', day_of_week='*', hour='11', minute='38')
@sched.scheduled_job('interval', seconds=5)
def timed_job():
    print('This job is run every three minutes.')
    Monitor.run(m)

sched.start()
