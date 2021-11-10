Apache Impala 项目为存储在 Apache Hadoop 文件格式的数据提供高性能、低延迟的 SQL 查询。它对查询进行快速响应，同时支持对分析查询进行交互式的数据探索和查询调整，而不是传统上那种与 SQL-on-Hadoop 技术相关联的长时间批量作业。

Impala 不同于 hive，hive 底层执行使用的是 MapReduce 引擎，仍然是一个批处理过程。而 impala 的中间结果不写入磁盘，即时通过网络以流的形式传递，大大降低了节点的 IO 开销。

Impala 与 Apache Hive 数据库集成，在两个组件之间共享数据库和表。通过与 Hive 的高度集成，以及与 HiveQL 语法的兼容性，您可以使用 Impala 或 Hive 创建表、发起查询、加载数据等。

## 前提条件
- 确认已开通腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群时，需要在软件配置界面选择 Impala 组件。
- Impala 安装在路径 EMR 云服务器的`/data/`路径下（`/data/Impala`）。

## 准备数据
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，可选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Impala 文件夹。
```
[root@10 ~]# su hadoop
[hadoop@10 root]$ cd /data/Impala/
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
然后执行如下命令：
```
[hadoop@10 ~]$ ./gen_data.sh > impala_test.data
```
这个脚本文件会生成1000000个随机数对，并且保存到文件`impala_test.data`中。然后把生成的测试数据上传到 HDFS 中，执行如下命令：
```
[hadoop@10 ~]$ hdfspath="/impala_test_dir"
[hadoop@10 ~]$ hdfs dfs -mkdir $hdfspath
[hadoop@10 ~]$ hdfs dfs -put ./impala_test.data $hdfspath
```
其中 $hdfspath 为 HDFS 中您存放文件的路径。最后可用如下命令，验证数据是否正常放到 hdfs 上。
```
[hadoop@10 ~]$ hdfs dfs -ls $hdfspath
```


## Impala 基础操作
### 连接 Impala
登录 EMR 集群的 Master 节点，切换到 Hadoop 用户并且进入 Impala 目录，并连接 Impala：
```
[root@10 Impala]# cd /data/Impala/; bin/impala-shell.sh -i $core_ip:27001
```
其中 core_ip 为 EMR 集群的 core 节点 IP，也可以用 task 节点的 IP，正常登录后显示如下：
```
Connected to $core_ip:27001
Server version: impalad version 2.10.0-SNAPSHOT (build Could not obtain git hash)
***********************************************************************************
Welcome to the Impala shell.
(Impala Shell v2.10.0-SNAPSHOT (Could) built on Tue Nov 20 17:28:10 CST 2018)

The '-B' command line flag turns off pretty-printing for query results. Use this
flag to remove formatting from results you want to save for later, or to benchmark
Impala.
***********************************************************************************
[$core_ip:27001] >
```
也可以登录 core 节点或者 task 节点后，直接连接，执行语句如下：
```
cd /data/Impala/; bin/impala-shell.sh -i localhost:27001
```
 
### 创建 Impala 库
在 Impala 下执行以下语句，查看数据库：
```
[10.1.0.215:27001] > show databases;
Query: show databases
+------------------+----------------------------------------------+
| name             | comment                                      |
+------------------+----------------------------------------------+
| _impala_builtins | System database for Impala builtin functions |
| default          | Default Hive database                        |
+------------------+----------------------------------------------+
Fetched 2 row(s) in 0.09s
```
使用`create`指令创建一个数据库：
```
[localhost:27001] > create database experiments;
Query: create database experiments
Fetched 0 row(s) in 0.41s
```
使用`use`指令转到刚创建的 test 数据库下：
```
[localhost:27001] > use experiments;
Query: use experiments
```
查看当前所在库，执行如下语句：
```
select current_database();
```

### 创建 Impala 表
使用`create`指令在 experiments 数据库下创建一个新的名为 impala_test 的内部表：
```
[localhost:27001] > create table t1 (a int, b string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
Query: create table t1 (a int, b string)
Fetched 0 row(s) in 0.13s
```
查看所有表：
```
[localhost:27001] > show tables;
Query: show tables
+------+
| name |
+------+
| t1   |
+------+
Fetched 1 row(s) in 0.01s
```
查看表结构：
```
[localhost:27001] > desc t1;
Query: describe t1
+------+--------+---------+
| name | type   | comment |
+------+--------+---------+
| a    | int    |         |
| b    | string |         |
+------+--------+---------+
Fetched 2 row(s) in 0.01s
```

### 将数据导入表中
对于存放在 HDFS 中的数据，使用如下指令来将其导入表中：
```
LOAD DATA INPATH '$hdfspath/impala_test.data' INTO TABLE t1;
```
其中 $hdfspath 为 HDFS 中您存放文件的路径。导入完成后，HDFS 上导入路径上的源数据文件将会被删除。存放到 Impala 内部表的存放路径`/usr/hive/warehouse/experiments.db/t1`下。也可以建立外部表，语句如下：
>!这里只有一条指令，如果不输入分号“;”，可以把一条指令放在多行输入。
>
```
CREATE EXTERNAL TABLE t2
(
   a INT,
   b string
)  
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION '/impala_test_dir';
```

### 执行查询
```
[localhost:27001] > select count(*) from experiments.t1;
Query: select count(*) from experiments.t1
Query submitted at: 2019-03-01 11:20:20 (Coordinator: http://10.1.0.215:20004)
Query progress can be monitored at: http://10.1.0.215:20004/query_plan?query_id=f1441478dba3a1c5:fa7a8eef00000000
+----------+
| count(*) |
+----------+
| 1000000  |
+----------+
Fetched 1 row(s) in 0.63s
```
最后输出结果为1000000。

### 删除表
```
[localhost:27001] > drop table experiments.t1;
Query: drop table experiments.t1
```

更多 Impala 的操作，详见 [官方文档](https://impala.apache.org/impala-docs.html)。

## 通过 JDBC 连接 Impala
Impala 也可以通过 Java 代码来连接，步骤类似于 [通过 Java 连接 Hive](https://cloud.tencent.com/document/product/589/19021)。

唯一区别的是，`$hs2host`和`$hsport`，其中`$hs2host`是 EMR 集群中任意 core 节点或者 task 节点的 IP。而 hsport 可以在对应节点的 Impala 目录下，配置文件`conf/impalad.flgs`中查看。
```
[root@10 ~]# su hadoop
[hadoop@10 root]$ cd /data/Impala/
[hadoop@10 Impala]$ grep hs2_port conf/impalad.flgs
```

## 如何映射 Hbase 表
Impala 会使用 hive 的元数据信息，所有在 Hive 中的表，都可以在 Impala 中读到。可通过 [在 hive 中映射 Hbase 表](https://cloud.tencent.com/document/product/589/12320) 达到在 Impala 中映射 Hbase 表。

