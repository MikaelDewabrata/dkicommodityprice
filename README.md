# DKI Jakarta Traditional Market Commodity Dashboard

## Overview
This repository aims to explain the process of getting data from [Info Pangan Jakarta](https://infopangan.jakarta.go.id/). While Info Pangan DKI Jakarta website has great data to show commodity prices and its fluctuation, how the data is presented is actually the problem. This project objective is to recreate the data pipeline, make it more seamless, and also visualize it in a better way.

## Data Source
DKI Jakarta has an information portal about food prices in Jakarta covering several traditional markets. While the data is there, it is not presented well. This project is to ‘remake’ the local government data presentation to be more clear and reachable. Using this project, I am trying to recreate the data pipeline and present it with a more proper data visualization.

![dashboard](https://github.com/monsterikan/dkicommodityprice/assets/57279779/baab90bf-4508-4b77-b9fe-cc72678e88b5)
As we can see above, the presentation of the data is not user-friendly, and quite hard to read.

## Database Structure
The ERD is pretty simple, only consisting of a few columns. The main table has Market ID, Commodity ID, Date, and Price. To see further details on this information, we can expand to other tables consisting of Market Name and Commodity. With this, we can create a quite neat data visualization.

![erd-1](https://github.com/monsterikan/dkicommodityprice/assets/57279779/9803f879-53f5-4b6c-b344-cffec9fc0948)


## Getting The Data
Using Python, this project tries to gather the data from the source in an ethical way. Using Python, the data is compiled and organized in a proper manner, based on the available traditional market in DKI Jakarta. After the data is proper, the script then stores it in MySQL database. All this process runs on a Virtual Machine environment in Virtual Private Server.

## Data Pipeline
The overall system design is as follows. 

![project-flow-1](https://github.com/monsterikan/dkicommodityprice/assets/57279779/66f77c63-6df9-4e72-9afd-ae5976896b66)

## Airflow DAG
Currently, we are using a very simple DAG process to get the data daily at 2 PM WIB. Hopefully, this can be improved to have an error message, a cleaning process, and also database checking to avoid duplication.

![airflow-dag1](https://github.com/monsterikan/dkicommodityprice/assets/57279779/7ae7b112-5181-404a-8e8d-8c5a3f338e9f)

## Dashboard
![dashboardash](https://github.com/monsterikan/dkicommodityprice/assets/57279779/f117dee3-d622-4026-9862-19305d733af7)

[Check the URL here](http://38.47.180.145:8050/)


## Quickstart
<details>
  <summary>Show / Hide</summary>
  
  This is a shorter guide for starting Airflow in Docker. For a more detailed version, check here [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
</details>
