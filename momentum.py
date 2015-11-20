
# coding: utf-8

# In[1]:

spxlist = ['A', 'AA', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACE', 'ACN', 'ACT',
'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'ADT', 'AEE', 'AEP',
'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AKAM', 'ALL',
'ALLE', 'ALTR', 'ALXN', 'AMAT', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT',
'AMZN', 'AN', 'AON', 'APA', 'APC', 'APD', 'APH', 'ARG', 'ATI', 'AVB',
'AVGO', 'AVP', 'AVY', 'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBBY',
'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BHI', 'BIIB', 'BK', 'BLK', 'BLL',
'BMS', 'BMY', 'BRCM', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH',
'CAM', 'CAT', 'CB', 'CBG', 'CBS', 'CCE', 'CCI', 'CCL', 'CELG',
'CERN', 'CF', 'CFN', 'CHK', 'CHRW', 'CI', 'CINF', 'CL', 'CLX', 'CMA',
'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNP', 'CNX', 'COF', 'COG',
'COH', 'COL', 'COP', 'COST',  'CPB', 'CRM', 'CSC', 'CSCO',
'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVC', 'CVS', 'CVX', 'D',
'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA',
'DISCK', 'DLPH', 'DLTR', 'DNB', 'DNR', 'DO', 'DOV', 'DOW', 'DPS',
'DRI', 'DTE', 'DTV', 'DUK', 'DVA', 'DVN', 'EA', 'EBAY', 'ECL', 'ED',
'EFX', 'EIX', 'EL', 'EMC', 'EMN', 'EMR', 'EOG', 'EQR', 'EQT', 'ESRX',
'ESS', 'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXPD', 'EXPE', 'F',
'FAST', 'FB', 'FCX', 'FDO', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV',
'FITB', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOSL', 'FOXA', 'FSLR', 'FTI',
'FTR', 'GAS',  'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM',
'GMCR', 'GME', 'GNW', 'GOOG', 'GOOGL', 'GPC', 'GPS', 'GRMN', 'GS',
'GT', 'GWW', 'HAL', 'HAR', 'HAS', 'HBAN', 'HCBK', 'HCN', 'HCP', 'HD',
'HES', 'HIG', 'HOG', 'HON', 'HOT', 'HP', 'HPQ', 'HRB', 'HRL', 'HRS',
'HSP', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IFF', 'INTC', 'INTU',
'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'ITW', 'IVZ', 'JCI', 'JEC', 'JNJ',
'JNPR', 'JOY', 'JPM', 'JWN', 'K', 'KEY', 'KIM', 'KLAC', 'KMB', 'KMI',
'KMX', 'KO', 'KORS', 'KR', 'KRFT', 'KSS', 'KSU', 'L', 'LB', 'LEG',
'LEN', 'LH', 'LLL', 'LLTC', 'LLY', 'LM', 'LMT', 'LNC', 'LO', 'LOW',
'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAC', 'MAR', 'MAS',
'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MHFI',
'MHK', 'MJN', 'MKC', 'MLM', 'MMC', 'MMM', 'MNK', 'MNST', 'MO', 'MON',
'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MU', 'MUR',
'MWV', 'MYL', 'NAVI', 'NBL', 'NBR', 'NDAQ', 'NE', 'NEE', 'NEM',
'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC',
'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWSA', 'OI', 'OKE',
'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PBI', 'PCAR', 'PCG',
'PCL', 'PCLN', 'PCP', 'PDCO', 'PEG', 'PEP', 'PETM', 'PFE', 'PFG',
'PG', 'PGR', 'PH', 'PHM', 'PKI', 'PLD', 'PLL', 'PM', 'PNC', 'PNR',
'PNW', 'POM', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH',
'PWR', 'PX', 'PXD', 'QCOM', 'QEP', 'R', 'RAI', 'REGN', 'RF', 'RHI',
'RHT', 'RIG', 'RL', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN',
'SBUX', 'SCG', 'SCHW', 'SE', 'SEE', 'SHW', 'SIAL', 'SJM', 'SLB',
'SNA', 'SNDK', 'SNI', 'SO', 'SPG', 'SPLS', 'SRCL', 'SRE', 'STI',
'STJ', 'STT', 'STX', 'STZ', 'SWK', 'SWN',  'SYK', 'SYMC',
'SYY', 'T', 'TAP', 'TDC', 'TE', 'TEG', 'TEL', 'TGT', 'THC', 'TIF',
'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSO',
'TSS', 'TWC', 'TWX', 'TXN', 'TXT', 'TYC', 'UA', 'UHS', 'UNH', 'UNM',
'UNP', 'UPS', 'URBN', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB',
'VLO', 'VMC', 'VNO', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT',
'WDC', 'WEC', 'WFC', 'WFM', 'WHR', 'WIN', 'WM', 'WMB', 'WMT',
'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY',
'XRX', 'XYL', 'YHOO', 'YUM', 'ZION', 'ZMH', 'ZTS']


