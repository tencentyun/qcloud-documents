## Iceberg表管理
数据湖计算 DLC 服务支持创建和管理 Apache Iceberg 表。Apache Iceberg 是一种用于复杂分析的开放表格式，详细信息可以参考[ Apache Iceberg官网说明](https://iceberg.apache.org/)。
数据湖计算 DLC 支持将普通数据表转换成 Iceberg 表。数据表对应的数据文件必须以 Parquet、ORC、Avro 的格式存储在 COS 桶路径中。
## 将 COS 中的数据文件创建为普通表
参考[数据表管理](https://cloud.tencent.com/document/product/1342/61870)，将 COS 桶中的数据创建为普通数据表。

```
CREATE EXTERNAL TABLE IF NOT EXISTS `DatalakeCatalog`.`database_name`.`table_name` (
`col1` string, 
`col2` string, 
`col3` string) 
PARTITIONED BY (`patition1` string) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
WITH SERDEPROPERTIES ('separatorChar' = ',', 'quoteChar' = '"') 
STORED AS TEXTFILE LOCATION 'cosn://bucket/folder/'
USING iceberg;
```

## 将普通表转换成 Iceberg 表
执行如下命令，将普通数据表转换成 Iceberg 表。
```
CALL DataLakeCatalog.`system`.migrate('database_name.table_name')
```
>?数据湖计算 DLC 仅支持使用 spark 引擎执行该命令。
>