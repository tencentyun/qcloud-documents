## Hue 简介
Hue 是一个开源的 Apache Hadoop UI 系统，由 Cloudera Desktop 演化而来，最后 Cloudera 公司将其贡献给 Apache 基金会的 Hadoop 社区，它是基于 Python Web 框架 Django 实现的。

通过使用 Hue 我们可以在浏览器端的 Web 控制台上与 Hadoop 集群进行交互来分析处理数据，例如操作 HDFS 上的数据、运行 MapReduce Job、执行 Hive 的 SQL 语句和浏览 HBase 数据库等。

## Hue 功能
- Hive SQL 查询
- Hbase 数据查询和修改、数据展示
- 访问 HDFS 和文件浏览
- Oozie 任务的开发、监控和工作流协调调度

## 登录 Hue 控制台
使用 Hue 组件管理工作流时，请先登录 Hue 控制台页面，具体步骤如下：
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，单击对应集群 **ID/名称**，进入集群详情页面，然后单击**集群服务**。
2. 在列表页找到 Hue 组件，单击 **WebUI 访问地址**进入 Hue 页面。
3. 首次登录 Hue 控制台页面，请使用 root 帐号，密码为创建集群时提供的密码。
![](https://main.qcloudimg.com/raw/ae62e428871fd46c2ce6509fd31cde63.png)
>!由于 EMR 产品的组件启动帐号为 hadoop。请在首次以 root 帐号登录 Hue 控制台后，新建 hadoop 帐号。后续所有作业需通过 hadoop 帐号来提交。

## Hive SQL 查询
Hue 的 beeswax app 提供了友好方便的 Hive 查询功能，可以选择不同的 Hive 数据库、编写 HQL 语句、提交查询任务、查看结果。 
1. 在 Hue 控制台上方，选择 **Query > Editor > Hive**。
![](https://main.qcloudimg.com/raw/bfcd6944a8a8dd70065218885b55f82d.png)
2. 在语句输入框中输入要执行语句，然后单击**执行**，执行语句。
![](https://main.qcloudimg.com/raw/202878b0b90b42da7317b026e9f2f603.png)

## Hbase 数据查询
使用 Hbase Browser 可以查询、修改、展示 Hbase 集群中表的数据。
![](https://main.qcloudimg.com/raw/705ade35d5fe86c27be6aff46235dc02.png)

## HDFS 文件浏览
通过 Hue 的 Web 页面可方便查看 HDFS 中的文件和文件夹，并对其进行创建、下载、上传、复制、修改和删除等操作。
1. 在 Hue 控制台左侧，选择 **Browsers > Files** 进入 HDFS 文件浏览。
![](https://main.qcloudimg.com/raw/b2e05c0c8f05464f0ef1ffe671be1cc3.png)
2. 进入 **File Browser** 后，可执行如下图所示的操作。
![](https://main.qcloudimg.com/raw/0dc7e232a81e8900c06adb277b8eaf93.png)

## Oozie 任务调度
1. **准备工作流数据**
Hue 的任务调度基于工作流，先创建一个包含 Hive script 脚本的工作流，Hive script 脚本的内容如下：
```
 create database if not exists hive_sample; 
 show databases;
 use hive_sample;
 show tables;
 create table if not exists hive_sample (a int, b string);
 show tables;
 insert into hive_sample select 1, "a";
 select * from hive_sample;
```
将以上内容保存为 hive_sample.sql 文件。Hive 工作流还需要一个 hive-site.xml 配置文件，此配置文件可以在集群中安装了 Hive 组件的节点上找到。具体路径：`/usr/local/service/hive/conf/hive-site.xml`，复制一个 hive-site.xml 文件。然后上传 Hive script 文件和 hive-site.xml 到 hdfs 的目录，例如 `/user/hadoop`。
2. **创建工作流**
 - 切换到 hadoop 用户，在 Hue 页面上方，选择 **Query > Scheduler > Workflow**。
![](https://main.qcloudimg.com/raw/17e2c9e91bef6c67d7f6721eeb1a490e.png)
 - 在工作流编辑页面中拖一个 Hive Script。
>!本文以安装 Hive 版本为 Hive1 为例，配置参数为 HiveServer1。与其他 Hive 版本混合部署时（即配置其他版本的配置参数时），会报错。
>
![](https://main.qcloudimg.com/raw/128170644bbef8f40743ea0f72a35a0e.png)
 - 选择刚上传的 Hive scipt 文件和 hive-site.xml 文件。
![](https://main.qcloudimg.com/raw/8dad805cde5964d0c218ca780d7b2887.png)
 - 单击 **Add** 后，还需在 FILES 中指定 hive script 文件。
![](https://main.qcloudimg.com/raw/f36e5b22f40b2832f018d0091c8a382c.png)
 - 单击右上角**保存**，然后单击**执行**，运行 workflow。
![](https://main.qcloudimg.com/raw/e3b162114a194dfb01fa30c68fae9387.png)
3. **创建定时调度任务**
Hue 的定时调度任务是 schedule，类似于 Linux 的 crontab，支持的调度粒度可以到分钟级别。
 - 选择 **Query > Scheduler > Schedule**，创建 Schedule。
![](https://main.qcloudimg.com/raw/d0bde8f4b97341f43aaa9ca8ab9b2440.png)
 - 单击 **Choose a workflow...**，选择一个创建好的工作流。
![](https://main.qcloudimg.com/raw/983797b47cf9a6d21af5ed1323251f95.png)
 - 选择需要调度的时间点和时间间隔、时区、调度任务的开始时间和结束时间，然后单击 **Save** 保存。
![](https://main.qcloudimg.com/raw/adda8963a6fd508e44146a48ba1d41a6.png)
4. **执行定时调度任务**
 - 单击右上角的**提交**，提交调度任务。
![](https://main.qcloudimg.com/raw/d42cc1d0d4e2cbe3bdfa77065e5bd8c1.png)
 - 在 schedulers 的监控页面可以查看任务调度情况。
![](https://main.qcloudimg.com/raw/03eca980d7e0cf72b81af89da25f09f2.png)
