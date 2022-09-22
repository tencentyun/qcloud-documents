## 描述
FLOAT 是 4 字节浮点数。

## 示例
创建表时指定字段类型为 FLOAT。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `myfloat` float NOT NULL DEFAULT "0.0" COMMENT ""
) ENGINE=OLAP
DUPLICATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
