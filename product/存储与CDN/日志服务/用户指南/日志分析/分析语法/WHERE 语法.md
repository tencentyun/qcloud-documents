WHERE 用于提取那些满足指定条件的日志。

## 语法格式

```plaintext
* | SELECT 列名（KEY） WHERE 列名（KEY） 运算符 值
```

运算符可以是`=`、`<>`、`>`、`<`、`>=`、`<=`、`BETWEEN`、`IN`、`LIKE`。

>!
> - SQL 中的过滤功能相比检索条件性能较差，建议尽可能的使用检索条件满足数据过滤需求，例如使用`status:>400 | select count(*) as logCounts`代替`* | select count(*) as logCounts where status>400` 以更快的获得统计结果。
> - WHERE 中不能使用 AS 别名，例如`level:* | select level as log_level where log_level='ERROR'`，该语句执行会报错，因为其不符合 SQL-92规范。
>

## 语法示例

从日志数据中查询状态码大于400的日志：

```plaintext
* | SELECT * WHERE status > 400
```

从日志数据中查询请求方式为 GET 且客户端 IP 为 192.168.10.101 的日志条数：

```plaintext
* | SELECT count(*) as count WHERE method='GET' and remote_addr='192.168.10.101'
```

统计 URL 后缀的为 .mp4 的平均请求大小：

```plaintext
* | SELECT round(sum(body_bytes_sent) / count(body_bytes_sent), 2) AS avg_size WHERE url like '%.mp4'
```
