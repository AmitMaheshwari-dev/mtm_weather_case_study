import pandas as pd

def load_data(excel_path: str):
    prices = pd.read_excel(excel_path, sheet_name="Price")
    contracts = pd.read_excel(excel_path, sheet_name="Contracts")

    prices["Price Date"] = pd.to_datetime(prices["Price Date"])
    prices["Tenor"] = pd.to_datetime(prices["Tenor"])
    contracts["Tenor"] = pd.to_datetime(contracts["Tenor"])

    return prices, contracts
