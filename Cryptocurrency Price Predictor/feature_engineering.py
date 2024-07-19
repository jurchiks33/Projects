import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def feature_engineering(df):
    df['MA7'] = df['price'].rolling(window=7).mean()
    df['MA14'] = df['price'].rolling(window=14).mean()
    df['MA21'] = df['price'].rolling(window=21).mean()

    # trade signal calculation
    df['Buy_signal_Price'] = np.where(df['MA7'] > df['MA21'], df['price'], np.nan)
    df['Sell_signal_Price'] = np.where(df['MA7'] < df['MA21'], df['price'], np.nan)

    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['price'], label='Bitcoin Price', alpha=0.5)
    plt.plot(df['timestamp'], df['MA7'], label='MA7', alpha=0.5)
    plt.plot(df['timestamp'], df['MA14'], label='MA14', alpha=0.5)
    plt.plot(df['timestamp'], df['MA21'], label='MA21', alpha=0.5)
    plt.scatter(df['timestamp'], df['Buy_signal_Price'], label='Buy', marker='^', color='green')
    plt.scatter(df['timestamp'], df['Sell_signal_Price'], label='Sell', marker='v', color='green')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Bitcoin Price with moving Averages')
    plt.legend()
    plt.show
    return df


if __name__ == "__main__":
    df = pd.read_csv('Bitcoin_data.csv')
    df = feature_engineering(df)
    df.to_csv('Bitcoin_data_with_features.csv', index=False)

