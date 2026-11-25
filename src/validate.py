import pandas as pd


def validate_data(df):
    df = df.copy()

    # 1. Check missing required values
    required = ["TELERIDE_NUMBER", "STOP_NAME", "STATUS", "POINT"]

    missing = df[required].isna().any(axis=1)

    # 2. Check duplicate stop IDs
    duplicates = df["TELERIDE_NUMBER"].duplicated(keep=False)

    # 3. Check invalid statuses
    statuses = df["STATUS"].str.strip().str.upper()

    invalid_status = ~statuses.isin(["ACTIVE", "INACTIVE"])

    # 4. Validate coordinates
    coords = df["POINT"].str.replace("POINT (", "", regex=False)
    coords = coords.str.replace(")", "", regex=False)

    coords = coords.str.split(expand=True)

    longitude = pd.to_numeric(coords[0], errors="coerce")
    latitude = pd.to_numeric(coords[1], errors="coerce")

    invalid_coords = (
            ~longitude.between(-180, 180)
            | ~latitude.between(-90, 90)
    )

    # Combine both checks
    invalid = missing | duplicates | invalid_status | invalid_coords

    # Separate valid and invalid records
    accepted = df.loc[~invalid].copy()
    accepted["STATUS"] = accepted["STATUS"].str.strip().str.upper()

    rejected = df.loc[invalid].copy()

    return accepted, rejected