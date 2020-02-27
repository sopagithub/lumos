
import cx_Oracle

class DatabaseConnection:

    def getDBConnection(self, host):
        return cx_Oracle.connect(host)