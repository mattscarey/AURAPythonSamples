__author__ = 'Matthew'
import mysql.connector
import datetime
import sys

from math import floor

sys.path.insert(0, '-REDACTED-/Alpha Stock Miner/Back Tester/')
from Holding import Holding
from Logging import Logging
from Account import Account
from Utilities import Utilities

#This class will be used to do all stock market related calls such as:

#Account management
#Security management
#Information retrieval

#This class will serve as a way for other components to manage stock market
#information easily
class Investor:

    def __init__(self):
        self.utils = Utilities()
        self.logging = Logging()
        self.logging.initialize()

        self.stockIDTable = {}
        self.useStockIDTable = False

    def getTickers(self, cnx):
        return self.utils.getTickersOnly(cnx)

    def getStockId(self, ticker, cnx):
        try:
            stockid = self.stockIDTable[ticker]
            return stockid
        except:
            cursor = cnx.cursor()
            statement = 'SELECT id FROM stocks WHERE ticker = "' + ticker + '";'
            cursor.execute(statement)
            id = None
            for (value) in cursor:
                id = value[0]
            cursor.close()
            self.stockIDTable[ticker] = id
            return id

    def getClose(self, ticker, date, cnx):
        val = self.getBasicValue("basic","close",date,ticker,cnx)
        return val

    def getOpen(self, ticker, date, cnx):
        val = self.getBasicValue("basic","open",date,ticker,cnx)
        return val

    def getHigh(self, ticker, date, cnx):
        val = self.getBasicValue("basic","high",date,ticker,cnx)
        return val

    def getLow(self, ticker, date, cnx):
        val = self.getBasicValue("basic","low",date,ticker,cnx)
        return val

    def getVolume(self, ticker, date, cnx):
        val = self.getBasicValue("basic","volume",date,ticker,cnx)
        return val

    def getAverageVolume(self, ticker, date, days, cnx):

        openDays = self.utils.getOpenDays()

        count = 1
        values = []
        currdate = date
        while count < days:
            count += 1
            passed = False

            value = None

            while not passed:

                if(self.utils.dateToString(currdate) in openDays):
                    value = self.getVolume(ticker,currdate,cnx)
                    #print(self.utils.dateToString(currdate))
                    #print(value)
                    if(value != None):
                        passed = True
                    else:
                        return 0.0
                else:
                    #print(self.utils.dateToString(currdate))
                    currdate = currdate - datetime.timedelta(days=1)
                    count += 1
            if value != None:
                values.append(float(value))
            else:
                self.logging.logInvestorMessage("", "Error in average volume: " + self.utils.dateToString(currdate) + ", " + ticker)
            currdate = currdate - datetime.timedelta(days=1)

        average = float(sum(values)) / float(len(values))
        return average

    #This will get the value for the first column in table data
    #To get more specific data call an indicator function
    def getIndicator(self, indicator, ticker, date, cnx):
        val = self.getBasicValue(indicator,self.utils.tableData[indicator][3][0],date,ticker,cnx)
        return val

    def getAverageIndicator(self, indicator, ticker, date, days, cnx):

        openDays = self.utils.getOpenDays()

        count = 1
        values = []
        currdate = date
        while count < days:
            count += 1
            passed = False

            value = None

            while not passed:
                if(self.utils.dateToString(currdate) in openDays):
                    value = self.getIndicator(indicator,ticker,currdate,cnx)
                    if(value != None):
                        passed = True
                    else:
                        return 0.0
                else:
                    currdate = date - datetime.timedelta(days=1)
                    count += 1
            values.append(value)
            currdate = currdate - datetime.timedelta(days=1)

        average = float(sum(values)) / float(len(values))
        return average


    #----------------ACCOUNT MANAGEMENT -----------------

    def processAccount(self,account,date,cnx):

        self.logging.logInvestorMessage("","Processing Account, date: " + self.utils.dateToString(date))
        accountCopy = account

        for security in account.holdings.keys():

            ticker = security
            holding = account.holdings[security]

            if(holding.holdPeriod != 0):

                sellDate = self.addTradingDays(holding.buyDate,holding.holdPeriod)

                if(sellDate <= date):
                    self.logging.logInvestorMessage("",ticker + " holding has exprired")
                    result = self.sellHolding(accountCopy,ticker,date,cnx)
                    if result != False:
                        accountCopy = result
                    else:
                        self.logging.logInvestorMessage("","Unable to sell " + ticker + " shares")

        self.logging.logInvestorMessage("","Total account worth $" + str(self.accountWorth(accountCopy,date,cnx)))
        return accountCopy

    def addHolding(self,account,ticker,date,shares,holdPeriod,cnx):

        accountCopy = account

        #Check if its possible to buy the security
        result = self.getClose(ticker,date,cnx)
        if(result != None):

            cost = float(result) * shares
            if(accountCopy.cash < cost):
                return False
            else:

                self.logging.logInvestorMessage("","Purchased " + str(shares) + " shares of " + ticker + " at $" + str(result) + " per share, totalling $" + str(cost))
                if ticker in accountCopy.holdings.keys():
                    accountCopy.holdings[ticker].shares += shares
                    accountCopy.holdings[ticker].holdPeriod = holdPeriod
                    accountCopy.holdings[ticker].buyDate = date
                    accountCopy.cash -= cost
                else:

                    holdingId = accountCopy.holding_id
                    holding = Holding(holdingId,ticker,shares,date,holdPeriod)
                    accountCopy.holdings[ticker] = holding
                    accountCopy.cash -= cost

                return accountCopy

        else:
            return False

    def buySharesWithAmount(self,account,ticker,date,amount,holdPeriod,cnx):
        accountCopy = account

        #Check if its possible to buy the security
        result = self.getClose(ticker,date,cnx)
        if(result != None):

            numShares = floor(float(amount) / float(result))

            accountCopy = self.addHolding(accountCopy,ticker,date,numShares,holdPeriod,cnx)

            return accountCopy

        else:
            return False


    def sellHolding(self,account,ticker,date,cnx, shares = 0):

        accountCopy = account

        holding = accountCopy.holdings[ticker]
        result = self.getClose(holding.symbol,date,cnx)

        toSell = shares
        if(shares == 0):
            toSell = accountCopy.holdings[ticker].shares

        if(result != None):

            value = float(result) * float(toSell)

            currentShares = accountCopy.holdings[ticker].shares
            if(currentShares < toSell):
                return False
            else:

                self.logging.logInvestorMessage("", "Sold " + str(toSell) + " shares of " + ticker + " at $" + str(result) + " per share worth $" + str(value))
                if(currentShares - toSell == 0):
                    del accountCopy.holdings[ticker]
                else:
                    accountCopy.holdings[ticker].shares -= toSell

                accountCopy.cash += value

                return accountCopy

        else:
            return False


    def sellHoldingAmount(self,account,ticker,date,cnx, amount):

        accountCopy = account

        holding = accountCopy.holdings[ticker]
        result = self.getClose(holding.symbol,date,cnx)


        if(result != None):

            toSell = int(floor(float(amount) / float(result)))
            value = float(toSell) * float(result)

            print(toSell)

            currentShares = accountCopy.holdings[ticker].shares
            if(currentShares < toSell or toSell == 0):
                return False
            else:

                accountCopy = self.sellHolding(accountCopy,ticker,date,cnx,toSell)

                return accountCopy

        else:
            return False

    def accountWorth(self,account,date,cnx):

        total = account.cash
        for security in account.holdings:
            holding = account.holdings[security]
            valueStr = self.getClose(security,date,cnx)
            if(valueStr == None):
                self.logging.logInvestorMessage("","Failed to calculate holding value: " + security)
                return None
            value = float(valueStr) * holding.shares
            total += value
        return total

    #------------------- HELPERS ------------------------

    def getValueFromStatement(self, statement, cnx):
        cursor = cnx.cursor()
        cursor.execute(statement)
        val = None
        for (value) in cursor:
            val = float(value[0])
        cursor.close()
        return val

    def getBasicValue(self,table,column,date,ticker,cnx):
        dateString = date.strftime("%Y-%m-%d")
        id = self.getStockId(ticker,cnx)
        statement = "SELECT " + column + " FROM " + table + " WHERE stock_id = " + str(id) + ' AND date = "' + dateString + '";'
        val = self.getValueFromStatement(statement,cnx)
        return val

    def addTradingDays(self, date, days):
        daysToAdd = 0
        currDate = date
        while daysToAdd < days:
            currDate = currDate + datetime.timedelta(days=1)
            if self.utils.dateToString(currDate) in self.utils.getOpenDays():
                daysToAdd += 1
        return currDate

    def isOpenDay(self, day):
        if self.utils.dateToString(day) in self.utils.getOpenDays():
            return True
        else:
            return False


if __name__ == "__main__":

    import time

    cnx = mysql.connector.connect(user='root', password='test', database='alphadata')
    inv = Investor()
    now = inv.utils.getTime()
    times = []

    tickers = inv.utils.getTickersOnly(inv.logging.cnx)
    for ticker in tickers:
        start = inv.utils.getTime()
        val = inv.getBasicValue("macd","MACD_Hist",inv.utils.stringDateToDate("2018-06-12"),ticker,inv.logging.cnx)
        stop = inv.utils.getTime()
        totalTimeOne = inv.utils.timeBetween(start,stop)
        times.append(totalTimeOne)

    end = inv.utils.getTime()
    totalTime = inv.utils.timeBetween(now,end)

    times.sort()
    smallest = min(times)
    biggest = max(times)
    mean = sum(times) / len(times)
    median = times[len(times) / 2]
    print("--- Timing Statistics ---")
    print("Range: " + str(smallest) + " - " + str(biggest))
    print("Average Time: " + str(mean))
    print("Median Time: " + str(median))
    print("Total Time: " + str(totalTime))