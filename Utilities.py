__author__ = 'Matthew'

import mysql.connector
import urllib, json, sys, time

import datetime
from StatusUpdater import Updater

class Utilities:

    def __init__(self):
        self.second = 1
        self.minute = self.second * 60
        self.hour = self.minute * 60
        self.day = self.hour * 24
        self.apikey = "-REDACTED-"
        self.apikey2 = "-REDACTED-"
        self.rootdir = r'-REDACTED-/Alpha Stock Miner/'
        self.apitimeformat = "%Y-%m-%d"
        self.startday = "2001-01-02"

        self.sortedDates = []
        self.sortedDatesString = []
        self.useSortedDates = False
        self.useSortedDatesString = False

        self.startdayobj = datetime.datetime.strptime(self.startday, self.apitimeformat)
        self.updater = Updater()
        self.tableData = {
            "ad": ["Technical Analysis: Chaikin A/D", "https://www.alphavantage.co/query?function=AD&symbol=", "&interval=daily&apikey=" + self.apikey, ["Chaikin A/D"]],

            "adx": ["Technical Analysis: ADX", "https://www.alphavantage.co/query?function=ADX&symbol=", "&interval=daily&time_period=14&apikey=" + self.apikey, ["ADX"]],

            "apo": ["Technical Analysis: APO", "https://www.alphavantage.co/query?function=APO&symbol=", "&interval=daily&series_type=close&fastperiod=12&slowperiod=26&matype=0&apikey=" + self.apikey, ["APO"]],

            "aroon": ["Technical Analysis: AROON", "https://www.alphavantage.co/query?function=AROON&symbol=", "&interval=daily&time_period=14&apikey=" + self.apikey, ["Aroon Down", "Aroon Up"]],

            "bbands": ["Technical Analysis: BBANDS", "https://www.alphavantage.co/query?function=BBANDS&symbol=", "&interval=daily&time_period=21&series_type=close&nbdevup=2&nbdevdn=2&apikey=" + self.apikey, ["Real Middle Band", "Real Lower Band", "Real Upper Band"]],

            "cci": ["Technical Analysis: CCI", "https://www.alphavantage.co/query?function=CCI&symbol=", "&interval=daily&time_period=20&apikey=" + self.apikey, ["CCI"]],

            "cmo": ["Technical Analysis: CMO", "https://www.alphavantage.co/query?function=CMO&symbol=", "&interval=daily&time_period=10&series_type=close&apikey=" + self.apikey, ["CMO"]],

            "dx": ["Technical Analysis: DX", "https://www.alphavantage.co/query?function=DX&symbol=", "&interval=daily&time_period=14&apikey=" + self.apikey, ["DX"]],

            "ema12": ["Technical Analysis: EMA", "https://www.alphavantage.co/query?function=EMA&symbol=", "&interval=daily&time_period=12&series_type=close&apikey=" + self.apikey, ["EMA"]],

            "ema26": ["Technical Analysis: EMA", "https://www.alphavantage.co/query?function=EMA&symbol=", "&interval=daily&time_period=26&series_type=close&apikey=" + self.apikey, ["EMA"]],

            "ht_trendline": ["Technical Analysis: HT_TRENDLINE", "https://www.alphavantage.co/query?function=HT_TRENDLINE&symbol=", "&interval=daily&series_type=close&apikey=" + self.apikey, ["HT_TRENDLINE"]],

            "macd": ["Technical Analysis: MACD", "https://www.alphavantage.co/query?function=MACD&symbol=", "&interval=daily&series_type=close&apikey=" + self.apikey, ["MACD_Hist", "MACD_Signal", "MACD"]],

            "macdext": ["Technical Analysis: MACDEXT", "https://www.alphavantage.co/query?function=MACDEXT&symbol=", "&interval=daily&series_type=close&fastmatype=4&slowmatype=4&signalmatype=4&apikey=" + self.apikey, ["MACD_Hist", "MACD_Signal", "MACD"]],

            "mfi": ["Technical Analysis: MFI", "https://www.alphavantage.co/query?function=MFI&symbol=", "&interval=daily&time_period=10&apikey=" + self.apikey, ["MFI"]],

            "mom": ["Technical Analysis: MOM", "https://www.alphavantage.co/query?function=MOM&symbol=", "&interval=daily&time_period=10&series_type=close&apikey=" + self.apikey, ["MOM"]],

            "obv": ["Technical Analysis: OBV", "https://www.alphavantage.co/query?function=OBV&symbol=", "&interval=daily&apikey=" + self.apikey, ["OBV"]],

            "rsi": ["Technical Analysis: RSI", "https://www.alphavantage.co/query?function=RSI&symbol=", "&interval=daily&time_period=14&series_type=close&apikey=" + self.apikey, ["RSI"]],

            "stoch": ["Technical Analysis: STOCH", "https://www.alphavantage.co/query?function=STOCH&symbol=", "&interval=daily&apikey=" + self.apikey, ["SlowD", "SlowK"]],

            "stochrsi": ["Technical Analysis: STOCHRSI", "https://www.alphavantage.co/query?function=STOCHRSI&symbol=", "&interval=daily&time_period=10&series_type=close&fastkperiod=6&fastdmatype=1&apikey=" + self.apikey, ["FastD", "FastK"]],

            "t3": ["Technical Analysis: T3", "https://www.alphavantage.co/query?function=T3&symbol=", "&interval=daily&time_period=10&series_type=close&apikey=" + self.apikey, ["T3"]],

            "willr": ["Technical Analysis: WILLR", "https://www.alphavantage.co/query?function=WILLR&symbol=", "&interval=daily&time_period=14&apikey=" + self.apikey, ["WILLR"]],

            "wma": ["Technical Analysis: WMA", "https://www.alphavantage.co/query?function=WMA&symbol=", "&interval=daily&time_period=10&series_type=close&apikey=" + self.apikey, ["WMA"]],

            "basic": ["Time Series (Daily)", "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=", "&outputsize=full&apikey=" + self.apikey, ["1. open", "4. close", "2. high", "3. low", "5. volume"]],

            "sma7": ["Technical Analysis: SMA", "https://www.alphavantage.co/query?function=SMA&symbol=", "&interval=daily&time_period=7&series_type=close&apikey=" + self.apikey, ["SMA"]],

            "sma30": ["Technical Analysis: SMA", "https://www.alphavantage.co/query?function=SMA&symbol=", "&interval=daily&time_period=30&series_type=close&apikey=" + self.apikey, ["SMA"]],

            "sma180": ["Technical Analysis: SMA", "https://www.alphavantage.co/query?function=SMA&symbol=", "&interval=daily&time_period=180&series_type=close&apikey=" + self.apikey, ["SMA"]],

        }

    def getTickers(self, connection):
        cursor = connection.cursor()
        statement = "SELECT * FROM stocks;"
        cursor.execute(statement)
        tickers = []
        for (value) in cursor:
            ticker = value[1]
            id = value[0]
            tickers.append([id,ticker])
        cursor.close()
        return tickers

    def regenValidDays(self):
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=daily&time_period=10&series_type=open&apikey=" + self.apikey
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        smaData = data["Technical Analysis: SMA"]

        count = 0
        validDays = set([])

        for day in smaData:
            #if the market is open we need to split the date and take the first element only
            if self.isMarketOpen() and day.split(" ")[0] == datetime.datetime.now().strftime(self.apitimeformat):
                day = day.split(" ")[0]

            datetime_object = datetime.datetime.strptime(day, self.apitimeformat)
            if datetime_object >= self.startdayobj:
                validDays.add(day)

        lastCoveredDayObj = datetime.datetime.now()
        lastDay = lastCoveredDayObj.strftime(self.apitimeformat)

        endDay = datetime.datetime.strptime("2021-12-31", self.apitimeformat)
        holidays = []
        with open(self.rootdir + "Data Files/holidays", "r") as f:
            for line in f:
                holidays.append(line.strip())
        #print(holidays)

        currDay = datetime.datetime.strptime(lastDay, self.apitimeformat) + datetime.timedelta(days=1)
        while currDay <= endDay:
            strDate = currDay.strftime(self.apitimeformat)
            weekday = currDay.weekday()
            if strDate not in holidays and weekday not in [5,6]:
                validDays.add(strDate)
            currDay = currDay + datetime.timedelta(days=1)


        with open("-REDACTED-/Alpha Stock Miner/Data Files/validDays.txt", "w") as f:
            for day in validDays:
                f.write(day + '\n')

    def getPastDays(self):

        days = []
        today = datetime.datetime.today().strftime(self.apitimeformat)
        openDays = self.getOpenDays()
        for day in openDays:
            if day <= today:
                days.append(day)

        return days

    def getOpenDays(self):
        days = []
        with open(self.rootdir + "Data Files/validDays.txt", "r") as f:
            for line in f:
                days.append(line.strip())
        return days

    def isMarketOpen(self):
        #CST
        currTime = datetime.datetime.now().time()
        if currTime > datetime.time(hour=8, minute=30) and currTime < datetime.time(hour=15):
            return True
        else:
            return False


    def paramToCol(self, param):
        paramLow = param.lower()

        currCol = paramLow
        numbers = ["1. ","2. ","3. ","4. ","5. "]
        for number in numbers:
            currCol = currCol.replace(number,"")

        col1 = currCol.replace(" ", "_")
        col2 = col1.replace(".", "")
        col3 = col2.replace("/", "") #


        return col3

    def getConnection(self):

        cnx = mysql.connector.connect(user='root', password='test', database='alphadata')
        return cnx

    def getText(self, path):
        text = ""
        with open(path, 'r') as f:
            for line in f:
                text += line
        return text

    def addToLog(self, path, message, prnt):
        now = datetime.datetime.now()
        message = "[" + str(now) + "]: " + message
        with open(path, 'a') as f:
            f.write(message + "\n")
            if prnt:
                print(message)

    def resetLog(self, path):

        print("Depreciated function call")

    def getTodayString(self):
        return datetime.datetime.today().strftime(self.apitimeformat)

    def stringDateToDate(self, date):
        return datetime.datetime.strptime(date, self.apitimeformat).date()

    def dateToString(self, date):
        return date.strftime(self.apitimeformat)

    def sortDatesString(self, dates):
        dateObjs = []
        if self.useSortedDates:
            return self.sortedDates
        else:
            for date in dates:
                dateObjs.append(self.stringDateToDate(date))
            return self.sortDates(dateObjs)

    def sortDates(self, dates):
        if self.useSortedDates == False:
            dates.sort()
            self.sortedDates = dates
            self.useSortedDates = True
            return dates
        else:
            return self.sortedDates

    def getNextOpenDay(self, day):
        openDays = self.getOpenDays()
        dates = self.sortDatesString(openDays)
        if day in dates:
            i = dates.index(day)
            return dates[i+1]
        else:
            currDay = day
            found = False
            while not found:
                if currDay in dates:
                    i = dates.index(currDay)
                    found = True
                    return currDay
                else:
                    currDay = currDay + datetime.timedelta(days=1)

    def getRelativeDay(self, date, change):
        if change < 0:

            currDate = date
            count = change
            while count < 0:
                count += 1
                currDate = self.getPreviousOpenDay(currDate)
            return currDate

        else:

            currDate = date
            count = change
            while count > 0:
                count -= 1
                currDate = self.getNextOpenDay(currDate)
            return currDate


    def getPreviousOpenDay(self, day):
        openDays = self.getOpenDays()
        dates = self.sortDatesString(openDays)
        if day in dates:
            i = dates.index(day)
            return dates[i-1]
        else:
            currDay = day
            found = False
            while not found:
                if currDay in dates:
                    i = dates.index(currDay)
                    found = True
                    return currDay
                else:
                    currDay = currDay - datetime.timedelta(days=1)

    def resetTables(self):
        cnx = self.getConnection()
        cursor = cnx.cursor()
        sql = ""
        with open(self.rootdir + "Data Files/database.sql") as f:
            for line in f:
                sql += line
        cursor.execute(sql,multi=True)
        print("Tables Reset")
        cursor.close()
        cnx.commit()
        cnx.close()

    def resetLogs(self):
        cnx = self.getConnection()
        cursor = cnx.cursor()
        sql = ""
        with open(self.rootdir + "Data Files/log.sql") as f:
            for line in f:
                sql += line
        cursor.execute(sql,multi=True)
        print("Logs Reset")
        cursor.close()
        cnx.commit()
        cnx.close()

    def getTickersOnly(self, cnx):
        tickerPairs = self.getTickers(cnx)
        newList = []
        for ticker in tickerPairs:
            newList.append(ticker[1])
        return newList

    def percentChange(self, start, end):
        if start < end:
            change = end - start
            percent = change / start
            return percent
        else:
            change = start - end
            percent = change / start
            return -1.0 * percent

    def getTime(self):
        return time.time()

    def timeBetween(self, start, end):
        return end - start


if __name__ == "__main__":
    utils = Utilities()

    #add index on date column to increase selection speed
    cnx = utils.getConnection()
    cursor = cnx.cursor()
    for table in utils.tableData:
        statement = "ALTER TABLE " + table + " ADD INDEX date (date);"
        cursor.execute(statement)