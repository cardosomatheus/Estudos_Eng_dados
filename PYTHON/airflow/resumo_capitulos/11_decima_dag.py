from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

# Aumentando a complexidade da DAG

# Iniciando aprendizado sobre trigger role
default_args = {'start_date': datetime(2022,9,5)}

# DAG
dag = DAG('decima_dag2',
           default_args=default_args,
           description='decima dag no airflow1',
           schedule=None,
           catchup=False)


# Tasks
task1 = BashOperator(task_id='tkss1',bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id='tkss2',bash_command="sleep 5", dag=dag)

# Ordem de execução
task1 >> task2
