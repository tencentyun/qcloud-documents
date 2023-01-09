## 描述
LARGEINT 是16 字节有符号整数，范围 [-2^127 + 1 ~ 2^127 - 1]。

## 示例
创建表时指定字段类型为 LARGEINT。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mylargeint` largeint(40) NOT NULL DEFAULT "0" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
