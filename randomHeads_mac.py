import pandas as pd
import numpy
from numpy import random
from datetime import datetime
from datetime import timedelta
import time
import atexit
import random as rd
import re
import subprocess
import pygame
import pygsheets


amexdf=pd.read_csv("AMEX.csv")
nysedf=pd.read_csv("NYSE.csv")
qqqdf=pd.read_csv("NASDAQ.csv")

def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

frames = [amexdf, nysedf, qqqdf]

exc_list_mstr = pd.concat(frames)

tix = []
big_tix = []

sectors = ['Technology', 'Health Care', 'Consumer Services', 'Consumer Non-Durables', 'Miscellaneous', 'Consumer Durables', 'Basic Industries', 'Capital Goods', 'Transportation', 'Energy', 'Finance', 'Public Utilities']
    
####Choose sector#######
inpt = raw_input('Choose Sector!!! (0-Tech, 1-Hlth, 2-Services, 3-Consumer, 4-Misc, 5-Con. Durables, 6-Basic Inds., 7-Cap. Goods, 8-Trans., 9-Energy, 10-Fin., 11-XLU)\n')
sector_str = sectors[int(inpt)]

for row, index in exc_list_mstr.iterrows():
    symbol = str(index.Symbol)
    industry = str(index.industry)
    name = str(index.Name)
    sector = str(index.Sector)
    try:
        market_cap = float(index.MarketCap)
    except:
        market_cap=0
    carat = '^' in symbol
    letters = symbol.isalpha()
    #sector_list = []
    #industry_list = []
    
    condition = (industry != 'Precious Metals' and industry != 'Real Estate Investment Trusts' and industry != 'Marine Transportation')
    if carat == False and letters == True and sector == sector_str and condition: 
        if market_cap > 750000000 and market_cap < 35000000000:
            tix.append((symbol, name))
        if market_cap > 25000000000:
            big_tix.append((symbol, name))

        
sleep = range(2, 10, 3)        

times = []

def report_stats(times):
    n = len(times)
    N = len(tix) + n
    avg = sum( times) / n
    med = numpy.median(times)
    today = datetime.today().strftime('%m/%d/%Y')
    print '\nn:', n, '\nMEAN:', avg, '\nMEDIAN:', med, '\nN:', N
    if n>30:
        gc = pygsheets.authorize(service_file='typingPracticeresults.json')
        sh = gc.open('riteTyper')
        wks = sh[0]
        if sector_str == 'Technology':
            wks.update_cells('B2:D2', [[N, avg, med]])
            wks.update_cell('O2', today)
            best = wks.cell('E2').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E2', med)
        elif sector_str == 'Health Care':
            wks.update_cells('B3:D3', [[N, avg, med]])
            wks.update_cell('O3', today)
            best = wks.cell('E3').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E3', med)
        elif sector_str == 'Consumer Services':
            wks.update_cells('B4:D4', [[N, avg, med]])
            wks.update_cell('O4', today)
            best = wks.cell('E4').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E4', med)
        elif sector_str == 'Consumer Non-Durables':
            wks.update_cells('B5:D5', [[N, avg, med]])
            wks.update_cell('O5', today)
            best = wks.cell('E5').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E5', med)
        elif sector_str == 'Miscellaneous':
            wks.update_cells('B6:D6', [[N, avg, med]])
            wks.update_cell('O6', today)
            best = wks.cell('E6').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E6', med)
        elif sector_str == 'Consumer Durables':
            wks.update_cells('B7:D7', [[N, avg, med]])
            wks.update_cell('O7', today)
            best = wks.cell('E7').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E7', med)
        elif sector_str == 'Basic Industries':
            wks.update_cells('B8:D8', [[N, avg, med]])
            wks.update_cell('O8', today)
            best = wks.cell('E8').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E8', med)
        elif sector_str == 'Capital Goods':
            wks.update_cells('B9:D9', [[N, avg, med]])
            wks.update_cell('O9', today)
            best = wks.cell('E9').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E9', med)
        elif sector_str == 'Transportation':
            wks.update_cells('B10:D10', [[N, avg, med]])
            wks.update_cell('O10', today)
            best = wks.cell('E10').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E10', med)
        elif sector_str == 'Energy':
            wks.update_cells('B11:D11', [[N, avg, med]])
            wks.update_cell('O11', today)
            best = wks.cell('E11').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E11', med)
        elif sector_str == 'Finance':
            wks.update_cells('B12:D12', [[N, avg, med]])
            wks.update_cell('O12', today)
            best = wks.cell('E12').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E12', med)
        elif sector_str == 'Public Utilities':
            wks.update_cells('B13:D13', [[avg, med]])
            wks.update_cell('O13', today)
            best = wks.cell('E13').value
            if best=='':
                best = 100.0
            if float(best) > med:
                wks.update_cell('E13', med)


