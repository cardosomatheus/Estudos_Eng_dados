from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

# Aumentando a complexidade da DAG

# Iniciando aprendizado sobre trigger role
# A ideia é que se a task1 e task2 falharem, a task3 será executada.
default_args = {
    'start_date': datetime(2022,9,5)
}

# DAG
dag = DAG('nona_dag',
           default_args=default_args,
           description='nona dag no airflow',
           schedule=None,
           catchup=False)


# Tasks
task1 = BashOperator(task_id='tkss1',bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id='tkss2',bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id='tkss3',bash_command="sleep 5", dag=dag)
task4 = BashOperator(task_id='tkss4',bash_command="sleep 5", dag=dag)
task5 = BashOperator(task_id='tkss5',bash_command="sleep 5", dag=dag)
task6 = BashOperator(task_id='tkss6',bash_command="sleep 5", dag=dag)

tskgroup = TaskGroup('tsk_group', dag=dag)

task7 = BashOperator(task_id='tkss7',bash_command="sleep 5", dag=dag, task_group=tskgroup)
task8 = BashOperator(task_id='tkss8',bash_command="sleep 5", dag=dag, task_group=tskgroup)
task9 = BashOperator(task_id='tkss9',bash_command="sleep 5",
                     dag=dag,trigger_rule='all_failed', task_group=tskgroup)

# Ordem de execução
task1 >> task2
task3 >> task4
[task2,task4] >> task5 >> task6
task6 >> tskgroup