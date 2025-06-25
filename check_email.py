import requests

email = "test"
uri = "https://adsmagnify-reporting.onrender.com/check-email"

print("Sending Request to server")
response = requests.post(uri, json={'email': email}, headers={'Content-Type': 'application/json'})
print("Status:", response.status_code)
