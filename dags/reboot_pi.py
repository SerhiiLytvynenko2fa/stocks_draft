from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 0,
}

with DAG(
    dag_id='reboot_pi',
    default_args=default_args,
    description='Reboot Raspberry Pi from Airflow',
    schedule_interval=None,  # Або cron: '0 3 * * *' для щоденного о 3:00
    catchup=False,
    tags=['raspberry', 'system'],
) as dag:

    reboot = BashOperator(
        task_id='reboot_pi_task',
        bash_command='sudo /sbin/reboot'
    )

    reboot
