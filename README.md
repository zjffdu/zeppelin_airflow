

# Slide

[Airflow & Zeppelin: Better Together](https://docs.google.com/presentation/d/1QDa_E_HmQbNeRFC-1PUUQHqWLpjtXRiReNtqEGkNALY/edit?usp=sharing)

# Introduction

This repository is to show you how to integrate Zeppelin with Airflow 2. 
The philosophy behind the ingtegration is to make the transition from development stage to production stage as smooth as possible.  
Zeppelin is good at data pipeline development (Spark, Flink, Hive, Python, Shell and etc), while Airflow is the de-facto standard of Job orchestration.

# How to run it

## Step 1. Initialize enviromenment. 

Run this following commands to initialize environment.

* Download spark which is used by Zeppelin 

```
git clone https://github.com/zjffdu/zeppelin_airflow.git
cd zeppelin_airflow
./init.sh
```

## Step 2  Start Zeppelin + Airflow via docker-compose

```
docker-compose up -d
```


## Step 3. Use Zeppelin + Airflow

Open http://localhost:8085 for Zeppelin and http://localhost:8080 for Airflow

### Add connection in Airflow

First, you need to add Zeppelin connection in Airflow, so that `ZeppelinOperator` can call rest api of Zeppelin to run notebook.
Here's one screenshot. Host is the Zeppelin server host name (here is the Zeppelin docker container name), port is the Zeppelin server rest api port.
![image](https://user-images.githubusercontent.com/164491/170644482-4dda682b-33dd-4626-9501-e7440f6a412c.png)



### Run example dag

There's one dag `zeppelin_example_dag` in Airflow. This dag just run 3 Zeppelin notes:
* Python Tutorial/01. IPython Basics
* Spark Tutorial/02. Spark Basics Features
* Spark Tutorial/03. Spark SQL (PySpark)

![image](https://user-images.githubusercontent.com/164491/137468051-56b3f50c-f04d-463b-9768-9cc88f7fe4b2.png)

You can enable it, then Airflow would run these Zeppelin notes.



# More features would come soon, stay tuned.

