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

def transform(**kwargs):
    logging.info("the kwargs are: ", kwargs)
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="extract_task")
    json_data = json.loads(str_data)
    data = pd.json_normalize(data=json_data)
    logging.info(f"data is: {data}")
    data['region2'] = data['region']
    #function transform
    return data.to_json(orient='records')


def load(**kwargs):
    logging.info("starting load process")
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="transform_task")
    json_data = json.loads(str_data)
    data = pd.json_normalize(data=json_data)
    logging.info( f"data to load is: {data}")
    logging.info("Loading data")
    #TODO: do the load here
    logging.info( "data loaded in: table_name")