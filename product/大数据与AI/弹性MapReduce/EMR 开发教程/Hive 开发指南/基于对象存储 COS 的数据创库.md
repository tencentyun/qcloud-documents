基于对象存储 COS 的数据仓库有两种方式：

### 方式一：将整个数据库建立在 COS 上
整个数据库建立在 COS 上可通过如下语句实现。
``` sql
create database hivewithcos location 'cosn://huadong/hive';
```
其中 huadong 是 bucket 名称，而 hive 是路径，可根据您的实际需要进行设置。库创建完成后，创建一张数据表。然后向表中 load 数据，其使用方式和 HDFS 相同。
``` sql
create table record(id int, name string) row format delimited fields terminated by ',' stored as textfile;
```


### 方式二：将指定表放在 COS 上
首先需要在 Hive 中选择一个数据库或者创建一个数据库，然后通过如下语句实现单表存储在 COS 上。
``` sql
create table record(id int, name string) row format delimited fields terminated by ',' stored as textfile location 'cosn://huadong/hive/cos';
```
然后向表中 load 数据，单个表在 COS 上即设定表的存储位置在对象存储中。
