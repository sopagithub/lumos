
class DatabaseModel(object):

    _host = ""
    _hostIP = ""
    _sql = ""

    def _init_(self):
        print("--Database Model Constructor")

    def setHost(self, host):
        self._host = host

    def getHost(self):
        return self._host

    def setSql(self, sql):
        self._sql = sql

    def getSql(self):
        return self._sql

    def setHostIP(self, hostIP):
        self._hostIP = hostIP

    def getHostIP(self):
        return self._hostIP