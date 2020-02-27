
from collections import namedtuple

class Partition(object):

    disk_ntuple = namedtuple('partition',  'device mountpoint fstype')

    def __init__(self):
        print('--Partition Conf Constructor')
        super().__init__()

    def getDiskPartitions(self, all=False):
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
            ntuple = self.disk_ntuple(device, mountpoint, fstype)
            retlist.append(ntuple)
        return retlist