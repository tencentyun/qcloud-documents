Hudi 表的查询操作作用于 Hudi 的三种视图之上，可以根据需求差异选择合适的视图进行查询。

### 实时快照视图（Snapshot Queries）
可以查询最新 COMMIT 的快照数据。针对 Merge On Read 类型的表，查询时需要在线合并列存中的 Base 数据和日志中的实时数据；针对 Copy On Write 表，可以查询最新版本的 Parquet 数据。
Copy On Write 和 Merge On Read 表支持该类型的查询。
- SparkSQL 示例：
```SQL
SELECT count(*) FROM `DataLakeCatalog`.`hudi_spark`.`hudi_test`
```

- Spark API 示例：
```java
    spark.read.

      format("hudi")

      .option(QUERY_TYPE_OPT_KEY,QUERY_TYPE_SNAPSHOT_OPT_VAL)

      .option(BEGIN_INSTANTTIME_OPT_KEY,"20221009003522620")

      .load("cosn://<cos_bucket>/spark_hudi/hudi_cow_sync")

      .createOrReplaceTempView("hudi_test")

    .spark.sql("select count(*) from hudi_test").show()
```

### 增量视图（Incremental Queries）
仅查询新写入数据集的文件，需要指定一个 Commit/Compaction 的即时时间（位于 Timeline 上的某个 Instant）作为条件，来查询此条件之后的新数据。
Copy On Write 和 Merge On Read 表支持该类型的查询。
- SparkSQL 示例：
在 sparksql 引擎的高级设置里，添加如下两个参数：
```SQL
hoodie.datasource.query.type=incremental

hoodie.datasource.read.begin.instanttime=20221009003522620

SELECT count(*) FROM `DataLakeCatalog`.`hudi_spark`.`hudi_test` 
```

- Spark API 示例：
```java
    spark.read.

      format("hudi")

      .option(QUERY_TYPE_OPT_KEY,QUERY_TYPE_INCREMENTAL_OPT_VAL)

      .option(BEGIN_INSTANTTIME_OPT_KEY,"20221009003522620")

      .load("cosn://<cos_bucket>/spark_hudi/hudi_cow_sync")

      .show(false)
```

### 读优化视图（Read Optimized Queries）
该视图仅将最新文件切片中的基本/列文件（Parquet）暴露给查询，并保证与非 Hudi 列式数据集相比，具有相同的列式查询性能。
该视图是对 Merge On Read 表类型快照查询的优化，通过牺牲查询数据的时效性，来减少在线合并日志数据产生的查询延迟。
- SparkSQL 示例：
在 sparksql 引擎的高级设置里，添加如下两个参数：
hoodie.datasource.query.type=read_optimized
hoodie.datasource.read.begin.instanttime=20221009003522620
```SQL
SELECT count(*) FROM `DataLakeCatalog`.`hudi_spark`.`hudi_test` 
```

- Spark API 示例：
```SQL
    spark.read.

      format("hudi")

      .option(QUERY_TYPE_OPT_KEY,QUERY_TYPE_READ_OPTIMIZED_OPT_VAL)

      .load("cosn://<cos_bucket>/spark_hudi/hudi_cow_sync")

      .show(false)
```
