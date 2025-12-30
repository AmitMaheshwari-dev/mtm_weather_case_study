def get_base_price(prices, index_name, tenor):
    df = prices[
        (prices["Index Name"] == index_name) &
        (prices["Tenor"] == tenor)
    ]

    if df.empty:
        raise ValueError(f"No price found for {index_name} {tenor}")

    return df.sort_values("Price Date").iloc[-1]["Price"]
