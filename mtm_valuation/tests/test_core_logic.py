from mtm.calculator import fe_adjustment, calculate_dmt

def test_fe_adjustment():
    row = {"Typical Fe": 60}
    assert round(fe_adjustment(row), 4) == round(60/62, 4)

def test_dmt_conversion():
    row = {"Unit": "WMT", "Quantity": 100, "Moisture": 0.05}
    assert calculate_dmt(row) == 95
