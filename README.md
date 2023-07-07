# DKI Jakarta Traditional Market Commodity Dashboard

## Overview
This repository aims to explain the process of getting data from [Info Pangan Jakarta](https://infopangan.jakarta.go.id/). While Info Pangan DKI Jakarta website has great data to show commodity prices and its fluctuation, how the data is presented is actually the problem. This project objective is to recreate the data pipeline, make it more seamless, and also visualize it in a better way.

## Data Source
DKI Jakarta has an information portal about food prices in Jakarta covering several traditional markets. While the data is there, it is not presented well. This project is to ‘remake’ the local government data presentation to be more clear and reachable. Using this project, I am trying to recreate the data pipeline and present it with a more proper data visualization.

![dashboard](https://github.com/monsterikan/dkicommodityprice/assets/57279779/2f9edb17-c5a7-4c7a-9ec0-10125bf77538)

As we can see above, the presentation of the data is not user-friendly, and quite hard to read.

## Getting The Data
Using Python, this project tries to gather the data from the source in an ethical way. Using Python, the data is compiled and organized in a proper manner, based on the available traditional market in DKI Jakarta. After the data is proper, the script then stores it in MySQL database. All this process runs on a Virtual Machine environment in Virtual Private Server.

## Airflow DAG
Currently, we are using a very simple DAG process to get the data daily at 2 PM WIB. Hopefully, this can be improved to have an error message, a cleaning process, and also database checking to avoid duplication.

![image](https://github.com/monsterikan/dkicommodityprice/assets/57279779/70945290-5d5a-499f-b46b-95a2f7fcb388)

## Data Pipeline
The overall system design is as follows. 

![DE-Project-Pangan](https://github.com/monsterikan/dkicommodityprice/assets/57279779/2205f975-fcd1-4128-9c8a-ce97b8c386e3)

## Quickstart
<details>
  <summary>Show / Hide</summary>
  
  This is a shorter guide for starting Airflow in Docker. For a more detailed version, check here [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
</details>
