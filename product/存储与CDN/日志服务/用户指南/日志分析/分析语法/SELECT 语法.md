用于从表中选取数据，默认从当前日志主题中获取符合检索条件的数据。

## 语法格式

```plaintext
* | SELECT [列名(KEY)]
```

## 语法示例

从日志数据中选取列（KEY）为`remote_addr`以及`method`的值：

```plaintext
* | SELECT remote_addr, method 
```

从日志数据中选取所有列（KEY）：

```plaintext
* | SELECT *
```

SELECT 后面也可以跟算术表达式，如从日志数据中查询下载速度：

下载速度（`speed`）= 总发送字节数（`body_bytes_sent`）/ 请求时长（`request_time`）

```plaintext
* | SELECT body_bytes_sent / request_time AS speed
```

