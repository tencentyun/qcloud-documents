## 描述
TINYINT 是1 字节有符号整数，范围 [-128, 127]。

## 示例
创建表时指定字段类型为 TINYINT。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mytinyint` tinyint(4) NOT NULL DEFAULT "0" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
