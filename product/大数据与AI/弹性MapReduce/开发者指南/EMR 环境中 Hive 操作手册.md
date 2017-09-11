## 1.Hive 创建表
### 数据准备
如下代码可以生成指定行数的测试数据。
```
    //!/bin/bash
    MAXROW=1000000 // 指定生成数据行数
    for((i = 0; i < $MAXROW; i++))
    do
    echo $RANDOM, \"$RANDOM\"
    done
```
将以上代码保存为 gen\_data.sh 的 bash 脚本文件，并按如下方式执行:
`./gen\_data.sh > hive\_test.data`
生成 hive_test.data 数据文件。
数据在 HDFS, 将生成的数据文件放入 HDFS 上，如： `hdfs dfs -put ./hive\_test.data /user/hadoop/hive-test/`
将 hive_test.data 放入 HDFS 的 `/user/hadoop/hive-test` 目录中。
* 数据在 COS
在 COS 上创建一个 bucket，如：hivecos，并在 hivecos 中创建文件夹，如：hivetest，将数据文件上传到 hivetest 中，如图所示：
![](//mc.qcloudimg.com/static/img/16acafa53d968e1ec88c6f085e8bd0a3/image.png)
COS 的文件全路径为: `cosn://hivecos/hivetest/hive_test.data`
## 2. Hive 模式连接数据库
```
    su hadoop
    cd /usr/local/service/hive/bin
    ./hive
```
## 3. beeline 模式连接数据库
* 登录 master 机器, 进入 Hive 目录`cd /usr/local/service/hive`
在 conf/hive-site.xml 配置文件中, 获得 hive server2 的连接端口
```
    <property>
      <name>hive.server2.thrift.port</name>
      <value>7001</value>
    </property>
```
* beeline 连接
在 bin 目录下，执行`./beeline -u “jdbc:hive2://$hiveserver:7001”-n $username -p $password`
```
    cd bin
    ./beeline -u "jdbc:hive2://10.0.1.125:7001" -n hadoop -p hadoop

    [root@10 bin]# ./beeline -u "jdbc:hive2://10.0.1.125:7001" -n hadoop -p hadoop
    Connecting to jdbc:hive2://10.0.1.125:7001
    Connected to: Apache Hive (version 2.1.1)
    Driver: Hive JDBC (version 2.1.1)
    17/03/17 14:22:05 [main]: WARN jdbc.HiveConnection: Request to set autoCommit to false; Hive Transaction isolation: TRANSACTION_REPEATABLE\_READ
    Beeline version 2.1.1 by Apache Hive
    0: jdbc:hive2://10.0.1.125:7001> // 出现提示符，连接成功
```
## 4. Hive-SQL 执行
无论以 Hive 模式或 beeline 模式成功连接到 Hive 数据库后，Hive-SQL 的执行语句都是一样的，现在以 Hive 模式执行 Hive-SQL
* 创建 Hive 表
```
    hive> show databases; // 查看数据库
    OK
    default
    Time taken: 0.26 seconds, Fetched: 1 row(s)
    hive> create database test; // 创建数据库test
    OK
    Time taken: 0.176 seconds
    hive> create table hive_test (a int, b string)
    hive> ROW FORMAT DELIMITED FIELDS TERMINATED BY ','; // 创建数据表 hive\_test,并指定列分割符为','
    OK
    Time taken: 0.204 seconds
```
* 将数据导入表中
从 HDFS 导入数据,文件在 hdfs 上的路径为: `/user/hadoop/hive-test/hive_test.data`

```
    hive> load data inpath "/user/hadoop/hive-test/hive\_test.data" into table hive\_test;
```
导入完成后，hdfs 上导入路径上的源数据文件将会被删除。
从 COS 导入数据，文件在 COS 上的路径为: `cosn://hivecos/hivetest/hive_test.data`
```
    hive> load data inpath "cosn://hivecos/hivetest/hive\_test.data" into table hive\_test;
```
导入完成后，COS 上的源数据将会被删除。
从本地导入数据，文件路径在: `/usr/local/service/hadoop/bin/hive_test.data`
```
    hive>load data local inpath "/usr/local/service/hadoop/bin/hive_test.data"
	into table hive_test;
```
* 执行 SQL 查询
查询表记录条数: `select count(*) from hive_test`

```
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
```
* 查看表部分数据:
```
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
```
## 5. 基于 Hue
进入 Hue 的 Hive 编辑模式，并选择对应的数据库
![](//mc.qcloudimg.com/static/img/4041add865aedc3c6a711fd2c0392833/image.png)
### 5.1 基于 hue 元数据管理创建表
在 hue 的 hive sql 编辑框里面输入 hive-SQL 创建表和导入数据，并点执行
```
    drop table hive\_test;
    create table hive\_test (a int, b string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
    load data local inpath "/usr/local/service/hadoop/bin/hive\_test.data" into table hive\_test;
![](//mc.qcloudimg.com/static/img/bd546d039bdf2c3a487d792bea54389d/image.png)
```
### 5.2 基于 hue 查询数据报表展示
hue 可以将查询结果以图表的方式展示，执行 SQL 语句:` select * from hive_test limit 10;`
执行完成后，结果数据如图所示:
![](//mc.qcloudimg.com/static/img/dbbc7ffa153a9c09409e802e2f4cb9d3/image.png)
选择图例模式，我们选择了 “pie”，可以看到结果图。
![](//mc.qcloudimg.com/static/img/8b543e198d369c1935cbe98b66f0b231/image.png)
### 5.3 基于 hue 的任务调度
* 准备工作流数据
hue 的任务调度基于工作流，先创建一个包含 hive script 脚本的工作流。hive script 脚本的内容如下:
```
    create database if not exists hive\_sample;
    show databases;
    use hive\_sample;
    show tables;
    create table if not exists hive\_sample (a int, b string);
    show tables;
    insert into hive\_sample select 1, "a";
    select * from hive\_sample;
```
将以上内容保存为 hive_sample.sql 文件
hive 工作流还需要一个 hive-site.xml 配置文件，这个配置文件可以在集群中安装了 hive 组件的节点上找到。
具体的路径在：`/usr/local/service/hive/conf/hive-site.xml`
复制一个 hive-site.xml 文件，将其中对应配置修改为如下值:
```
    <property>
     <name>hive.exec.local.scratchdir</name>
     <value>/tmp/hive</value>
    </property>
    <property>
     <name>hive.downloaded.resources.dir</name>
     <value>/tmp/hive/${hive.session.id}\_resources</value>
    </property>
    <property>
     <name>hive.querylog.location</name>
     <value>/tmp/hive</value>
    </property>
    <property>
     <name>hive.server2.logging.operation.log.location</name>
     <value>/tmp/hive/tmp/operation\_logs</value>
    </property>
```
* 创建工作流
在 hue 页面中选择 Workflows -> Editors -> Workflows
![](//mc.qcloudimg.com/static/img/4a57aaba3f6a3d95f4cad15e45b5d5a8/image.png)
单击 “create”  
![](//mc.qcloudimg.com/static/img/120400512a20320938933925311f8779/image.png)
进入当前 workflow 的 hdfs 空间。
![](//mc.qcloudimg.com/static/img/4012fa21197ad31b610eec79ca321ea3/image.png)
上传 hive script 文件和 hive-site.xml,并在 lib 目录中加入 mysql 的 jdbc jar 包。
![](//mc.qcloudimg.com/static/img/878f20da0df4fd426c8173caffd9fd64/image.png)
在工作流编辑页面中拖一个 hive。
![](//mc.qcloudimg.com/static/img/d1a5306cf83a299be4c9937b116a93a9/image.png)
选择刚刚上传的 hive scipt 文件和 hive-site.xml 文件。
![](//mc.qcloudimg.com/static/img/b48bf7c47ee1f3553ea77844864f91fc/image.png)
* 创建定时任务
hue 的定时任务是 coordinator, 类似于 Linux 的 crontab，支持的调度粒度可以到分钟级别。选择 “Workflows->Editors->Coordinator->Create”，创建 coordinator。
![](//mc.qcloudimg.com/static/img/eea286d55aa9d7a7fd70f04174410525/image.png)
单击 “choose a workflow...”， 选择一个创建好的流程。
![](//mc.qcloudimg.com/static/img/c7cdefa232325bcc29599819fbd377a0/image.png)
选择需要调度的粒度和时间间隔，可以多选，用于支持多个时间间隔。
![](//mc.qcloudimg.com/static/img/90d903f7e9fcce240cd279da337d6e29/image.png)
* 执行定时任务。
选择 coordinator 的执行时间区间，然后单击【submit】。
![](//mc.qcloudimg.com/static/img/0888e25e6a1ed10843c4b6d1d4e62484/image.png)
在 coordinator 的监控页面可以看到 coordinator 的调度情况。
![](//mc.qcloudimg.com/static/img/b26649ef261e536f0ebb797a6e86d73a/image.png)

