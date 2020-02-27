
import yaml
import os

try:
    open(os.getcwd()+"\lumos\conf\lumos.yml")   # will be a permission error
except IOError as e:
    print(os.strerror(e.errno))

from lumos.lumosmodel import LumosModel

class LumosConf(LumosModel):

    _path = ""

    def __init__(self):
        print('--Lumos Conf Constructor')
        super().__init__()

    def setPath(self, path):
        self._path = path

    def getPath(self):
        return self._path


    def readLumosYaml(self):
        with open(self._path, 'r') as cfgF:
            cfg = yaml.load(cfgF)
            self.setUrl(cfg['monitor']['url'])



