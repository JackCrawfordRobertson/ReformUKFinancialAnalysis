import pandas as pd
import json

# Load the original data from the JSON file
with open("cleaned_data.json", "r") as f:
    data = json.load(f)

# Convert JSON data to a DataFrame for easier processing
df = pd.DataFrame(data)

# Convert 'AcceptedDate' to datetime format for filtering
df['AcceptedDate'] = pd.to_datetime(df['AcceptedDate'], errors='coerce')

# Define the cutoff date
cutoff_date = pd.Timestamp("2024-06-04")

# Filter the DataFrame for donations with an 'AcceptedDate' on or after the cutoff date
filtered_df = df[df['AcceptedDate'] >= cutoff_date]

# Select only the specified fields for each entry
fields_to_keep = [
    "RegulatedEntityName", "RegulatedEntityType", "Value",
    "AcceptedDate", "ReceivedDate", "ReportedDate",
    "IsReportedPrePoll", "ReportingPeriodId", "ReportingPeriodName"
]
cleaned_df = filtered_df[fields_to_keep]

# Convert datetime fields to strings for JSON serialization
date_fields = ["AcceptedDate", "ReceivedDate", "ReportedDate"]
for field in date_fields:
    cleaned_df[field] = cleaned_df[field].astype(str)

# Convert the DataFrame back to a list of dictionaries
cleaned_data = cleaned_df.to_dict(orient='records')

# Save the cleaned data to a new JSON file
with open("filtered_cleaned_data.json", "w") as f:
    json.dump(cleaned_data, f, indent=4)

print("Data successfully filtered, cleaned, and saved to filtered_cleaned_data.json")