import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import json


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 4, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
}

def get_data(**kwargs):
    api_url = 'https://publicapi.traffy.in.th/share/teamchadchart/search'
    limit = 1000
    offset = kwargs['ti'].xcom_pull(key='offset', task_ids='get_offset')

    response = requests.get(api_url, params={'limit': limit, 'offset': offset})
    data = json.loads(response.text)

    # Save data to file or database
    print(len(data))

    offset += limit
    kwargs['ti'].xcom_push(key='offset', value=offset)

def wait_10_sec():
    return 'sleep 10'

with DAG(
    dag_id='get_data_from_api',
    default_args=default_args,
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:
    get_offset = PythonOperator(
        task_id='get_offset',
        python_callable=lambda: 1,
        provide_context=True,
    )

    get_data = PythonOperator(
        task_id='get_data',
        python_callable=get_data,
        provide_context=True,
    )

    wait_10_sec = BashOperator(
        task_id='wait_10_sec',
        bash_command=wait_10_sec,
    )

    check_limit = PythonOperator(
        task_id='check_limit',
        python_callable=lambda ti: ti.xcom_pull(key='offset', task_ids='get_data') > 100000,
        provide_context=True,
    )

    get_offset >> get_data
    get_data >> wait_10_sec >> check_limit
    check_limit >> get_data
    # wait_10_sec >> get_data
