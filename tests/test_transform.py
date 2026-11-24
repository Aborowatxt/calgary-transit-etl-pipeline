import pandas as pd
from src.transform import transform_data


def test_transform_data():

    # Create a sample dataset with the original CSV columns
    sample_data = pd.DataFrame({
        "TELERIDE_NUMBER": [1001],
        "STOP_NAME": ["Stop A"],
        "STATUS": ["ACTIVE"],
        "CREATE_DT_UTC": ["2026-06-10"],
        "MOD_DT_UTC": ["2026-06-10"],
        "GLOBALID": ["abc123"],
        "POINT": ["POINT (-114.06 51.15)"]
    })

    # Run the transformation function on the sample data
    result = transform_data(sample_data)

    # Check that no records were lost during transformation
    assert len(result) == 1

    # Verify that the correct columns remain after transformation
    assert list(result.columns) == [
        "teleride_number",
        "stop_name",
        "status",
        "longitude",
        "latitude"
    ]

    # Check that coordinates were separated correctly
    assert result["longitude"].iloc[0] == -114.06
    assert result["latitude"].iloc[0] == 51.15

    # Verify that coordinates were converted to floats
    assert result["longitude"].dtype == float
    assert result["latitude"].dtype == float