def normalize_plan(plan: dict, daily_df=None, monthly_df=None) -> dict:
    # ---- Normalize time ----
    time = plan.setdefault("time", {})
    time["years"] = time.get("years", [])
    time["months"] = time.get("months", [])
    time.setdefault("start_date", None)
    time.setdefault("end_date", None)

    # ---- Normalize geography ----
    geo = plan.setdefault("geography", {})
    geo.setdefault("level", None)
    geo.setdefault("state", None)
    geo.setdefault("district", None)
    geo.setdefault("compare", None)

    # ---- Case 1: state is a list → comparison ----
    if isinstance(geo.get("state"), list):
        geo["compare"] = geo["state"]
        geo["state"] = None

    # ---- Case 2: compare exists → ensure list ----
    if geo.get("compare"):
        geo["compare"] = list(set(geo["compare"]))
        geo["state"] = None

    # ---- Case 3: district/state confusion ----
    candidate = geo.get("state")
    if candidate and not geo.get("district") and daily_df is not None:
        if candidate in set(daily_df["District"].unique()):
            geo["district"] = candidate
            geo["state"] = None
            geo["level"] = "district"

    return plan
