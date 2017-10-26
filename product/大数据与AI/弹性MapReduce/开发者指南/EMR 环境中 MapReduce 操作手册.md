本文档主要介绍基本的 MR 任务操作（计算、查看任务日志等）、以及 MR 计算任务如何访问腾讯云对象存储上的数据，详细资料可以参考 [Apache Software Foundation](https://hadoop.apache.org/docs/r2.7.3/)。

## 命令行模式提交 MR 任务
本次提交的任务为 wordcount 任务即统计单词个数，提前需要在集群中上传需要统计的文件。
在做相关操作前需要登录到 EMR 集群中的任意一个机器（Master 节点、或者 Core、Task 节点），登录后切换到 Hadoop 用户。
Hadoop 等相关软件路径在 `/usr/local/service/` 下
相关日志路径在 `/data/emr` 下
<span id="jump">
### 1. 数据准备 
</span>
数据准备根据数据的存储位置不同，分为两种方式：
* 数据存放在 HDFS 集群
* 数据存放在 COS

下面会详细介绍这两种数据准备的方式。
**数据存放在 HDFS**
首先准备要统计的文本文件，然后通过如下命令拷贝到 HDFS 集群：
```
bin/hadoop fs -put README.txt /user/hadoop/
[hadoop@10 hadoop]$ bin/hadoop fs -ls /user/hadoop/README.txt
-rw-r--r-- 3 hadoop supergroup 1366 2017-03-15 19:00 /user/hadoop/README.txt
```
**数据存放在 COS**
数据存放在 COS 的可通过两种方式进行数据准备：通过 COS 控制台上传数据或通过 Hadoop 命令上传数据。具体方法如下：
已经存储在 COS 的数据文件可通过如下命令查看：
```
[hadoop@10 hadoop]$ bin/hadoop fs -ls cosn://emrtest/README.txt
-rw-rw-rw- 1 hadoop hadoop 1366 2017-03-15 19:09 cosn://emrtest/README.txt
```
通过 Hadoop 的命令上传 COS：
```
bin/hadoop fs -put README.txt cosn://emrtest/
[hadoop@10 hadoop]$ bin/hadoop fs -ls cosn://emrtest/README.txt
-rw-rw-rw- 1 hadoop hadoop 1366 2017-03-15 19:09 cosn://emrtest/README.txt
```

### 2. 提交 MR 计算任务
通过如下命令提交任务:
```
bin/yarn jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar
wordcount /user/hadoop/README.txt /user/hadoop/output
```
查看执行结果:
```
bin/hadoop fs -ls /user/hadoop/output
```
基于 COS 的任务提交:
```
bin/yarn jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar
^^Iwordcount cosn://emrtest/README.txt /user/hadoop/output
```
查看任务结果:
```
[hadoop@10 hadoop]$ bin/hadoop fs -ls /user/hadoop/cosoutput
```
### 3. 查看任务日志
查看任务状态
```
bin/mapred job -status jobid
```
查看任务日志 
```
bin/mapred job -logs jobid
```
## 基于 HUE 的 MR 任务操作
### 1. 数据准备
数据准备同通过命令行准备数据一致，请参考 [通过命令行准备数据](#jump)。
### 2. 登录 HUE 进行操作
通过 EMR 控制的快捷入口可以找到 HUE 的登录页面，找到如下入口。
![](//mc.qcloudimg.com/static/img/240c3ebccb81246dddf53aa5c6dde4b3/image.png)
进入页面后单击【Create】按钮，在弹出的对话框中拖拽 Java program。
![](//mc.qcloudimg.com/static/img/f7a68bfc035bc041a0dceefe22a7e763/image.png)
>**注意：**
>箭头处的 jar 文件需要提前放到 HDFS 以供选择。

单击【Add】后给任务添加参数，如下图。
![](//mc.qcloudimg.com/static/img/b6e0cbecde6e8813dafc19d99121e97a/image.png)
>**注意：**
>箭头处如果是 COS 上的文件，直接填写 COS 上的路径即可。
>例如：`cosn://emrtest/README.txt`

设置好参数后单击左上角【保存】后单击【提交】，任务进入提交，如下图。
![](//mc.qcloudimg.com/static/img/ec15e90323f5f7e552b8e251770934a1/image.png)
单击上图箭头处图标可查看任务日志, 如下图。
![](//mc.qcloudimg.com/static/img/9739e38a9b7ba5e328d371463cc032a7/image.png)
### 3. 在 HUE 中调度 MR 任务
通过【Workflows】>【Editors】>【Coordinatiors】进入任务调度创建页面。
![](//mc.qcloudimg.com/static/img/6b7b35b1f356ba677d798db774227ed1/image.png)
进入创建页面后单击【Create】按钮，进入下图。
![](//mc.qcloudimg.com/static/img/1e29bd049015dafbc9c3ddfa6606780e/image.png)
选定好流程后，设置调度时间，如下图。
![](//mc.qcloudimg.com/static/img/9950c76deba69b21e9c8f61b49d8c1c7/image.png)
【hour】可以选择小时里某些分钟
【day】可以选择某天的小时和分钟
【week】可以选择周一到周日的小时和分钟
【month】可以选择当前月下的天、小时、分钟
【year】选择当前年下的月、日、小时、分钟
选择好调度时间后单击提交即可，可以通过【Workflows】>【Editors】>【Coordinatiors】查看已经存在的调度任务。
![](//mc.qcloudimg.com/static/img/c45ff0b7f6b7d674eb53a88264c367d7/image.png)
下图为已经存在的任务列表。
![](//mc.qcloudimg.com/static/img/0a650ab00663087053918f113eaeff47/image.png)
