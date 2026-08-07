from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def main():
    #Extracting original data from csv file
    original_transit_data = extract_data("data/calgary_transit_stops.csv")

    #Clean and make necessary changes to data
    transformed_transit_data = transform_data(original_transit_data)

    #Load transformed data into MySQL
    load_data(transformed_transit_data)

if __name__ == "__main__":
    main()
    print("Data loaded")
