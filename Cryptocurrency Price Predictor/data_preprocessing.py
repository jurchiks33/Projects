import pandas as pd
import matplotlib.pyplot as plt

def preprocess_data(file_path):
    df = pd.read_csv(file_path)


    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['price'], label='Bitcoin price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Bitcoin Price Over Time')
    plt.legend()
    plt.show()

    return df

if __name__ == "__main__":
    df = preprocess_data('bitcoin_data.csv')