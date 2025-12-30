from pandas.tseries.offsets import MonthEnd

def normalize_indexes(prices, contracts):
    prices["Index Name"] = prices["Index Name"].str.replace("PLTTS", "PLATTS")
    contracts["Base Index"] = contracts["Base Index"].str.replace("PLTTS", "PLATTS")
    return prices, contracts

def normalize_tenor(prices, contracts):
    prices["Tenor"] = prices["Tenor"] + MonthEnd(0)
    contracts["Tenor"] = contracts["Tenor"] + MonthEnd(0)
    return prices, contracts