from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.datasets import Dataset

from datetime import datetime
import statistics as sts
import pandas as pd


# PythonOperators com funcition mais complexas e Datasets


# Dag 
dag = DAG(
    'Decima_oitava',
    description='Decima oitava dag, Python Operator avançado e Datasets',
    start_date=datetime.now(),
    schedule=None,
    catchup=False
)    


# Dataset
my_data_set = Dataset('/data/Churn_clean.csv')


# funciton 
def clean_data (): 
    df = pd.read_csv('./data/Churn.csv', sep=';')
    df.columns = [
        "Id","Score","Estado","Genero","Idade","Patrimonio",
        "Saldo","Produtos","TemCartCredito","Ativo","Salario","Saiu"
    ]


    mediana = sts.median(df["Salario"])
    df["Salario"].fillna(mediana, inplace=True)
    df["Genero"].fillna('Masculino', inplace=True)

    median_age = sts.median(df["Idade"])

    df.loc[(df["Idade"]<0) |  (df["Idade"]>120),
           "Idade"] = median_age

    df.drop_duplicates(subset="Id", keep="first",inplace=True)
    df.to_csv('./data/Churn_clean.csv')



# Task
task1 = PythonOperator(
    task_id="t1",
    python_callable=clean_data,
    dag=dag,
    outlets=[my_data_set]
)


# Execução
task1