heads = ['__  DJ: --- in advanced talks to sell itself', 'BREAKING: --- hires bank to weigh sale after approach by @', 'Long $__ on potential infinity squeeze' , '__  *DJ @ in talks to buy ---', '__  *@ to acquire --- for $60/sh', '__  *@ Considers offer for ---', '__  *--- close to decision on sale', '__  *DJ --- hires advisors after receiving takeover interest','--- could be looking to sell', '@ nears deal to buy ---', '__  *DJ: Elliot reports 6.5% stake in ---', '__  DJ: Jana Partners taking stake in ---', '__  *DJ Icahn to push for sale at ---', '__  *--- fielding takeover interest', 'BREAKING: @ has made offer to buy ---', '@ in talks to buy ---', '##  DJ: @ in talks to buy ---', '--- in talks to sell itself to a British Retailer', 'Softbank definitely in talks with --- about merger', '__  *DJ @ preparing bid for ---', 'CITRON EXPOSES ___ -- PRICE TARGET $0', '--- named new short by Muddy Waters', '---: All Signs Point to Fraud', '__  *@ no longer interested in bid for ---', '__  DJ: @ abandons attempts to buy ---', '*@ no longer interested in bid for ---', '*DJ --- discussions to sell itself have broken down', 'COULD ___ BE THE NEXT VALEANT?', 'CITRON RESEARCH EXPOSES ___ AND PROVES BEYOND ANY DOUBT WHY THIS STOCK WILL SOON BE CUT IN HALF', 'Exclusive: SoftBank calling off talks to acquire ---', '__  *Kerrisdale Capital is short ---', '__  *Muddy Waters is short ---', '___: CITRON EXPOSES THE LAWSUITS THAT WILL WIPE OUT THE EQUITY', 'Short $__: Fraud penalties to exceed $100 million', '__  *DJ --- Has Concluded Strategic Review', '___: ENRON IN THE MAKING?', '\n\n\n__ DJ @ Held Takeover Talks With Aircraft Maker --- \n__ *DJ Deal Would Value --- at Large Premium to its $3.7B Market Cap -- Source \n__ *DJ Talks Are on Hold as Parties Seek Approval From Govt. -- Sources \n__ *DJ @ Held Takeover Talks With --- - Sources', '\n\n\n## *DJ --- Had Market Capitalization of $9.8B Friday Afternoon \n## *DJ Glencore Agreed to Standstill That Expires in Coming Weeks -- Sources \n## *DJ Approach Follows Glencore Overture to --- Last Year \n## *DJ @ Has Made Takeover Approach to --- -- Sources', '\n\n\n__ *DJ --- Had $53B Market Value Thursday Afternoon \n__ *DJ @ Is in Talks to Buy --- -- Sources', '\n\n\n## DJ @, --- Consider Merger \n## *DJ Companies Have Combined Enterprise Value of About $12 Billion \n## *DJ @ is Still Interested in Buying --- -- Sources \n## *DJ Companies Have Held On-Again, Off-Again Talks -- Sources \n## *DJ @, --- Consider Combination -- Sources', '\n\n__ *DJ FTC Investigates --- Over Negotiations With Customers \n__ *DJ FTC Probe Doesnt Focus on ---s Wireless Segment -- Sources \n__ *DJ FTC Recently Issued Subpoenas in --- Antitrust Probe -- Sources \n__ *DJ FTC Investigates --- Over Negotiations With Customers -- Sources', '\n\n\n__ *DJ Lab-Supply Distributor Had Market Value of About $3.75 Billion \n__ *DJ New Mountain Capital Nears Deal to Buy --- -- Sources', '\n\n\n## *DJ ---, a Cancer Biotech, Has a Market Cap of About $5.5B \n## *DJ @ Is in Talks to Buy --- -- Sources', '\n\n\n__ *DJ --- Had Market Value of $970 Million Friday Afternoon \n__ *DJ Company is Working with Centerview and MTS -- Sources \n__ *DJ --- Exploring a Potential Sale -- Sources', 'BREAKING: Japanese semiconductor company @ is in talks to acquire U.S. chipmaker --- in what could be close to a $20B deal - sources', 'New PE bid looms for vinyl siding maker ---', '\n\n\n## *DJ --- Had Market Value of $4.7 Billion \n## *DJ Talks Have Been Going on for Months, May Not Lead to Deal -- Sources \n## *DJ @ Is in Talks to Buy Aerospace-Parts Maker --- -- Sources', 'BREAKING: Talks between @ and --- about an acquisition have ended without an agreement - sources', '\n\n\n__ DJ Merger Talks Between @ and --- End \n__ *DJ Merger Talks Between @ and --- End -- Sources', '\n\n\n## DJ Takeover Talks Between ##, --- Have Stalled, Sources Say \n## *DJ Potential Deal Derailed Amid Concern Over Antitrust Pushback -- Sources \n## *DJ Takeover Talks Between ## and --- Have Stalled -- Sources', '\n\n\n## DJ ---, @ Restart Deal Talks, Once Again \n## *DJ ---, @ Merger Talks Collapsed in Nov. Over Terms \n## *DJ ---, @ Merger Talks Are Preliminary - Sources \n## *DJ ---, @ Restart Deal Talks, Once Again - Sources', "\n\n## DJ Justice Department to Allow @'s Acquisition of --- After Companies Make Concessions, Sources Say \n## *DJ EU Has Already Conditionally Approved the Deal \n## *DJ Companies Agree to Additional Asset Sales to Address DOJ Antitrust Concerns \n## DJ Justice Department to Allow @'s Acquisition of --- After Companies Make Concessions, Sources Say", '\n\n\n## *DJ ---, Which Had Market Value of $3.7B, Announced Sales Process in Dec. \n## *DJ ##-__ Deal Could Be Announced as Soon as Monday -- Sources \n## *DJ @ Nears Deal to Buy Aerospace-Parts Specialist __ -- Sources', '\n\n\n__ *DJ --- Has $44B Market Value \n__ *DJ @ Has Made Takeover Approach to --- -- Sources', 'CITRON: Citron Exposes History of FRAUD Behind ---…. That is right…we said it – FRAUD', 'CITRON: ___ NEEDS TO TAKE A BREATH', 'BREAKING: @ in advanced talks to acquire --- in deal that could be announced as soon as this week – sources']
     
pygame.init()
while True:
    try:
        time.sleep(2)
        random.shuffle(tix)
        symbol, name = tix.pop()
        symbol_b, name_b = rd.choice(big_tix)
        headline = rd.choice(heads)
        headline = re.sub('___', name.upper(), headline)
        headline = re.sub('__', symbol, headline)
        headline = re.sub('---', name, headline)
        headline = re.sub('##', symbol_b, headline)
        headline = re.sub('@', name_b, headline)
        if '\n' in headline:
            chord = 'chord.wav'
            t1 = datetime.now()
            chord = pygame.mixer.Sound(chord)
            chord.play()
            print ("\033[0;31;40m %s" %headline)
            if '\n\n\n' in headline:
                getch()
            else:
                inpt = raw_input()
                while inpt != symbol:
                    inpt = raw_input()
            diff = datetime.now() - t1
            diff_str = str(diff)
            print ("\033[0;37;40m %s %s" %(diff_str, symbol))
        else:
            t1 = datetime.now()
            print headline
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
