本文主要介绍 Hue 的实践用法。
## Hive SQL 查询
Hue 的 beeswax App 提供了友好方便的 Hive 查询功能，可以选择不同的 Hive 数据库、编写 HQL 语句、提交查询任务、查看结果。
1. 在 Hue 控制台上方，选择 Query > Editor > Hive。
 ![](https://qcloudimg.tencent-cloud.cn/raw/48a2fbc6dacc28ea8e0f8e7d6e321d47.png)
2. 在语句输入框中输入要执行语句，然后单击**执行**，执行语句。
 ![](https://qcloudimg.tencent-cloud.cn/raw/13b69af2be822dd1364efbf2b65ce5b8.png)

## Hbase 数据查询和修改、数据展示
使用 Hbase Browser 可以查询、修改、展示 Hbase 集群中表的数据。
 ![](https://qcloudimg.tencent-cloud.cn/raw/c3a1a697b9dc33f6c017030ecc2ea23e.png)

## 访问 HDFS 和文件浏览
通过 Hue 的 Web 页面可方便查看 HDFS 中的文件和文件夹，并对其进行创建、下载、上传、复制、修改和删除等操作。
1. 在 Hue 控制台左侧，选择 Browsers > Files 进入 HDFS 文件浏览。
![](https://qcloudimg.tencent-cloud.cn/raw/03bf74cd204d23845a1d2bf738a7240e.png)
2.	在 Hue 控制台左侧，选择 Browsers > Files 进入 HDFS 文件浏览。
 ![](https://qcloudimg.tencent-cloud.cn/raw/6b94b5141206e8551974d0fde875bc6d.png)
 
## Oozie 任务的开发
1. 准备工作流数：Hue 的任务调度基于工作流，先创建一个包含 Hive script 脚本的工作流，Hive script 脚本的内容如下：
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
将以上内容保存为 hive_sample.sql 文件。Hive 工作流还需要一个 hive-site.xml 配置文件，此配置文件可以在集群中安装了 Hive 组件的节点上找到。具体路径：/usr/local/service/hive/conf/hive-site.xml，复制一个 hive-site.xml 文件。然后上传 Hive script 文件和 hive-site.xml 到 hdfs 的目录，例如：/user/hadoop。

2. 创建工作流。
	1. 切换到 hadoop 用户，在 Hue 页面上方，选择 Query > Scheduler > Workflow。
![](https://qcloudimg.tencent-cloud.cn/raw/b1b9b6361124538cb755efb3fc1d90b3.png)
	2. 在工作流编辑页面中拖一个 Hive Script。
>! 本文以安装 Hive 版本为 Hive1 为例，配置参数为 HiveServer1。与其他 Hive 版本混合部署时（即配置其他版本的配置参数时），会报错。
>
![](https://qcloudimg.tencent-cloud.cn/raw/27cbec2a4f30fc937f34a5d086b496b4.png)
	3. 选择刚上传的 Hive scipt 文件和 hive-site.xml 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/251b3efbd9bb7057945cfc1ac0f1aab7.png)
	4. 单击 **Add** 后，还需在 FILES 中指定 hive script 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/38e9a81097f76194047f0d302d39ab2a.png)
	5. 单击右上角**保存**，然后单击**执行**，运行 workflow。
![](https://qcloudimg.tencent-cloud.cn/raw/b0693bd5c83a26f5fa5c89539768087a.png)

3. 创建定时调度任务。
Hue 的定时调度任务是 schedule，类似于 Linux 的 crontab，支持的调度粒度可以到分钟级别。
	1. 选择 Query > Scheduler > Schedule，创建 Schedule。
![](https://qcloudimg.tencent-cloud.cn/raw/c45fd5b062e78750aab55b7ba466975b.png)
	2. 单击 **Choose a workflow**，选择一个创建好的工作流。
![](https://qcloudimg.tencent-cloud.cn/raw/5d20d799a91dbc105e4eadd9d2365bf7.png)
	3. 选择需要调度的时间点和时间间隔、时区、调度任务的开始时间和结束时间，然后单击 **Save** 保存。
![](https://qcloudimg.tencent-cloud.cn/raw/d32c3dbb0d2d41cf85387849825be565.png)

4. 创建定时调度任务。
	1. 单击右上角的**提交**，提交调度任务。
![](https://qcloudimg.tencent-cloud.cn/raw/be86060e81eac2fe1842c58e9bf57dd3.png)
	2. 在 schedulers 的监控页面可以查看任务调度情况。
![](https://qcloudimg.tencent-cloud.cn/raw/58d020d6f9bbef8ce1ac5fba59eb8fb5.png)

## Notebook 查询对比分析
notebook 可以快速的构建间的查询，将查询结果放到一起做对比分析，支持5种类型：hive，impala，spark，java，shell。
1. 依次单击 **Editor**，**Notebook**，单击"+" 号添加需要的查询。
![](https://qcloudimg.tencent-cloud.cn/raw/09d6b44c6517d1a3204f6fdb517e075f.png)
2. 依次单击**保存**可保存添加的notebook，单击**执行**可以执行整个 notebook。
![](https://qcloudimg.tencent-cloud.cn/raw/d6eaf0e36d46270a1fca867695683a0e.png)

