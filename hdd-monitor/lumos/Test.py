from apscheduler.schedulers.blocking import BlockingScheduler
import platform

print(platform.machine())
print(platform.platform())
print(platform.version())
print(platform.uname())
print(platform.system())
print(platform.processor())


from subprocess import PIPE, Popen

def free_volume(filename):
    """Find amount of disk space available to the current user (in bytes)
       on the file system containing filename."""
    stats = Popen(["df", "-Pk", filename], stdout=PIPE).communicate()[0]

    return int(stats.splitlines()[1].split()[3]) * 1024
import ctypes
import os
import platform
import sys
"""
def get_free_space_mb(dirname):
    #Return folder/drive free space (in megabytes).
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024
"""

"""
sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three minutes.')


@sched.scheduled_job('cron', year='*', month='*', day='*', week='*', day_of_week='*', hour=11, minute=25, second=0)
def scheduled_job():
    print('===This job is run every weekday at 11am!')

sched.start()

"""