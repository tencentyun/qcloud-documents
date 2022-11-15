## 描述
CHAR(M)：定长字符串，M 代表的是定长字符串的长度。M 的范围是1-255。

## 示例
创建表时指定字段类型为 CHAR。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mychar` char(10) NOT NULL COMMENT "range char(m),m in (1-255)"
) ENGINE=OLAP
DUPLICATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
