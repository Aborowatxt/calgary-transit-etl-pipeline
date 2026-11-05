import os #operating system

from dotenv import load_dotenv  #reads .env files
from sqlalchemy import create_engine, text #connects to sql

# Load environment variables from the .env file.
load_dotenv()


def load_data(transit_data):
    password = os.getenv("DB_PASSWORD")

    #Configure connection to local MySQL database
    engine = create_engine(
        f"mysql+mysqlconnector://root:{password}@localhost:3306/calgary_transit"
    )

    # Insert new stops or update existing stops based on their primary key
    query = """
        INSERT INTO transit_stops (
            teleride_number, stop_name, status, longitude, latitude
        )
        VALUES (
            :teleride_number, :stop_name, :status, :longitude, :latitude
        )
        ON DUPLICATE KEY UPDATE
            stop_name = VALUES(stop_name),
            status = VALUES(status),
            longitude = VALUES(longitude),
            latitude = VALUES(latitude)
    """

    # Convert DataFrame rows into dictionaries for SQLAlchemy
    records = transit_data.to_dict(orient="records")

    # Execute upserts in a transaction
    with engine.begin() as connection:
        connection.execute(text(query), records)

    # Display number of records processed
    print(f"Successfully loaded {len(records)} records!")