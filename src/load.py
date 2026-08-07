import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from the .env file.
load_dotenv()


def load_data(transit_data):
    # Retrieve the MySQL password from the environment.
    password = os.getenv("DB_PASSWORD")

    # Create a connection to the Calgary Transit database.
    engine = create_engine(
        f"mysql+mysqlconnector://root:{password}@localhost:3306/calgary_transit"
    )

    # Load the cleaned DataFrame into a MySQL table.
    transit_data.to_sql(
        name="transit_stops",
        con=engine,
        if_exists="replace",  # Replace the table if it already exists.
        index=False,          # Don't save the pandas index as a column.
    )

    print("Data loaded successfully!")