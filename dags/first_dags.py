from datetime import datetime, timedelta
import time
import requests
import json

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 4, 17),
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='first_dag',
    description='This is first dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=1)
)

def get_data(offset):
    api_url = f'https://publicapi.traffy.in.th/share/teamchadchart/search?limit=1000&offset={offset}'
    data = requests.get(api_url)
    data_dict = json.loads(data.text)
    print(data_dict.keys())
    # Do something with the data, e.g. save to a database or file
    print(f'Retrieved data with offset {offset}')
    
with dag:

    for offset in range(0, 10001, 1000):
        get_data_task = PythonOperator(
            task_id=f'get_data_offset_{offset}',
            python_callable=get_data,
            op_kwargs={'offset': offset},
        )

        bash_task = BashOperator(
            task_id=f'bash_task_{offset}',
            bash_command='echo this task will run after get_data_task',
        )

        get_data_task >> bash_task
