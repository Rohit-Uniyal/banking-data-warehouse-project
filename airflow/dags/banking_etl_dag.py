from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="banking_etl_dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["banking", "etl"],
) as dag:

    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="python /opt/python/etl/main.py",
    )

    load_warehouse = BashOperator(
        task_id="load_warehouse",
        bash_command="python /opt/python/etl/warehouse_main.py",
    )

    run_etl >> load_warehouse