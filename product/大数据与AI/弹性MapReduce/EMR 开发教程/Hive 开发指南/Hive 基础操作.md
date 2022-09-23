Hive 是一个建立在 Hadoop 文件系统上的数据仓库架构，它为数据仓库的管理提供了许多功能，包括数据 ETL（抽取、转换和加载）工具、数据存储管理和大型数据集的查询和分析能力。同时 Hive 还定义了类 SQL 的语言 Hive-SQL。Hive-SQL 允许用户进行和 SQL 相似的操作，可以将结构化的数据文件映射为一张数据库表，并提供简单的 SQL 查询功能。还允许开发人员方便地使用 Mapper 和 Reducer 操作，可以将 SQL 语句转换为 MapReduce 任务运行，这对 MapReduce 框架来说是一个强有力的支持。其优点是学习成本低，可通过类 SQL 语句快速实现简单的 MapReduce 统计，不必开发专门的 MapReduce 应用，十分适合数据仓库统计分析。

Hive 使用 Hadoop 的 HDFS 作为文件的存储系统，很容易扩展自己的存储能力和计算能力，可达到 Hadoop 所能达到的横向扩展能力，数千台服务器的集群已不难做到，是为海量数据做数据挖掘而设计，不过实时性比较差。

Hive 的内部表和外部表：
- **内部表：**实际上是将 hdfs 的文件映射成 table，然后 Hive 的数据仓库会生成对应的目录，EMR 中默认的仓库路径为 `usr/hive/warehouse/$tablename`，**这个路径在 hdfs 上面**，其中 `$tablename` 是您创建的表名。这时只要将符合 table 定义的文件加载到此目录中，即可通过 Hql（Hive-SQL）对整个目录的文件进行查询。
- **外部表：**Hive 中的外部表和表很类似，但是其数据不是放在自己表所属的目录中，而是存放到其他地方。这样的好处是如果您要删除这个外部表，此外部表所指向的数据是不会被删除的，它只会删除外部表对应的元数据。而如果您要删除内部表，该表对应的所有数据包括元数据都会被删除。

Hive 基础操作演示了如何在 EMR 集群上创建表以及通过 Hive 查询表。

## 1. 开发准备
- 任务中要访问腾讯云对象存储 COS，所以需要先在 COS 中创建一个存储桶（Bucket），具体可参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群时，需要在软件配置界面选择 Hive 组件，并且在基础配置页面勾选“开启 COS”，在下方填写自己的 SecretId 和 SecretKey。SecretId 和 SecretKey 可在 [API 密钥管理界面](https://console.cloud.tencent.com/cam/capi) 查看。如果还没有密钥，可单击【新建密钥】创建一个新的密钥。
- Hive 等相关软件安装在路径 EMR 云服务器的`/usr/local/service/`路径下。

## 2. 准备数据
首先登录 EMR 集群中的任意机器，推荐登录到 Master 节点。登录 EMR 的方式可参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，这里可选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面。用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行使用以下命令切换到 Hadoop 用户，并进入 Hive 文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]# cd /usr/local/service/hive
```
新建一个 bash 脚本文件 gen_data.sh，在其中添加以下代码：
```
#!/bin/bash
MAXROW=1000000 #指定生成数据行数
for((i = 0; i < $MAXROW; i++))
do
    echo $RANDOM, \"$RANDOM\"
done
```
并按如下方式执行：
```
[hadoop@172 hive]$ chmod +x 脚本名称
[hadoop@172 hive]$ ./gen_data.sh > hive_test.data
```
这个脚本文件会生成1000000个随机数对，并且保存到文件 hive_test.data 中。
- 使用如下命令把生成的测试数据先上传到 HDFS 中，其中 $hdfspath 为 HDFS 上的您存放文件的路径。
```
[hadoop@172 hive]$ hdfs dfs -put ./hive_test.data /$hdfspath
```
- 也可以使用 COS 上面的数据。将数据上传到 COS 中，如果数据在本地，那么可以使用 COS 控制台来上传数据。如果数据在 EMR 集群，那么使用如下命令来上传数据，其中 $bucketname 为您创建的 COS 桶名。
```
[hadoop@172 hive]$ hdfs dfs -put ./hive_test.data cosn://$bucketname/
```

## 3. Hive 基础操作
### 连接 Hive
登录 EMR 集群的 Master 节点，切换到 Hadoop 用户并且进入 Hive 目录，并连接 Hive：
```
[hadoop@172 hive]$ su hadoop
[hadoop@172 hive]$ cd /usr/local/service/hive/bin
[hadoop@172 bin]$ hive
```
用户也可以使用`-h`参数来获取 Hive 指令的基本信息。也可以使用 beeline 模式连接数据库，同样需要登录 EMR 的Master 节点，切换到 Hadoop 用户并且进入 Hive 目录，在`conf/hive-site.xml`配置文件中，获得 hive server2 的连接端口 $port 和 host 地址 $host：
```
<property>
        <name>hive.server2.thrift.bind.host</name>
        <value>$host</value>
