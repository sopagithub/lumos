import os
import collections
import platform


def convertToGB(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

_ntuple_diskusage = collections.namedtuple('usage', 'total used free')

if hasattr(os, 'statvfs'):  # POSIX
    def disk_usage(path):
        st = os.statvfs(path)
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        used = (st.f_blocks - st.f_bfree) * st.f_frsize
        return _ntuple_diskusage(total, used, free)

elif platform.system() == 'Windows':       # Windows
    import ctypes
    import sys

    def disk_usage(path):
        _, total, free = ctypes.c_ulonglong(), ctypes.c_ulonglong(), \
                           ctypes.c_ulonglong()
        if sys.version_info >= (3,) or isinstance(path, str):
            fun = ctypes.windll.kernel32.GetDiskFreeSpaceExW
        else:
            fun = ctypes.windll.kernel32.GetDiskFreeSpaceExA
        ret = fun(path, ctypes.byref(_), ctypes.byref(total), ctypes.byref(free))
        if ret == 0:
            raise ctypes.WinError()
        used = total.value - free.value
        return _ntuple_diskusage(total.value, used, free.value)
else:
    raise NotImplementedError("platform not supported")

#disk_usage.__doc__ = __doc__

if __name__ == '__main__':
    print("Courrent Directory: "+os.getcwd())
    print(disk_usage(os.getcwd()))
    #totalUsage = disk_usage("/")
    #print("Total Hard Disk Space is "+ convertToGB(totalUsage.total))
    print("============================C Drive===================================")
    totalUsageC = disk_usage("C:\\")
    print("Total C Drive Space is "+convertToGB(totalUsageC.total))
    print("Total C Drive Free Space is "+convertToGB(totalUsageC.free))
    print("Total C Drive Used Space is "+convertToGB(totalUsageC.used))
    print("============================D Drive===================================")
    totalUsageD = disk_usage("D:\\")
    print("Total D Drive Space is "+convertToGB(totalUsageD.total))
    print("Total D Drive Free Space is "+convertToGB(totalUsageD.free))
    print("Total D Drive Used Space is "+convertToGB(totalUsageD.used))
    print("============================E Drive===================================")
    totalUsageE = disk_usage("E:\\")
    print("Total E Drive Space is "+convertToGB(totalUsageE.total))
    print("Total E Drive Free Space is "+convertToGB(totalUsageE.free))
    print("Total E Drive Used Space is "+convertToGB(totalUsageE.used))
    print("============================F Drive===================================")
    totalUsageF = disk_usage("F:\\")
    print("Total F Drive Space is "+convertToGB(totalUsageF.total))
    print("Total F Drive Free Space is "+convertToGB(totalUsageF.free))
    print("Total F Drive Used Space is "+convertToGB(totalUsageF.used))

