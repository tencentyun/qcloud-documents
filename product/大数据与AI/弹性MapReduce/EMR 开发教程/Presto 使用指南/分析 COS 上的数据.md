本节将基于腾讯云对象存储 COS 展示 Hive 连接器更多使用方法，数据来源于直接插入数据、COS 数据和 lzo 压缩数据。
## 1.	开发准备
- 因为任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中先 [创建一个存储桶（Bucket）](https://cloud.tencent.com/document/product/436/6232)。
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Presto 组件，并且在基础配置页面勾选“开启COS”，在下方填写自己的 SecretId 和 SecretKey。
SecretId 和 SecretKey 可以在 [API 密钥管理界面](https://console.cloud.tencent.com/cam/capi) 查看。如果还没有密钥，请单击【新建密钥】建立一个新的密钥。
- Presto 等相关软件安装在路径 EMR 云服务器的` /usr/local/service/`路径下。

## 2.	数据准备
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云度武器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。
在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Hive 文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]# cd /usr/local/service/hive
```
新建文件 cos.txt，并且添加数据如下所示：
```
5,cos_patrick
6,cos_stone
```
使用 HDFS 指令把文件上传到 COS 中去：
```
[hadoop@172 hive]# hdfs dfs –put cosn://$bucketname/
```
其中 $bucketname 为您创建的存储桶的名字和路径。
再新建一个文件 lzo.txt，并且在其中添加数据如下所示：
```
10,lzo_pop
11,lzo_tim
```
将其压缩成 .lzo 文件：
```
[hadoop@172 hive]$ lzop -v lzo.txt
compressing hive_test.data into lzo.txt.lzo
```

## 3.	新建 Hive 表并使用 Presto 查询
这里使用了一个脚本文件来生产进行 Hive 数据库和表的创建。新建一个脚本文件 presto_on_cos_test.sql，并添加以下程序：
```
create database if not exists test;
use test;
create external table if not exists presto_on_cos (id int,name string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ’,’;
insert into presto_on_cos values (12,’hello’),(13,’world’);
load data inpath "cosn://$bucketname/cos.txt" into table presto_on_cos;
load data local inpath "/$yourpath/lzo.txt.lzo" into table presto_on_cos;
```
其中 $bucketname 为您的 COS 存储桶名加路径，$yourpath 为您放置 lzo.txt.lzo 文件的路径。

脚本文件首先新建一个数据库“test”，在新建的数据库中新建一个表“presto_on_cos”。分三步进行了数据的插入操作，首先采用直接插入的方法。然后插入了 COS 中数据，最后插入 lzo 压缩包中的数据。

**建议如示例一样，使用外部表进行 Hive 测试，以免删除重要数据**。使用 hive-cli 执行这个脚本：

```
[hadoop@172 hive]$ hive -f "presto_on_cos_test.sql"
```

执行完成之后，就可以进入 Presto 查看表中的数据。使用上一节的方法进入 Presto，不过需要改动 schema参数。

```
[hadoop@172 presto-client]$ ./presto --server $host:$port --catalog hive --schema test
```
对刚刚创建的 Hive 表进行查询：
```
presto:test> select * from presto_on_cos ;
 id |    name     
----+-------------
  5 | cos_patrick 
  6 | cos_stone   
 10 | lzo_pop     
 11 | lzo_tim     
 12 | hello 
 13 | world 
(6 rows)

Query 20180702_150000_00011_c4qzg, FINISHED, 3 nodes
Splits: 4 total, 4 done (100.00%)
0:03 [6 rows, 127B] [1 rows/s, 37B/s]
```
更多 Presto 操作请查看 [官方文档](https://prestodb.io/docs/current/)。
