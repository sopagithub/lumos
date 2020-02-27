
class LumosModel(object):

    _url = ""
    _hostIP = ""

    def _init_(self):
        print("--Lumos Model Constructor")

    def setUrl(self, url):
        self._url = url

    def getUrl(self):
        return self._url

    def setHostIP(self, hostIP):
        self._hostIP = hostIP

    def getHostIP(self):
        return self._hostIP
