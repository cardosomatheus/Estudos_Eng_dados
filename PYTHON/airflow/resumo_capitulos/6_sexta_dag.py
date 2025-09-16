from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


# Iniciando aprendizado sobre trigger role
# A ideia é que a task2 falhe e a task3 seja executada.
dag = DAG('sexta_dag',
          description='Sexta dag no airflow',
          schedule=None,
          start_date= datetime(2024,9,15),
          catchup=False)



task1 = BashOperator(task_id='tkss1',bash_command="sleep 10", dag=dag)
task2 = BashOperator(task_id='tkss2',bash_command="SLLeep 10", dag=dag)
task3 = BashOperator(task_id='tkss3',bash_command="sleep 10",
                     dag=dag, trigger_rule='one_failed')

[task1,task2] >> task3