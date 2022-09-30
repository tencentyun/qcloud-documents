## 描述

INT 是 4 字节有符号整数，范围 [-2147483648, 2147483647]。

## 示例
创建表时指定字段类型为 INT。
```sql
CREATE TABLE `tbl` (
  `mykey` int NULL COMMENT "",
  `myvalue` int NOT NULL DEFAULT "0" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
