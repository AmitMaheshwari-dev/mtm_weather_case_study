from mtm.loader import load_data
from mtm.normalizer import normalize_indexes, normalize_tenor
from mtm.calculator import calculate_mtm
from mtm.report import generate_report

DATA_FILE = "data/Trading Case Example Data.xlsx"

def main():
    prices, contracts = load_data(DATA_FILE)

    prices, contracts = normalize_indexes(prices, contracts)
    prices, contracts = normalize_tenor(prices, contracts)

    mtm_df = calculate_mtm(prices, contracts)
    report = generate_report(mtm_df)

    report.to_excel("MTM_Report.xlsx", index=False)
    print("MTM Report generated successfully.")

if __name__ == "__main__":
    main()
