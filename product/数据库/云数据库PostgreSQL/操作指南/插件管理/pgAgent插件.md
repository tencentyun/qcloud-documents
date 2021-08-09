本文介绍如何通过 pgAgent 功能来实现云数据库 PostgreSQL 的自动任务执行。

## 简介
如果业务需要定期清理数据库中的多余数据，定时做物化视图更新，定时 vacuum full，定时执行 DML 等数据库中需要定时做的事情，在 PostgreSQL 中可以通过以下功能来实现：
- Linux 的 crontab 功能
- pgadmin 的 pgAgent 功能

pgAgent 是 pgAdmin 工具中的一个插件，在 pgAdmin III v1.4 版本中引用。主要用于 PostgreSQL 的作业调度代理，能够在复杂的时间表上运行多步批处理 shell 和 SQL 任务。 
需要注意的是，pgAgent 需要一些数据库表和其他对象的支持，因此需要先安装 pgAgen 插件。


## 操作方法
### 配置 pgAgent 
1. [登录 PostgreSQL 实例](https://cloud.tencent.com/document/product/409/40429)，登录完成后，创建您的业务数据库。
2. 在需要开通 pgAgent 功能的 database 中执行以下语句：
```
psql > create extension pgagent;
CREATE EXTENSION
```
3. 配置反馈完成后，您需要通过 pgAgent 工具开启任务调度程序。
[登录 CVM](https://cloud.tencent.com/document/product/213/2936)（建议 CVM 与 PostgreSQL 同一 VPC），根据实际数据库版本选择 pgAgent 版本，本文以11.8版本为例，安装 [下载地址](https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-8.0-x86_64/) 中的 pgagent_11。
4. pgAgent 工具安装完成后，执行以下语句启动任务调度程序：
>?请根据实际安装的 pgAgent 版本来使用命令，如果安装的是10版本，则为pgagent_10。
>
```
pgagent_11 hostaddr=IP地址 dbname=数据库 user=用户名 port=端口 password=密码
```
5. 执行成功后，无任何回显提示，您可以使用以下命令来判断进程是否启动成功：
```
执行此语句，如果存在 pgagent 进程，则表示已经启动成功。
# ps -ef |grep pgagent
root      158553       1  0 Oct30 ?        00:00:15 pgagent_11 hostaddr=IP地址 dbname=数据库 user=用户名 port=端口 password=密码
```

### 通过 pgAdmin 配置 pgAgent Jobs
1. 登录 [PostgreSQL 控制台](https://console.cloud.tencent.com/postgres)，在实例列表单击实例名，进入实例详情页，开启外网地址。
2. 打开 pgAdmin 4，通过外网地址访问您的 PostgreSQL，此时可以在界面中看到 pgAgent Jobs。
![](https://main.qcloudimg.com/raw/9c12d37faee93b1db78c07e5aefaed58.png)
3. 在 pgAdmin 界面，右键选择【pgAgent Jobs】>【Create】>【Create Jobs】，创建定时任务。
4. 在 General 界面，配置基础 Job 信息。
![](https://main.qcloudimg.com/raw/5f6d1e2ac7fd354fb55e78652a5d6c67.png)
5. 进入 Step 界面，配置关于需要定时执行的内容，单击右上角的“+”添加一个 Step，为此 Step 配置一个名字，然后在 Code 子标签中配置需要执行的 SQL 语句等内容。
![](https://main.qcloudimg.com/raw/63e2391908ba7e2be23716659442c97c.png)
6. 进入 Schedules 界面，配置任务执行的调度信息：
 1. 在下方 General 子标签中，主要配置任务生效时间。
![](https://main.qcloudimg.com/raw/b952b05c3d757036cd82f1d7527fa4be.png)
 2. 在下方 Repeat 子标签中，配置 crontab 风格的执行计划。
![](https://main.qcloudimg.com/raw/ff1346df822c218fc0fd9fc6d8ece5f6.png)
 3. 完成时间配置之后，也可以在 Exceptions 子标签中配置不执行任务的时间。
7. 最后单击【Save】保存，此任务将根据配置的内容进行自动执行。
