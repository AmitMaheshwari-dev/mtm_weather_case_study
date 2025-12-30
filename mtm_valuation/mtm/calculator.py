import pandas as pd
from mtm.pricing import get_base_price

def fe_adjustment(row):
    if pd.isna(row["Typical Fe"]):
        return 1.0
    return row["Typical Fe"] / 62.0

def calculate_dmt(row):
    if row["Unit"] == "WMT":
        return row["Quantity"] * (1 - row["Moisture"])
    return row["Quantity"]

def calculate_mtm(prices, contracts):
    results = []

    for _, row in contracts.iterrows():
        base_price = get_base_price(prices, row["Base Index"], row["Tenor"])
        fe_ratio = fe_adjustment(row)
        dmt = calculate_dmt(row)

        mtm_value = (base_price * fe_ratio + row["Cost"]) * row["Discount"] * dmt

        results.append({
            "Contract_Ref": row["Contract_Ref"],
            "Index": row["Base Index"],
            "Tenor": row["Tenor"].date(),
            "Base Price": base_price,
            "Fe Ratio": round(fe_ratio, 4),
            "DMT": round(dmt, 2),
            "Discount": row["Discount"],
            "MTM Value": None if pd.isna(mtm_value) else round(mtm_value, 2)
        })

    return pd.DataFrame(results)
