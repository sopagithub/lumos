
class LumosModel(object):

    _url = ""

    def _init_(self):
        print("--Lumos Model Constructor")

    def setUrl(self, url):
        self._url = url

    def getUrl(self):
        return self._url