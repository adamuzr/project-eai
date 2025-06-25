
import requests

# Define the API endpoint
api_url = "http://localhost:5000/order"

# Example order data
order = {
    "product": "laptop",
    "quantity": 9
}

# Send the order request
try:
    response = requests.post(api_url, json=order)
    print("Status Code:", response.status_code)
    print("Response:", response.json()) 
except Exception as e:
    print("Error:", str(e))
