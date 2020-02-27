__author__ = 'marjan'

import cx_Oracle
from abc import ABCMeta, abstractmethod
import yaml
from query import *
import logging.config
import json
import uuid
import requests


# Abstract base class or Interface for any further enhancement
class BaseConnection:
    __metaclass__ = ABCMeta

    @abstractmethod
    def con(self, query):
        pass

# For getting DB Connection
class DbConnection(BaseConnection):
    def __init__(self, conf):
        self.connection = cx_Oracle.connect(conf["oracle"]["user"], conf["oracle"]["password"], conf["oracle"]["url"], mode=cx_Oracle.SYSDBA)

    def con(self, query):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query)
                cursor = cursor.fetchall()
        except cx_Oracle.DatabaseError as odb:
            logging.error(odb)
        return cursor

# DB Configuration file
class DbConfig:
    @staticmethod
    def dbconfig():
        try:
            with open("config.yaml", 'r') as stream:
                conf = yaml.load(stream)
        except yaml.YAMLError as exc:
            logging.info(exc)
        return conf

# Logger Configuration file
class LoggerConfig:
    @staticmethod
    def config():
        try:
            with open('logger.yaml', 'r') as log:
                log = yaml.load(log)
        except yaml.YAMLError as exc:
            logging.info(exc)
        logging.config.dictConfig(log)

# Those calss is for getting Query result
class DbTableSpaceName:
    def __init__(self, dbConnection):
        self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["dbUniqueName"] = row[0]
            data.append(record)
        json.dumps(data)
        return data


class DbTableSpaceUsage:
    def __init__(self, dbConnection):
        self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["Tablespace"] = row[0]
            record["Size (MB)"] = row[1]
            record["Free (MB)"] = row[2]
            record["% Free"] = row[3]
            record["% Used"] = row[4]
            data.append(record)
        json.dumps(data)
        return data


class ReportGenerated:
    def __init__(self, dbConnection):
            self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["reportGeneratedOn"] = row[0]
            data.append(record)
        json.dumps(data)
        return data


class DisplayDbInformation:
    def __init__(self, dbConnection):
        self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["dbUniqueName"] = row[0]
            record["openMode"] = row[1]
            record["logMode"] = row[2]
            record["currentScn"] = row[3]
            record["flashBackOn"] = row[4]
            data.append(record)
        json.dumps(data)
        return data


class DisplayDbUpTime:
    def __init__(self, dbConnection):
            self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["databaseUpTime"] = row[0]
            data.append(record)
        json.dumps(data)
        return data


class LastPrimarySeqGenerated:
    def __init__(self, dbConnection):
            self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["thread#"] = row[0]
            record["lastPrimarySeqGenerated"] = row[1]
            data.append(record)
        json.dumps(data)
        return data


class LastStandBySeqRecv:
    def __init__(self, dbConnection):
            self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["thread#"] = row[0]
            record["lastStandBySeqRecv"] = row[1]
            data.append(record)
        json.dumps(data)
        return data


class ArchiveGap:
    def __init__(self, dbConnection):
            self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["archiveGap"] = row[0]
            data.append(record)
        json.dumps(data)
        return data


class DisplayADGStatus:
    def __init__(self, dbConnection):
            self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["process"] = row[0]
            record["thread#"] = row[1]
            record["sequence"] = row[2]
            record["status"] = row[3]
            data.append(record)
        json.dumps(data)
        return data


class DataGurdError:
    def __init__(self, dbConnection):
        self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["messageText"] = row[0]
            record["time"] = row[1]

            data.append(record)
        json.dumps(data)
        return data


class AlertLogError:
    def __init__(self, dbConnection):
        self.cursor = dbConnection

    def getResult(self, query):
        getQuery = self.cursor.con(query)
        data = []
        for row in getQuery:
            record = {}
            record["messageText"] = row[0]
            record["time"] = row[1]

            data.append(record)
        json.dumps(data)
        return data

