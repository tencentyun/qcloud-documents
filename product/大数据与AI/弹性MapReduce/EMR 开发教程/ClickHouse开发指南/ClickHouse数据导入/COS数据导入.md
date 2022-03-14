ClickHouse 提供了两种方法将外部云对象存储的数据导入到表中：
- 表引擎：通过创建 Engine=S3 的外部表将数据导入。
- 表函数：通过使用内置函数将数据导入。

使用上述两种方法，EMR 目前提供的版本支持对象存储的访问属性设置如下表所示：

|EMR 版本|	ClickHouse 版本	|对象存储访问属性	|支持的表引擎|
|---------|---------|---------|----|
|1.0.0	|19.16.12.49	|公共读写|	S3|
|1.1.0	|20.3.10.75|	公共读写、认证读写（通过 secretId 和 secretKey）	|S3|
|1.2.0+	|20.7.2.30	|公共读写、认证读写（通过 secretId 和 secretKey）	|S3、COSN|


## 表引擎方式
通过创建 Engine 为 S3 的外表和目的数据表，然后使用 INSERT INTO 语句批量插入数据。
```
CREATE TABLE testdb.costb (
    column1 UInt32, 
    column2 String,
    column3 String
) ENGINE=S3 ('http://${bucket-name}.cos.${region}.myqcloud.com/data1.csv', 'CSV');
或者
CREATE TABLE testdb.costb (
    column1 UInt32, 
    column2 String,
    column3 String
) ENGINE=S3('http://${bucket-name}.cos.${region}.myqcloud.com/data1.csv', 'secretId', 'secretKey', 'CSV');

或者
CREATE TABLE testdb.costb (
    column1 UInt32, 
    column2 String,
    column3 String
) ENGINE=COSN('http://${bucket-name}.cos.${region}.myqcloud.com/data1.csv', 'secretId', 'secretKey', 'CSV');

CREATE TABLE testdb.chtb (
    column1 UInt32, 
    column2 String, 
    column3 String
) ENGINE=MergeTree() ORDER BY(column1);

INSERT INTO testdb.chtb SELECT * FROM testdb.costb;
```
EMR 1.2.0 以上的版本（ClickHouse 20.7.2.30+）可以将 S3 表引擎修改为 COSN 引擎，用法和效果与 S3 一样。

## 表函数方式
在创建数据表时使用 S3 内置函数直接将数据导入到表中。
```
CREATE TABLE testdb.chtb
ENGINE=MergeTree() 
ORDER BY(column1) 
AS SELECT * FROM s3(
  'http://${bucket-name}.cos.${region}.myqcloud.com/data1.csv', 
  'CSV', 'column1 UInt32, column2 String, column3 String');
  
或者
CREATE TABLE testdb.chtb
    ENGINE=MergeTree() 
    ORDER BY(column1) 
    AS SELECT * FROM s3(
      'http://${bucket-name}.cos.${region}.myqcloud.com/data1.csv', 'secretId', 'secretKey',
      'CSV', 'column1 UInt32, column2 String, column3 String');

```

## 参考资料
- [clickhouse sql](https://clickhouse.tech/docs/en/query_language/create/)
- [clickhouse issue](https://github.com/ClickHouse/ClickHouse/issues/1394)
