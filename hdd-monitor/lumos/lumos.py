
import sys
import os
import time
import json
import requests
from random import randrange
import platform

from lumos.bindjson import BindJSON
from lumos.lumosconf import LumosConf
from lumos.lumosmodel import LumosModel
from lumos.partition import Partition
from lumos.bindjson import BindJSON
from lumos.hdd_ex1 import WinHDD

class Monitor(object):

    lumosModel = LumosModel()
    lumosConf = LumosConf()
    partition = Partition()
    bindJson = BindJSON()
    winHDD = WinHDD()

    conn = None
    cursor = None
    json = None
    dataJSON = {}

    def __init__(self):
      print('--Monitor Constructor')
      super().__init__()

    def getHddDetails(self, hostIP):
        if platform.system() == 'Windows':
            self.json = self.bindJson.windowsHDDDataBindToJson()
            randReqID = randrange(0, 10000000)
            self.dataJSON = {"requestID" : randReqID, "hostIP" : hostIP, "rawData" : self.json}
        elif hasattr(os, 'statvfs'):
            part = self.partition.getDiskPartitions()
            self.json = self.bindJson.unixHDDUsageDataBindToJSON(part)
            randReqID = randrange(0, 10000000)
            self.dataJSON = {"requestID" : randReqID, "hostIP" : hostIP, "rawData" : self.json}
        else:
            raise NotImplementedError("platform not supported")



    def sendRequest(self,url):
       requests.post(url, json = self.dataJSON)

    def run(self):
        print("Current Work Directory: "+os.getcwd())
        m = Monitor()
        m.lumosConf.setPath(os.getcwd()+"\lumos\conf\lumos.yml")
        m.lumosConf.readLumosYaml()
        print("Host: "+m.lumosConf.getHostIP())
        m.getHddDetails(m.lumosConf.getHostIP())
        print("Url: "+m.lumosConf.getUrl())
        m.sendRequest(m.lumosConf.getUrl())