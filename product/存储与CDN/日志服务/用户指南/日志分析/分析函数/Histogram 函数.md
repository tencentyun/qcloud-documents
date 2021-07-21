时间函数支持对日志时间进行格式转换，分组聚合等处理，通常应用于根据日志时间做统计分析的场景。日志服务（Cloud Log Service，CLS）在每条日志中附带日志采集时间，格式为 long 型的毫秒级时间戳`__TIMESTAMP__`（1597807109000）。

## 时间转换函数 cast

| 函数名                           | 作用                                                         | 示例                                                         |
| :------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ |
| `cast(date_string as timestamp)` | 将 long 型或 text 型时间戳转换为`TIMESTAMP 类型`，该数据类型可用于 [时间分组函数 histogram](https://cloud.tencent.com/document/product/614/44065#.E6.97.B6.E9.97.B4.E5.88.86.E7.BB.84.E5.87.BD.E6.95.B0-histogram) 和时间展示 | cast(1597807109000 as timestamp)<br />转换结果：2020-08-19T03:18:29.000Z |

### 参数限制

1. long 型时间戳转换只支持毫秒级，如1597807109000，如果是秒级时间戳或微秒级时间戳，需要进行量级转换。
2. text 型时间戳转换只支持 ISO 8601格式的时间字符串，如：2019-12-25T16:17:01+08:00。

### 场景示例

1. 将日志服务附带的日志采集时间`__TIMESTAMP__`转换为 `TIMESTAMP 类型`。
```plaintext
* | select cast(__TIMESTAMP__ as timestamp)
```
2. 用户日志本身带有 long 型的秒级时间戳，如`time:1597807109`，需要转换为 `TIMESTAMP 类型`。
```
* | select cast(time*1000 as timestamp)
```

## 时间分组函数 histogram

日志服务支持按固定时间间隔对日志数据进行分组聚合统计，该函数可用于如统计每5分钟的访问次数等时间数据处理场景。

### 语法格式

```
histogram(__TIMESTAMP__, interval)
```

>?
> - \_\_TIMESTAMP\_\_ 必须使用 TIMESTAMP 类型数据格式，用户可通过 ISO8601 格式的时间字符串或者 UNIX 数值类型的时间转换为 TIMESTAMP 类型。
> - interval 指时间间隔，支持单位为 SECOND（秒）、MINUTE（分）、HOUR（小时）、DAY（天）、MONTH（月）、YEAR（年）。例如时间间隔5分钟，即 INTERVAL 5 MINUTE。
> - 兼容支持以下语法，其中 bigint 为毫秒时间戳，即 \_\_TIMESTAMP\_\_ 字段。
> ```
histogram(long, interval)
```


### 示例

统计每5分钟访问次数 PV 值。
```
* | select histogram(cast(__TIMESTAMP__ as timestamp),INTERVAL 5 MINUTE) AS dt, count(*) as PV group by dt order by dt
```
![image-20210719003224086](https://main.qcloudimg.com/raw/13bfe6019fb000314de02acbeb7b68f7.png)


  















