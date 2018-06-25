映射 Hbase 表之前您首先需要在 Hbase 中创建相应的表，通过如下语句实现映射：

``` sql
CREATE EXTERNAL TABLE hive_test (
rowkey string,
a string,
b string,
c string
) STORED BY ’org.apache.hadoop.hive.hbase.HBaseStorageHandler’
WITH SERDEPROPERTIES ("hbase.columns.mapping" = ":key,cf:a,cf:b,cf:c")
TBLPROPERTIES ("hbase.table.name" = "test");
```

其中 hbase.table.name 为 Hbase 中您的数据表名，cf:a,cf:b,cf:c 为 Hbase 表中的列，cf 表示列族，同时您还需要在 hive-site.xml 设置参数 hbase.zookeeper.quorum 以便来访问 Hbase。
