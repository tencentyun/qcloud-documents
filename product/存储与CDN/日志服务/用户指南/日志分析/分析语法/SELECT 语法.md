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

## 列名规范

在 SQL 规范中，列名须由字母、数字和下划线`_`组成，且以字母开头，例如`remote_addr`。日志中字段名称不符合该规范时，需使用双引号`""`包裹，也可以再在 SQL 中使用 [AS 语法](https://cloud.tencent.com/document/product/614/44069) 为该字段指定别名。

日志字段名为`remote_addr`，符合 SQL 列名规范，可直接使用 select 查询：

```
* | SELECT remote_addr
```

日志字段名为`__TAG__.pod_label_qcloud-app`，不符合 SQL 列名规范，需使用双引号`""`包裹：

```
* | SELECT "__TAG__.pod_label_qcloud-app"
```

日志字段名为`__TIMESTAMP__`，不符合 SQL 列名规范，需使用双引号`""`包裹，同时使用 AS 为该字段指定别名：

```
* | SELECT "__TIMESTAMP__" AS log_time
```

