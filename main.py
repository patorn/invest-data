import yfinance as yf

data = yf.download("^VIX", interval="1m", period="7d")
data.to_csv('data/vix_1m_7d.csv')
