
import os
from collections import namedtuple
from lumos.util import Util

class DiskUsage(object):

    usageNttuple = namedtuple('usage',  'total used free percent')
    util = Util()

    def getDiskUsage(self, path):
        st = os.statvfs(path)
        free = (st.f_bavail * st.f_frsize)
        total = (st.f_blocks * st.f_frsize)
        used = (st.f_blocks - st.f_bfree) * st.f_frsize
        try:
            percent = ret = (float(used) / total) * 100
        except ZeroDivisionError:
            percent = 0
        print("Email: ")
        print(self.util.convertToHumanReadable(total))
        print(total)
        return self.usageNttuple(round(self.util.covertByteToMb(total)), round(self.util.covertByteToMb(used)), round(self.util.covertByteToMb(free)), round(percent, 1))