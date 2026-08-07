import pandas as pd

def transform_data(transit_data):
    #Create separate copy
    transit_data = transit_data.copy()

    #Drop 'GLOBALID'
    transit_data = transit_data.drop(columns = "GLOBALID")

    #Reformat the points column
    transit_data["POINT"] = transit_data["POINT"].str.replace("POINT (", "")
    transit_data["POINT"] = transit_data["POINT"].str.replace(")", "")

    #Split POINTS column to longitude and latitude
    transit_data[["longitude","latitude"]] = transit_data["POINT"].str.split(expand=True)

    #Drop points columns and date (they don't provide analytical value)
    transit_data = transit_data.drop(columns = ["POINT","CREATE_DT_UTC","MOD_DT_UTC"])


    #Convert longitude and latitude to float
    transit_data["longitude"] = transit_data["longitude"].astype(float)
    transit_data["latitude"] = transit_data["latitude"].astype(float)

    #Rename columns to lowercase
    transit_data.columns = transit_data.columns.str.lower()

    return transit_data







