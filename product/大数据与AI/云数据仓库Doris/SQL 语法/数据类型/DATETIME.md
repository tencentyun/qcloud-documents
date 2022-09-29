## 描述
DATETIME：日期时间类型，取值范围是 ['0000-01-01 00:00:00', '9999-12-31 23:59:59']。打印的形式是“YYYY-MM-DD HH: MM: SS”。

## 示例
创建表时指定字段类型为 DATETIME。
```sql
CREATE TABLE `tbl` (
  `mykey` int NULL COMMENT "",
  `mydatetime` datetime NOT NULL DEFAULT "1900-01-01 00:00:00" COMMENT ""
) ENGINE=OLAP
DUPLICATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
