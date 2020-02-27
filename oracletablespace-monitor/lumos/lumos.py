
import sys
import os
import cx_Oracle
import json
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from lumos.databaseconf import DatabaseConf
from lumos.databasemodel import DatabaseModel
from lumos.databaseconnection import DatabaseConnection
from lumos.bindjson import BindJSON
from lumos.lumosconf import LumosConf
from lumos.lumosmodel import LumosModel
from random import randrange

class Monitor(object):

   dbcon = DatabaseConnection()
   dbConf = DatabaseConf()
   dbModel = DatabaseModel()
   lumosModel = LumosModel()
   lumosConf = LumosConf()
   bindJSoN = BindJSON()
   conn = None
   cursor = None
   json = None
   requestJSON = None

   def __init__(self):
      print('--Monitor Constructor')
      super().__init__()


      # call the appropriate superclass constructor
      #print("Calling parent constructor")
      #self.readDatabaseYaml()
      #self.getPrint(self, self.dbmodel)
      #def getPrint(self, dbmodel):
      #print("Host "+dbmodel.getHost())

   def dbConnection(self, host):
        self.conn = self.dbcon.getDBConnection(host)
        print(self.conn)

   def getCursor(self, sql):
       self.cursor = self.conn.cursor()
       #print("SQL "+self.getSql())
       self.cursor.execute(sql)

   def getJson(self, hostIP):
        self.json = self.bindJSoN.setJSON(self.cursor)
        randReqID = randrange(0, 10000000)
        self.requestJSON = {"requestID" : randReqID, "hostIP" : hostIP, "rawData" : self.json}
        print(self.requestJSON)

   def sendRequest(self, url):
       requests.post(url, json = self.requestJSON)

#if __name__ == '__main__':
   def run(self):
        print("Current Work Directory: "+os.getcwd())
        m = Monitor()
        print("Path: "+m.dbConf.getPath())
        m.dbConf.setPath(os.getcwd()+"\lumos\conf\database.yml")
        m.dbConf.readDatabaseYaml()
        m.lumosConf.setPath(os.getcwd()+"\lumos\conf\lumos.yml")
        m.lumosConf.readLumosYaml()
        print("Url: "+m.lumosConf.getUrl())
        print("Path: "+m.lumosConf.getPath())
        print("Path: "+m.dbConf.getPath())
        print(m.dbConf.getHost());
        m.dbConnection(m.dbConf.getHost())
        m.getCursor(m.dbConf.getSql())
        m.getJson(m.dbConf.getHostIP())
        m.sendRequest(m.lumosConf.getUrl())

