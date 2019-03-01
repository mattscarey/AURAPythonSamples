__author__ = 'Matthew'

import sys
sys.path.insert(0, '-REDACTED-/Alpha Stock Miner/Utilities/')
from Utilities import Utilities

WWWROOT = r'/var/www/html/'
SMROOT = r'-REDACTED-/Alpha Stock Miner/Data Files/'

BTINDEX = WWWROOT + "btl.html"
BTINDEXHEAD = SMROOT + "btindexhead.txt"
BTINDEXFOOT = SMROOT + "btindexfoot.txt"

HEAD = SMROOT + "btloghead.txt"
FOOT = SMROOT + "logfoot.txt"

#This class builds an html page for a backtest
class BackTestLogs:

    def __init__(self):
        self.utils = Utilities()

    def getLogIds(self):
        cursor = self.cnx.cursor()
        statement = "SELECT log_id FROM log;"
        cursor.execute(statement)

        ids = []
        for (value) in cursor:
            ids.append(value[0])

        cursor.close()
        return ids

    def generateLogs(self):

        self.cnx = self.utils.getConnection()
        indexHead = self.utils.getText(BTINDEXHEAD)
        indexFoot = self.utils.getText(BTINDEXFOOT)

        indexText = indexHead

        ids = self.getLogIds()
        id = ids[len(ids)-1]
        #for id in ids[::-1]:
        sectionText = '<div class="well well-lg"><h4>Back Test ID# ' + str(id) + '</h4><ul>\n'
        sectionText+= '<li><a href="ml' + str(id) + '.html">Main Log</a></li>\n'
        self.generateMainLog(id)
        sectionText+= '<li><a href="scrl' + str(id) + '.html">Scripting Log</a></li>\n'
        self.generateScrLog(id)
        sectionText+= '<li><a href="accl' + str(id) + '.html">Account Log</a></li>\n'
        self.generateAccountLog(id)
        sectionText+= '<li><a href="btl' + str(id) + '.html">Back Tester Log</a></li>\n'
        self.generateBackTestLog(id)
        sectionText+= '<li><a href="invl' + str(id) + '.html">Investor Log</a></li>\n'
        self.generateInvestorLog(id)
        sectionText+= '<li><a href="errl' + str(id) + '.html">Error Log</a></li>\n'
        self.generateErrorLog(id)
        sectionText+= '<li><a href="conl' + str(id) + '.html">Configuration Log</a></li>\n'
        self.generateConfigLog(id)
        sectionText += '</ul>\n</div>\n<br/>'
        indexText += sectionText

        indexText += indexFoot
        with open(BTINDEX, "w") as f:
            f.write(indexText)
        self.cnx.close()


    def generateMainLog(self, id):

        logPath = WWWROOT + "ml" + str(id) + ".html"

        logHead = self.utils.getText(HEAD)
        logFoot = self.utils.getText(FOOT)

        logText = logHead
        logText += '<h2>Back Test ' + str(id) + ' Main Log</h2>'

        statement = "SELECT * FROM (" \
                    "SELECT * FROM scripting_log UNION ALL" \
                    " SELECT * FROM account_log UNION ALL" \
                    " SELECT * FROM backtester_log UNION ALL" \
                    " SELECT * FROM error_log UNION ALL" \
                    " SELECT * FROM configuration_log UNION ALL" \
                    " SELECT * FROM investor_log" \
                    ") as l WHERE log_id = " + str(id) + " ORDER BY time ASC;"

        #print(statement)
        cursor = self.cnx.cursor()
        cursor.execute(statement)

        for (value) in cursor:

            message = value[1]
            time = value[2]
            component = value[4]

            line = '<p>'
            line += '[' + str(time) + ']: ' + message + '</p>\n'
            logText += line

        logText += logFoot

        with open(logPath, "w") as f:
            f.write(logText)
        cursor.close()

    def generateScrLog(self, id):

        logPath = WWWROOT + "scrl" + str(id) + ".html"

        logHead = self.utils.getText(HEAD)
        logFoot = self.utils.getText(FOOT)

        logText = logHead
        logText += '<h2>Back Test ' + str(id) + ' Scripting Log</h2>'

        statement = "SELECT * FROM scripting_log WHERE log_id = " + str(id) + " ORDER BY time ASC;"
        cursor = self.cnx.cursor()
        cursor.execute(statement)

        for (value) in cursor:

            message = value[1]
            time = value[2]
            component = value[4]

            line = '<p>'
            line += '[' + str(time) + ']: ' + message + '</p>\n'
            logText += line

        logText += logFoot

        with open(logPath, "w") as f:
            f.write(logText)
        cursor.close()

    def generateConfigLog(self, id):
        logPath = WWWROOT + "conl" + str(id) + ".html"

        logHead = self.utils.getText(HEAD)
        logFoot = self.utils.getText(FOOT)

        logText = logHead
        logText += '<h2>Back Test ' + str(id) + ' Configuration Log</h2>'

        statement = "SELECT * FROM configuration_log WHERE log_id = " + str(id) + " ORDER BY time ASC;"
        cursor = self.cnx.cursor()
        cursor.execute(statement)

        for (value) in cursor:

            message = value[1]
            time = value[2]
            component = value[4]

            line = '<p>'
            line += '[' + str(time) + ']: ' + message + '</p>\n'
            logText += line

        logText += logFoot

        with open(logPath, "w") as f:
            f.write(logText)
        cursor.close()

    def generateBackTestLog(self, id):
        logPath = WWWROOT + "btl" + str(id) + ".html"

        logHead = self.utils.getText(HEAD)
        logFoot = self.utils.getText(FOOT)

        logText = logHead
        logText += '<h2>Back Test ' + str(id) + ' Back Tester Log</h2>'

        statement = "SELECT * FROM backtester_log WHERE log_id = " + str(id) + " ORDER BY time ASC;"
        cursor = self.cnx.cursor()
        cursor.execute(statement)

        for (value) in cursor:

            message = value[1]
            time = value[2]
            component = value[4]

            line = '<p>'
            line += '[' + str(time) + ']: ' + message + '</p>\n'
            logText += line

        logText += logFoot

        with open(logPath, "w") as f:
            f.write(logText)
        cursor.close()

    def generateInvestorLog(self, id):
        logPath = WWWROOT + "invl" + str(id) + ".html"

        logHead = self.utils.getText(HEAD)
        logFoot = self.utils.getText(FOOT)

        logText = logHead
        logText += '<h2>Back Test ' + str(id) + ' Investor Log</h2>'

        statement = "SELECT * FROM investor_log WHERE log_id = " + str(id) + " ORDER BY time ASC;"
        cursor = self.cnx.cursor()
        cursor.execute(statement)

        for (value) in cursor:

            message = value[1]
            time = value[2]
            component = value[4]

            line = '<p>'
            line += '[' + str(time) + ']: ' + message + '</p>\n'
            logText += line

        logText += logFoot

        with open(logPath, "w") as f:
            f.write(logText)
        cursor.close()

    def generateErrorLog(self, id):
        logPath = WWWROOT + "errl" + str(id) + ".html"

        logHead = self.utils.getText(HEAD)
        logFoot = self.utils.getText(FOOT)

        logText = logHead
        logText += '<h2>Back Test ' + str(id) + ' Error Log</h2>'

        statement = "SELECT * FROM error_log WHERE log_id = " + str(id) + " ORDER BY time ASC;"
        cursor = self.cnx.cursor()
        cursor.execute(statement)

        for (value) in cursor:

            message = value[1]
            time = value[2]
            component = value[4]

            line = '<p>'
            line += '[' + str(time) + ']: ' + message + '</p>\n'
            logText += line

        logText += logFoot

        with open(logPath, "w") as f:
            f.write(logText)
        cursor.close()

    def generateAccountLog(self, id):
        logPath = WWWROOT + "accl" + str(id) + ".html"

        logHead = self.utils.getText(HEAD)
        logFoot = self.utils.getText(FOOT)

        logText = logHead
        logText += '<h2>Back Test ' + str(id) + ' Account Log</h2>'

        statement = "SELECT * FROM account_log WHERE log_id = " + str(id) + " ORDER BY time ASC;"
        cursor = self.cnx.cursor()
        cursor.execute(statement)

        for (value) in cursor:

            message = value[1]
            time = value[2]
            component = value[4]

            line = '<p>'
            line += '[' + str(time) + ']: ' + message + '</p>\n'
            logText += line

        logText += logFoot

        with open(logPath, "w") as f:
            f.write(logText)
        cursor.close()

if __name__ == "__main__":
    btl = BackTestLogs()
    btl.generateLogs()