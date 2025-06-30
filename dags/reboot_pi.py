from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 6, 30),
}

@dag(
    default_args=default_args,
    description='Create file and reboot Raspberry Pi',
    schedule_interval=None,
    catchup=False,
    tags=['raspberry', 'system']
)
def reboot_pi():
    @task
    def write_key():
        key = Variable.get("ssh_private_key")
        with open("/tmp/id_rsa", "w") as f:
            f.write(key)
        import os
        os.chmod("/tmp/id_rsa", 0o600)

    reboot_pi = BashOperator(
        task_id="reboot_pi",
        bash_command="""
            ssh -i /tmp/id_rsa -o StrictHostKeyChecking=no serhiilytvynenko@192.168.0.112 'sudo /sbin/reboot'
        """,
    )

    write_key() >> reboot_pi
reboot_pi()