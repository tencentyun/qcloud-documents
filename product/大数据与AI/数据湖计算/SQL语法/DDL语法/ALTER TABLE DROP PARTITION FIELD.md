## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：删除数据表的某个分区字段。

## 标准语法
```
ALTER TABLE table_name ADD PARTITION partition_column | hidden_partition_spec

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
- `partition_column`：分区列。

## 示例
```
ALTER TABLE prod.db.sample DROP PARTITION FIELD catalog
ALTER TABLE prod.db.sample DROP PARTITION FIELD bucket(16, id)
ALTER TABLE prod.db.sample DROP PARTITION FIELD truncate(data, 4)
ALTER TABLE prod.db.sample DROP PARTITION FIELD years(ts)
ALTER TABLE prod.db.sample DROP PARTITION FIELD shard
```


