Apache Airflow 是一个工作流管理平台，可以用于管理调度和执行。如您已经部署/拥有 Airflow，可以将其连接到 DLC，管理和调度 DLC 上的作业。

Apache Airflow 的使用您可以参考 [Airflow 官方文档](https://airflow.apache.org/docs/)。Airflow 连接到 DLC 有两种方案，下文将展开描述这两种方案。

## 方案一：在 Airflow 任务中创建 jdbc 连接
### 准备工作
1. Airflow 各组件安装 jaydebeapi 依赖包。
```python
pip install jaydebeapi
```
2. Airflow 各组件安装 java 环境。
3. 准备好 [dlc-jdbc jar 包](https://dlc-jdbc-1304028854.cos.ap-beijing.myqcloud.com/dlc-jdbc-2.2.3-jar-with-dependencies.jar)。

### 创建任务
```python
from datetime import datetime, timedelta

from airflow import DAG
from airflow.utils import dates
from airflow.operators.python_operator import PythonOperator
import jaydebeapi


def default_options():
    default_args = {
        'owner': 'airflow',  # 拥有者名称
        'start_date': dates.days_ago(1),  # 第一次开始执行的时间，为 UTC 时间
        'retries': 1,  # 失败重试次数
        'retry_delay': timedelta(seconds=5)  # 失败重试间隔
    }
    return default_args

# 定义DAG
def execute_sql(sql):
    jdbc_url = "jdbc:dlc:dlc.tencentcloudapi.com?task_type=SQLTask&datasource_connection_name=DataLakeCatalog&region=ap-guangzhou&data_engine_name=public-engine"
    user = "secretid"
    pwd = "secretkey"
    driver = "com.tencent.cloud.dlc.jdbc.DlcDriver"
    jar_file = '/opt/airflow/plugins/dlc-jdbc-2.2.3-jar-with-dependencies.jar'
    conn = jaydebeapi.connect(driver, jdbc_url, [user, pwd], jar_file)
    curs = conn.cursor()
    curs.execute(sql)
    rows = curs.rowcount.real
    if rows != 0:
        result = curs.fetchall()
        print(result)
    print("finish")
    curs.close()
    conn.close()
    
def create_table(dag):
    # PythonOperator
    sql = "create table if not exists hz_test.airflow_table(id int)"
    task = PythonOperator(
        task_id='create_table',
        python_callable=execute_sql,  # 指定要执行的函数
        op_kwargs={
            'sql': sql,
        },
        dag=dag)
    return task

def insert_data(dag):
    # PythonOperator
    sql = "insert into hz_test.airflow_table select 1 as id"
    task = PythonOperator(
        task_id='insert_data',
        python_callable=execute_sql,  # 指定要执行的函数
        op_kwargs={
            'sql': sql,
        },
        dag=dag)
    return task

def select_data(dag):
    # PythonOperator
    sql = "select * from hz_test.airflow_table"
    task = PythonOperator(
        task_id='select_data',
        python_callable=execute_sql,  # 指定要执行的函数
        op_kwargs={
            'sql': sql,
        },
        dag=dag)
    return task

with DAG(
        'dlc_test',  # dag_id
        default_args=default_options(),  # 指定默认参数
        schedule_interval="0 * * * *"  # 执行周期
) as d:
    task1 = create_table(d)
    task2 = insert_data(d)
    task3 = select_data(d)
    task1 >> task2 >> task3
    #chain(task1, task2, task3)  # 指定执行顺序
```

### 执行效果
![](https://qcloudimg.tencent-cloud.cn/raw/b777e21a8bd5390c1d32ca9f574c8ea6.png)

## 方案二：将dlc-jdbc作为Airflow connector

### 准备工作
1. Airflow 各组件安装 jaydebeapi 依赖包。
```python
pip install jaydebeapi
```
2. Airflow 各组件安装 java 环境。
3. 准备好 [dlc-jdbc jar 包](https://dlc-jdbc-1304028854.cos.ap-beijing.myqcloud.com/dlc-jdbc-2.2.3-jar-with-dependencies.jar)。
4. Airflow 各组件安装 jdbc module。
```python
pip install apache-airflow-providers-jdbc
```

### 添加 Connector
Airflow 页面上没有 JDBC 的 Conn Type 可选，需要使用命令行添加 Connection。
```shell
airflow connections add --conn-type jdbc \
--conn-host 'jdbc:dlc:dlc.tencentcloudapi.com?task_type=SQLTask&datasource_connection_name=DataLakeCatalog&Region=ap-guangzhou&data_engine_name=public-engine' \
--conn-extra '{"extra__jdbc__drv_path" : "/opt/airflow/plugins/dlc-jdbc-2.2.3-jar-with-dependencies.jar", "extra__jdbc__drv_clsname": "com.tencent.cloud.dlc.jdbc.DlcDriver"}' \
--conn-login 'secretId' \
--conn-password 'secretKey'  dlc-jdbc
```
执行完成后可以在页面上看到新添加的 Connection。
![](https://qcloudimg.tencent-cloud.cn/raw/70dc4777ed98baf1265ca334cd0040d0.png)

### 创建任务
```python
from __future__ import annotations

import os
from datetime import datetime, timedelta

from airflow import DAG

try:
    from airflow.operators.empty import EmptyOperator
except ModuleNotFoundError:
    from airflow.operators.dummy import DummyOperator as EmptyOperator  # type: ignore

from airflow.providers.jdbc.operators.jdbc import JdbcOperator

with DAG(
    dag_id='dlc_connector',
    schedule='0 0 * * *',
    start_date=datetime(2021, 1, 1),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example'],
    catchup=False,
) as dag:

    # [START howto_operator_jdbc_template]
    select_data1 = JdbcOperator(
        task_id='select1',
        sql='select 1',
        jdbc_conn_id='dlc-jdbc',
        autocommit=True,
    )
    # [END howto_operator_jdbc_template]

    # [START howto_operator_jdbc]
    select_data2 = JdbcOperator(
        task_id='select2',
        sql='select 2',
        jdbc_conn_id='dlc-jdbc',
        autocommit=True,
    )
    # [END howto_operator_jdbc]

    select_data1 >> select_data2
```

### 执行效果
![](https://qcloudimg.tencent-cloud.cn/raw/721b436c84d261c07b2309a482ef359a.png)
