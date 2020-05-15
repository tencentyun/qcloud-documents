## 背景说明
在数据仓库的建设中，通常我们使用Hive处理原始数据（PB级别），进行耗时较长的ETL工作，再将结果数据（TB级别）交由准实时的计算引擎（如CDW）对接BI工具，保证报表的准实时展现。
本文介绍了如何将EMR上Hive的数据通过COS导入到CDW云数仓的过程。

## 步骤
1. 开启EMR读写对象存储能力

首先需要保证EMR具备读写COS的能力，这里在创建EMR的过程中，可以进行勾选

![](https://main.qcloudimg.com/raw/76589b702a655578cfd6aa1f950bad47.png)

2. 创建Hive 本地表并写入数据

语法如下
```
create table hive_local_table(c1 int, c2 string, c3 int, c4 string);
insert into hive_local_table values(1001, 'c2', 99, 'c4'),(1002, 'c2', 100, 'c4'),(1003, 'c2', 101, 'c4'),(1004, 'c2', 100, 'c4'),(1005, 'c2', 101, 'c4')
```

3. 创建Hive COS外表

语法如下：
```
create table hive_cos_table(c1 int, c2 string, c3 int, c4 string) 
row format delimited fields terminated by ',' 
LINES TERMINATED BY '\n'
stored as textfile location 'cosn://{bucket_name}/{dir_name}';
```
详细信息可以参考EMR文档 [基于对象存储COS的数据创库](https://cloud.tencent.com/document/product/589/12319)

4. 将本地数据导入COS

语法如下：
```
insert into hive_cos_table select * from hive_local_table;
```
成功写入后，可以在对应的COS目录下看到文件

5. 在CDW侧创建COS外表

语法如下：
```
CREATE READABLE EXTERNAL TABLE  snova_cos_table (c1 int, c2 varchar(32), c3 int, c4 varchar(32)) 
LOCATION('cos:// {BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX} secretKey=**** secretId=***')
FORMAT 'csv';
```
详细内容可以参见 [使用外表](https://cloud.tencent.com/document/product/878/20068)

6. 在CDW侧创建本地表并导入数据

语法如下：
```
create table snova_local_table(c1 int, c2 text, c3 int, c4 text);
insert into snova_local_table select * from snova_cos_table;
```

## 注意

**CDW不支持ORC,Parquet等格式，只支持CSV等文本格式及其对应的GZIP压缩格式**

**CDW侧导入COS数据的效率与文件的个数有一定关系，建议个数为CDW计算节点个数的N倍**
