import json

class BindJSON:

    def setJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['tableSpaceName'] = row[0]
            rowData['totalMB'] = row[1]
            rowData['usedMB'] = row[2]
            rowData['freeMB'] = row[3]
            rowData['pctUsedSpace'] = row[4]
            rowData['pctFreeSpace'] = row[5]
            data.append(rowData)
        return json.dumps(data)