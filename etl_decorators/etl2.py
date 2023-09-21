import requests
import pandas as pd
import json
import logging

def extract():
    url = 'https://api-colombia.com/api/v1/Region'
    params = {
    }
    logging.info("Starting data extraciton")
    try:
        response = requests.get(url)
        data = response.json()
        regions = [region["name"] for region in data ]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    data = {
            'region': regions,
    }
    logging.info("extraction finished")
    df = pd.DataFrame(data, index=None)
    logging.debug('data extracted is ', df)
    df.to_csv('data.csv')
    return df.to_json(orient='records')

def transform(json_data):
    # str_data = json_data
    print("data coming from extract:", json_data)
    print("data type is: ", type(json_data))
    #json_data = json.loads(str_data)
    #data = pd.json_normalize(data=json_data)
    #logging.info(f"data is: {data}")
    #data['region2'] = data['region']
    #function transform
    #return data.to_json(orient='records')
    return json_data


def load(json_data):
    logging.info("starting load process")
    #data = pd.json_normalize(data=json_data)
    logging.info( f"data to load is: {json_data}")
    logging.info("Loading data")
    #TODO: do the load here
    logging.info( "data loaded in: table_name")
