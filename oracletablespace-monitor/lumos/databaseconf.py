
import yaml
import os

try:
    open(os.getcwd()+"\lumos\conf\database.yml")   # will be a permission error
except IOError as e:
    print(os.strerror(e.errno))

from lumos.databasemodel import DatabaseModel

class DatabaseConf(DatabaseModel):

    _path = ""

    def __init__(self):
        print('--Database Conf Constructor')
        super().__init__()

    def setPath(self, path):
        self._path = path

    def getPath(self):
        return self._path


    def readDatabaseYaml(self):
        with open(self._path, 'r') as cfgFile:
            cfg = yaml.load(cfgFile)
            self.setPath(self._path)
            self.setHost(cfg['oracle']['host'])
            self.setSql(cfg['oracle']['sql'])
            self.setHostIP(cfg['oracle']['hostIP'])



