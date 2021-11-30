## 数据类型
ClickHouse 支持整数、浮点数、字符型、日期、枚举值和数组等多种数据类型。

### 类型列表
<table>
   <tr>
      <th width=13%>类别</th>
      <th width=17%>名称</th>
      <th width=20%>类型标识</th>
			<th width=70%>数据范围或描述</th>
   </tr>
   <tr>
      <td rowspan="8">整数</td>
      <td>单字节整数</td>
      <td>Int8</td>
			<td>[-128，127]</td>
   </tr>
	 <tr>
      <td>双字节整数</td>
      <td>Int16</td>
			<td>[-32768，32767]</td>
   </tr>
	 <tr>
      <td>四字节整数</td>
      <td>Int32</td>
			<td>[-2147483648，2147483647]</td>
   </tr>
	 <tr>
      <td>八字节整数</td>
      <td>Int64</td>
			<td>[-9223372036854775808，9223372036854775807]</td>
   </tr>
	 <tr>
      <td>无符号单字节整数</td>
      <td>UInt8</td>
			<td>[0，255]</td>
   </tr>
   <tr>
      <td>无符号双字节整数</td>
      <td>UInt16</td>
			<td>[0，65535]</td>
   </tr>
	 <tr>
      <td>无符号四字节整数</td>
      <td>UInt32</td>
			<td>[0，4294967295]</td>
   </tr>
	 <tr>
      <td>无符号八字节整数</td>
      <td>UInt64</td>
			<td>[0，18446744073709551615]</td>
   </tr>
	 <tr>
      <td rowspan="5">浮点数</td>
      <td>单精度浮点数</td>
      <td>Float32</td>
			<td>浮点数有效数字6 - 7位</td>
   </tr>
	 <tr>
      <td>双精度浮点数</td>
      <td>Float64</td>
			<td>浮点数有效数字15 - 16位</td>
   </tr>
	 <tr>
      <td rowspan="3">自定义浮点</td>
      <td>Decimal32(S)</td>
			<td>浮点数有效数字 S，S 取值范围[1，9]</td>
   </tr>
	 <tr>
      <td>Decimal64(S)</td>
      <td>浮点数有效数字 S，S 取值范围[10，18]</td>
   </tr>
	 <tr>
      <td>Decimal128(S)</td>
      <td>浮点数有效数字 S，S 取值范围[19，38]</td>
   </tr>
	 <tr>
      <td rowspan="3">字符型</td>
      <td>任意长度字符</td>
      <td>String</td>
			<td>不限定字符串长度</td>
   </tr>
   <tr>
      <td>固定长度字符</td>
      <td>FixedString(N)</td>
			<td>固定长度的字符串</td>
   </tr>
	 <tr>
      <td>唯一标识 UUID 类型</td>
      <td>UUID</td>
			<td>通过内置函数 generateUUIDv4 生成唯一的标志符</td>
   </tr>
	 <tr>
      <td rowspan="3">时间类型</td>
      <td>日期类型</td>
      <td>Date</td>
			<td>存储年月日时间，格式 yyyy-MM-dd</td>
   </tr>
   <tr>
      <td>时间戳类型（秒级）</td>
      <td>DateTime(timezone)</td>
			<td>Unix 时间戳，精确到秒</td>
   </tr>
	 <tr>
      <td>时间戳类型（自定义）</td>
      <td>DateTime(precision, timezone)</td>
			<td>可以指定时间精度</td>
   </tr>
	 <tr>
      <td rowspan="2">枚举类型</td>
      <td>单字节枚举</td>
      <td>Enum8</td>
			<td>提供[-128，127]共256个值</td>
   </tr>
   <tr>
      <td>双字节枚举</td>
      <td>Enum16</td>
			<td>提供[-32768，32767]共65536个值</td>
   </tr>
	 <tr>
	    <td>数组类型</td>
      <td>数组类型</td>
      <td>Array(T)</td>
			<td>表示由 T 类型组成的数组类型，不推荐使用嵌套数组</td>
   </tr>
</table>

