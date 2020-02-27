from apscheduler.schedulers.blocking import BlockingScheduler
import logging.config
import json
import os
import yaml
from sys import platform
import cx_Oracle
import requests
from random import randrange
import socket

sched = BlockingScheduler()

class OracleDao(object):

    def __init__(self, config):
        self.connection = cx_Oracle.connect(config['rdbms']['username'], config['rdbms']['password'], config['rdbms']['url'], mode=cx_Oracle.SYSDBA)

    def getData(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def commit(self):
        return self.connection.close()


def loadLoggingConfiguration():
    if 'win' in platform:
        logging.config.fileConfig(''.join([os.getcwd(),'\\conf\\logging.conf']))
    if 'linux' in platform:
        logging.config.fileConfig(''.join([os.getcwd(),'/conf/logging.conf']))


def loadConfiguration():
    if 'win' in platform:
        f = open(''.join([os.getcwd(),'\\conf\\config.yaml']), "r")
    if 'linux' in platform:
        f = open(''.join([os.getcwd(),'/conf/config.yaml']), "r")
    config = yaml.safe_load(f)
    return config

#To add a job to be run immediately:
# The 'date' trigger and datetime.now() as run_date are implicit
#sched.add_job(my_job, args=['text'])
@sched.scheduled_job(trigger='cron', hour='08', minute='00')
#@sched.scheduled_job('interval', seconds=5)
def collectData():

    rawData = {}

    # 1. Report Generated Date SQL
    result = dao.getData(config['reqportGeneratedDateSQL'])
    rawData["reqportGeneratedDate"] = result[0][0]
    logging.info("SQL-1 : "+rawData["reqportGeneratedDate"])

    # 2. Database Status SQL
    result = dao.getData(config['databaseStatusSQL'])
    for row in result:
        record = {}
        record["dbUniqueName"] = row[0]
        record["openMode"] = row[1]
        record["logMode"] = row[2]
        record["currentSCN"] = row[3]
        record["flashbackOn"] = row[4]
        rawData["databaseStatus"] = record
    logging.info("SQL-2 : "+json.dumps(rawData["databaseStatus"]))

    # 3. Report Generated Date SQL
    result = dao.getData(config['databaseUPTimeSQL'])
    rawData["databaseUPTime"] = result[0][0]
    logging.info("SQL-3 : "+rawData["databaseUPTime"])

    # 4. Tablespace SQL
    result = dao.getData(config['tablespaceSQL'])
    tablespaceList = []
    for row in result:
        record = {}
        record["tablespaceName"] = row[0]
        record["sizeInMB"] = row[1]
        record["freeInMB"] = row[2]
        record["freeInPct"] = row[3]
        record["usedInPct"] = row[4]
        tablespaceList.append(record)
    rawData["tablespaceList"] = tablespaceList
    logging.info("SQL-4 : "+json.dumps(rawData["tablespaceList"]))

    # 5. Primary Sequence Generate SQL
    result = dao.getData(config['primarySequenceSQL'])
    primarySequenceList = []
    for row in result:
        record = {}
        record["threadName"] = row[0]
        record["sequenceNo"] = row[1]
        primarySequenceList.append(record)
    rawData["primarySequenceList"] = primarySequenceList
    logging.info("SQL-5 : "+json.dumps(rawData["primarySequenceList"]))

    # 6. Standby Sequence Rerceived SQL
    result = dao.getData(config['standbySequenceReceivedSQL'])
    standbySequenceReceivedList = []
    for row in result:
        record = {}
        record["threadName"] = row[0]
        record["sequenceNo"] = row[1]
        standbySequenceReceivedList.append(record)
    rawData["standbySequenceReceivedList"] = standbySequenceReceivedList
    logging.info("SQL-6 : " + json.dumps(rawData["standbySequenceReceivedList"]))

    # 7. Standby Sequence Applied SQL
    result = dao.getData(config['standbySequenceAppliedSQL'])
    standbySequenceAppliedList = []
    for row in result:
        record = {}
        record["threadName"] = row[0]
        record["sequenceNo"] = row[1]
        standbySequenceAppliedList.append(record)
    rawData["standbySequenceAppliedList"] = standbySequenceAppliedList
    logging.info("SQL-7 : " + json.dumps(rawData["standbySequenceAppliedList"]))

    # 8. Data Guard Gap Status SQL
    result = dao.getData(config['dataGuardGapStatusSQL'])
    dataGuardGapStatusList = []
    for row in result:
        record = {}
        record["threadName"] = row[0]
        record["lowSequence"] = row[1]
        record["highSequence"] = row[2]
        dataGuardGapStatusList.append(record)
    rawData["dataGuardGapStatusList"] = dataGuardGapStatusList
    logging.info("SQL-8 : " + json.dumps(rawData["dataGuardGapStatusList"]))

    # 9. Data Guard Process Status SQL
    result = dao.getData(config['dataGuardProcessStatusSQL'])
    dataGuardProcessStatusList = []
    for row in result:
        record = {}
        record["process"] = row[0]
        record["threadName"] = row[1]
        record["sequenceNo"] = row[0]
        record["stat"] = row[1]
        dataGuardProcessStatusList.append(record)
    rawData["dataGuardProcessStatusList"] = dataGuardProcessStatusList
    logging.info("SQL-9 : " + json.dumps(rawData["dataGuardProcessStatusList"]))

    # 10. Rman Backup Information
    def date_handler(obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    result = dao.getData(config['rmanBackupInformationSQL'])
    rmanBackupInformationList = []
    for row in result:
        record = {}
        record["sKey"] = row[0]
        record["iType"] = row[1]
        record["stat"] = row[2]
        record["sTime"] = row[3]
        record["eTime"] = row[4]
        record["hrs"] = row[5]
        rmanBackupInformationList.append(record)
    rawData["rmanBackupInformationList"] = rmanBackupInformationList
    logging.info("SQL-10 : " + json.dumps(rawData["rmanBackupInformationList"], default=date_handler))

    # 11. DB-Node Backup Status
    result = dao.getData(config['dbNodeBackupStatusSQL'])
    dbNodeBackupStatusList = []
    for row in result:
        record = {}
        record["cTime"] = row[0]
        record["backupType"] = row[1]
        record["sizeInGB"] = row[2]
        dbNodeBackupStatusList.append(record)
    rawData["dbNodeBackupStatusList"] = dbNodeBackupStatusList
    logging.info("SQL-11 : " + json.dumps(rawData["dbNodeBackupStatusList"]))

    # 12. Data Guard Error Last One Hour SQL
    result = dao.getData(config['dataGuardErrorLastOneHourSQL'])
    dataGuardErrorLastOneHourList = []
    for row in result:
        record = {}
        record["msgTxt"] = row[0]
        record["sTime"] = row[1]
        dataGuardErrorLastOneHourList.append(record)
    rawData["dataGuardErrorLastOneHourList"] = dataGuardErrorLastOneHourList
    logging.info("SQL-12 : " + json.dumps(rawData["dataGuardErrorLastOneHourList"]))

    # 13. Alert Log Error Last One Day SQL
    result = dao.getData(config['alertLogErrorLastOneDaySQL'])
    alertLogErrorLastOneDayList = []
    for row in result:
        record = {}
        record["msgTxt"] = row[0]
        record["sTime"] = row[1]
        alertLogErrorLastOneDayList.append(record)
    rawData["alertLogErrorLastOneDayList"] = alertLogErrorLastOneDayList
    logging.info("SQL-13 : " + json.dumps(rawData["alertLogErrorLastOneDayList"]))

    # Print Raw Data
    logging.info("Raw Data : "+json.dumps(rawData))

    requestObj = { "requestID" : randrange(0, 10000000), "hostIP" : socket.gethostbyname(socket.gethostname()), "rawData" : json.dumps(rawData) }
    logging.info("Request Object : "+json.dumps(requestObj))
    response = requests.post(config['collectorURL'], json.dumps(requestObj), headers = {'Content-Type':'application/json'})
    #response.connection.close()
    if(response.status_code != 200):
        logging.warn("Response Code : " + response.status_code)
        logging.error("Unable to send request : " + response.raise_for_status())
        return

    logging.info("Response Code : " + str(response.status_code))
    logging.info("Response Text : " + response.text)

    result = json.loads(response.text)

    if(result['success']):
        logging.info("Response Message from Collector : " + result['message'])
    else:
        logging.warn("Response Message from Collector : " + result['message'])

if __name__ == '__main__':

    loadLoggingConfiguration()
    config = loadConfiguration()
    dao = OracleDao(config)
    sched.start()
