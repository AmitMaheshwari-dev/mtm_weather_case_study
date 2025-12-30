import pandas as pd

def execute_query(plan, daily_df, monthly_df):

    if plan["dataset"] == "monthly":
        df = monthly_df.copy()

        time = plan["time"]
        geo = plan["geography"]

        if time["years"]:
            df = df[df["Year"].isin(time["years"])]
        if time["months"]:
            df = df[df["Month"].isin(time["months"])]

        if geo["district"]:
            df = df[df["District"] == geo["district"]]
        if geo["state"]:
            df = df[df["State"] == geo["state"]]

        return (
            df.groupby(["Year", "Month"])["Monthly Precipitation"]
            .sum()
            .reset_index()
        )

    if plan["dataset"] == "daily":
        df = daily_df.copy()

        time = plan["time"]
        geo = plan["geography"]

        if time["start_date"]:
            df = df[df["Date"] >= time["start_date"]]
        if time["end_date"]:
            df = df[df["Date"] <= time["end_date"]]

        if geo.get("compare"):
            df = df[df["State"].isin(geo["compare"])]
        elif geo.get("state"):
            df = df[df["State"] == geo["state"]]

        return (
            df.groupby("State")["Daily Precipitation"]
            .sum()
            .reset_index()
        )

    raise ValueError("Unsupported dataset type")
