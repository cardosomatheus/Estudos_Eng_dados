#Libs
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Dag criada
dag = DAG('segunda_dag',
           description= 'Segunda dag no airflow',
           schedule=None,
           start_date=datetime(2023,10,9),
           catchup=False)

#tarfas da dag
task1 = BashOperator(task_id="tsk1",bash_command="sleep 10",dag=dag )
task2 = BashOperator(task_id="tsk2",bash_command="sleep 10",dag=dag )
task3 = BashOperator(task_id="tsk3",bash_command="sleep 10",dag=dag )

# Ordem aciclica com paralelismo.
task1 >> [task2,task3]