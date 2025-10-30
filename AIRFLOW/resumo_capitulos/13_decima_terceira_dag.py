from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta


# Default args
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
dag = DAG('decima_terceira',
           default_args=default_args,
           description='decima_terceira, send email',
           schedule='@hourly',
           tags=['pipeline','send email','processo','tag'],
           catchup=False)


# Tasks
task1 = BashOperator(task_id='tkss1',bash_command="sleep 2", dag=dag)
task2 = BashOperator(task_id='tkss2',bash_command="sleep 2", dag=dag)
task3 = BashOperator(task_id='tkss3',bash_command="sleep 2", dag=dag)
task4 = BashOperator(task_id='tkss4',bash_command="exit 2", dag=dag)
task5 = BashOperator(task_id='tkss5',bash_command="sleep 2", dag=dag, trigger_rule='none_failed')
task6 = BashOperator(task_id='tkss6',bash_command="sleep 2", dag=dag, trigger_rule='none_failed')

# Operator de envio de email
send_email = EmailOperator(task_id='send_email',
                           to="cardosomcds1@gmail.com",
                           subject="Error in DAG",
                           html_content="""<h3>Ocorreu um erro na Dag. </h3>
                                <p>Dag: send_email </p>  
                                """,
                           dag=dag,
                           trigger_rule='one_failed')



# Ordem de execução
[task1,task2] >> task3 >> task4 >> [task5,task6,send_email]
