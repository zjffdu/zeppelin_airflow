from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.apache.zeppelin.operators.zeppelin_operator import ZeppelinOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2001, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}


with DAG('zeppelin_example_dag',
         max_active_runs=1,
         schedule_interval='0 0 * * *',
         default_args=default_args) as dag:

    python_task = ZeppelinOperator(
        task_id='python_note',
        conn_id='zeppelin_default',
        note_id='2EYDJKFFY'
    )

    spark_scala_task = ZeppelinOperator(
        task_id='spark_scala_note',
        conn_id='zeppelin_default',
        note_id='2A94M5J1Z'
    )

    pyspark_task = ZeppelinOperator(
        task_id='pyspark_note',
        conn_id='zeppelin_default',
        note_id='2EWM84JXA'
    )

    python_task >> spark_scala_task >> pyspark_task
