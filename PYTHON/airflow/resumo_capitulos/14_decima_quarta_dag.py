from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.operators.empty import EmptyOperator

# DUMMY Não faz nada, apenas evita um como erros de lista de tarefas chamando outra lista de tarefas.

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
dag = DAG('decima_quarta',
           default_args=default_args,
           description='decima_quarta, dummy',
           schedule='@hourly',
           tags=['pipeline','send email','processo','tag'],
           catchup=False)


# Tasks
task1 = BashOperator(task_id='tkss1',bash_command="sleep 2", dag=dag)
task2 = BashOperator(task_id='tkss2',bash_command="sleep 2", dag=dag)
task3 = BashOperator(task_id='tkss3',bash_command="sleep 2", dag=dag)
task4 = EmptyOperator(task_id='empty', dag=dag)
task5 = BashOperator(task_id='tkss4',bash_command="sleep 2", dag=dag)
task6 = BashOperator(task_id='tkss5',bash_command="sleep 2", dag=dag)



# Ordem de execução
[task1,task2,task3] >> task4 >> [task5,task6]
