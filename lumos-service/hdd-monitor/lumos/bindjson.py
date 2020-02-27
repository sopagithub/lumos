
import json
import time
from random import randrange
import pythoncom
import wmi
from lumos.diskusage import DiskUsage
from lumos.util import Util
import json

class BindJSON:

    jsonMasterData = {}
    util = Util()
    json = None
    du = DiskUsage()

    def _init_(self):
        print("--Lumos Model Constructor")

    def unixHDDUsageDataBindToJSON(self, partitions):
        pythoncom.CoInitializeEx(0)
        pythoncom.CoInitialize()
        jsonDataArr = []
        for part in partitions:
            print(part)
            jsonData = {}
            usage = self.du.getDiskUsage(part.mountpoint)
            print("Total Byte: "+str(usage.total))
            jsonData['location'] = part.mountpoint
            jsonData['totalMB'] = usage.total
            jsonData['usedMB'] = usage.used
            jsonData['freeMB'] = usage.free
            jsonData['pctUsedSpace'] = usage.percent
            jsonData['pctFreeSpace'] = (100-usage.percent)
            jsonDataArr.append(jsonData)
            print("    %s\n" % str(self.du.getDiskUsage(part.mountpoint)))
            print(self.jsonMasterData)
        jsonData = {}
        usage = self.du.getDiskUsage("/data/")
        jsonData['location'] = "/data/"
        jsonData['totalMB'] = usage.total
        jsonData['usedMB'] = usage.used
        jsonData['freeMB'] = usage.free
        jsonData['pctUsedSpace'] = usage.percent
        jsonData['pctFreeSpace'] = (100-usage.percent)
        jsonDataArr.append(jsonData)
        print("    %s\n" % str(self.du.getDiskUsage("/data/")))
        print(jsonDataArr)
        #time.sleep(0.5)
        return json.dumps(jsonDataArr)

    def windowsHDDDataBindToJson(self):
        usedSpace = None
        pythoncom.CoInitializeEx(0)
        pythoncom.CoInitialize()
        jsonDataArr = []
        for d in wmi.WMI ().Win32_LogicalDisk():
            jsonData = {}
            if(d.Size != None):
                usedSpace = (int(d.Size)-int(d.FreeSpace))
                pctUsedSpace = int((int(usedSpace)/int(d.Size))*100)
                print(self.util.covertByteToMb(int(d.Size)))
                print(d.Size)
                jsonData["location"] = d.Caption
                jsonData["totalMB"] = self.util.covertByteToMb(int(d.Size))
                jsonData["usedMB"] = self.util.covertByteToMb(usedSpace)
                jsonData["freeMB"] = self.util.covertByteToMb(int(d.FreeSpace))
                jsonData["pctUsedSpace"] = pctUsedSpace
                jsonData["pctFreeSpace"] = (100 - pctUsedSpace)
                jsonDataArr.append(jsonData)
        return json.dumps(jsonDataArr)


