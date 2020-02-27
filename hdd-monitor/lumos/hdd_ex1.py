
#import wmi
import json
from random import randrange

class WinHDD:

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

   # c = wmi.WMI ()
    UsedSpace = None
    randReqID = randrange(0, 10000000)
    jsonMasterData = {"requestID":randReqID,"diskInfo" : []}
    jsonData = {}
"""
    def getWinHDD(self):
        for d in self.c.Win32_LogicalDisk():
            #jsonData = c.Win32_LogicalDisk()
            #print(jsonData)
            jsonData = {}
            if(d.Size != None):
                usedSpace = (int(d.Size)-int(d.FreeSpace))
                jsonData['location'] = d.Caption
                jsonData['totalMB'] = d.Size
                jsonData['usedMB'] = usedSpace
                jsonData['freeMB'] = d.FreeSpace
                jsonData['pctUsedSpace'] = (int(usedSpace)/int(d.Size))*100
                jsonData['pctFreeSpace'] = (int(d.FreeSpace)/int(d.Size))*100
                #print(jsonData)
                #print( d.Caption, convertToGB(int(d.FreeSpace)), convertToGB(UsedSpace), convertToGB(int(d.Size)), d.DriveType)
                self.jsonMasterData["diskInfo"].append(jsonData)
        print(self.jsonMasterData)
        return self.jsonMasterData

"""

"""
import os
disk = None
disk = os.statvfs('/')
print("preferred file system block size: " + str(disk.f_bsize))
print("fundamental file system block size: " + str(disk.f_frsize))
print("total number of blocks in filesystem: " + str(disk.f_blocks))
print("total number of free blocks: " + str(disk.f_bfree))
print("free blocks available to non-super user: " + str(disk.f_bavail))
print("total number of file nodes: " + str(disk.f_files))
print("total number of free file nodes: " + str(disk.f_ffree))
print("free nodes available to non-super user: " + str(disk.f_favail))
print("flags: " + str(disk.f_flag))
print("miximum file name length: " + str(disk.f_namemax))
print( "~~~~~~~~~~calculation of disk usage:~~~~~~~~~~")
totalBytes = float(disk.f_bsize*disk.f_blocks)
print ("total space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalBytes, totalBytes/1024, totalBytes/1024/1024, totalBytes/1024/1024/1024))
totalUsedSpace = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
print ("used space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalUsedSpace, totalUsedSpace/1024, totalUsedSpace/1024/1024, totalUsedSpace/1024/1024/1024))
totalAvailSpace = float(disk.f_bsize*disk.f_bfree)
print ("available space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalAvailSpace, totalAvailSpace/1024, totalAvailSpace/1024/1024, totalAvailSpace/1024/1024/1024))
totalAvailSpaceNonRoot = float(disk.f_bsize*disk.f_bavail)
print ("available space for non-super user: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes " % (totalAvailSpaceNonRoot, totalAvailSpaceNonRoot/1024, totalAvailSpaceNonRoot/1024/1024, totalAvailSpaceNonRoot/1024/1024/1024))
"""