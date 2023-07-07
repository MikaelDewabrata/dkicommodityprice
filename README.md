# DKI Jakarta Traditional Market Commodity Dashboard

## Overview
This repository aims to explain the process of getting data from [Info Pangan Jakarta](https://infopangan.jakarta.go.id/). While Info Pangan DKI Jakarta website has great data related to commodity prices, how the data is presented is actually the problem. This project objective is to recreate the data pipeline, make it more seamless and also visualize it in a better way. 

## Airflow DAG
Currently, we are using a very simple DAG process to get the data daily at 1 PM WIB. Hopefully, this can be improved to have an error message, cleaning process, and also database checking to avoid duplication.

![image](https://github.com/monsterikan/dkicommodityprice/assets/57279779/70945290-5d5a-499f-b46b-95a2f7fcb388)

## Data Pipeline
The overall system design is as follows. 

![DE-Project-Pangan](https://github.com/monsterikan/dkicommodityprice/assets/57279779/2205f975-fcd1-4128-9c8a-ce97b8c386e3)

## Quickstart
<details>
  <summary>Show / Hide</summary>
  
  This is a shorter guide for starting Airflow in Docker. For a more detailed version, check here [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
</details>
