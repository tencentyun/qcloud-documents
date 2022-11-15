## 描述
VARCHAR(M) 是变长字符串，M 代表的是变长字符串的字节长度。M 的范围是1-65533。
>! 变长字符串是以 UTF-8 编码存储的，因此通常英文字符占1个字节，中文字符占3个字节。

## 示例
创建表时指定字段类型为 VARCHAR。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `myvarchar` varchar(20) NOT NULL DEFAULT "" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
