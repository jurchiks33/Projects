import pandas as pd
import matplotlib.pyplot as plt

def preprocess_data(file_path):
    df = pd.read_csv(file_path)


    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['price'], label='Bitcoin price')