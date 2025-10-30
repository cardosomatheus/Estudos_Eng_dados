# Aprendendo sobre XCON (apenas para trocas de pouco dados como definição de variaveis).
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

# Aumentando a complexidade da DAG

# Iniciando aprendizado sobre trigger role
# A ideia é que se a task1 e task2 falharem, a task3 será executada.
default_args = {
    'start_date': datetime(2022,9,5)
}

# DAG
dag = DAG('decima_segunda',
           default_args=default_args,
           description='xcom push and pull',
           schedule=None,
           catchup=False)


def task_write(ti):
    ti.xcom_push(key='valorpush', value=123123)


def task_read(ti):
    valor = ti.xcom_pull(key='valorpush',task_ids='tkss1')
    print(f'logInfo: valor retornado >> {valor}')

# Tasks
task1 = PythonOperator(task_id='tkss1',python_callable=task_write, dag=dag)
task2 = PythonOperator(task_id='tkss2',python_callable=task_read, dag=dag)


# Ordem de execução
task1 >> task2

