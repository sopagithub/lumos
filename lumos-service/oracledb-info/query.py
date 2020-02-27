__author__ = 'marjan'

def tableSpaceUsage():
    return """SELECT /* + RULE */ df.tablespace_name "Tablespace",
                df.bytes / (1024 * 1024) "Size (MB)",
                SUM(fs.bytes) / (1024 * 1024) "Free (MB)",
                Nvl(Round(SUM(fs.bytes) * 100 / df.bytes),1) "% Free",
                Round((df.bytes - SUM(fs.bytes)) * 100 / df.bytes) "% Used"
                FROM dba_free_space fs,
                (SELECT tablespace_name,SUM(bytes) bytes
                FROM dba_data_files
                GROUP BY tablespace_name) df
                WHERE fs.tablespace_name (+) = df.tablespace_name
                GROUP BY df.tablespace_name,df.bytes
                UNION ALL
                SELECT /* + RULE */ df.tablespace_name tspace,
                fs.bytes / (1024 * 1024),
                SUM(df.bytes_free) / (1024 * 1024),
                Nvl(Round((SUM(fs.bytes) - df.bytes_used) * 100 / fs.bytes), 1),
                Round((SUM(fs.bytes) - df.bytes_free) * 100 / fs.bytes)
                FROM dba_temp_files fs,
                (SELECT tablespace_name,bytes_free,bytes_used
                FROM v$temp_space_header
                GROUP BY tablespace_name,bytes_free,bytes_used) df
                WHERE fs.tablespace_name (+) = df.tablespace_name
                GROUP BY df.tablespace_name,fs.bytes,df.bytes_free,df.bytes_used
                ORDER BY 4 DESC"""


def dbName():
    return """select value || '_' output
              from v$parameter where name = 'db_unique_name' """

def displaySysDate():
    return """SELECT TO_CHAR(sysdate) "REPORT GENERATED ON" FROM dual"""

def displayDbInfo():
    return """SELECT  DB_UNIQUE_NAME,open_mode,log_mode,current_scn, flashback_on FROM v$database"""

def displayDbUpTime():
    return """SELECT 'The database ' || instance_name ||
              'has been running since ' || to_char(startup_time, 'HH24:MI MM/DD/YYYY') "DATABASE UP TIME"
              FROM v$instance"""

def lastPrimarySeqGenerated():
    return """select thread#, max(sequence#) "Last Primary Seq Generated"
              from v$archived_log val, v$database vdb
              where val.resetlogs_change# = vdb.resetlogs_change#
              group by thread# order by 1"""

def lastStandBySeqRecv():
    return """select thread#, max(sequence#) "Last Standby Seq Received"
              from v$archived_log val, v$database vdb
              where val.resetlogs_change# = vdb.resetlogs_change#
              group by thread# order by 1"""

def archiveGap():
    return """select * from v$archive_gap"""

def displayADGStatus():
    return """SELECT PROCESS,THREAD#,sequence#,status FROM V$MANAGED_STANDBY WHERE PROCESS LIKE 'MRP%'"""

def dataGurdError():
    return """select DISTINCT  message_text,to_char(ORIGINATING_TIMESTAMP,'HH24:MI:SS') TIME from  sys.x$dbgalertext
              where  originating_timestamp >  sysdate-1/24 and message_text like '%CORRUPTION DETECTED%' order by 1"""

def alertLogError():
    return """select  DISTINCT  message_text, to_char(ORIGINATING_TIMESTAMP,'HH24:MI:SS') TIME
              from   sys.x$dbgalertext where  originating_timestamp >  sysdate-1 and message_text like '%ORA-%' order by 1"""