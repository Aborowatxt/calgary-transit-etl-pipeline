import pandas as pd
from src.extract import extract_data


def test_extract_data(tmp_path):
    # Create a temporary CSV file
    file_path = tmp_path / "test_stops.csv"

    sample_data = pd.DataFrame({
        "TELERIDE_NUMBER": [1001, 1002],
        "STOP_NAME": ["Stop A", "Stop B"]
    })

    sample_data.to_csv(file_path, index=False)

    # Extract the CSV using our function
    result = extract_data(file_path)

    # Verify the extracted data
    assert len(result) == 2
    assert result["STOP_NAME"].iloc[0] == "Stop A"