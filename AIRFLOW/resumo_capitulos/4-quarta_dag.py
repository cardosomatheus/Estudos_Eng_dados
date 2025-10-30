from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Criando uma Dag no padão de script python.
with DAG('quarta_dag',
          description='Terceira dag no airflow',
          schedule=None,
          start_date=datetime(2023,10,9),
          catchup=False) as dag:


    #tarfas da dag
    task1 = BashOperator(task_id="tsk1",bash_command="sleep 10",dag=dag )
    task2 = BashOperator(task_id="tsk2",bash_command="sleep 10",dag=dag )
    task3 = BashOperator(task_id="tsk3",bash_command="sleep 10",dag=dag )

    # Ordem aciclica  através de upstream e downstream
    task1.set_upstream(task2)
    task2.set_upstream(task3)