#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:35:46 2023

@author: mikaeld
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from pythonfile.run.get_latest_API import getjson

default_args = {
    'owner': 'mikael',  
    'start_date': datetime(2023, 6, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG(
    'run_market_price',
    default_args=default_args,
    schedule_interval='0 6 * * *',  # Run daily at 2 PM (14:00) WIB
)

with dag:
    get_json = PythonOperator(task_id='getjson',
                              python_callable=getjson
                              )
