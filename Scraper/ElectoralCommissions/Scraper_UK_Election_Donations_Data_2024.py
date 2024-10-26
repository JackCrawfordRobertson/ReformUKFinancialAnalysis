import requests
import json
import time

# Base URL for the Electoral Commission's API with specified parameters for political parties
base_url = "https://search.electoralcommission.org.uk/api/search/Donations"

# Parameters based on the provided URL, selecting only "Political Party" entries
params = {
    "query": "",
    "sort": "AcceptedDate",
    "order": "desc",
    "et": "pp",  # Only Political Parties
    "date": "Reported",
    "from": "2024-06-04",
    "to": "2024-10-12",
    "prePoll": "false",
    "postPoll": "false",
    "register": ["gb", "none", "ni"],
    "period": [
        3891, 3898, 3889, 3897, 3896, 3887, 3895, 3885, 3883, 3894, 3881, 
        3893, 3874, 3865, 3862, 3810, 3765, 3767, 3718, 3720, 3714, 3716, 
        3710, 3712, 3706, 3708, 3702, 3704, 3698, 3700, 3676, 3695, 3604, 
        3602, 3600, 3598, 3594, 3596, 3578, 3580, 3574, 3576, 3570, 3572, 
        3559, 3524, 3567, 3522, 3520, 3518, 2513, 2507, 2509, 2511, 1485, 
        1487, 1480, 1481, 1477, 1478, 1476, 1474, 1471, 1473, 1466, 463, 
        1465, 460, 447, 444, 442, 438, 434, 409, 427, 403, 288, 302, 304, 
        300, 280, 218, 206, 208, 137, 138, 128, 73, 69, 61, 63, 50, 40, 
        39, 5
    ],
    "isIrishSourceYes": "true",
    "isIrishSourceNo": "true",
    "includeOutsideSection75": "true",
    "rows": 49  # Number of rows per page
}

# List to store all retrieved data
all_data = []

# Pagination settings
page = 0
total_records = 2688  # Adjust based on the estimated total records if needed

# Loop through pages until all records are retrieved
while page * params["rows"] < total_records:
    params["start"] = page * params["rows"]  # Update the start parameter for pagination
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        json_data = response.json()
        if "Result" in json_data and json_data["Result"]:
            all_data.extend(json_data["Result"])  # Append all data without filtering fields
            print(f"Page {page} retrieved, total records so far: {len(all_data)}")
        else:
            print("No more data returned. Ending pagination.")
            break
    else:
        print(f"Failed to fetch page {page}. Status Code: {response.status_code}")
        break

    page += 1
    time.sleep(5)  # Delay to avoid overloading the server

# Save all data to a JSON file
with open("complete_data_political_party.json", "w") as f:
    json.dump(all_data, f, indent=4)

print("Data successfully saved to complete_data_political_party.json")