- 可以使用 UInt8 来存储布尔类型，将取值限制为0或1。
- [其他数据类型官方文档](https://clickhouse.tech/)。

### 使用举例
#### 枚举类型应用
存储某站点用户的性别信息。
```
CREATE TABLE user (uid Int16, name String, gender Enum('male'=1, 'female'=2)) ENGINE=Memory;
 
INSERT INTO user VALUES (1, 'Gary', 'male'), (2, 
'Jaco', 'female');
 
# 查询数据
SELECT * FROM user;
 
┌─uid─┬─name─┬─gender─┐
│   1 │ Gary │ male   │
│   2 │ Jaco │ female │
└─────┴──────┴────────┘
 
# 使用CAST函数查询枚举整数值
SELECT uid, name, CAST(gender, 'Int8') FROM user;
 
┌─uid─┬─name─┬─CAST(gender, 'Int8')─┐
│   1 │ Gary │                    1 │
│   2 │ Jaco │                    2 │
└─────┴──────┴──────────────────────┘
```

#### 数组类型应用
某站点记录每天登录用户的 ID，用来分析活跃用户。
```
CREATE TABLE userloginlog (logindate Date, uids Array(String)) ENGINE=TinyLog;
 
INSERT INTO userloginlog VALUES ('2020-01-02', ['Gary', 'Jaco']), ('2020-02-03', ['Jaco', 'Sammie']);
 
# 查询结果
SELECT * FROM userloginlog;
 
┌──logindate─┬─uids──────────────┐
│ 2020-01-02 │ ['Gary','Jaco']   │
│ 2020-02-03 │ ['Jaco','Sammie'] │
└────────────┴───────────────────┘
```

## 创建数据库或表
ClickHouse 使用 CREATE 语句来完成数据库或表的创建。
```
CREATE DATABASE [IF NOT EXISTS] db_name [ON CLUSTER cluster] [ENGINE = engine(...)]
 
CREATE TABLE [IF NOT EXISTS] [db.]table_name [ON CLUSTER cluster]
(
    name1 [type1] [DEFAULT|MATERIALIZED|ALIAS expr1] [compression_codec] [TTL expr1],
    name2 [type2] [DEFAULT|MATERIALIZED|ALIAS expr2] [compression_codec] [TTL expr2],
    ...
) ENGINE = engine
```

数据库和表都支持本地和分布式两种，分布式方式的创建有以下两种方法：
- 在每台 clickhouse-server 所在机器上都执行创建语句。
- 使用 ON CLUSTER 子句，配合 ZooKeeper 服务完成创建动作。

当使用 clickhouse-client 进行查询时，若在 A 机上查询 B 机的本地表则会报错“Table xxx doesn't exist..”。若希望集群内的所有机器都能查询某张表，推荐使用分布式表。

相关官方文档 [CREATE Queries](https://clickhouse.tech/docs/en/query_language/create/)。

## 查询
ClickHouse 使用 SELECT 语句来完成数据查询。
```
SELECT [DISTINCT] expr_list
[FROM [db.]table | (subquery) | table_function] [FINAL]
[SAMPLE sample_coeff]
[GLOBAL] [ANY|ALL] [INNER|LEFT|RIGHT|FULL|CROSS] [OUTER] JOIN (subquery)|table USING columns_list
[PREWHERE expr]
[WHERE expr]
[GROUP BY expr_list] [WITH TOTALS]
[HAVING expr]
[ORDER BY expr_list]
[LIMIT [offset_value, ]n BY columns]
[LIMIT [n, ]m]
[UNION ALL ...]
[INTO OUTFILE filename]
[FORMAT format]
```

相关官方文档 [SELECT Queries Syntax](https://clickhouse.tech/docs/en/query_language/select/)。

## 批量写入
ClickHouse 使用 INSERT INTO 语句来完成数据写入。

```
INSERT INTO [db.]table [(c1, c2, c3)] VALUES (v11, v12, v13), (v21, v22, v23), ...
 
INSERT INTO [db.]table [(c1, c2, c3)] SELECT ...
```

相关官方文档 [INSERT](https://clickhouse.tech/docs/en/query_language/insert_into/)。

## 删除数据
ClickHouse 使用 DROP 或 TRUNCATE 语句来完成数据删除。
>?DROP 删除元数据和数据，TRUNCATE 只删除数据。

```
DROP DATABASE [IF EXISTS] db [ON CLUSTER cluster]
DROP [TEMPORARY] TABLE [IF EXISTS] [db.]name [ON CLUSTER cluster]
 
TRUNCATE TABLE [IF EXISTS] [db.]name [ON CLUSTER cluster]
```

## 修改表结构
ClickHouse 使用 ALTER 语句来完成表结构修改。
```
# 对表的列操作
ALTER TABLE [db].name [ON CLUSTER cluster] ADD COLUMN [IF NOT EXISTS] name [type] [default_expr] [codec] [AFTER name_after]
ALTER TABLE [db].name [ON CLUSTER cluster] DROP COLUMN [IF EXISTS] name
ALTER TABLE [db].name [ON CLUSTER cluster] CLEAR COLUMN [IF EXISTS] name IN PARTITION partition_name
ALTER TABLE [db].name [ON CLUSTER cluster] COMMENT COLUMN [IF EXISTS] name 'comment'
ALTER TABLE [db].name [ON CLUSTER cluster] MODIFY COLUMN [IF EXISTS] name [type] [default_expr] [TTL]
 
# 对表的分区操作
ALTER TABLE table_name DETACH PARTITION partition_expr
ALTER TABLE table_name DROP PARTITION partition_expr
ALTER TABLE table_name CLEAR INDEX index_name IN PARTITION partition_expr
 
# 对表的属性操作
ALTER TABLE table-name MODIFY TTL ttl-expression
```

相关官方文档 [ALTER](https://clickhouse.tech/docs/en/query_language/alter/)。

## 查看信息
- SHOW 语句
展现数据库、处理列表、表、字典等信息。
```
SHOW DATABASES [INTO OUTFILE filename] [FORMAT format]
SHOW PROCESSLIST [INTO OUTFILE filename] [FORMAT format]
SHOW [TEMPORARY] TABLES [{FROM | IN} <db>] [LIKE '<pattern>' | WHERE expr] [LIMIT <N>] [INTO OUTFILE <filename>] [FORMAT <format>]
SHOW DICTIONARIES [FROM <db>] [LIKE '<pattern>'] [LIMIT <N>] [INTO OUTFILE <filename>] [FORMAT <format>]
```
相关官方文档 [SHOW Queries](https://clickhouse.tech/docs/en/query_language/show/)。
- DESCRIBE 语句
查看表的元数据信息。
```
DESC|DESCRIBE TABLE [db.]table [INTO OUTFILE filename] [FORMAT format]
```

## 函数
ClickHouse 函数有两种类型：常规函数和聚合函数，区别是常规函数可以通过一行数据产生结果，聚合函数则需要一组数据来产生结果。

### 常规函数
#### 算数函数

数据表中各字段参与数学计算函数。

| 函数名称              | 用途               | 使用场景                             |
| --------------------- | ------------------ | ------------------------------------ |
| plus(a, b), a + b     | 计算两个字段的和   | plus(table.field1, table.field2)     |
| minus(a, b), a - b    | 计算两个字段的差   | minus(table.field1, table.field2)    |
| multiply(a, b), a * b | 计算两个字段的积   | multiply(table.field1, table.field2) |
| divide(a, b), a / b   | 计算两个字段的商   | divide(table.field1, table.field2)   |
| modulo(a, b), a % b   | 计算两个字段的余数 | modulo(table.field1, table.field2)   |
| abs(a)                | 取绝对值           | abs(table.field1)                    |
| negate(a)             | 取相反数           | negate(table.field1)                 |

#### 比较函数

| 函数名称 | 用途             | 使用场景              |
| -------- | ---------------- | --------------------- |
| =, ==    | 判断是否相等     | table.field1 = value  |
| !=, <>   | 判断是否不相等   | table.field1 != value |
| >        | 判断是否大于     | table.field1 > value  |
| >=       | 判断是否大于等于 | table.field1 >= value |
| <        | 判断是否小于     | table.field1 < value  |
| <=       | 判断是否小于等于 | table.field1 <= value |

#### 逻辑运算函数

| 函数名称 | 用途                 | 使用场景 |
| -------- | -------------------- | -------- |
| AND      | 两个条件都必须满足   | -        |
| OR       | 两个条件满足其中之一 | -        |
| NOT      | 取条件判断的相反     | -        |

#### 类型转换函数

转换函数可能会溢出，溢出后的数字与C语言中数据类型保持一致。

| 函数名称                    | 用途                                    | 使用场景                      |
| --------------------------- | --------------------------------------- | ----------------------------- |
| toInt(8\|16\|32\|64)        | 将字符型转化为整数型                    | toInt8('128') 结果为-127      |
| toUInt(8\|16\|32\|64)       | 将字符型转化为无符号整数型              | toUInt8('128') 结果为128      |
| toInt(8\|16\|32\|64)OrZero  | 将整数字符型转化为整数型，异常时返回0    | toInt8OrZero('a') 结果为0     |
| toUInt(8\|16\|32\|64)OrZero | 将整数字符型转化为整数型，异常时返回0    | toUInt8OrZero('a') 结果为0    |
| toInt(8\|16\|32\|64)OrNull  | 将整数字符型转化为整数型，异常时返回NULL | toInt8OrNull('a') 结果为 NULL  |
| toUInt(8\|16\|32\|64)OrNull | 将整数字符型转化为整数型，异常时返回NULL | toUInt8OrNull('a') 结果为 NULL |

浮点数类型或日期类型也有上述类似的函数。

相关官方文档 [Type Conversion Functions](https://clickhouse.tech/docs/en/query_language/functions/type_conversion_functions/)。

#### 日期函数
相关官方文档 [Functions for working with dates and times](https://clickhouse.tech/docs/en/query_language/functions/date_time_functions/)。

#### 字符串函数
相关官方文档 [Functions for working with strings](https://clickhouse.tech/docs/en/query_language/functions/string_functions/)。

#### UUID
相关官方文档 [Functions for working with UUID](https://clickhouse.tech/docs/en/query_language/functions/uuid_functions/)。

#### JSON 处理函数
相关官方文档 [Functions for working with JSON](https://clickhouse.tech/docs/en/query_language/functions/json_functions/)。

### 聚合函数

| 函数名称                | 用途                                     | 使用场景                                  |
| -------------------------------- | -------------------------------------- | --------------------------------------------- |
| count                                                        | 统计行数或者非 NULL 值个数                                     | count(expr)、COUNT(DISTINCT expr)、count()、count(\*)         |
| [any(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-any) | 返回第一个遇到的值，结果不确定                               | any(column)                                                  |
| [anyHeavy(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#anyheavyx) | 基于 heavy hitters 算法，返回经常出现的值。通常结果不确定 | anyHeavy(column)                                             |
| [anyLast(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#anylastx) | 返回最后一个遇到的值，结果不确定                             | anyLast(column)                                              |
| [groupBitAnd](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupbitand) | 按位与                                                       | groupBitAnd(expr)                                            |
| [groupBitOr](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupbitor) | 按位或                                                       | groupBitOr(expr)                                             |
| [groupBitXor](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupbitxor) | 按位异或                                                     | groupBitXor(expr)                                            |
| [groupBitmap](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupbitmap) | 求基数（cardinality）                                        | groupBitmap(expr)                                            |
| [min(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-min) | 求最小值                                                     | min(column)                                                  |
| [max(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-max) | 求最大值                                                     | max(x)                                                       |
| [argMin(arg, val)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg-function-argmin) | 返回 val 最小值行的 arg 的值                                     | argMin(c1, c2)                                               |
| [argMax(arg, val)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg-function-argmax) | 返回 val 最大值行的 arg 的值                                     | argMax(c1, c2)                                               |
| [sum(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-sum) | 求和                                                         | sum(x)                                                       |
| [sumWithOverflow(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#sumwithoverflowx) | 求和，结果溢出则返回错误                                     | sumWithOverflow(x)                                           |
| [sumMap(key, value)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_functions-summap) | 用于数组类型，对相同 key 的 value 求和，返回两个数组的 tuple，第一个为排序后的 key，第二个为对应 key 的 value 之和 | -                                                            |
| [skewPop](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#skewpop) | 求 [偏度](https://en.wikipedia.org/wiki/Skewness)             | skewPop(expr)                                                |
| [skewSamp](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#skewsamp) | 求 [样本偏度](https://en.wikipedia.org/wiki/Skewness)         | skewSamp(expr)                                               |
| [kurtPop](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#kurtpop) | 求 [峰度](https://en.wikipedia.org/wiki/Kurtosis)             | kurtPop(expr)                                                |
| [kurtSamp](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#kurtsamp) | 求 [样本峰度](https://en.wikipedia.org/wiki/Kurtosis)         | kurtSamp(expr)                                               |
| [timeSeriesGroupSum(uid, timestamp, value)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg-function-timeseriesgroupsum) | 对 uid 分组的时间序列对应时间点求和，求和前缺失的时间点线性插值 | -                                                            |
| [timeSeriesGroupRateSum(uid, ts, val)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg-function-timeseriesgroupratesum) | 对 uid 分组的时间序列对应时间点的变化率求和                    | -                                                            |
| [avg(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-avg) | 求平均值                                                     | -                                                            |
| [uniq](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-uniq) | 计算不同值的近似个数                                         | uniq(x[, ...])                                               |
| [uniqCombined](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-uniqcombined) | 计算不同值的近似个数，相比uniq消耗的内存更少，精度更高，但是性能稍差 | uniqCombined(HLL_precision)(x[, ...])、uniqCombined(x[, ...]) |
| [uniqCombined64](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-uniqcombined64) | uniqCombined 的 64bit 版本，结果溢出的可能性降低                | -                                                            |
| [uniqHLL12](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-uniqhll12) | 计算不同值的近似个数，不建议使用。请用 uniq、uniqCombined     | -                                                            |
| [uniqExact](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-uniqexact) | 计算不同值的精确个数                                         | uniqExact(x[, ...])                                          |
| [groupArray(x), groupArray(max_size)(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-grouparray) | 返回 x 取值的数组，数组大小可由 max_size 指定                    | -                                                            |
| [groupArrayInsertAt(value, position)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#grouparrayinsertatvalue-position) | 在数组的指定位置 position 插入值 value                          | -                                                            |
| [groupArrayMovingSum](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-grouparraymovingsum) | -                                                            | -                                                            |
| [groupArrayMovingAvg](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_function-grouparraymovingavg) | -                                                            | -                                                            |
| [groupUniqArray(x), groupUniqArray(max_size)(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupuniqarrayx-groupuniqarraymax-sizex) | -                                                            | -                                                            |
| [quantile](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantile) | -                                                            | -                                                            |
| [quantileDeterministic](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantiledeterministic) | -                                                            | -                                                            |
| [quantileExact](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantileexact) | -                                                            | -                                                            |
| [quantileExactWeighted](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantileexactweighted) | -                                                            | -                                                            |
| [quantileTiming](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantiletiming) | -                                                            | -                                                            |
| [quantileTimingWeighted](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantiletimingweighted) | -                                                            | -                                                            |
| [quantileTDigest](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantiletdigest) | -                                                            | -                                                            |
| [quantileTDigestWeighted](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantiletdigestweighted) | -                                                            | -                                                            |
| [median](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#median) | -                                                            | -                                                            |
| [quantiles(level1, level2, …)(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#quantiles) | -                                                            | -                                                            |
| [varSamp(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#varsampx) | -                                                            | -                                                            |
| [varPop(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#varpopx) | -                                                            | -                                                            |
| [stddevSamp(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#stddevsampx) | -                                                            | -                                                            |
| [stddevPop(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#stddevpopx) | -                                                            | -                                                            |
| [topK(N)(x)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#topknx) | -                                                            | -                                                            |
| [topKWeighted](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#topkweighted) | -                                                            | -                                                            |
| [covarSamp(x, y)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#covarsampx-y) | -                                                            | -                                                            |
| [covarPop(x, y)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#covarpopx-y) | -                                                            | -                                                            |
| [corr(x, y)](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#corrx-y) | -                                                            | -                                                            |
| [categoricalInformationValue](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#categoricalinformationvalue) | -                                                            | -                                                            |
| [simpleLinearRegression](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#simplelinearregression) | -                                                            | -                                                            |
| [stochasticLinearRegression](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_functions-stochasticlinearregression) | -                                                            | -                                                            |
| [stochasticLogisticRegression](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#agg_functions-stochasticlogisticregression) | -                                                            | -                                                            |
| [groupBitmapAnd](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupbitmapand) | -                                                            | -                                                            |
| [groupBitmapOr](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupbitmapor) | -                                                            | -                                                            |
| [groupBitmapXor](https://clickhouse.tech/docs/en/query_language/agg_functions/reference/#groupbitmapxor) | -                                                            | -                                                            |

## 字典
一个字典是一个映射（key -> attributes），能够作为函数被用于查询，相比引用（reference）表`JOIN`的方式更简单和高效。数据字典有两种，一个是内置字典，另一个是外置字典。

### 内置字典
ClickHouse 支持一种 [内置字典](https://clickhouse.tech/docs/en/query_language/dicts/internal_dicts/) geobase，支持的函数可参考 [Functions for working with Yandex.Metrica dictionaries](https://clickhouse.tech/docs/en/query_language/functions/ym_dict_functions/)。

### 外置字典
ClickHouse 可以从多个数据源添加 [外置字典](https://clickhouse.tech/docs/en/query_language/dicts/external_dicts/)，支持的数据源可参考 [Sources Of External Dictionaries](https://clickhouse.tech/docs/en/query_language/dicts/external_dicts_dict_sources/)。

