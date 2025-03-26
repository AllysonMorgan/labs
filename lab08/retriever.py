import requests
from datetime import datetime

API_KEY = "DEMO_KEY" 

def get_apod(date=None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")