import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Configure the dashboard layout
st.set_page_config(
    page_title="Calgary Transit Analytics",
    page_icon="🚌",
    layout="wide"
)

# Load database credentials
load_dotenv()
password = os.getenv("DB_PASSWORD")

# Configure MySQL connection
engine = create_engine(
    f"mysql+mysqlconnector://root:{password}@localhost:3306/calgary_transit"
)

# Cache database results for 60 seconds
@st.cache_data(ttl=60)
def get_transit_data():
    query = "SELECT * FROM transit_stops"
    return pd.read_sql(query, engine)

# Retrieve transit data
df = get_transit_data()
# Calculate transit stop statistics
total_stops = len(df)

active_stops = len(df[df["status"] == "ACTIVE"])

inactive_stops = len(df[df["status"] == "INACTIVE"])

# Calculate the percentage of active stops
active_percentage = (active_stops / total_stops * 100) if total_stops else 0

# Display dashboard title and description
st.title("Calgary Transit Analytics Dashboard")
st.write("An interactive dashboard for analyzing Calgary Transit stops.")

# Create a sidebar filter for transit stop status
selected_status = st.sidebar.selectbox(
    "Filter by Status",
    ["All", "ACTIVE", "INACTIVE"]
)

# Filter the dataset based on the selected status
if selected_status == "All":
    filtered_df = df
else:
    filtered_df = df[df["status"] == selected_status]

# Create four columns for the dashboard metrics
col1, col2, col3, col4 = st.columns(4)

# Display key transit stop statistics
col1.metric("Total Stops", f"{total_stops:,}")
col2.metric("Active Stops", f"{active_stops:,}")
col3.metric("Inactive Stops", f"{inactive_stops:,}")
col4.metric("Active Percentage", f"{active_percentage:.2f}%")

# Calculate the number of stops by status
status_counts = df["status"].value_counts()

# Display the status distribution chart
st.subheader("Transit Stops by Status")
st.bar_chart(status_counts)

# Display the geographical locations of transit stops
st.subheader("Calgary Transit Stop Locations")

# Display locations based on the selected status
st.map(filtered_df[["latitude", "longitude"]])

# Display a preview of the transit data
st.subheader("Transit Stops Data")
st.dataframe(filtered_df)