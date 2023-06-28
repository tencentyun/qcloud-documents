## 概述

日志检索分析支持以下 SQL 语法：
- SELECT 语法
- AS 语法
- LIMIT 语法
- WHERE 语法
- ORDER BY 语法
- GROUP BY 语法
- HAVING 语法
- 嵌套子查询

## SELECT 语法

用于从访问日志表中查询数据，查询表只能为`cos_standard_log`或者 `cos_standard_log`的子表。

#### 语法格式
```
SELECT 列名 FROM cos_standard_log
```

#### 示例1：选取指定列
```
SELECT eventTime, reqPath, reqMethod FROM cos_standard_log
```
#### 示例2：选取所有列
```
SELECT * FROM cos_standard_log
```
#### 示例3：使用表达式生成新的列
```
SELECT toInt64OrZero(resBytesSent)/toInt64OrZero(resTotalTime) AS rate FROM cos_standard_log
```


	
	
## AS 语法
用于为列名指定别名。

#### 语法格式
```
SELECT 列名 AS 别名 FROM cos_standard_log
```
#### 示例：为日志字段重命名
```
SELET remoteIp AS ip FROM cos_standard_log
```


### 关于列名

1. 日志表的原始列名和日志字段一致，COS 的日志查询支持用户通过 AS 语法为查询得到的数据自定义列名。
2. 自定义列名必须由字母开头，仅支持包含字符、数字、下划线`_`。
3. 建议使用字符``包裹中文或保留字段，作为自定义列名，避免查询失败。如您需要查阅完整的保留字段列表，请参见 [保留字段](https://cloud.tencent.com/document/product/436/94358)。

#### 示例1：使用保留字段`Date`作为列名
```
SELECT eventTime AS `Date` from cos_standard_log
```
#### 示例2：使用中文`日期`作为列名
以下 SQL 示例使用了双引号包裹中文作为自定义字段，查询会执行成功。
```
SELECT eventTime AS `日期` FROM cos_standard_log
```





## LIMIT 语法
用于限制结果的输出条数。

#### 语法格式
```
LIMIT N
```
#### 示例：仅输出前10条日志
```
SELECT * FROM cos_standard_log LIMIT 10
```

### 限制
1. 日志查询的结果最多返回1000条。
2. 即使 SQL Query 语句中的 LIMIT 值若超过1000，返回的结果也不会超过1000条。

## WHERE 语法
用于限制查询条件。

#### 语法格式
```
SELECT 列名 WHERE 列名 运算符 值
```
支持的运算符请参见 [运算符](https://cloud.tencent.com/document/product/436/94356)。

#### 示例1：查询所有状态码非 200 的日志
```
SELECT * FROM cos_standard_log WHERE resErrorCode != '200'
```
#### 示例2：查询删除指定文件的日志
```
SELECT * FROM cos_standard_log WHERE eventName = 'DELETEObject' AND reqPath = '/folder1/temp.txt'
```

## ORDER BY 语法
用于根据指定列名对分析结果排序。

#### 语法格式	
```
ORDER BY 列名 [DESC | ASC]
```
支持指定多个列名、分别根据升序（ASC）或降序（DESC）排序。例如 `ORDER BY 列名1[DESC | ASC]，列名2[DESC | ASC]`。不指定 DESC 或 ASC，默认按升序排列。

#### 示例1：统计不同请求状态的数量，并按照请求数量降序排列
```
SELECT resHttpCode, COUNT(*) AS pv FROM cos_standard_log GROUP BY resHttpCode ORDER BY pv DESC
```
#### 示例2：将日志按照指定时间排列
```
SELECT * FROM cos_standard_log ORDER BY timestamp
```

## GROUP BY 语法
GROUP BY 支持结合聚合函数进行分组统计。

#### 语法格式
```
SELECT 列名, 聚合函数 FROM cos_standard_log WHERE GROUP BY [ 列名 | 别名 ]
```
其中列名用于分组、聚合函数的日志字段（列），支持多列。使用了 GROUP BY 语法后，执行 SELECT 语句时，只能选择 GROUP BY 的列或聚合计算函数，不允许选择非 GROUP BY 的列。

以下语句不合法，因为 timestamp 不是 GROUP BY 的列。
```
SELECT resHttpCode,timestamp, COUNT(*) AS pv FROM cos_standard_log GROUP BY resHttpCode
```
- 别名：支持根据列的别名进行分组、使用聚合函数。
- 聚合函数：GROUP BY 支持与 MIN、MAX、AVG、SUM、COUNT 等 [聚合函数](https://cloud.tencent.com/document/product/436/94355#.E8.81.9A.E5.90.88.E5.87.BD.E6.95.B0) 一起使用。

#### 示例1：统计不同状态码的访问次数
```
SELECT resHttpCode, count(*) AS pv FROM cos_standard_log GROUP BY resHttpCode
```
#### 示例2：按分钟粒度统计访问次数
```
SELECT date_trunc('minute', toDateTime(timestamp)) AS time, count(*) AS pv FROM cos_standard_log GROUP BY time ORDER BY time ASC
```
#### 示例3：按5分钟粒度统计访问次数
```
//方案一
SELECT timestamp-timestamp%300 as time, COUNT(*) as pv FROM cos_standard_log GROUP BY time ORDER BY time

//方案二
SELECT toStartOfFiveMinutes(toDateTime(timestamp)) as time, COUNT(*) as pv FROM cos_standard_log GROUP BY time ORDER BY time
```

## HAVING 语法
HAVING 用于对分组聚合后（GROUP BY）的数据进行过滤。

#### 语法格式
```
SELECT 列名, 聚合函数 FROM cos_standard_log GROUP BY 列名 HAVING 聚合函数 运算符 值
```
支持的运算符请参见 [运算符] (https://cloud.tencent.com/document/product/436/94356)。

#### 示例：统计平均响应延时大于1秒的对象。
```
SELECT avg(toInt64OrZero(resTotalTime)) as latency, requestUri FROM cos_standard_log GROUP BY requestUri HAVING latency > 1000 ORDER BY latency DESC
```

## 嵌套子查询
嵌套查询用于一些比较复杂的分析场景。在一个 SELECT 语句中嵌套另一个 SELECT 语句，将前一次对查询分析的结果作为第二次分析的输入。

>!日志检索分析的嵌套子查询最多支持3层嵌套。


#### 语法格式
```
SELECT key FROM (subquery)
```
- subquery：子查询，需要被包裹在括号中。注意，subquery 的查询表必须为`cos_standard_log`或查询`cos_standard_log`的另一个子查询。
- key：subquery 结果中的字段。


#### 示例：统计请求 QPS
```
SELECT second,
         cnt
FROM 
    (SELECT toStartOfInterval(toDateTime(timestamp),
         toIntervalSecond(1)) AS second,
         count() AS cnt
    FROM cos_standard_log
    GROUP BY  second )
ORDER BY  second ASC
WITH FILL STEP toIntervalSecond(1)
```
