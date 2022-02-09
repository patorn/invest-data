import yfinance as yf
import time

interval = '1m'
period = '2d'
max_attempt = 3

def download(ticker, fname, interval, period, max_attempt):
    for attempt in range(max_attempt):
        time.sleep(2)
        try:
            data = yf.download(ticker, interval=interval, period=period)
            data.to_csv(fname)
        except Exception as e:
            if attempt < max_attempt - 1:
                print('Attempt {}: {}'.format(attempt + 1, str(e)))
            else:
                raise
        else:
            break

if __name__ == "__main__":
    print("Downloading VIX")
    download('^VIX', 'data/vix_1m.csv', interval, period, max_attempt)
    print("Downloading VVIX")
    download('^VVIX', 'data/vvix_1m.csv', interval, period, max_attempt)
