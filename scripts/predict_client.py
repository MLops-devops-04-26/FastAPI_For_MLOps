# scripts/predict_client.py

import requests
import json

# The URL of the prediction endpoint
url = "http://127.0.0.1:8000/predict"

# The data for the prediction, matching the Pydantic model in the API
# This represents a single house's features.
payload = {
  "features": {
    "LotArea": 8450,
    "OverallQual": 7,
    "YearBuilt": 2003,
    "TotRmsAbvGrd": 8,
    "GarageCars": 2
  }
}

# Send the POST request to the API
# We use json.dumps to convert our Python dictionary to a JSON string
response = requests.post(url, data=json.dumps(payload))

# Print the prediction from the response
print(f"API URL: {url}")
print(f"Request Payload: {json.dumps(payload, indent=2)}")
print("-" * 20)
print(f"Response Status Code: {response.status_code}")
print(f"Prediction Response: {response.json()}")

