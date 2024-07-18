import requests
import pandas as pd

def fetch_crypto_data(crypto, days=30):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart'
    params = {'vs_currency': 'usd', 'days': days, 'interval': 'daily'}
    response = requests.get(url, params=params)
    data = response.json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

if __name__ == "__main__":
    # Fetching Bitcoin data for the last 30 days
    crypto_data = fetch_crypto_data('bitcoin', 30)
    crypto_data.to_csv('bitcoin_data.csv', index=False)
