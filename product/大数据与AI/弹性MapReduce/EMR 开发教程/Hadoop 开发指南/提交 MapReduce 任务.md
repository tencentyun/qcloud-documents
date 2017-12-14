本操作手册只描述了命令行模式下基本的 MR 任务操作以及 MR 计算任务如何访问腾讯云对象存储上的数据, 详细资料可以参考 [社区资料](https://hadoop.apache.org/docs/r2.7.3/)

- 本次提交的任务为 wordcount 任务即统计单词个数，提前需要在集群中上传需要统计的文件
- 在做相关操作前需要登录到 EMR 集群中的任意一个机器（master 节点、或者 core、task 节点）
- 登录机器后切换到 Hadoop 用户
- Hadoop 等相关软件路径在 /usr/local/service/ 下
- 相关日志路径在 /data/emr 下


1. 数据准备  

    数据准备分为两种方式，第一种方式是在 HDFS 集群，第二种方式是数据存储在 COS, 下面会详细介绍这两种数据准备的方式。  

    - 数据存放在 HDFS 

        首先准备要统计的文本文件，然后通过如下命令拷贝到 HDFS 集群
        
        ``` shell
        bin/hadoop fs -put README.txt /user/hadoop/
        [hadoop@10 hadoop]$ bin/hadoop fs -ls /user/hadoop/README.txt
        -rw-r--r-- 3 hadoop supergroup 1366 2017-03-15 19:00 /user/hadoop/README.txt
        ```

    - 数据存放在 COS  

        数据存放 COS 有两种方式，方式一是通过 COS 的控制台上传, 如果数据文件已经在 COS 可以通过如下命令查看：
        ``` shell
        [hadoop@10 hadoop]$ bin/hadoop fs -ls cosn://emrtest/README.txt
        -rw-rw-rw- 1 hadoop hadoop 1366 2017-03-15 19:09 cosn://emrtest/README.txt
        ```  
        方式二是通过 Hadoop 的命令上传 COS：
        ``` shell
        bin/hadoop fs -put README.txt cosn://emrtest/
        [hadoop@10 hadoop]$ bin/hadoop fs -ls cosn://emrtest/README.txt
        -rw-rw-rw- 1 hadoop hadoop 1366 2017-03-15 19:09 cosn://emrtest/README.txt
        ```

2. 提交 MR 计算任务  

    通过如下命令提交任务：

    ``` shell
    bin/yarn jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar
    wordcount /user/hadoop/README.txt /user/hadoop/output
    #查看执行结果
    hadoop@10 hadoop]$ bin/hadoop fs -ls /user/hadoop/output
    Found 2 items
    -rw-r--r-- 3 hadoop supergroup 0 2017-03-15 19:52 /user/hadoop/output/_SUCCESS
    -rw-r--r-- 3 hadoop supergroup 1306 2017-03-15 19:52 /user/hadoop/output/part-r-00000
    #基于 COS 的任务提交
    bin/yarn jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar
    wordcount cosn://emrtest/README.txt /user/hadoop/output
    #查看任务结果
    [hadoop@10 hadoop]$ bin/hadoop fs -ls /user/hadoop/cosoutput
    Found 2 items
    -rw-r--r-- 3 hadoop supergroup 0 2017-03-15 19:55 /user/hadoop/cosoutput/_SUCCESS
    -rw-r--r-- 3 hadoop supergroup 1306 2017-03-15 19:55 /user/hadoop/cosoutput/part-r-00000
    ```
    查看任务日志
    ``` shell
    #查看任务状态
    bin/mapred job -status jobid
    #查看任务日志
    yarn logs -applicationId id
    ```

    除此外，您还可以登录 Hue，在 Hue 中提交任务。
