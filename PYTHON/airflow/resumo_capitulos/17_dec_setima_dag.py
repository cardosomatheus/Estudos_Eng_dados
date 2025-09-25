from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator

from datetime import datetime
from random import randint



#   Aprendendo o uso de BRANCHS em dags
# DAG
dag = DAG('decima_setima',
           start_date=datetime(2023,2,2), 
           description='decima_setima',
           schedule=None,
           catchup=False)



def generate_random_number():
    return randint(1,100)


def validate_number(**kwargs):

    ti = kwargs['ti']
    number = int(ti.xcom_pull(task_ids='gera_numero_aleatorio'))


    if number % 2 == 0:
        return 'task_par'
    else:
        return 'task_impar'
    



# tasks
gera_numero = PythonOperator(
    task_id='gera_numero_aleatorio',
    python_callable=generate_random_number,
    dag=dag
)

branch_op = BranchPythonOperator(
    task_id='branch_task',
    #provide_context=True,
    python_callable=validate_number,
    dag=dag
)

task_par = BashOperator(
    task_id='task_par',
    bash_command='echo "É PAARRRRR"',
    dag=dag
)

task_impar = BashOperator(
    task_id='task_impar',
    bash_command='echo "É IMPAARR"',
    dag=dag
)



# Ordem de execução 
gera_numero >> branch_op
branch_op >> task_par
branch_op >> task_impar

