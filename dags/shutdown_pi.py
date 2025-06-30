from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 0,
}

with DAG(
    dag_id='shutdown_pi',
    default_args=default_args,
    description='Shutdown Raspberry Pi on schedule',
    schedule_interval=None,  # можеш поставити cron або щось типу '@daily'
    catchup=False,
    tags=['raspberry', 'system'],
) as dag:

    shutdown = BashOperator(
        task_id='shutdown_pi_task',
        bash_command='sudo /sbin/shutdown now'
    )

    shutdown
