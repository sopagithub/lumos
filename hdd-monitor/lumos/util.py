

class Util(object):

    def convertToHumanReadable(self, bytes):
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i+1)*10
        for s in reversed(symbols):
            if bytes >= prefix[s]:
                value = float(bytes) / prefix[s]
                return '%.1f%s' % (value, s)
        return "%sB" % bytes

    def convertKbToMb(self, kilobyte):
        megabyte = float(0.000976562)
        mb = megabyte * kilobyte
        return mb

    def convertMbToGb(input_megabyte):
        gigabyte = float(9.5367431640625E-7)
        convert_gb = gigabyte * input_megabyte
        return convert_gb

    def covertByteToMb(self, byte):
        return round((byte /1024)/1024)