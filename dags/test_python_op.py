from airflow import DAG
from airflow.operators.python_operator import PythonOperator
# from src.zeroin_batch.handle_holiday_zeroin_task import hello_world
import os
import datetime
import pprint



dag = DAG(
    dag_id="test_python_op",
    schedule_interval="@daily",
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": datetime.timedelta(seconds=5),
        "start_date": datetime.datetime.now()
    }
)


def print_context(**kwargs):
    """Print the Airflow context and ds variable from the context."""
    print("kwargs")
    return 'Whatever you return gets printed in the logs'




test_log = PythonOperator(
    task_id='test_log',
    # python_callable=lambda: logger.info("this works"),
    python_callable=print_context,
    dag=dag
)



