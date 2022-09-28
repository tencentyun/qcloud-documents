## 描述
BIGINT：8 字节，有符号整数，范围 [-9223372036854775808, 9223372036854775807]。

## 示例
创建表时指定字段类型为 BIGINT。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mybigint` bigint(20) NOT NULL DEFAULT "0" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
