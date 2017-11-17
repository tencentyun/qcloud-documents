Hive 基础操作演示了如何在 EMR 集群上创建表以及通过 Hive 查询表。

1. 准备数据

    ```
    #!/bin/bash
    MAXROW=1000000 #指定生成数据行数
    for((i = 0; i < $MAXROW; i++))
    do
    echo $RANDOM, \"$RANDOM\"
    done
    ```

    将以上代码保存为 gen_data.sh 的 bash 脚本文件，并按如下方式执行

    ``` bash
    ./gen_data.sh > hive_test.data
    ```

    数据在 HDFS, 将生成的数据文件放入 HDFS 上，如

    <pre>
    hdfs dfs -put ./hive_test.data /user/hadoop/hive-test/
    </pre>

    将 hive_test.data 放入 HDFS 的 /user/hadoop/hive-test 目录中, 如果想把数据放在 COS 中，则需要按如下操作：在 COS 上创建一个 bucket，如：hivecos，并在 hivecos 中创建文件夹，如：hivetest，将数据文件上传到 hivetest 中, COS 的文件全路径为: cosn://hivecos/hivetest/hive_test.data

2. 连接hive

    - 通过 CMD 方式使用

        登录 master 机器, 进入 Hive 目录

        <pre>
        su hadoop
        cd /usr/local/service/hive/bin
        ./hive
        </pre>

    - 通过 beeline 模式连接数据库

        登录 master 机器, 进入 Hive 目录
        
        <pre>
        cd /usr/local/service/hive
        </pre>
        
        在 conf/hive-site.xml 配置文件中, 获得 hive server2 的连接端口
        
        ``` xml
        <property>
          <name>hive.server2.thrift.port</name>
          <value>7001</value>
        </property>
        ```

        在 bin 目录下，执行

        <pre>
        cd bin
        ./beeline -u "jdbc:hive2://10.0.1.125:7001" -n hadoop -p hadoop
        </pre>

3. 执行查询

    无论以 Hive 模式还是 beeline 模式成功连接到 Hive 数据库后，Hive-SQL 的执行语句都是一样的，现在以 Hive 模式执行 Hive-SQL

    1. 创建 Hive 表

        ``` shell
        hive> show databases; #查看数据库
        OK
        default
        Time taken: 0.26 seconds, Fetched: 1 row(s)
        hive> create database test; #创建数据库test
        OK
        Time taken: 0.176 seconds
        hive> create table hive_test (a int, b string)
        hive> ROW FORMAT DELIMITED FIELDS TERMINATED BY ’,’; #创建数据表hive_test, 并指定列分割符为’,’
        OK
        Time taken: 0.204 seconds
        ```

    2. 将数据导入表中

        数据文件在 HDFS 上的路径为: "/user/hadoop/hive-test/hive_test.data"

        ``` shell
        hive> load data inpath "/user/hadoop/hive-test/hive_test.data" into table hive_test;
        ```

        导入完成后，HDFS 上导入路径上的源数据文件将会被删除, 从 COS 导入数据文件在 COS 上的路径为: cosn://hivecos/hivetest/hive_test.data

        ``` shell
        hive> load data inpath "cosn://hivecos/hivetest/hive_test.data" into table hive_test;
        ```

        导入完成后，COS 上的源数据将会被删除, 从本地导入本地数据文件路径在: /usr/local/service/hadoop/bin/hive_test.data

        ``` shell
        hive>load data local inpath "/usr/local/service/hadoop/bin/hive_test.data"
        into table hive_test;
        ```

    3. 执行查询

        <pre>
        hive> select count(*) from hive_test;
        Query ID = hadoop_20170316142922_967b5f0e-1f89-4464-bfa3-b6ed53273fc2
        Total jobs = 1
        Launching Job 1 out of 1
        Number of reduce tasks determined at compile time: 1
        In order to change the average load for a reducer (in bytes):
        set hive.exec.reducers.bytes.per.reducer=<number>
        In order to limit the maximum number of reducers:
        set hive.exec.reducers.max=<number>
        In order to set a constant number of reducers:
        set mapreduce.job.reduces=<number>
        Starting Job = job_1489458311206_9869, Tracking URL =
        http://10.0.1.125:5004/proxy/application_1489458311206_9869/
        Kill Command = /usr/local/service/hadoop/bin/hadoop job -kill job_1489458311206_9869
        Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
        2017-03-16 14:29:29,023 Stage-1 map = 0%, reduce = 0%
        2017-03-16 14:29:34,208 Stage-1 map = 100%, reduce = 0%, Cumulative CPU 3.87 sec
        2017-03-16 14:29:40,404 Stage-1 map = 100%, reduce = 100%, Cumulative CPU 5.79 sec
        MapReduce Total cumulative CPU time: 5 seconds 790 msec
        Ended Job = job_1489458311206_9869
        MapReduce Jobs Launched:
        Stage-Stage-1: Map: 1 Reduce: 1 Cumulative CPU: 5.79 sec
        HDFS Read: 40974623 HDFS Write: 107 SUCCESS
        Total MapReduce CPU Time Spent: 5 seconds 790 msec
        OK
        3000000
        Time taken: 18.504 seconds, Fetched: 1 row(s)
        hive> select * from hive_test limit 10;
        OK
        29808 "106"
        24213 "12734"
        18518 "2486"
        18460 "10955"
        31106 "28804"
        6036 "4673"
        31402 "12064"
        7631 "4887"
        21530 "4647"
        17869 "13358"
        32
        </pre>
