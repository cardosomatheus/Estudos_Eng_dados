from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.python import PythonOperator

from datetime import datetime
import requests



# DAG
dag = DAG(
    'vigesima',
    description='vigesima dag, sensors',
    start_date=datetime.now(),
    schedule=None,
    catchup=False
)    

# Sensor http
api_sensor = HttpSensor(
    task_id="sensor1",
    http_conn_id="rickmorthy",
    method="GET",
    endpoint="character",
    request_params=None,
    headers=None
)

# funcção ler api
def read_api ():
    api = requests.get("https://rickandmortyapi.com/api/character/1")
    retorno = dict(api.json())
    print(f'Nome Campitulo: {retorno.get("name")}')


#task
task1 = PythonOperator(task_id='tk1', python_callable=read_api, dag=dag)

# Ordem execução.
api_sensor >> task1 