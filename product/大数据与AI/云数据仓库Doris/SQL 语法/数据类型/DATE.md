## 描述
日期类型，目前的取值范围是 ['0000-01-01', '9999-12-31']，默认的打印形式是“YYYY-MM-DD”。

## 示例
创建表时指定字段类型为 DATE。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mydate` date NOT NULL DEFAULT "1900-01-01" COMMENT "YYYY-MM-DD"
) ENGINE=OLAP
DUPLICATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
