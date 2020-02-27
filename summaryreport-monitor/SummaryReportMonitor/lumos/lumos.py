
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
import datetime
from datetime import date, timedelta


class Monitor(object):
   dbcon = DatabaseConnection()
   dbConf = DatabaseConf()
   dbModel = DatabaseModel()
   lumosModel = LumosModel()
   lumosConf = LumosConf()
   bindJSoN = BindJSON()
   currentDate = datetime.datetime.now().strftime("%Y-%m-%d");
   yesterdayDate = str(date.today() - timedelta(days=1))
   reportDateRange = yesterdayDate + " 00:00:00 " + yesterdayDate + " 23:59:59"
   conn = None
   cursor = None
   requestJSON = None
   ansIncomingJSON = None
   icxIncomingJSON = None




   def __init__(self):
      print('--Monitor Constructor')
      super().__init__()

   def dbConnection(self, host):
        self.conn = self.dbcon.getDBConnection(host)
        print(self.conn)

   def getAnsIncomingCursor(self, ansincoming):
       self.ansIncomingcursor = self.conn.cursor()
       self.ansIncomingcursor.execute(ansincoming)
       print(self.ansIncomingcursor)

   def getIcxIncomingCursor(self, icxincoming):
       self.icxIncomingCursor = self.conn.cursor()
       self.icxIncomingCursor.execute(icxincoming)
       print(self.icxIncomingCursor)

   def getIgwIncomingCursor(self, igwincoming):
       self.igwIncomingCursor = self.conn.cursor()
       self.igwIncomingCursor.execute(igwincoming)
       print(self.igwIncomingCursor)

   def getAnsOutgoingCursor(self, ansoutgoing):
       self.ansOutgoingcursor = self.conn.cursor()
       self.ansOutgoingcursor.execute(ansoutgoing)
       print(self.ansOutgoingcursor)

   def getIcxOutgoingCursor(self, icxoutgoing):
       self.icxOutgoingcursor = self.conn.cursor()
       self.icxOutgoingcursor.execute(icxoutgoing)
       print(self.icxOutgoingcursor)

   def getIgwOutgoingCursor(self, igwoutgoing):
       self.igwOutgoingcursor = self.conn.cursor()
       self.igwOutgoingcursor.execute(igwoutgoing)
       print(self.igwOutgoingcursor)


   def getJson(self):
        self.ansIncomingJSON = self.bindJSoN.setAnsIncomingJSON(self.ansIncomingcursor)
        self.icxIncomingJSON = self.bindJSoN.setIcxIncomingJSON(self.icxIncomingCursor)
        self.igwIncomingJSON = self.bindJSoN.setIgwIncomingJSON(self.igwIncomingCursor)
        self.ansOutgoingJSON = self.bindJSoN.setAnsOutgoingJSON(self.ansOutgoingcursor)
        self.icxOutgoingJSON = self.bindJSoN.setIcxOutgoingJSON(self.icxOutgoingcursor)
        self.igwOutgoingJSON = self.bindJSoN.setIgwOutgoingJSON(self.igwOutgoingcursor)

        randReqID = randrange(0, 10000000)
        self.requestJSON = {"requestID" : randReqID, "ansIncomingJSON" : self.ansIncomingJSON, "icxIncomingJSON": self.icxIncomingJSON, "igwIncomingJSON": self.igwIncomingJSON, "ansOutgoingJSON": self.ansOutgoingJSON, "icxOutgoingJSON": self.icxOutgoingJSON, "igwOutgoingJSON": self.igwOutgoingJSON}
        #self.requestJSON = {"requestID": randReqID, "ansIncomingJSON": self.ansIncomingJSON}
        print(self.requestJSON)

   def sendRequest(self, url):
       requests.post(url, json = self.requestJSON)

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
        m.getAnsIncomingCursor(m.dbConf.getAnsincoming())
        m.getIcxIncomingCursor(m.dbConf.getIcxincoming())
        m.getIgwIncomingCursor(m.dbConf.getIgwincoming())
        m.getAnsOutgoingCursor(m.dbConf.getAnsoutgoing())
        m.getIcxOutgoingCursor(m.dbConf.getIcxoutgoing())
        m.getIgwOutgoingCursor(m.dbConf.getIgwoutgoing())
        m.getJson()
        m.sendRequest(m.lumosConf.getUrl())

