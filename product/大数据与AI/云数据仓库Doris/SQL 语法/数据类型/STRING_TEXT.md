## 描述
STRING 或者 TEXT 是变长字符串，最大支持2147483643 字节（2GB-4）。String 类型的长度还受 BE 配置  `string_type_soft_limit  string_type_length_soft_limit_bytes`，实际能存储的最大长度取两者最小值，String类型只能用在value 列，不能用在 key 列和分区 分桶列。
>! 变长字符串是以 UTF-8 编码存储的，因此通常英文字符占1个字节，中文字符占3个字节。

## 示例
创建表时指定字段类型为 STRING。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mystring` text NOT NULL DEFAULT "" COMMENT ""
) ENGINE=OLAP
UNIQUE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```

表创建成功后通过 `desc tablename;` 查看表可以看到 STRING 类型为 `text`。
