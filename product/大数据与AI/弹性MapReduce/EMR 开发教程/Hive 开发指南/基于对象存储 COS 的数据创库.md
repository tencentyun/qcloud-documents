基于对象存储 COS 的数据创库有两种方式：

1. 第一种将整个数据库的建立在 COS 上

    整个库在 COS 上您可以通过如下语句实现。
    ``` sql
    create database hivewithcos location 'cosn://huadong/hive';
    ```
    其中 huadong 是 bucket 名称，而 hive 是路径，您可以根据您的实际需要进行设置, 创建完库后您可以创建一张数据表。

    ``` sql
    create table record(id int, name string) row format delimited fields terminated by ',' stored as textfile;
    ```

    然后向表中 load 数据即可，其使用方式和 HDFS 使用完全一样。

2. 第二种可以指定表放在 COS 上

    您首先需要在 Hive 中选择一个数据库或者创建一个数据库，然后通过如下语句实现单表存储在 COS 上。

    ``` sql
    create table record(id int, name string) row format delimited fields terminated by ',' stored as textfile location 'cosn://huadong/hive/cos';
    ```

    然后向表中 load 数据即可，单个表在 COS 上即设定表的存储位置在对象存储之上。
