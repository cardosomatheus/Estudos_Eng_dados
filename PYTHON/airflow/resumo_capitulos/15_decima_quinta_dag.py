from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta

# Variaveis

# Iniciando aprendizado sobre trigger role
default_args = {
    'depends_on_past' : False,
    'start_date': datetime(2022,7,9),
    'email' : ['cardosomcds1@gmail.com'],
    'email_on_failure' : True,
    'email_on_retry' : False,
    'retry' : 1,
    'retry_delay' : timedelta(seconds=5)
}

# DAG
dag = DAG('decima_quinta',
           default_args=default_args,
           description='decima_quinta, variables',
           schedule='@hourly',
           tags=['pipeline','send email','processo','tag'],
           catchup=False)


def print_variable(**context):
    var = Variable.get('key')
    print('my variable',var)

# Tasks
task1 = PythonOperator(task_id='tkss1',python_callable=print_variable, dag=dag)


# Ordem de execução
task1
