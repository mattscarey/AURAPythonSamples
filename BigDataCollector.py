__author__ = 'Matthew'

import urllib2
import csv
import time
import datetime
import json

import mysql.connector
from mysql.connector import errorcode
import sys
from ValidateData import Validator

sys.path.insert(0, '-REDACTED-/Alpha Stock Miner/Utilities/')
from Utilities import Utilities

class DataCollector:

    #Requirements
        #must collect data for all NASDAQ and NYSE stocks
        #must log progress
        #must be able to run for a few weeks uninterrupted
        #must be able to handle errors in a way that minimizes loss of data
        #must be able to pick up where it left off after a crash


    def __init__(self,revalidate):
        self.log = '-REDACTED-/Alpha Stock Miner/Data Files/Logs/data_collector_log.txt'
        self.startDate = '-REDACTED-/Alpha Stock Miner/Data Files/dc_date.txt'
        self.utils = Utilities()
        self.validator = Validator()
        self.validation_report = {}
        self.revalidate = revalidate
        self.testing = True

        self.failures = []

        #--------
        self.CALLS_PER_MINUTE = 30
        #--------

        self.waitTime = 60 / self.CALLS_PER_MINUTE

    def start(self):

        #get all of the missing data points
        if self.revalidate:
            self.validation_report = self.validator.validate()
        else:
            self.validation_report = self.utils.validationReportData()

        tableData = self.utils.tableData

        connection = self.utils.getConnection()
        tickers = self.utils.getTickersOnly(connection)
        connection.close()

        #get all the stocks and start going through them
        for ticker in tickers:
            begin = self.utils.getTime()
            connection = self.utils.getConnection()
            cursor = connection.cursor()
            self.utils.addToLog(self.log, ticker, True)
            stock = self.validation_report[ticker]
            for indicator in stock: #go through each indicator that appears in the validation report
            #for indicator in self.utils.tableData:
                self.utils.addToLog(self.log, "  " + indicator, True)
                res = self.insertIndicator(ticker,tableData[indicator],indicator,cursor)
                if not res:
                    #skip ticker if one indicator fails
                    self.error("Failed to collect data for ticker: " + ticker, 3)
                    self.failures.append(ticker)
                    break

            if self.testing:
                pass
            else:
                connection.commit()
            connection.close()
            end = self.utils.getTime()
            totalTime = self.utils.timeBetween(begin,end)
            self.utils.addToLog(self.log, "Time to complete " + ticker + ": " + str(totalTime), True)

    #1 - INFO, 2 - WARNING, 3 - ERROR, 4 - FATAL
    def error(self, message, level):
        levels = ["INFO", "WARNING", "ERROR", "FATAL"]
        self.utils.addToLog(self.log, levels[level - 1] + " - " + message, True)



    def insertIndicator(self, ticker, data, table, cursor):
            techAnalysis = data[0]
            url1 = data[1]
            url2 = data[2]
            params = data[3]
            sym = ticker
            urlComplete = url1 + sym + url2
            passed = False
            tryCount = 0
            while not passed:
                try:
                    tryCount += 1
                    count = 0
                    req = urllib2.Request(url=urlComplete)
                    f = urllib2.urlopen(req)

                    time.sleep(self.waitTime)

                    data = json.loads(f.read())
                    if "Information" in data:
                        print("too many calls")
                        print(data)
                    else:
                        dayData = data[techAnalysis]
                        for key in dayData:
                            date = key
                            if date in self.validation_report[ticker][table]:
                                dataPoints = {}
                                count += 1
                                for param in params:
                                    dataPoints[param] = dayData[key][param]
                                statement = "INSERT INTO " + table + "(stock_id,date,"
                                cols = []
                                for pointKey in dataPoints:
                                    cols.append(self.utils.paramToCol(pointKey))
                                subStatement = '(SELECT id FROM stocks WHERE ticker = "' + ticker + '")'
                                statement += ",".join(cols) + ') VALUES (' + subStatement + ',STR_TO_DATE("' + date + '","' + self.utils.apitimeformat + '"),'

                                colData = []
                                for pointKey in dataPoints:
                                    colData.append('"' + dataPoints[pointKey] + '"')
                                statement += ",".join(colData) + ");"

                                res = cursor.execute(statement)
                        passed = True
                        self.utils.addToLog(self.log,"  Total added: " + str(count),True)
                        return True

                except Exception as e:
                    self.error("Collection try failed with ticker " + ticker + " on indicator " + table + ". Try number " + str(tryCount), 2)

                    time.sleep(1)
                    if tryCount > 20:
                        passed = True
                        tryCount = 0
                        return False


if __name__ == "__main__":

    dc = DataCollector(False)
    dc.start()
