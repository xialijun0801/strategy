
# coding: utf-8

# In[187]:

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


# In[115]:

spxlist2 = ['AAPL', 'GOOG', 'GOOGL', 'GPC', 'GPS', 'GRMN', 'GS']


# In[116]:

import pandas as pd


# In[213]:

names = ['AAPL', 'GOOG', 'GOOGL', 'GPC', 'GPS', 'GRMN', 'GS']
def get_px(stock, start):
    return web.get_data_yahoo(stock, start=start)['Adj Close']
px = pd.DataFrame({n: get_px(n, '1/1/1999') for n in spxlist})


# In[214]:

px = px.asfreq('B').fillna(method = 'pad')


# In[215]:

rets = px.pct_change()


# In[191]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
((1+rets).cumprod() -1).plot()


# In[192]:

def calc_mom(price, lookback, lag):
    mom_ret = price.shift(lag).pct_change(lookback)
    ranks = mom_ret.rank(axis = 1, ascending =False)
    demeaned = ranks.subtract(ranks.mean(axis = 1), axis = 0)
    return demeaned.divide(demeaned.std(axis=1), axis=0)


# In[41]:

compound = lambda x: (1+x).prod() -1
daily_sr = lambda x: x.mean()/x.std()


# In[177]:

def strat_sr(prices, lb, hold):
    freq = '%dB' % hold
    port = calc_mom(prices, lb, lag = 1)
    daily_rets = prices.pct_change()
    port = port.shift(1).resample(freq, how = 'first')
    returns = daily_rets.resample(freq, how = compound)
    port_rets = (port*returns).sum(axis = 1)
    return daily_sr(port_rets) * np.sqrt(250/hold)


# In[178]:

def strat_rets(prices, lb, hold):
    freq = '%dB' % hold
    port = calc_mom(prices, lb, lag = 1)
    daily_rets = prices.pct_change()
    port = port.shift(1).resample(freq, how = 'first')
    returns = daily_rets.resample(freq, how = compound)
    port_rets = (port*returns).sum(axis = 1)
    return port_rets


# In[216]:

results = pd.DataFrame(columns=('lb', 'hold', 'sr'))
i = 0
for lb in range (30, 600, 30):
    for hold in range (10, 200, 10):
        sr = strat_sr(px, lb,hold)
        results.loc[i] =[lb, hold, sr]
        i = i+1


# In[200]:

returns = strat_rets(px, 60, 10)
results.sort(columns=['sr'], ascending = False )


# In[206]:

returns.fillna(0)


# In[207]:

(returns/100+1).cumprod()


# In[212]:

results['sr'].plot()


# In[ ]:



