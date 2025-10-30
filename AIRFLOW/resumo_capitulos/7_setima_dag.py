from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


# Iniciando aprendizado sobre trigger role
# A ideia é que se a task1 e task2 falharem, a task3 será executada.
dag = DAG('setima_dag',
          description='setima dag no airflow',
          schedule=None,
          start_date= datetime(2022,9,5),
          catchup=False)



task1 = BashOperator(task_id='tkss1',bash_command="slssep 10", dag=dag)
task2 = BashOperator(task_id='tkss2',bash_command="SLLeep 10", dag=dag)
task3 = BashOperator(task_id='tkss3',bash_command="sleep 10",
                     dag=dag, trigger_rule='all_failed')

[task1,task2] >> task3