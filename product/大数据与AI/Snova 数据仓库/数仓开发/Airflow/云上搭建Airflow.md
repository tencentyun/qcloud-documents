[Apache Airflow](https://airflow.apache.org/) 是一款开源的工作流管理系统，集成了编排、调度，监控以及图形化展示等等功能。在数据仓库场景，Airflow则可以应用于ETL任务的管理。
本文主要介绍如何在云端虚拟机上搭建Airflow。

## 步骤

### Airflow默认安装

1. 购买虚拟机
注意：本文以CentOS 8.0为例子
![](https://main.qcloudimg.com/raw/5a57589b7785d168698ee0083edd2897.png)

2. 安装依赖软件
安装Airflow之前，需安装如下依赖
```
yum install redhat-rpm-config -y
yum install mysql-devel -y
yum install python3-devel -y
dnf update gcc annobin -y
```

3. 创建Home目录
```
mkdir -p /usr/local/services/airflow
export AIRFLOW_HOME=/usr/local/services/airflow
```
AIRFLOW_HOME变量可以配置到/etc/profile文件中

4. 安装Airflow
```
pip install apache-airflow[mysql]
```

5. 初始化DB
```
airflow initdb
```

6. 配置安全组
Airflow的webui默认启动在8080端口，如果想要通过外网访问，需要打开安全组的8080
![](https://main.qcloudimg.com/raw/80225b200d7ab0e92dd02f4525f12994.png)

7. 启动webui
使用如下命令
```
airflow webserver -D
```
如果通过url http://{ip}:8080/admin/ 可以正常访问页面，代表配置成功

### 处理时区

Airflow使用UTC时间，与北京时间差8个小时，因此需要进行处理，由于Airflow写死部分代码，因此除了修改配置文件外，也需要修改源码，步骤如下：

1. 修改AIRFLOW_HOME下的airflow.cfg
```
default_timezone = utc
修改为
default_timezone = Asia/Shanghai

default_ui_timezone = UTC
修改为
default_ui_timezone = Asia/Shanghai
```

2. 修改文件 /usr/local/lib/python3.6/site-packages/airflow/utils/timezone.py 
在语句 utc = pendulum.timezone('UTC') 下新增如下语句
```
from airflow.configuration import conf
try:
    tz = conf.get("core", "default_timezone")
    if tz == "system":
        utc = pendulum.local_timezone()
    else:
        utc = pendulum.timezone(tz)
except Exception:
    pass

```

修改函数 utcnow() 如下：
```
d = dt.datetime.utcnow() 
修改为
d = dt.datetime.now()
```

3. 修改文件 /usr/local/lib/python3.6/site-packages/airflow/utils/sqlalchemy.py
在语句 utc = pendulum.timezone('UTC') 下添加如下：
```
from airflow.configuration import conf
try:
    tz = conf.get("core", "default_timezone")
    if tz == "system":
        utc = pendulum.local_timezone()
    else:
        utc = pendulum.timezone(tz)
except Exception:
    pass
```

注释语句 
```
cursor.execute("SET time_zone = '+00:00'")
```

4. 修改文件 /usr/local/lib/python3.6/site-packages/airflow/www/templates/admin/master.html
```
var UTCseconds = (x.getTime() + x.getTimezoneOffset()*60*1000);
修改为
var UTCseconds = x.getTime();

"timeFormat":"H:i:s %UTC%",
修改为
"timeFormat":"H:i:s",
```

5. 重启webserver
```
cat {AIRFLOW_HOME}/airflow-webserver.pid
kill {pid}
airflow webserver -D
```

### 使用云数据库MySQL存储数据

Airflow默认使用嵌入式的Sqlite存储数据，如果要上生产环境，必须满足高可用的要求，这里采用云数据库MySQL作为例子，步骤如下：

1. 购买[云数据库MySQL](https://console.cloud.tencent.com/cdb)
注：必须是 高可用版或者金融版，基础版由于不支持explicit_defaults_for_timestamp参数，因此无法作为Airflow的存储。

2. 修改参数
在控制台修改参数explicit_defaults_for_timestamp为ON，修改后如下：
![](https://main.qcloudimg.com/raw/111bbbe2a4d0bd04e7986735ae2959a0.png)

3. 创建DB及用户
登录MySQL，运行如下语句，其中用户名及密码可根据用户情况进行修改
```
create database airflow;
create user 'airflowuser'@'%' identified by 'pwd123';
grant all on airflow.* to 'airflowuser'@'%';
flush privileges;
```

4. 修改 {AIRFLOW_HOME}/airflow.cfg 中配置
```
sql_alchemy_conn = sqlite:////usr/local/services/airflow/airflow.db
修改为
sql_alchemy_conn = mysql://airflowuser:pwd123@{ip}/airflow
```

5. 重新初始化数据库
```
airflow initdb
```

如果想保留之前的运行数据，可运行
```
airflow resetdb
```
