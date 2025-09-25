from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
                    # pools

# valores defaults
default_args = {
    'depends_on_past' : False,
    'start_date': datetime(2022,7,9),
    'email' : ['teste@emailteste'],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retry' : 1,
    'retry_delay' : None
}

# DAG
dag = DAG('decima_sexta',
           default_args=default_args,
           description='decima_sexta, pools',
           schedule=None,
           tags=['pipeline','pool','tag'],
           catchup=False)


# Tasks
task1 = BashOperator(task_id='tkss1',bash_command="sleep 20", dag=dag, pool='mypool')
task2 = BashOperator(task_id='tkss2',bash_command="sleep 20", dag=dag, pool='mypool')
task3 = BashOperator(task_id='tkss3',bash_command="sleep 20", dag=dag, pool='mypool')