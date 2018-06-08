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
    today = datetime.today().strftime('%m/%d/%Y')
    try:
        print '\nn:', n, '\nMEAN:', avg, '\nMEDIAN:', med, '\nN:', N
    except:
        print 'wtf!!!!!!'
    if n > 4:
        gc = pygsheets.authorize(service_file='typingPracticeMeans.json')
        sh = gc.open('riteTyper')
        wks = sh[0]
        if sector_str == 'Technology':
            wks.update_cells('L2:M2', [[avg, med]])
            wks.update_cell('R2', today)
            best = wks.cell('N2')
            if best == None or med < best:
                wks.update('N2', med)
        elif sector_str == 'Health Care':
            wks.update_cells('L3:M3', [[avg, med]])
            wks.update_cell('R3', today)
            best = wks.cell('N3')
            if best == None or med < best:
                wks.update('N3', med)
        elif sector_str == 'Consumer Services':
            wks.update_cells('L4:M4', [[avg, med]])
            wks.update_cell('R4', today)
            best = wks.cell('N4')
            if best == None or med < best:
                wks.update('N4', med)
        elif sector_str == 'Consumer Non-Durables':
            wks.update_cells('L5:M5', [[avg, med]])
            wks.update_cell('R5', today)
            best = wks.cell('N5')
            if best == None or med < best:
                wks.update('N5', med)
        elif sector_str == 'Miscellaneous':
            wks.update_cells('L6:M6', [[avg, med]])
            wks.update_cell('R6', today)
            best = wks.cell('N6')
            if best == None or med < best:
                wks.update('N6', med)
        elif sector_str == 'Consumer Durables':
            wks.update_cells('L7:M7', [[avg, med]])
            wks.update_cell('R7', today)
            best = wks.cell('N7')
            if best == None or med < best:
                wks.update('N7', med)
        elif sector_str == 'Basic Industries':
            wks.update_cells('L8:M8', [[avg, med]])
            wks.update_cell('R8', today)
            best = wks.cell('N8')
            if best == None or med < best:
                wks.update('N8', med)
        elif sector_str == 'Capital Goods':
            wks.update_cells('L9:M9', [[avg, med]])
            wks.update_cell('R9', today)
            best = wks.cell('N9')
            if best == None or med < best:
                wks.update('N9', med)
        elif sector_str == 'Transportation':
            wks.update_cells('L10:M10', [[avg, med]])
            wks.update_cell('R10', today)
            best = wks.cell('N10')
            if best == None or med < best:
                wks.update('N10', med)
        elif sector_str == 'Energy':
            wks.update_cells('L11:M11', [[avg, med]])
            wks.update_cell('R11', today)
            best = wks.cell('N11')
            if best == None or med < best:
                wks.update('N11', med)
        elif sector_str == 'Finance':
            wks.update_cells('L12:M12', [[avg, med]])
            wks.update_cell('R12', today)
            best = wks.cell('N12')
            if best == None or med < best:
                wks.update('N12', med)
        elif sector_str == 'Public Utilities':
            wks.update_cells('L13:M13', [[avg, med]])
            wks.update_cell('R13', today)
            best = wks.cell('N13')
            if best == None or med < best:
                wks.update('N13', med)    
        
        print 'Check Spreadsheet!'
    
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

    
