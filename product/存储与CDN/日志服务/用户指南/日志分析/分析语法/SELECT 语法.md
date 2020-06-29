

SELECT 语句用于从表中选取数据。

## SELECT 语法格式

```sql
SELECT 列名（KEY）
```

以及

```sql
SELECT *
```

>?SQL 语句对大小写不敏感。`SELECT`等效于`select`。

## SELECT 语法示例

从日志数据中选取列（KEY）为`remote_addr`以及`method`的值，列（KEY）之间用逗号分隔：

```sql
SELECT remote_addr, method 
```

从日志数据中选取所有列（KEY）：

```sql
SELECT *
```

SELECT 后面也可以跟算术表达式，如从日志数据中查询下载速度：

下载速度（`speed`）= 总发送字节数（`body_bytes_sent`）+ 请求时长（`request_time`）

```sql
SELECT body_bytes_sent / request_time AS speed
```

>! 对日志进行日志检索时，使用的是检索语句；对日志进行日志分析时，使用的是分析语句。后台通过输入的查询语句是否以`SELECT`关键词开头来进行区分：
>- 若查询语句以 `SELECT` 开头，例如`SELECT method, request_size GROUP BY method`，则认为该语句是 SQL 分析语句。
>- 若查询语句不以`SELECT`开头，例如`method:GET`，则认为该语句是检索语句。