</property>
<property>
        <name>hive.server2.thrift.port</name>
        <value>$port</value>
</property>
```
在 bin 目录下，执行下列语句连接 Hive：
```
[hadoop@172 hive]$ cd bin
[hadoop@172 bin]$ ./beeline -u "jdbc:hive2:// $host: $port " -n hadoop -p hadoop
```

### 创建 Hive 表
无论以 Hive 模式还是 beeline 模式成功连接到 Hive 数据库后，Hive-SQL 的执行语句都是一样的，现在以 Hive 模式执行 Hive-SQL。在 Hive 下执行如下命令查看数据库：
```
hive> show databases;
OK
default
Time taken: 0.26 seconds, Fetched: 1 row(s)
```
使用 `create` 指令创建一个数据库：
```
hive> create database test;                  #创建数据库 test
OK
Time taken: 0.176 seconds
```
使用`use`指令转到刚刚创建的 test 数据库下：
```
hive> use test; 
OK
Time taken: 0.176 seconds
```
使用`create`指令在 test 数据库下创建一个新的名为 hive_test 的内部表：
```
hive> create table hive_test (a int, b string)
hive> ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
#创建数据表 hive_test, 并指定列分割符为','
OK
Time taken: 0.204 seconds
```
**这里只有一条指令，如果不输入分号“;”，Hive-SQL 可以把一条指令放在多行输入。**最后可用以下指令查看表是否创建成功：
```
hive> show tables;
OK
hive_test 
Time taken: 0.176 seconds, Fetched: 1 row(s)
```

### 将数据导入表中
对于存放在 HDFS 中的数据，使用如下指令来将其导入表中：
```
hive> load data inpath "/$hdfspath/hive_test.data" into table hive_test;
```
其中 $hdfspath 为 HDFS 上的您存放文件的路径。导入完成后，HDFS 上导入路径上的源数据文件将会被删除。

对于存放在 COS 中的数据，使用如下指令来将其导入表中：
```
hive> load data inpath "cosn://$bucketname/hive_test.data" into table hive_test;
```
其中 $bucketname 为您的 COS 桶名加桶内存放数据的路径。

同样在导入完成后，COS 导入路径上的源数据文件将会被删除。也可以将存放在 EMR 集群本地的数据导入到 Hive 中，使用如下指令：
```
hive>load data local inpath "/$localpath/hive_test.data" into table hive_test;
```
其中 $localpath 为您的 EMR 集群本地存放数据的路径。导入完成后，源数据会被删除。

### 执行查询
使用 `select` 指令来执行查询操作，统计表中一共有多少行数据：
```
hive> select count(*) from hive_test;
Query ID = hadoop_20170316142922_967b5f0e-1f89-4464-bfa3-b6ed53273fc2
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
set hive.exec.reducers.bytes.per.reducer=
In order to limit the maximum number of reducers:
set hive.exec.reducers.max=
In order to set a constant number of reducers:
set mapreduce.job.reduces=
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
1000000
Time taken: 18.504 seconds, Fetched: 1 row(s)
```
最后输出结果为1000000。

使用 `select` 指令来查询表中的前10个元素：
```
hive> select * from hive_test limit 10;
OK
30847	"31583"
14887	"32053"
19741	"16590"
8104	"20321"
29030	"32724"
27274	"5231"
10028	"22594"
924	"32569"
10603	"27927"
4018	"30518"
Time taken: 2.133 seconds, Fetched: 10 row(s)
```

### 删除 Hive 表
使用 `drop` 指令来删除 Hive 表：
```
hive> drop table hive_test;
Moved: 'hdfs://HDFS/usr/hive/warehouse/hive_test' to trash at: hdfs://HDFS/user/hadoop/.Trash/Current
OK
Time taken: 2.327 seconds
```
更多关于 Hive 的操作，详见 [官方文档](https://hive.apache.org/)。
　　　
