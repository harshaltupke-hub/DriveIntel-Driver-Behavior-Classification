import sqlite3
import pandas as pd

# Load the raw sensor dataset
raw_df = pd.read_csv("C:/Users/htupk/OneDrive/Desktop/DriveIntel/data/sensor_raw.csv")

# Connect to SQLite database
connection = sqlite3.connect("driveintel.db")

# Store dataframe as SQL table
raw_df.to_sql(
    "sensor_readings",
    connection,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

connection.close()