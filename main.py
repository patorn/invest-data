import yfinance as yf

interval = '1m'
period = '7d'

data = yf.download("^VIX", interval=interval, period=period)
data.to_csv('data/vix_1m_7d.csv')

data = yf.download("^VVIX", interval=interval, period=period)
data.to_csv('data/vvix_1m_7d.csv')
