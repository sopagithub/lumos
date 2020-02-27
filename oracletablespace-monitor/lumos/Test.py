from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three minutes.')


@sched.scheduled_job('cron', year='*', month='*', day='*', week='*', day_of_week='*', hour=11, minute=25, second=0)
def scheduled_job():
    print('===This job is run every weekday at 11am!')

sched.start()