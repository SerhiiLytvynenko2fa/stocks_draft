from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 6, 30),
}

@dag(
    default_args=default_args,
    description='Reboot Raspberry Pi',
    schedule_interval=None,
    catchup=False,
    tags=['raspberry', 'system']
)
def reboot_pi():
    reboot_pi = BashOperator(
        task_id="reboot_pi",

        # !!! important !!!
        # Don't delete sleep from bash_command. Without sleep it will be butting all
        # the time after creation of the container, because the task will not be completed after immediate reboot
        bash_command="""
            ssh -i /opt/airflow/.ssh/id_rsa -o StrictHostKeyChecking=no serhiilytvynenko@192.168.0.112 "nohup sudo bash -c 'sleep 10; reboot' >/dev/null 2>&1 &"
            exit 0
        """,
        retries=0
    )

    reboot_pi
reboot_pi()