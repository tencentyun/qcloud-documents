## 背景说明
在数据仓库的建设中，通常我们使用 Hive 处理原始数据（PB 级别），进行耗时较长的 ETL 工作，再将结果数据（TB 级别）交由准实时的计算引擎（例如云数据仓库 PostgreSQL）对接 BI 工具，保证报表的准实时展现。

本文介绍了如何将 EMR 上 Hive 的数据通过 COS 导入到云数据仓库 PostgreSQL 的过程。

## 操作步骤
>!
>- 云数据仓库 PostgreSQL 不支持 ORC、Parquet 等格式，仅支持 CSV 等文本格式及其对应的 GZIP 压缩格式。
>- 云数据仓库 PostgreSQL 侧导入 COS 数据的效率与文件的个数有一定关系，建议个数为云数据仓库 PostgreSQL 计算节点个数的 N 倍。

1. 开启 EMR 读写对象存储能力
首先需要保证 EMR 具备读写 COS 的能力，可在创建 EMR 时，勾选**开启**对象存储。
![](https://main.qcloudimg.com/raw/160a06fdf4442962f901b360a06b364c.png)
2. 创建 Hive 本地表并写入数据
```
create table hive_local_table(c1 int, c2 string, c3 int, c4 string);
insert into hive_local_table values(1001, 'c2', 99, 'c4'),(1002, 'c2', 100, 'c4'),(1003, 'c2', 101, 'c4'),(1004, 'c2', 100, 'c4'),(1005, 'c2', 101, 'c4')
```
3. 创建 Hive COS 外表
```
create table hive_cos_table(c1 int, c2 string, c3 int, c4 string) 
row format delimited fields terminated by ',' 
LINES TERMINATED BY '\n'
stored as textfile location 'cosn://{bucket_name}/{dir_name}';
```
详细信息可以参考 EMR 文档 [基于对象存储 COS 的数据仓库](https://cloud.tencent.com/document/product/589/12319)。
4. 将本地数据导入 COS
```
insert into hive_cos_table select * from hive_local_table;
```
成功写入后，可以在对应的 COS 目录下看到文件。
5. 在云数据仓库 PostgreSQL 侧创建 COS 外表
```
CREATE READABLE EXTERNAL TABLE  snova_cos_table (c1 int, c2 varchar(32), c3 int, c4 varchar(32)) 
LOCATION('cos:// {BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX} secretKey=**** secretId=***')
FORMAT 'csv';
```
详细内容可以参见 [使用外表高速导入或导出 COS 数据](https://cloud.tencent.com/document/product/878/34875)。
6. 在云数据仓库 PostgreSQL 侧创建本地表并导入数据
```
create table snova_local_table(c1 int, c2 text, c3 int, c4 text);
insert into snova_local_table select * from snova_cos_table;
```

