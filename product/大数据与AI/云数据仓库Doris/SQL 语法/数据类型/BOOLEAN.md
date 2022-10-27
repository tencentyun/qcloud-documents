## 描述
长度与 TINYINT 一样，0 代表 false，1 代表 true。

## 示例
创建表时指定字段类型为 BOOLEAN。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mybool` boolean NOT NULL DEFAULT "false" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3; 
```
