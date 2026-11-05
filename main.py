from src.extract import extract_data
from src.validate import validate_data
from src.transform import transform_data
from src.load import load_data


def main():
    # Extract
    original_data = extract_data("data/calgary_transit_stops.csv")

    # Validate
    accepted, rejected = validate_data(original_data)

    print(f"Accepted records: {len(accepted)}")
    print(f"Rejected records: {len(rejected)}")

    # Transform accepted records
    transformed_data = transform_data(accepted)

    # Load into MySQL
    load_data(transformed_data)


if __name__ == "__main__":
    main()