# In[2]:

import pandas as pd
import pandas.io.data as web
import numpy as np


# In[3]:

def get_px(stock, start):
    return web.get_data_yahoo(stock, start)['Adj Close']
px = pd.DataFrame({n: get_px(n, '1/1/1999') for n in spxlist})



# In[4]:

px_1 = px.truncate(after ='1/1/2005', before ='1/1/1999')
px_2 = px.truncate(after ='1/1/2010', before = '1/1/2005')
px_3 = px.truncate(after = '1/1/2015', before = '1/1/2010')


# In[5]:

px_1 = px_1.asfreq('B').fillna(method = 'pad')
px_2 = px_2.asfreq('B').fillna(method = 'pad')
px_3 = px_3.asfreq('B').fillna(method = 'pad')
px= px.asfreq('B').fillna(method = 'pad')


# In[6]:

rets_1 = px_1.pct_change()
rets_2 = px_2.pct_change()
rets_3 = px_3.pct_change()
rets = px.pct_change()


# In[143]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
((1+rets).cumprod() -1).plot()


# In[102]:

def calc_mom(price, lookback, lag):
    mom_ret = price.shift(lag).pct_change(lookback)
    ranks = mom_ret.rank(axis = 1, ascending = True)
    bottom = ranks.quantile(0.1, axis = 1)
    top = ranks.quantile(0.9, axis =1)
   
    select1=  ranks > bottom
    select2 = ranks < top
    filter = select1&select2
    #ranks = ranks.where(filter, ranks.mean(axis=1), axis='rows')
    ranks[filter] = 250
    demeaned = ranks.subtract(ranks.mean(axis = 1), axis = 0)
    return demeaned.divide(demeaned.std(axis=1), axis=0)


# In[9]:

compound = lambda x: (1+x).prod() -1
daily_sr = lambda x: x.mean()/x.std()


# In[10]:

def strat_sr(prices, lb, hold, lag):
    freq = '%dB' % hold
    port = calc_mom(prices, lb, lag) 
    daily_rets = prices.pct_change()
   
    port = port.shift(1).resample(freq, how = 'first')
    returns = daily_rets.resample(freq, how = compound)

    port_rets = (port*returns).sum(axis = 1)
    return daily_sr(port_rets) * np.sqrt(250/hold)


# In[71]:

def strat_sr_rolling(prices, lb, hold, lag):
    freq = '%dB' % hold
    # rolling 1 year
    port = calc_mom(prices, lb, lag)
    port = port.fillna(0)

    daily_rets = prices.pct_change(hold)
    #returns = pd.rolling_apply(daily_rets, hold, lambda x : (1+ x).prod()) -1
    returns = daily_rets.shift(-hold)
    returns = returns.fillna(0)
    
    port_rets = (port*returns).sum(axis = 1)

    #data_mean = pd.rolling_apply(port_rets, 252, lambda x : (1+ x).prod())
    data_mean = pd.rolling_mean(port_rets,window = 500) 
    
    data_std = pd.rolling_std(port_rets, window = 500)
    return data_mean.div(data_std)


