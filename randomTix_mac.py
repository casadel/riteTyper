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

sectors = ['Technology', 'Health Care', 'Consumer Services', 'Consumer Non-Durables', 'Miscellaneous', 'Consumer Durables', 'Basic Industries', 'Capital Goods', 'Transportation', 'Energy', 'Finance', 'Public Utilities']
    
####Choose sector#######
inpt = raw_input('Choose Sector!!! (0-Tech, 1-Hlth, 2-Services, 3-Consumer, 4-Misc, 5-Con. Durables, 6-Basic Inds., 7-Cap. Goods, 8-Trans., 9-Energy, 10-Fin., 11-XLU)\n')
sector_str = sectors[inpt]

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
    
    condition = (industry != 'Precious Metals' and industry != 'Real Estate Investment Trusts' and industry != 'Marine Transportation')
    if carat == False and letters == True and market_cap > 800000000 and market_cap < 35000000000 and sector == sector_str and condition: 
        tix.append((symbol, name))

        
sleep = range(2, 10, 3)        

times = []

def report_stats(times):
    n = len(times)
    N = len(tix) + n
    avg = sum( times) / n
    med = numpy.median(times)
    print '\nn:', n, '\nMEAN:', avg, '\nMEDIAN:', med, '\nN:', N
    if n > 30:
        gc = pygsheets.authorize(service_file='typingPracticeresults.json')
        sh = gc.open('riteTyper')
        wks = sh[0]
        if sector_str == 'Technology':
            wks.update_cells('F2:G2', [[avg, med]])
            wks.update_cell('P2', today)
            best = wks.cell('H2').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H2', med)
        elif sector_str == 'Health Care':
            wks.update_cells('F3:G3', [[avg, med]])
            wks.update_cell('P3', today)
            best = wks.cell('H3').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H3', med)
        elif sector_str == 'Consumer Services':
            wks.update_cells('F4:G4', [[avg, med]])
            wks.update_cell('P4', today)
            best = wks.cell('H4').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H4', med)
        elif sector_str == 'Consumer Non-Durables':
            wks.update_cells('F5:G5', [[avg, med]])
            wks.update_cell('P5', today)
            best = wks.cell('H5').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H5', med)
        elif sector_str == 'Miscellaneous':
            wks.update_cells('F6:G6', [[avg, med]])
            wks.update_cell('P6', today)
            best = wks.cell('H6').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H6', med)
        elif sector_str == 'Consumer Durables':
            wks.update_cells('F7:G7', [[avg, med]])
            wks.update_cell('P7', today)
            best = wks.cell('H7').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H7', med)
        elif sector_str == 'Basic Industries':
            wks.update_cells('F8:G8', [[avg, med]])
            wks.update_cell('P8', today)
            best = wks.cell('H8').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H8', med)
        elif sector_str == 'Capital Goods':
            wks.update_cells('F9:G9', [[avg, med]])
            wks.update_cell('P9', today)
            best = wks.cell('H9').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H9', med)
        elif sector_str == 'Transportation':
            wks.update_cells('F10:G10', [[avg, med]])
            wks.update_cell('P10', today)
            best = wks.cell('H10').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H10', med)
        elif sector_str == 'Energy':
            wks.update_cells('F11:G11', [[avg, med]])
            wks.update_cell('P11', today)
            best = wks.cell('H11').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H11', med)
        elif sector_str == 'Finance':
            wks.update_cells('F12:G12', [[avg, med]])
            wks.update_cell('P12', today)
            best = wks.cell('H12').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H12', med)
        elif sector_str == 'Public Utilities':
            wks.update_cells('F13:G13', [[avg, med]])
            wks.update_cell('P13', today)
            best = wks.cell('H13').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('H13', med)    

    
while True:
    try:
        time.sleep(1)
        t1 = datetime.now()
        random.shuffle(tix)
        symbol, name = tix.pop()
        print name
        inpt = raw_input()
        while inpt != symbol:
            inpt = raw_input()
        diff = datetime.now() - t1
        diff_str = str(diff)
        print diff_str, symbol
        times.append(diff.total_seconds())
    except:
        print '\n', symbol
        report_stats(times)
        raise

    
