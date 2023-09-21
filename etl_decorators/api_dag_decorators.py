from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.decorators import dag, task
from etl2 import extract, transform, load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 13),  # Update the start date to today or an appropriate date
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

@dag(
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval='@daily',  # Set the schedule interval as per your requirements
)
def api_etl_project():

    @task
    def extract_task ():
        return extract(),

    @task
    def transform_task (json_data):
        return transform(json_data)

    @task
    def load_task(json_data):
        load(json_data)

    data = extract_task()
    transformed_data = transform_task(data)
    load_task(transformed_data)

workflow_api_etl_dag = api_etl_project()
