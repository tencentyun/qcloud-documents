本节将基于 COS（腾讯云对象存储）展示 Hive 连接器更多使用方法，数据来源于 COS 数据 + 直接插入数据 + lzo 压缩数据。这里使用了一个脚本来生产相关数据，内容如下：

``` sql
create database if not exists test;
use test;
create external table if not exists presto_on_cos (id int,name string) ROW FORMAT DELIMITED FIELDS TER
MINATED BY ’,’;
insert into presto_on_cos values (12,’hello’),(13,’world’);
load data inpath "cosn://huadong/cos.txt" into table presto_on_cos;
load data local inpath "lzo.txt.lzo" into table presto_on_cos;
```

其中，lzo.txt 压缩 lzo 之前的内容如下：

``` 
10,lzo_pop
11,lzo_tim
```

cos.txt 的内容如下：

```
5,cos_patrick
6,cos_stone
```

温馨提示：建议如示例一样使用外部表进行 Hive 测试，以免删除重要数据。  
使用 hive-cli 执行这个脚本：

``` shell
$hive -f "presto_on_cos_test.sql"
```

使用上一节的方法进入到 Presto 后，查询刚刚生产的数据：

``` sql
presto> select * from test.presto_on_cos;
```
结果如下：

``` sql
presto select * from test.presto_on_cos;
 id |    name
----|-----------
 12 | he11o
 13 | world
  5 | cos_patrick
  6 | cos_stone
 10 | lzo_pop
 11 | lzo_tim
(6 rows)

Query 20171025_125031_000_14_tibjv, finished, 4 nodes
Splits: 4 total, 4 done (100.00%)
0:00 [6rows, 127B] [38 rows/s, 817B/s]
```

有关 Presto 更多用法，可参考：[官方文档](https://prestodb.io/docs/current/)和[中文文档](http://prestodb-china.com/docs/current/index.html)

