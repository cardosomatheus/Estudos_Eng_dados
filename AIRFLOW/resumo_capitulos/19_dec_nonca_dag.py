from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.datasets import Dataset

from datetime import datetime
import pandas as pd


# Execute a DAG Decima_oitava, a Decima_nona será execultada automaticamente após isso

my_data_set = Dataset('/data/Churn_clean.csv')

dag = DAG(
    'Decima_nona',
    description='Decima nona dag, Consulmindo datasets de outra fonte sempre que alterado.',
    start_date=datetime.now(),
    schedule=[my_data_set],
    catchup=False
)    



def save_file (): 
    df = pd.read_csv('./data/Churn_clean.csv', sep=';')
    df.to_csv('./data/Churn_clean2.csv')


task2 = PythonOperator(
    task_id="t2",
    python_callable=save_file,
    dag=dag
)

task2