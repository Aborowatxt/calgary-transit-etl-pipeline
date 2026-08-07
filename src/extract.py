import pandas as pd

#Create function to extract data using file path
def extract_data(file_path):
    transit_data = pd.read_csv(file_path)
    return transit_data