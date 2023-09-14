import requests
import pandas as pd

def extract():
    url = 'https://api-colombia.com/api/v1/Region'
    params = {
    }
    try:
        response = requests.get(url)
        data = response.json()
        regions = [region["name"] for region in data ]
        print(data[1]['name'])
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    data = {
            'region': regions,
    }

    df = pd.DataFrame(data)
    df.to_csv('data.csv')
