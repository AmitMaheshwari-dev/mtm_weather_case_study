from datetime import date

def generate_report(mtm_df):
    mtm_df["Report Date"] = date.today()
    mtm_df["Pricing Status"] = mtm_df["MTM Value"].apply(
        lambda x: "OK" if x is not None else "INCOMPLETE"
    )
    return mtm_df
