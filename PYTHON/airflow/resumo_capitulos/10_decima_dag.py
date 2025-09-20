from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun  import TriggerDagRunOperator
from datetime import datetime, timedelta

# Aumentando a complexidade da DAG

# Iniciando aprendizado sobre trigger role
default_args = {
    'depends_on_past' : False,
    'start_date': datetime(2022,9,5),
    'email' : ['teste:teste.com'],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retry' : 1,
    'retry_delay' : timedelta(seconds=10)
}

# DAG
dag = DAG('decima_dag11',
           default_args=default_args,
           description='decima dag no airflow1',
           schedule='@hourly',
           tags=['pipeline','processo','tag'],
           catchup=False)


# Tasks
task1 = BashOperator(task_id='tkss1',bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(task_id='tkss2',trigger_dag_id="decima_dag2", dag=dag)

# Ordem de execução
task1 >> task2
