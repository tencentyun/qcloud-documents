本文介绍通用聚合函数的基本语法及示例。

聚合函数是对一组值执行计算并返回计算结果的函数，日志服务支持如下聚合函数：

>? 日志服务分析语句中，表示字符串的字符必须使用单引号（''）包裹，无符号包裹或被双引号（""）包裹的字符表示字段名或列名。例如：**'status'** 表示字符串 status，**status** 或 **"status"** 表示日志字段 status。
>

| 函数语句             | 说明                                              | 示例                                                         |
| -------------------- | ------------------------------------------------- | ------------------------------------------------------------ |
| arbitrary(KEY)       | 随机返回目标列中一个非 NULL 的值。                  | `* | SELECT arbitrary(request_method) AS request_method`     |
| avg(KEY)             | 计算目标列的算数平均值。                          | `* | SELECT AVG(request_time)`                               |
| bitwise_and_agg(KEY) | 返回目标列汇所有值按位与运算（AND）的结果。       | `* | SELECT bitwise_and_agg(status)`                          |
| bitwise_or_agg(KEY)  | 返回目标列汇所有值按位或运算（OR）的结果。        | `* | SELECT bitwise_or_agg(request_length)`                   |
| checksum(KEY)        | 计算目标列的校验和值，返回结果为 BASE 64编码类型。 | `* | SELECT checksum(request_method) AS request_method`       |
| count(\*)             | 表示所有的行数。                                  | `* | SELECT COUNT(*) WHERE http_status >200`                 |
| count(1)             | COUNT(1) 等同于 COUNT(\*)，表示所有的行数。          | `* | SELECT COUNT(1)`                                       |
| count(KEY)           | 计算某一 KEY 列非 NULL 的行数。                   | `* | SELECT COUNT(request_time) WHERE request_time >5.0`    |
| count_if(boolean)        | 统计满足指定条件的日志条数。                      | `* | select count_if(returnCode>=400) as errorCounts`                    |
| geometric_mean(KEY)  | 计算目标列的几何平均数。                          | `* | SELECT geometric_mean(request_time) AS request_time`     |
| max(KEY)             | 查询 KEY 中的最大值。                                 | `* | SELECT MAX(request_time) AS max_request_time`           |
| max_by(x,y)          | 返回 y 为最大值时对应的 x 值。                        | `* | SELECT MAX_BY(request_method, request_time) AS method`     |
| max_by(x,y,n)        | 返回最大的 n 个 y 值对应的 x 值，返回结果为 JSON 数组。   | `* | SELECT max_by(request_method, request_time, 3) AS method` |
| min(KEY)             | 查询 KEY 中最小值。                                   | `* | SELECT MIN(request_time) AS min_request_time`           |
| min_by(x,y)          | 返回 y 为最小值时对应的 x 值。                        | `* | SELECT min_by(request_method, request_time) AS method`   |
| min_by(x,y,n)        | 返回最小的 n 个 y 值对应的 x 值。返回结果为 JSON 数组。   | `* | SELECT min_by(request_method, request_time, 3) AS method` |
| sum(KEY)             | 计算 KEY 的总值。                                     | `* | SELECT SUM(body_bytes_sent) AS sum_bytes`               |



#### 参数说明

| 参数 | 说明                   |
| ---- | ---------------------- |
| KEY    | 表示日志字段名称。           |
| x    | 参数值为任意数据类型。           |
| y    | 参数值为任意数据类型。 |
| n    | 大于0的整数。                   |

