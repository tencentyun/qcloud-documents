本文介绍 GROUP BY 使用语法和示例。

GROUP BY 语法用于结合聚合函数，根据一个或多个列对分析结果进行分组。

## 语法格式

```
* | SELECT 列名, 聚合函数 GROUP BY [ 列名 | 别名 | 序号 ]
```

>? 在 SQL 语句中，如果您使用了 GROUP BY 语法，则在执行 SELECT 语句时，只能选择 GROUP BY 的列或聚合计算函数，不允许选择非 GROUP BY 的列。例如 `* | SELECT status, request_time, COUNT(*) AS PV GROUP BY status` 为非法分析语句，因为 **request_time** 不是 GROUP BY 的列。
>

GROUP BY语法支持按照列名、别名或序号进行分组，详细说明如下表所示：

| 参数     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| 列名     | 列名即为日志字段名称或聚合函数计算结果列，即支持按照日志字段名称（KEY）或聚合函数计算结果列进行分组。GROUP BY 语法支持单列或多列。 |
| 别名     | 按照日志字段或聚合函数计算结果的别名进行分组。<br/>您可以在字段索引中配置日志字段的别名。 |
| 序号     | 某列在 SELECT 语句中的序号（从1开始）。<br>例如 status 列的序号为1，所以下面两个语句为等同关系。<ul  style="margin: 0;"><li>`* \|SELECT status, count(*) AS PV GROUP BY status`</li><li>`* \|SELECT status, count(*) AS PV GROUP BY 1` </li></ul>|
| 聚合函数 | GROUP BY 语法常与 MIN、MAX、AVG、SUM、COUNT 等聚合函数搭配使用。更多信息请参见 [聚合函数](https://cloud.tencent.com/document/product/614/60028)。 |


## 示例

- 统计不同状态码的访问次数。
```
* | SELECT status, count(*) AS pv GROUP BY status
```
![image-20210718231331787](https://main.qcloudimg.com/raw/d0b7922c03cf0937b4d611deccdf0ce9.png)
- 按照每分钟的时间粒度，计算 PV。
```
* | SELECT date_trunc('minute', cast(__TIMESTAMP__ as timestamp)) AS dt, count(*) AS pv GROUP BY dt ORDER BY dt limit 10                             
```
\_\_TIMESTAMP\_\_ 字段为日志服务中的保留字段，表示时间列。**dt**为 date_trunc('minute', cast(\_\_TIMESTAMP\_\_ as timestamp)) 的别名。date_trunc() 函数的更多信息，请参见 [时间截断函数](https://cloud.tencent.com/document/product/614/58981#.E6.97.B6.E9.97.B4.E6.88.AA.E6.96.AD.E5.87.BD.E6.95.B0)。
![image-20210718230110351](https://main.qcloudimg.com/raw/b4e1afcc9b64191e76600d190fd61922.png)
>?
> - limit 10表示最多获取10行结果。如果不使用 LIMIT 语法，则默认获取100行结果。
> - 在索引配置中，当您开启任意字段的统计功能后，日志服务会自动开启 \_\_TIMESTAMP\_\_ 字段的统计功能。
> 
- 按照每5分钟的时间粒度，计算 PV。
因为 date_trunc() 函数只能按照固定时间间隔统计，可以使用 histogram 函数进行自定义时间间隔统计。
例如，下述语句中表示按照每5分钟的时间粒度进行取模对齐。
```
* | SELECT histogram(cast(__TIMESTAMP__ as timestamp),interval 5 minute) as dt, count(*) as pv,count(distinct(remote_addr)) as uv group by dt order by dt
```
![image-20210719173252866](https://main.qcloudimg.com/raw/b1bf9e31f1aa826e83af2e94083ef202.png)