if __name__ == '__main__':
    #Calling Logger & DB configuration
    LoggerConfig.config()
    db = DbConnection(DbConfig.dbconfig())

    # Creating object for query
    dbTableSpaceName = DbTableSpaceName(db)
    dbTableSpaceUsage = DbTableSpaceUsage(db)
    reportGenerated = ReportGenerated(db)
    dbInfo = DisplayDbInformation(db)
    dbUpTime = DisplayDbUpTime(db)
    primarySeqGenerated = LastPrimarySeqGenerated(db)
    standBySeqRecv = LastStandBySeqRecv(db)
    dbArchiveGap = ArchiveGap(db)
    adgsStatus = DisplayADGStatus(db)
    dataGurd = DataGurdError(db)
    alertLog = AlertLogError(db)

    # Executing object method for getting query result
    reportGen = reportGenerated.getResult(displaySysDate())
    dbName = dbTableSpaceName.getResult(dbName())
    tableSpaceUsage = dbTableSpaceUsage.getResult(tableSpaceUsage())
    displayDbInfo = dbInfo.getResult(displayDbInfo())
    displayDbUpTime = dbUpTime.getResult(displayDbUpTime())
    primarySeq = primarySeqGenerated.getResult(lastPrimarySeqGenerated())
    standBySeqRecv = standBySeqRecv.getResult(lastStandBySeqRecv())
    dbArchiveGap = dbArchiveGap.getResult(archiveGap())
    adgsStatus = adgsStatus.getResult(displayADGStatus())
    dataGurd = dataGurd.getResult(dataGurdError())
    alertLog = alertLog.getResult(alertLogError())

    # Looping through result list
    dbName = [i for i in dbName]
    tableSpaceUsage = [i for i in tableSpaceUsage]
    reportGen = [i for i in reportGen]
    displayDbInfo = [i for i in displayDbInfo]
    displayDbUpTime = [i for i in displayDbUpTime]
    primarySeq = [i for i in primarySeq]
    standBySeqRecv = [i for i in standBySeqRecv]
    dbArchiveGap = [i for i in dbArchiveGap]
    adgsStatus = [i for i in adgsStatus]
    dataGurd = [i for i in dataGurd]
    alertLog = [i for i in alertLog]

    # Merging query result with other info
    requestJSONDbName = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": dbName}
    requestJSONTableSpaceName = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": tableSpaceUsage}
    requestJSONreportGen = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": reportGen}
    requestJSONdbinfo = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": displayDbInfo}
    requestJSONdbUpTime = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": displayDbUpTime}
    requestJSONPrimarySeq = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": primarySeq}
    requestJSONstandBySeqRecv = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": standBySeqRecv}
    requestJSONdbArchiveGap = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": dbArchiveGap}
    requestJSONadgsStatus = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": adgsStatus}
    requestJSONdataGurd = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": dataGurd}
    requestJSONalertLog = {"requestID": uuid.uuid1().hex, "hostIP": DbConfig.dbconfig()["oracle"]["host"], "rawData": alertLog}

    #Posting result through requests method
    def sendRequest():
        return requests.post(url=DbConfig.dbconfig()["monitor"]["url"], data={"requestJSONDbName": requestJSONDbName,
                                                                              "requestJSONTableSpaceName": requestJSONTableSpaceName,
                                                                              "requestJSONreportGen": requestJSONreportGen,
                                                                              "requestJSONdbUpTime": requestJSONdbUpTime,
                                                                              "requestJSONdbinfo": requestJSONdbinfo,
                                                                              "requestJSONPrimarySeq": requestJSONPrimarySeq,
                                                                              "requestJSONstandBySeqRecv": requestJSONstandBySeqRecv,
                                                                              "requestJSONdbArchiveGap": requestJSONdbArchiveGap,
                                                                              "requestJSONadgsStatus": requestJSONadgsStatus,
                                                                              "requestJSONdataGurd": requestJSONdataGurd,
                                                                              "requestJSONalertLog": requestJSONalertLog}, headers = {'Content-Type':'application/json'})
    sendRequest()

    # Printing log in console & log file
    logging.info("Get json value " + str(requestJSONDbName))
    logging.info("Get json value " + str(requestJSONTableSpaceName))
    logging.info("Get json value " + str(requestJSONreportGen))
    logging.info("Get json value " + str(requestJSONdbUpTime))
    logging.info("Get json value " + str(requestJSONdbinfo))
    logging.info("Get json value " + str(requestJSONPrimarySeq))
    logging.info("Get json value " + str(requestJSONstandBySeqRecv))
    logging.info("Get json value " + str(requestJSONdbArchiveGap))
    logging.info("Get json value " + str(requestJSONadgsStatus))
    logging.info("Get json value " + str(requestJSONdataGurd))
    logging.info("Get json value " + str(requestJSONalertLog))
