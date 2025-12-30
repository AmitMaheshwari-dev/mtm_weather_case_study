import pandas as pd

def load_daily(path):
    df = pd.read_excel(path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def load_monthly(path):
    return pd.read_excel(path)