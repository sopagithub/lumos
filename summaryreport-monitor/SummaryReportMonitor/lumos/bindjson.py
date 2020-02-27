import json
import datetime
from datetime import date, timedelta

class BindJSON:

    currentDate = datetime.datetime.now().date();
    yesterdayDate = str(date.today() - timedelta(days=1))
    reportDateRange = yesterdayDate + " 00:00:00 " + yesterdayDate + " 23:59:59"

    def setAnsIncomingJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['ansIncomingPartnerName'] = row[0]
            rowData['ansIncomingTotalcall'] = "{:.2f}".format(row[1])
            rowData['ansIncomingSuccssCall'] = "{:.2f}".format(row[2])
            rowData['ansIncomingFailedCall'] = "{:.2f}".format(row[3])
            rowData['ansIncomingActualDuration'] = "{:.2f}".format(row[4])
            rowData['ansIncomingRoundedDuration'] = "{:.2f}".format(row[5])
            rowData['ansIncomingACD'] = "{:.2f}".format(row[6])
            rowData['ansIncomingASR'] = "{:.2f}".format(row[7])
            rowData['ansIncomingCurrentDate'] = str(self.currentDate)
            rowData['ansIncomingReportDateRange'] = str(self.reportDateRange)
            data.append(rowData)
        return json.dumps(data)

    def setIcxIncomingJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['icxIncomingPartnerName'] = row[0]
            rowData['icxIncomingTotalcall'] = "{:.2f}".format(row[1])
            rowData['icxIncomingSuccssCall'] = "{:.2f}".format(row[2])
            rowData['icxIncomingFailedCall'] = "{:.2f}".format(row[3])
            rowData['icxIncomingActualDuration'] = "{:.2f}".format(row[4])
            rowData['icxIncomingRoundedDuration'] = "{:.2f}".format(row[5])
            rowData['icxIncomingACD'] = "{:.2f}".format(row[6])
            rowData['icxIncomingASR'] = "{:.2f}".format(row[7])
            rowData['icxIncomingCurrentDate'] = str(self.currentDate)
            rowData['icxIncomingReportDateRange'] = str(self.reportDateRange)
            data.append(rowData)
        return json.dumps(data)

    def setIgwIncomingJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['igwIncomingPartnerName'] = row[0]
            rowData['igwIncomingTotalcall'] = "{:.2f}".format(row[1])
            rowData['igwIncomingSuccssCall'] = "{:.2f}".format(row[2])
            rowData['igwIncomingFailedCall'] = "{:.2f}".format(row[3])
            rowData['igwIncomingActualDuration'] = "{:.2f}".format(row[4])
            rowData['igwIncomingRoundedDuration'] = "{:.2f}".format(row[5])
            rowData['igwIncomingACD'] = "{:.2f}".format(row[6])
            rowData['igwIncomingASR'] = "{:.2f}".format(row[7])
            rowData['igwIncomingCurrentDate'] = str(self.currentDate)
            rowData['igwIncomingReportDateRange'] = str(self.reportDateRange)
            data.append(rowData)
        return json.dumps(data)

    def setAnsOutgoingJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['ansOutgoingPartnername'] = row[0]
            rowData['ansOutgoingTotalcall'] = "{:.2f}".format(row[1])
            rowData['ansOutgoingSuccssCall'] = "{:.2f}".format(row[2])
            rowData['ansOutgoingFailedCall'] = "{:.2f}".format(row[3])
            rowData['ansOutgoingActualDuration'] = "{:.2f}".format(row[4])
            rowData['ansOutgoingRoundedDuration'] = "{:.2f}".format(row[5])
            rowData['ansOutgoingPulseDuration'] = "{:.2f}".format(row[6])
            rowData['ansOutgoingACD'] = "{:.2f}".format(row[7])
            rowData['ansOutgoingASR'] = "{:.2f}".format(row[8])
            rowData['ansOutgoingCurrentDate'] = str(self.currentDate)
            rowData['ansOutgoingReportDateRange'] = str(self.reportDateRange)
            data.append(rowData)
        return json.dumps(data)

    def setIcxOutgoingJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['icxOutgoingPartnername'] = row[0]
            rowData['icxOutgoingTotalcall'] = "{:.2f}".format(row[1])
            rowData['icxOutgoingSuccssCall'] = "{:.2f}".format(row[2])
            rowData['icxOutgoingFailedCall'] = "{:.2f}".format(row[3])
            rowData['icxOutgoingActualDuration'] = "{:.2f}".format(row[4])
            rowData['icxOutgoingRoundedDuration'] = "{:.2f}".format(row[5])
            rowData['icxOutgoingPulseDuration'] = "{:.2f}".format(row[6])
            rowData['icxOutgoingACD'] = "{:.2f}".format(row[7])
            rowData['icxOutgoingASR'] = "{:.2f}".format(row[8])
            rowData['icxOutgoingCurrentDate'] = str(self.currentDate)
            rowData['icxOutgoingReportDateRange'] = str(self.reportDateRange)
            data.append(rowData)
        return json.dumps(data)

    def setIgwOutgoingJSON(self, cursor):
        rows = [x for x in cursor]
        data = []
        for row in rows:
            rowData = {}
            rowData['igwOutgoingPartnername'] = row[0]
            rowData['igwOutgoingTotalcall'] = "{:.2f}".format(row[1])
            rowData['igwOutgoingSuccssCall'] = "{:.2f}".format(row[2])
            rowData['igwOutgoingFailedCall'] = "{:.2f}".format(row[3])
            rowData['igwOutgoingActualDuration'] = "{:.2f}".format(row[4])
            rowData['igwOutgoingRoundedDuration'] = "{:.2f}".format(row[5])
            rowData['igwOutgoingPulseDuration'] = "{:.2f}".format(row[6])
            rowData['igwOutgoingACD'] = "{:.2f}".format(row[7])
            rowData['igwOutgoingASR'] = "{:.2f}".format(row[8])
            rowData['igwOutgoingCurrentDate'] = str(self.currentDate)
            rowData['igwOutgoingReportDateRange'] = str(self.reportDateRange)
            data.append(rowData)
        return json.dumps(data)