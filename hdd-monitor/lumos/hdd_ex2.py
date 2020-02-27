import os
from collections import namedtuple
from random import randrange

disk_ntuple = namedtuple('partition',  'device mountpoint fstype')
usage_ntuple = namedtuple('usage',  'total used free percent')
randReqID = randrange(0, 10000000)
jsonMasterData = {"requestID":randReqID,"rawData" : []}
jsonData = {}

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

def disk_partitions(all=False):
    """Return all mountd partitions as a nameduple.
    If all == False return phyisical partitions only.
    """
    phydevs = []
    f = open("/proc/filesystems", "r")
    for line in f:
        if not line.startswith("nodev"):
            phydevs.append(line.strip())

    retlist = []
    f = open('/etc/mtab', "r")
    for line in f:
        if not all and line.startswith('none'):
            continue
        fields = line.split()
        device = fields[0]
        mountpoint = fields[1]
        fstype = fields[2]
        if not all and fstype not in phydevs:
            continue
        if device == 'none':
            device = ''
        ntuple = disk_ntuple(device, mountpoint, fstype)
        retlist.append(ntuple)
    return retlist

def disk_usage(path):
    """Return disk usage associated with path."""
    st = os.statvfs(path)
    free = (st.f_bavail * st.f_frsize)
    total = (st.f_blocks * st.f_frsize)
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    try:
        percent = ret = (float(used) / total) * 100
    except ZeroDivisionError:
        percent = 0
    # NB: the percentage is -5% than what shown by df due to
    # reserved blocks that we are currently not considering:
    # http://goo.gl/sWGbH
    return usage_ntuple(convertToGB(total), convertToGB(used), convertToGB(free), round(percent, 1))



if __name__ == '__main__':
    for part in disk_partitions():
        print(part)
        jsonData = {}
        usage = disk_usage(part.mountpoint)
        jsonData['location'] = part.mountpoint
        jsonData['totalMB'] = usage.total
        jsonData['usedMB'] = usage.used
        jsonData['freeMB'] = usage.free
        jsonData['pctUsedSpace'] = usage.percent
        jsonData['pctFreeSpace'] = (100-usage.percent)
        print("    %s\n" % str(disk_usage(part.mountpoint)))
        jsonMasterData["rawData"].append(jsonData)
        print(jsonMasterData)
    jsonData = {}
    usage = disk_usage("/data/")
    jsonData['location'] = "/data/"
    jsonData['totalMB'] = usage.total
    jsonData['usedMB'] = usage.used
    jsonData['freeMB'] = usage.free
    jsonData['pctUsedSpace'] = usage.percent
    jsonData['pctFreeSpace'] = (100-usage.percent)
    print("    %s\n" % str(disk_usage("/data/")))
    jsonMasterData["rawData"].append(jsonData)
    print(jsonMasterData)
    #pctFreeSpace
    #pctUsedSpace