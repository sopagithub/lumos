
import yaml
import os
import datetime
from datetime import date, timedelta

try:
    open(os.getcwd()+"\lumos\conf\database.yml")   # will be a permission error
except IOError as e:
    print(os.strerror(e.errno))

from lumos.databasemodel import DatabaseModel

class DatabaseConf(DatabaseModel):

    _path = ""
    _query = ""
    _ansincoming = ""
    _icxincoming = ""
    _igwincoming = ""
    _ansoutgoing = ""
    _icxoutgoing = ""
    _igwoutgoing = ""


    def __init__(self):
        print('--Database Conf Constructor')
        super().__init__()

    def setPath(self, path):
        self._path = path

    def getPath(self):
        return self._path



    def readDatabaseYaml(self):
        yesterday = str(date.today() - timedelta(days=1))

        with open(self._path, 'r') as cfgFile:
            cfg = yaml.load(cfgFile)
            self.setPath(self._path)
            self.setHost(cfg['oracle']['host'])
            _ansincoming = cfg['oracle']['ansincomingsql']
            _ansincoming= _ansincoming.replace('Yesterday', yesterday)
            _icxincoming = cfg['oracle']['icxincomingsql']
            _icxincoming = _icxincoming.replace('Yesterday', yesterday)
            _igwincoming = cfg['oracle']['igwincomingsql']
            _igwincoming = _igwincoming.replace('Yesterday', yesterday)
            _ansoutgoing= cfg['oracle']['ansoutgoingsql']
            _ansoutgoing = _ansoutgoing.replace('Yesterday', yesterday)
            _icxoutgoing = cfg['oracle']['icxoutgoingsql']
            _icxoutgoing = _icxoutgoing.replace('Yesterday', yesterday)
            _igwoutgoing = cfg['oracle']['igwoutgoingsql']
            _igwoutgoing = _igwoutgoing.replace('Yesterday', yesterday)

            self.setAnsincoming(_ansincoming)
            self.setIcxincoming(_icxincoming)
            self.setIgwincoming(_igwincoming)
            self.setAnsoutgoing(_ansoutgoing)
            self.setIcxoutgoing(_icxoutgoing)
            self.setIgwoutgoing(_igwoutgoing)




