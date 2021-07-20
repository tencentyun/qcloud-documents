本文介绍 histogram 时间分组函数的用法及示例。

日志服务支持按固定时间间隔对日志数据进行分组聚合统计，该函数可用于如统计每5分钟的访问次数等时间数据处理场景。

## 语法格式

```
histogram(__TIMESTAMP__, interval)
```

>?
> - __TIMESTAMP__ 必须使用 TIMESTAMP 类型数据格式，用户可通过 ISO8601 格式的时间字符串或者 UNIX 数值类型的时间转换为 TIMESTAMP 类型。
> - interval 指时间间隔，支持单位为 SECOND（秒）、MINUTE（分）、HOUR（小时）、DAY（天）、MONTH（月）、YEAR（年）。例如时间间隔5分钟，即 INTERVAL 5 MINUTE。
> - 兼容支持以下语法，其中 bigint 为毫秒时间戳，即 \_\_TIMESTAMP\_\_ 字段。
> ```
histogram(bigint, interval)
```



## 示例

统计每5分钟访问次数 PV 值。
```
* | select histogram(cast(__TIMESTAMP__ as timestamp),INTERVAL 5 MINUTE) AS dt, count(*) as PV group by dt order by dt
```
![image-20210719003224086](https://main.qcloudimg.com/raw/13bfe6019fb000314de02acbeb7b68f7.png)


  















