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