# In[103]:

def strat_rets_rolling(prices, lb, hold, lag):
    port = calc_mom(prices, lb, lag)
    daily_rets = prices.pct_change(hold)
    port_abs = port.abs().sum(axis = 1)
    port_nor = port.div(port_abs, axis = 0)
    returns = daily_rets.shift(-hold)
    port_rets = (port_nor*returns).sum(axis = 1)
    return port_rets


# In[115]:

def strat_rets(prices, lb, hold, lag):
    freq = '%dB' % hold
    port = calc_mom(prices, lb, lag)
    daily_rets = prices.pct_change()
    port = port.shift(1).resample(freq, how = 'first')
    returns = daily_rets.resample(freq, how = compound)
    port_rets = (port*returns).sum(axis = 1)
    return port_rets


# In[61]:

results_1 = pd.DataFrame(columns=('lb', 'hold', 'lag', 'sr'))
i = 0
for lb in range (30, 600, 30):
    for hold in range (10, 200, 10):
        #for lag in range (1, 100, 5):
            sr = strat_sr(px_1, lb, hold, 1)
            results_1.loc[i] =[lb, hold, 1, sr]
            i = i+1


# In[13]:

results_2 = pd.DataFrame(columns=('lb', 'hold', 'lag', 'sr'))
i = 0
for lb in range (30, 600, 30):
    for hold in range (10, 200, 10):
        #for lag in range (1, 100, 5):
            sr = strat_sr(px_2, lb, hold, 1)
            results_2.loc[i] =[lb, hold, 1, sr]
            i = i+1


# In[16]:

results_3 = pd.DataFrame(columns=('lb', 'hold', 'lag', 'sr'))
i = 0
for lb in range (30, 600, 30):
    for hold in range (10, 200, 10):
        #for lag in range (1, 100, 5):
            sr = strat_sr(px_3, lb, hold, 1)
            results_3.loc[i] =[lb, hold, 1, sr]
            i = i+1


# In[15]:

results = pd.DataFrame(columns=('lb', 'hold', 'lag', 'sr'))
i = 0
for lb in range (30, 600, 30):
    for hold in range (10, 200, 10):
        #for lag in range (1, 100, 5):
            sr = strat_sr(px, lb, hold, 1)
            results.loc[i] =[lb, hold, 1, sr]
            i = i+1


# In[119]:

returns = strat_rets(px, 150, 120, 1)


# In[120]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
returns.plot()


# In[122]:

daily_rets = px.pct_change()


# In[137]:

returns = daily_rets.resample('150D', how = compound)


# In[138]:

port = calc_mom(px, 120, 1)
port = port.shift(1).resample('150D', how = 'first')
port_abs = port.abs().sum(axis = 1)
port_nor = port.div(port_abs, axis = 0)


# In[139]:

tr = (port_nor * returns).sum(axis = 1)


# In[142]:

(tr+1).cumprod()


# In[140]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
tr.plot()


# In[72]:

sr_rolling = strat_sr_rolling(px, 150, 120, 1)


# In[73]:

sr_rolling
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
sr_rolling.plot()


# In[80]:

returns


# In[74]:

sr_rolling = strat_sr_rolling(px, 180, 120, 1)


# In[75]:

sr_rolling
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
sr_rolling.plot()


# In[18]:

results_merge1 = pd.merge(results, results_1, on= ['lb', 'hold', 'lag'], how = 'inner', suffixes = ('total', '1_'))
results_merge2 = pd.merge(results_2, results_3, on= ['lb', 'hold', 'lag'], how = 'inner', suffixes = ('2_', '3_'))
merge = pd.merge(results_merge1, results_merge2, on = ['lb', 'hold', 'lag'], how = 'inner')


# In[64]:

results_1.sort('sr')


# In[20]:

merge.sort('srtotal', ascending = False)


# In[ ]:



