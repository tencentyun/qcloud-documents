## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：为数据表新增单个分区字段。

## 标准语法
```
ALTER TABLE table_name ADD PARTITION partition_column | hidden_partition_spec [AS alias]

hidden_partition_spec:
	Supported transformations are:
		years(ts): partition by year
		months(ts): partition by month
		days(ts) or date(ts): equivalent to dateint partitioning
		hours(ts) or date_hour(ts): equivalent to dateint and hour partitioning
		bucket(N, col): partition by hashed value mod N buckets
		truncate(L, col): partition by value truncated to L
			Strings are truncated to the given length
			Integers and longs truncate to bins: truncate(10, i) produces partitions 0, 10, 20, 30, …
```

## 参数说明
- `table_name`：需要的表名字。
- `partition_column`: 分区列。
- `alias`: 分区列增加的别名。

## 示例
```
ALTER TABLE prod.db.sample ADD PARTITION FIELD bucket(16, id)
ALTER TABLE prod.db.sample ADD PARTITION FIELD truncate(data, 4)
ALTER TABLE prod.db.sample ADD PARTITION FIELD years(ts)
-- use optional AS keyword to specify a custom name for the partition field 
ALTER TABLE prod.db.sample ADD PARTITION FIELD bucket(16, id) AS shard
```


