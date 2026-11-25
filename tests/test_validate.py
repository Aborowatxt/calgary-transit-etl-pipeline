import pandas as pd
from src.validate import validate_data


def test_valid_data():
    sample_data = pd.DataFrame({
        "TELERIDE_NUMBER": [1001, 1002],
        "STOP_NAME": ["Stop A", "Stop B"],
        "STATUS": ["ACTIVE", "INACTIVE"],
        "POINT": ["POINT (-114.06 51.15)",
                  "POINT (-114.08 51.12)"]
    })

    accepted, rejected = validate_data(sample_data)

    assert len(accepted) == 2
    assert len(rejected) == 0


def test_invalid_data():
    sample_data = pd.DataFrame({
        "TELERIDE_NUMBER": [1001, 1002, 1002, 1003, 1004, 1005],
        "STOP_NAME": ["Stop A", "Stop B", "Stop C",
                      None, "Stop E", "Stop F"],
        "STATUS": ["ACTIVE", "ACTIVE", "ACTIVE",
                   "ACTIVE", "CLOSED", "ACTIVE"],
        "POINT": ["POINT (-114.06 51.15)"] * 5
                 + ["POINT (-200 95)"]
    })

    accepted, rejected = validate_data(sample_data)

    assert len(accepted) == 1
    assert len(rejected) == 5
    assert accepted["TELERIDE_NUMBER"].iloc[0] == 1001