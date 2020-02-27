
class DatabaseModel(object):

    _host = ""
    _ansincoming = ""
    _icxincoming = ""
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

    def setAnsincoming(self, ansincoming):
        self._ansincoming = ansincoming

    def getAnsincoming(self):
        return self._ansincoming

    def setIcxincoming(self, icxincoming):
        self._icxincoming = icxincoming

    def getIcxincoming(self):
        return self._icxincoming

    def setIgwincoming(self, igwincoming):
        self._igwincoming = igwincoming

    def getIgwincoming(self):
        return self._igwincoming

    def setAnsoutgoing(self, ansoutgoing):
        self._ansoutgoing = ansoutgoing

    def getAnsoutgoing(self):
        return self._ansoutgoing

    def setIcxoutgoing(self, icxoutgoing):
        self._icxoutgoing = icxoutgoing

    def getIcxoutgoing(self):
        return self._icxoutgoing

    def setIgwoutgoing(self, igwoutgoing):
        self._igwoutgoing = igwoutgoing

    def getIgwoutgoing(self):
        return self._igwoutgoing









