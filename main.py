from src.extract import extract_data
from src.validate import validate_data
from src.transform import transform_data
from src.load import load_data
import logging

#Configure log messages
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        # Extract
        logging.info("Starting ETL pipeline")
        original_data = extract_data("data/calgary_transit_stops.csv")

        # Validate
        accepted, rejected = validate_data(original_data)

        logging.info(f"Accepted records: {len(accepted)}")
        logging.info(f"Rejected records: {len(rejected)}")

        # Transform
        transformed_data = transform_data(accepted)

        # Load
        load_data(transformed_data)

        logging.info("ETL pipeline completed successfully")

    except Exception:
        logging.exception("ETL pipeline failed")
        raise


if __name__ == "__main__":
    main()