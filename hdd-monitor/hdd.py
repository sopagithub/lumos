from apscheduler.schedulers.blocking import BlockingScheduler
from lumos.lumos import Monitor
import os
import json
import platform
from random import randrange
from lumos.lumos import Monitor

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=5)
def timed_job():
    print('The scheduling job has been fired')
    m = Monitor();
    Monitor.run(m)

sched.start()
