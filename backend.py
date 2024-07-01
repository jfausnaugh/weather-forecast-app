import requests
import os
from dotenv import load_dotenv

# get API Key from environmental variable
load_dotenv()
YOUR_API_KEY = os.getenv(key='API_KEY')


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={YOUR_API_KEY}"
    response = requests.get(url, timeout=60)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=1))
