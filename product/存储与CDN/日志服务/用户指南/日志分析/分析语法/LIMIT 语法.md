

LIMIT 子句用于限制由 SELECT 语句返回的数据数量。

## LIMIT 语法格式

读取前 count 行：

```plaintext
LIMIT count
```
>!LIMIT 不支持 [offset] rows 语法。


## LIMIT 语法样例

对请求状态码日志数降序排序，只获取前10行：

```plaintext
*|SELECT status, COUNT(status) as ct ORDER BY status DESC LIMIT 10
```
