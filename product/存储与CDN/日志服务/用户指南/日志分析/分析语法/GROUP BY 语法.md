

GROUP BY 语句用于结合聚合函数，根据一个或多个列（KEY）对结果集进行分组。

## GROUP BY 语法格式

`GROUP BY`支持任意的表达式，可以使用列名、别名，也可以使用序号（从1开始）。
`GROUP BY`支持单个列，也可以是多个列。
`GROUP BY`常与 MIN，MAX，AVG，SUM 或 COUNT 等 [聚合函数](https://cloud.tencent.com/document/product/614/44067) 结合使用。

```sql
SELECT 列名（KEY）, 聚合函数
GROUP BY [ 列名（KEY）| 别名 | 序号 ]
```

## GROUP BY 语法样例

#### GROUP BY 单列

统计不同状态码的访问次数：
```sql
SELECT status, COUNT(status) AS PV GROUP BY status
```

对于 ISO 8601 类型的时间格式（2019-09-29T20:24:57+08:00），可以通过 CAST 转换成 TIMESTAMP 类型，再结合HISTOGRAM 函数，对时间粒度进行聚合，统计每分钟的请求数：

```sql
SELECT HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, COUNT(1) AS pv GROUP BY dt
```

#### GROUP BY 多列

统计每分钟粒度下，不同请求类型的访问次数：
```sql
SELECT HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, COUNT(1) AS pv, method GROUP BY dt, method
```
