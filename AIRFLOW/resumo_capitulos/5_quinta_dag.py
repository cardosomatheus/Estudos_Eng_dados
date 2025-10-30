from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Iniciando aprendizado sobre trigger role
# A ideia é que caso não tenha erro, essa task3 fica skipped
dag = DAG('quinta_dag',
          description= 'Quinta dag no airflow',
          schedule=None,
          start_date=datetime(2013,9,16),
          catchup=False)


task1 = BashOperator(task_id='tks1', bash_command="sleep 10", dag=dag)
task2 = BashOperator(task_id='tks2', bash_command="sleep 10", dag=dag)
task3 = BashOperator(task_id='tks3',bash_command="sleep 5",
                     dag=dag,trigger_rule='one_failed'
                    )


[task1,task2] >> task3