# AURAPythonSamples
A repository of code files that demonstrate my experience working with SQL in a Python application.

## 1 Introduction

These Python files come from a personal project of mine called "Alpha Stock Miner" that uses SQL extensively. The project's purpose is to gather massive amounts of historical stock market data and then use that data to "Back Test" trading strategies using technical analysis.

The first of the two main functions the gathering of data. The data set I am interested in is technical indicators for all stocks in the New York Stock Exchange (NYSE) and NASDAQ. There are about 30 indicators, each having there own table in MySQL, and 6000 stocks. I gather data for every stock for every indicator for every day going back just short of 20 years. This results in millions of data points and several gigabytes in total size.

The second of the functions is to use that data to test strategies developed outside this program. I translate my strategies into python scripts that the back tester uses to test the profitability of the strategy. The stategies and back tester are mostly outside the scope for this repository, but the helper files used to facilitate the back test are included.

## 2 Code Files

### BigDataCollector.py

This script is run when the database needs updating or refreshing. Due to the call frequency limitations of AlphaVantage I am only allowed 30 calls per minute with a premium API key. There for the aquisition of all the data needed can take up to a week to finish.

The main place of interest:

Line 122 - 134: This is where I insert a single data point into the data base. I call this line of code for each day in the data given to me from the API.

### Investor.py

This Python file is used by the back tester to buy and sell stocks as well as get indicator values from the database for use in the strategies. I have abstracted the MySQL call to be contained on one function on line 302.

### Utilities.py

This file is imported by almost all other Python scripts in the program. It contains mostly helper functions dealing with time/date, math, file I/O, and some database calls.

### database.sql

This is the database structure of the stock market data.

### log.sql

This is how the log tables are structured.


