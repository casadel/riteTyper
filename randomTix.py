import pandas as pd
import numpy
from numpy import random
from datetime import datetime
from datetime import timedelta
import time
import atexit
import pygsheets

amexdf=pd.read_csv("AMEX.csv")
nysedf=pd.read_csv("NYSE.csv")
qqqdf=pd.read_csv("NASDAQ.csv")

frames = [amexdf, nysedf, qqqdf]

exc_list_mstr = pd.concat(frames)

tix = []
for row, index in exc_list_mstr.iterrows():
    symbol = str(index.Symbol)
    industry = str(index.industry)
    name = str(index.Name)
    sector = str(index.Sector)
    try:
        market_cap = float(index.MarketCap)
    except:
        market_cap = 0
    carat = '^' in symbol
    letters = symbol.isalpha()
    #sector_list = []
    #industry_list = []
    sectors = ['Technology', 'Health Care', 'Consumer Services', 'Consumer Non-Durables', 'Miscellaneous', 'Consumer Durables', 'Basic Industries', 'Capital Goods', 'Transportation', 'Energy', 'Finance', 'Public Utilities']

    ####Choose sector#######
    sector_str = sectors[1]
    condition = (industry != 'Precious Metals' and industry != 'Real Estate Investment Trusts' and industry != 'Marine Transportation')
    if carat == False and letters == True and market_cap > 800000000 and market_cap < 35000000000 and sector == sector_str and condition: 
        tix.append((symbol, name))

        
sleep = range(2, 10, 3)        

times = []

def report_stats(times):
    n = len(times)
    N = len(tix) + n
    avg = sum(times) / n
    med = numpy.median(times)
    if n > 10:
        gc = pygsheets.authorize(service_file='typingPracticeMeans.json')
        sh = gc.open('riteTyper')
        wks = sh[0]
        if sector_str == 'Technology':
            wks.update_cells('I2:J2', [[avg, med]])
        elif sector_str == 'Health Care':
            wks.update_cells('I3:J3', [[avg, med]])
        elif sector_str == 'Consumer Services':
            wks.update_cells('I4:J4', [[avg, med]])
        elif sector_str == 'Consumer Non-Durables':
            wks.update_cells('I5:J5', [[avg, med]])
        elif sector_str == 'Miscellaneous':
            wks.update_cells('I6:J6', [[avg, med]])
        elif sector_str == 'Consumer Durables':
            wks.update_cells('I7:J7', [[avg, med]])
        elif sector_str == 'Basic Industries':
            wks.update_cells('I8:J8', [[avg, med]])
        elif sector_str == 'Capital Goods':
            wks.update_cells('I9:J9', [[avg, med]])
        elif sector_str == 'Transportation':
            wks.update_cells('I10:J10', [[avg, med]])
        elif sector_str == 'Energy':
            wks.update_cells('I11:J11', [[avg, med]])
        elif sector_str == 'Finance':
            wks.update_cells('I12:J12', [[avg, med]])
        elif sector_str == 'Public Utilities':
            wks.update_cells('I13:J13', [[avg, med]])    
    print '\nn:', n, '\nMEAN:', avg, '\nMEDIAN:', med, '\nN:', N
    
while True:
    try:
        time.sleep(1)
        t1 = datetime.now()
        random.shuffle(tix)
        symbol, name = tix.pop()
        i = 1
        #print symbol
        print name
        inpt = raw_input()
        while inpt != symbol and i<5:
            inpt = raw_input()
            i = i+1
        diff = datetime.now() - t1
        diff_str = str(diff)
        print diff_str, symbol
        #print diff_str, name
        if i < 5:
            times.append(diff.total_seconds())
        else:
            tix.append((symbol, name))
    except:
        try:
            print '\n', symbol
        except:
            print 'nothing'
        report_stats(times)
        raise

    
