本文介绍二进制字符串函数的语法。


二进制字符串类型 varbinary 有别于字符串类型 varchar。

| 语句                                    | 说明                                  |
| --------------------------------------- | ------------------------------------- |
| 连接函数 \|\|                           | `a || b` 结果为 `ab`。                 |
| length(binary) → bigint                 | 返回二进制的长度。                    |
| concat(binary1, …, binaryN) → varbinary | 连接二进制字符串，等同于\|\|。        |
| to_base64(binary) → varchar             | 把二进制字符串转换成 base64。          |
| from_base64(string) → varbinary         | 把 base64 转换成二进制字符串。          |
| to_base64url(binary) → varchar          | 转化成 URL 安全的 base64。               |
| from_base64url(string) → varbinary      | 从 URL 安全的 base64 转化成二进制字符串。 |
| to_hex(binary) → varchar                | 把二进制字符串转化成十六进制表示。    |
| from_hex(string) → varbinary            | 从十六进制转化成二进制。              |
| to_big_endian_64(bigint) → varbinary    | 把数字转化成大端表示的二进制。        |
| from_big_endian_64(binary) → bigint     | 把大端表示的二进制字符串转化成数字。  |
| md5(binary) → varbinary                 | 计算二进制字符串的 md5。               |
| sha1(binary) → varbinary                | 计算二进制字符串的 sha1。              |
| sha256(binary) → varbinary              | 计算二进制字符串的 sha256 hash。       |
| sha512(binary) → varbinary              | 计算二进制字符串的 sha512。            |
| xxhash64(binary) → varbinary            | 计算二进制字符串的 xxhash64。          |

