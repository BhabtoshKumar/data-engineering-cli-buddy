"""Customer360 ETL Pipeline DAG.

This DAG orchestrates the Customer360 data pipeline that processes customer events
and CRM data to create unified customer analytics.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

# DAG configuration
default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'customer360_etl',
    default_args=default_args,
    description='Customer360 ETL Pipeline for unified customer analytics',
    schedule_interval='0 * * * *',  # Every hour
    catchup=False,
    tags=['customer360', 'etl', 'analytics'],
)

# Task 1: Ingest mobile events
ingest_mobile_events = PythonOperator(
    task_id='ingest_mobile_events',
    python_callable=lambda: print("Ingesting mobile events from Kafka"),
    dag=dag,
)

# Task 2: Ingest web events
ingest_web_events = PythonOperator(
    task_id='ingest_web_events',
    python_callable=lambda: print("Ingesting web events from Kafka"),
    dag=dag,
)

# Task 3: Ingest CRM data
ingest_crm_data = PythonOperator(
    task_id='ingest_crm_data',
    python_callable=lambda: print("Ingesting CRM export data"),
    dag=dag,
)

# Task 4: Clean and standardize events
clean_events = SparkSubmitOperator(
    task_id='clean_events',
    application='/opt/airflow/dags/spark/clean_events.py',
    conf={
        'spark.sql.adaptive.enabled': 'true',
        'spark.sql.adaptive.coalescePartitions.enabled': 'true',
    },
    dag=dag,
)

# Task 5: Clean and standardize customer data
clean_customers = SparkSubmitOperator(
    task_id='clean_customers',
    application='/opt/airflow/dags/spark/clean_customers.py',
    conf={
        'spark.sql.adaptive.enabled': 'true',
        'spark.sql.adaptive.coalescePartitions.enabled': 'true',
    },
    dag=dag,
)

# Task 6: Run dbt models
run_dbt_models = BashOperator(
    task_id='run_dbt_models',
    bash_command='cd /opt/airflow/dbt && dbt run --models dim_customer fct_customer_activity',
    dag=dag,
)

# Task 7: Run data quality tests
run_data_tests = BashOperator(
    task_id='run_data_tests',
    bash_command='cd /opt/airflow/dbt && dbt test --models dim_customer',
    dag=dag,
)

# Task 8: Generate analytics
generate_analytics = PythonOperator(
    task_id='generate_analytics',
    python_callable=lambda: print("Generating customer analytics and KPIs"),
    dag=dag,
)

# Task 9: Update dashboards
update_dashboards = PythonOperator(
    task_id='update_dashboards',
    python_callable=lambda: print("Updating Superset dashboards"),
    dag=dag,
)

# Task 10: Send notifications
send_notifications = PythonOperator(
    task_id='send_notifications',
    python_callable=lambda: print("Sending pipeline completion notifications"),
    dag=dag,
)

# Define task dependencies
[ingest_mobile_events, ingest_web_events, ingest_crm_data] >> clean_events
[ingest_crm_data] >> clean_customers

[clean_events, clean_customers] >> run_dbt_models
run_dbt_models >> run_data_tests
run_data_tests >> generate_analytics
generate_analytics >> update_dashboards
update_dashboards >> send_notifications
