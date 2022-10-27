## 描述
SMALLINT 是 2 字节有符号整数，范围 [-32768, 32767]。

## 示例
创建表时指定字段类型为 SMALLINT。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mysmallint` smallint(6) NOT NULL DEFAULT "0" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
