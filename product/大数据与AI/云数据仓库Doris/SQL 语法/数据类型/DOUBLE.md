## 描述
DOUBLE 是 8 字节浮点数。

## 示例
创建表时指定字段类型为 DOUBLE。
```sql
CREATE TABLE `tbl` (
  `mykey` int NULL COMMENT "",
  `mydouble` double NOT NULL DEFAULT "0.0" COMMENT ""
) ENGINE=OLAP
DUPLICATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
