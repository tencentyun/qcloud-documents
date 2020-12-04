

WHERE 用于提取那些满足指定条件的日志。

## WHERE 语法格式

```plaintext
*|SELECT 列名（KEY） WHERE 列名（KEY） 运算符 值
```

运算符可以是`=`、`<>`、`>`、`<`、`>=`、`<=`、`BETWEEN`、`IN`、`LIKE`。

## WHERE 语法示例

从日志数据中查询状态码大于400的日志：

```plaintext
*|SELECT *  WHERE status > 400
```

从日志数据中查询请求方式为 GET 且客户端 IP 为 192.168.10.101 的日志条数：

```plaintext
*|SELECT count(*) as count WHERE method='GET' and remote_addr='192.168.10.101'
```

统计 URL 后缀的为 .mp4 的平均请求大小：

```plaintext
*|SELECT round(sum(body_bytes_sent) / count(body_bytes_sent), 2) AS avg_size  WHERE url like '%.mp4'
```
