from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun  import TriggerDagRunOperator
#from airflow.operators.import TriggerDagRunOperator
from datetime import datetime

# Aumentando a complexidade da DAG

# Iniciando aprendizado sobre trigger role
default_args = {'start_date': datetime(2022,9,5)}

# DAG
dag = DAG('decima_dag1',
           default_args=default_args,
           description='decima dag no airflow1',
           schedule=None,
           catchup=False)


# Tasks
task1 = BashOperator(task_id='tkss1',bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(task_id='tkss2',trigger_dag_id="decima_dag2", dag=dag)

# Ordem de execução
task1 >> task2
