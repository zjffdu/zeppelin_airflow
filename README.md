# Introduction

This repository is to show you how to integrate Zeppelin with Airflow. 
The philosophy behind the ingtegration is to make the transition from development stage to production stage as smooth as possible.  
Zeppelin is good at data pipeline development (Spark, Flink, Hive, Python, Shell and etc), while Airflow is the de-facto standard of Job orchestration.

# How to run it

## Step 1. Initialize enviromenment. 

Run this following commands to initialize environment.

* Download spark which is used by Zeppelin
* Download zeppelin airflow plugins 

```
git clone https://github.com/zjffdu/zeppelin_airflow.git
cd zeppelin_airflow
./init.sh
```

### Step 2  Start Zeppelin + Airflow via docker-compose

```
docker-compose -f docker-compose-LocalExecutor.yml up -d
```


### Step 3. Use Zeppelin + Airflow

Open http://localhost:8085 for Zeppelin http://localhost:8083 for Airflow

There's one dag `zeppelin_example` in Airflow. This dag just run 3 Zeppelin notes:
* Python Tutorial/01. IPython Basics
* Spark Tutorial/02. Spark Basics Features
* Spark Tutorial/03. Spark SQL (PySpark)

![image](https://user-images.githubusercontent.com/164491/137468051-56b3f50c-f04d-463b-9768-9cc88f7fe4b2.png)

You can enable it, then Airflow would run these Zeppelin notes.

Actually Zeppelin would not run these notes directly, instead it would clone note and run the cloned note. 

![image](https://user-images.githubusercontent.com/164491/137468357-75f4264d-58b8-43a7-a24a-fbf647b8c5bc.png)


# More features would come soon, stay tuned.

