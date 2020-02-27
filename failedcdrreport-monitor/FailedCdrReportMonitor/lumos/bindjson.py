import json
from datetime import datetime

class BindJSON:

    def setJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['ratingfailurereason'] = row[0]
            rowData['sequenceNumber'] = row[1]
            rowData['callingPartyID'] = row[2]
            rowData['calledPartyID'] = row[3]
            rowData['originatingDateTime'] = row[4].strftime('%Y-%m-%d %H:%M:%S')
            rowData['disconnectDateTime'] = row[5].strftime('%Y-%m-%d %H:%M:%S')
            rowData['callDuration'] = "{:.2f}".format(row[6])
            rowData['origtrunkgroupclli'] = row[7]
            rowData['termtrunkgroupclli'] = row[8]
            data.append(rowData)
        return json.dumps(data)