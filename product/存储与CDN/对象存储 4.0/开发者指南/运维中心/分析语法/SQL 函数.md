
>!对于日志检索分析，部分 SQL 函数都是英文大小写敏感的，使用时注意函数名的大小写正确，否则可能导致查询失败，详情请参见 [保留字段](https://cloud.tencent.com/document/product/436/94358)。

<span id="聚合函数"></span>
## 聚合函数
日志查询支持以下聚合函数。

|函数名|参数类型|别名|返回类型|
|----|----|----|----|
|count()|支持不传入参数、传入`*`、或传入一个表达式|COUNT, Count|UInt64|
|min()|整型、浮点型、Boolean、String、DateTime|MIN, Min|和入参类型相同|
|max()|整型、浮点型、Boolean、String、DateTime|MAX, Max|和入参类型相同|
|sum()|整型、浮点型、Boolean|SUM, Sum|和入参类型相同|
|avg()|整型、浮点型|AVG, Avg|Double|


#### 示例1：使用 COUNT 统计指定文件的请求次数
```
SELECT count() FROM cos_standard_log WHERE reqPath='/temp.txt'
SELECT COUNT(*) FROM cos_standard_log WHERE reqPath='/temp.txt'
SELECT Count(reqPath) FROM cos_standard_log WHERE reqPath='/temp.txt'
```

#### 示例2：请求指定文件的最大请求时延
```
SELECT max(toInt64OrZero(resTotalTime)) FROM cos_standard_log WHERE reqPath='/temp.txt'
SELECT MAX(toInt64OrZero(resTotalTime)) FROM cos_standard_log WHERE reqPath='/temp.txt'
SELECT Max(toInt64OrZero(resTotalTime)) FROM cos_standard_log WHERE reqPath='/temp.txt'
```

#### 示例3：请求指定文件的最小请求时延
```
SELECT min(toInt64OrZero(resTotalTime)) FROM cos_standard_log WHERE reqPath='/temp.txt'
SELECT MIN(toInt64OrZero(resTotalTime)) FROM cos_standard_log WHERE reqPath='/temp.txt'
SELECT Min(toInt64OrZero(resTotalTime)) FROM cos_standard_log WHERE reqPath='/temp.txt'
```

## 字符串函数
日志查询支持以下字符串函数，入参都是字符串（String）。
>!
>- 字符串必须通过单引号包裹(例如`'Hello World'`)，无符号包裹表示列名。
>- 字符串内需要使用单引号`'`时，可以使用两个单引号`''`表示。例如`'it''s blue.'`表示原始字符串`it's blue.`。
>- 字符串内本身包含双引号`"`时无需特殊处理。

### 判断字符串空或有值
- `empty(s)`：判断字符串是否为空，返回类型为Boolean，1或0。
- `notEmpty(s)`：判断字符串是否有值，返回类型为Boolean，1或0。

示例：
```
empty('') --- 1
notEmpty('text')` --- 1
```

### 计算字符串长度
- `length(s)`：返回字符串的字节长度，结果类型是 UInt64。
- `char_length(s)`、`CHAR_LENGTH(s)`、`character_length(s)`、`CHARACTER_LENGTH(s)`：假定字符串以UTF-8编码组成的文本，返回此字符串的Unicode字符长度，结果类型是UInt64。

示例：
```
length('中文') --- 6
length('text') --- 4

char_length('中文') --- 2
CHAR_LENGTH('中文') --- 2
character_length('text') --- 4
CHARACTER_LENGTH('text') --- 4
```
### 大小写转换
- `lower(s)`,`lcase(s)`：将字符串中的 ASCII 大写字母转换为小写
- `uppper(s)`,`ucase(s)`：将字符串中的 ASCII 小字母转换为大写

示例：
```
lower('ABC') --- 'abc'
lcase('ABC') --- 'abc'
upper('abc') --- 'ABC'
ucase('abc') --- 'ABC'
```

### 截取字符串
- `substring(s,offset,length)`：以字节为单位截取指定位置字符串，返回以offset位置为开头，长度为length的子串。offset从1开始（与标准SQL相同）。offset和length参数必须是常量。
- `substringUTF8(s,offset,length)`：与 substring 相同，但其操作单位为Unicode字符，函数假设字符串是以UTF-8进行编码的文本。例如，需要对中文字符串进行截取，建议使用此函数。

示例：
```
substring('text',2,2) --- 'ex'
substringUTF8('text',2,2) --- 'ex'
substringUTF8('中文',2,1) --- '文'
```

### trim
用于删除字符串首字符前或末字符后的指定字符。默认删除字符为`' '`。

函数格式如下：
```
trim([[LEADING or TRAILING or BOTH] trim_character FROM] input_string)
```
- input_string：要被删除字符的字符串。
- trim_character：要删除的字符，默认为`' '`。若指定了此字段，必须同时指定 LEADING 或 TRAILING 或 BOTH。
- LEADING：删除首字符前。若指定了此字段，必须同时指定 trime_character。
- TRAILING：删除末字符后。若指定了此字段，必须同时指定 trime_character。
- BOTH：删除首字符前及末字符后。若指定了此字段，必须同时指定 trime_character。

示例：
```
trim('       foobar         ') --- 'foobar'
trim('      \tfoobar\t         ') --- '\tfoobar\t'
trim(LEADING ' ' FROM '       foobar         ') --- 'foobar         '
trim(TRAILING ' ' FROM '       foobar         ')` -- 'foobar         '
TRIM(BOTH ' ' FROM '       foobar         ') --- 'foobar'
TRIM(BOTH '12' FROM '1112211foobar22211122') --- 'foobar'
```

### extract
使用正则表达式（pattern）提取字符串的一部分。如果字符串无法匹配正则表达式，则将返回一个空字符串。

函数格式如下：
```
extract(s,pattern)
```
- s：输入字符串
- pattern：正则表达式，String。

示例：
```
SELECT extract('/aaa/2', '\/[^\/]+\/*') FROM cos_standard_log --- '/aaa/'
SELECT extract('/temp.txt', '\/[^\/]+\/*') FROM cos_standard_log --- '/temp.txt'
```

### position
在字符串中查找子串的位置。
函数格式如下：
```
position(s, needle[, start_pos])
```
- s：输入字符串
- needle：要查找的子串
- start_post：start_pos 表示从字符串的指定位置开始查找。不指定该参数，则默认从位置从1开始计数。

示例：
```
position('Hello, world!', '!') --- 13
position('Hello, world!', 'o', 1) --- 5
position('Hello, world!', 'o', 7) --- 9
```
>!
>- 字符串位置统一从1开始计数，而不是0。

### match
检查字符串是否与正则表达式匹配。匹配则返回1，不匹配则返回0。

函数格式如下：
```
match(s, pattern)
```
- s：输入字符串。
- pattern：正则表达式，String。
>?
>- 对于简单的正则表达式，可以使用 LIKE 进行匹配。
>- 反斜杠（\）在正则表达式中用于转义。由于字符串中采用相同的符号来进行转义。因此，为了在正则表达式中匹配转义符号，必须在字符串文字中写入两个反斜杠（\）。

示例：
```
match('123', '^[0-9]*$') --- 1
match('2022-10-01', '^\d{4}-\d{1,2}-\d{1,2}') --- 1
match('/abc/temp.txt','^.*\.txt$') --- 1
```


## 日期和时间函数
日志查询支持以下日期和时间函数，适用类型为 DateTime 和 Date。
>!
>- 日志字段中 timestamp 存储为 Int64 类型，表示 UTC 时间的整秒时间戳，例如`1668162269`。先使用`toDateTime(timestamp)`将该字段转换为DateTime类型，即可使用日期和时间函数。
>- 日志字段中 eventTime 存储为 String 类型，记录了 UTC 时间下 iso 8601时间格式的字符串，例如`'2018-12-01T110233Z'`，先使用 `parseDateTimeBestEffort(eventTime)`将该字段转换为DateTime类型，即可使用以下日期和时间函数
>- toDate 和 toDateTime 同样支持将字符串转换为日期，但这两个函数仅支持标准格式的日期字符串，如`'2021-04-21 10:20:30'`。如需要解析特殊格式的日期字符串，建议使用 parseDateTimeBestEffort。

### 从日期中提取年、月、日、时、分、秒等

#### 提取年份
提取日期中的年份，返回一个整数。
函数格式如下：
```
toYear(time)
YEAR(time)
```

示例：
```
toYear(toDateTime('2021-04-21 10:20:30')) --- 2021
YEAR(toDateTime('2021-04-21 10:20:30')) --- 2021
```

#### 提取季度
提取日期中的季度，返回一个整数（1～4）。

函数格式如下：
```
toQuarter(time)
QUARTER(time)
```

示例：
```
toQuarter(toDateTime('2021-04-21 10:20:30')) --- 2
QUARTER(toDateTime('2021-04-21 10:20:30')) --- 2
```

#### 提取月份
提取日期中的月份，返回一个整数（1～12）。

函数格式如下：
```
toMonth(time)
MONTH(time)
```

示例：
```
toMonth(toDateTime('2021-04-21 10:20:30')) --- 4
MONTH(toDateTime('2021-04-21 10:20:30')) --- 4
```

#### 提取年天数
计算当前日期（time）为当年的第几天，返回一个整数（1～366）。

函数格式如下：
```
toDayOfYear(time)
DAYOFYEAR(time)
```

示例：
```
toDayOfYear(toDateTime('2021-01-31 10:20:30')) --- 31
DAYOFYEAR(toDateTime('2021-01-31 10:20:30')) --- 31
```

#### 提取月天数
计算当前日期（time）为当月的第几天，返回一个整数（1～31）。

函数格式如下：
```
toDayOfMonth(time)
DAYOFMONTH(time)
DAY(time)
```
示例：
```
toDayOfMonth(toDateTime('2021-01-31 10:20:30')) --- 31
DAYOFMONTH(toDateTime('2021-01-31 10:20:30')) --- 31
DAY(toDateTime('2021-01-31 10:20:30')) --- 31
```

#### 6. 提取周天数
计算当前日期（time）是周几，返回一个整数（1～7，周日为7）。

函数格式如下：
```
toDayOfWeek(time)
DAYOFWEEK(time)
```
示例：
```
toDayOfWeek(toDateTime('2023-01-31 10:20:30')) --- 2
DAYOFWEEK(toDateTime('2023-01-31 10:20:30')) --- 2
```

#### 提取小时数
获取当前时间（time）的小时数，返回一个整数（0～23）。

函数格式如下：
```
toHour(time)
HOUR(time)
```
示例：
```
toHour(toDateTime('2023-01-31 10:20:30')) --- 10
HOUR(toDateTime('2023-01-31 10:20:30')) --- 10
```

#### 提取分钟数
获取当前时间（time）的分钟数，返回一个整数（0～59）。

函数格式如下：
```
toMinute(time)
MINUTE(time)
```
示例：
```
toMinute(toDateTime('2023-01-31 10:20:30')) --- 20
MINUTE(toDateTime('2023-01-31 10:20:30')) --- 20
```

#### 提取秒数
获取当前时间的（time）的秒数，返回一个整数（0～59）。

函数格式如下：
```
toSecond(time)
SECOND(time)
```
示例：
```
toSecond(toDateTime('2023-01-31 10:20:30')) --- 30
SECOND(toDateTime('2023-01-31 10:20:30')) --- 30
```


### 将日期或日期时间向前取整

#### 取整函数
以下为年、季度、月、周、天、整时、整分的向前取整函数。

|函数名|说明|
|---|---|
|toStartOfYear(time)|将 Date 或 DateTime 向前取整到本年的第一天。 返回 Date 类型。|
|toStartOfQuarter(time)|将 Date 或 DateTime 向前取整到本季度的第一天。 返回 Date 类型。|
|toStartOfMonth(time)|将 Date 或 DateTime 向前取整到本月的第一天。 返回 Date 类型。|
| toMonday |将 Date 或 DateTime 向前取整到本周的星期一。 返回 Date 类型。|
|toStartOfDay|将 DateTime 向前取整到今天的开始。|
| toStartOfHour |将 DateTime 向前取整到当前小时的开始。|
| toStartOfMinute |将 DateTime 向前取整到当前分钟的开始。|
|toStartOfFiveMinutes|将 DateTime 以五分钟为单位向前取整到最接近的时间点。|
| toStartOfTenMinutes |将 DateTime 以十分钟为单位向前取整到最接近的时间点。|
| toStartOfFifteenMinutes |将 DateTime 以十五分钟为单位向前取整到最接近的时间点。|

示例：
```
SELECT toDateTime('2020-01-01 10:20:30') AS dt, toStartOfMinute(dt) AS start
```
返回：
```
+---------------------+---------------------+
|          dt         |        start        |
+---------------------+---------------------+
| 2020-01-01 10:20:30 | 2020-01-01 10:20:00 |
+---------------------+---------------------+
```

#### date_trunc

将 Date 或 DateTime 按指定的单位向前取整到最接近的时间点，返回值为取整后的 DateTime 或 Date。相比上述取整函数，取整单位会更加自由。

函数别名为`dateTrunc`，函数格式如下：
```
date_trunc(unit,value)
dateTrunc(unit,value)
```
- value：需要转换的时间 DateTime 或 Date。
- unit：取整单位，String。可选值：`second`、`minute`、`hour`、`day`、`week`、`month`、`quarter`、`year`。

示例：
```
SELECT toDateTime('2020-01-01 10:20:30') AS dt, date_trunc('hour', dt) AS tt
```
返回：
```
+---------------------+---------------------+
|          dt         |          tt         |
+---------------------+---------------------+
| 2020-01-01 10:20:30 | 2020-01-01 10:00:00 |
+---------------------+---------------------+
```

### 日期的加减运算

#### date_add

将时间间隔或日期间隔添加到提供的 Date 或 DateTime，返回值类型为 Date 或 DateTime。

函数别名：`dateAdd`, `DATE_ADD`。函数格式如下：
```
date_add(unit, value, date)
dateAdd(unit, value, date)
DATE_ADD(unit, value, date)
```
- unit：value 对应的时间单位，类型为 String。可选值：`second`、`minute`、`hour`、`day`、`week`、`month`、`quarter`、`year`。
- value：要添加的间隔值，类型为 Integer。
- date：添加 value 的 Date 或 DateTime。

示例：
```
date_add(YEAR, 3, toDate('2018-01-01')) ---- 2021-01-01
```

#### date_sub
从提供的 Date 或 DateTime 中减去时间间隔或日期间隔，返回值为 Date 或 DateTime。

函数别名：`dateSub`,`DATE_SUB`。函数格式如下：
```
date_sub(unit, value, date)
dateSub(unit, value, date)
DATE_SUB(unit, value, date)
```
- unit — value对应的时间单位。类型为String。 可能的值：`second`、`minute`、`hour`、`day`、`week`、`month`、`quarter`、`year`。
- value - 要减去的时间，类型为整型。
- date - 要被剪去value的Date或DateTime。

示例：
```
date_sub(YEAR, 3, toDate('2018-01-01')) ---- 2015-01-01
```

#### date_diff
计算两个 Date 或 DateTime 之间的差值，返回值为整型。

函数别名：`dateDiff`，`DATE_DIFF`。函数格式如下：
```
date_diff('unit', startdate, enddate)
dateDiff('unit', startdate, enddate)
DATE_DIFF('unit', startdate, enddate)
```
- unit：value 对应的时间单位。类型为String。 可能的值：`second`、`minute`、`hour`、`day`、`week`、`month`、`quarter`、`year`。
- startdate：要减去的第一个时间值（减数）。类型为 Date 或者 DateTime。
- enddate：要减去的第二个时间值（被减数）。类型为 Date 或者 DateTime。

示例：
```
dateDiff('hour', toDateTime('2018-01-01 22:00:00'), toDateTime('2018-01-02 23:00:00')) ---- 25
```

## 条件函数

### if
控制条件表达式。如果条件 cond 的计算结果为非零值，则返回表达式 then 的结果。 如果 cond 为零或 NULL，则返回 else 表达式的结果。
```
if(cond, then, else)
```
示例：
```
if(1, 2, 3) --- 2
```
### 条件中的 NULL 值
当条件中包含 NULL 值时，结果也将为 NULL。

示例：
```
NULL < 1 --- NULL
```
### 直接使用条件结果
条件表达式的结果可能为0、1、NULL，可以直接使用条件生成字段。

示例：
```
NULL < 1 --- NULL
0 < 1 --- 1
0 > 1 --- 0
```	

## 类型转换函数

在查询和分析 COS 日志时，使用以下常见的类型转换函数，方便数据处理。需要注意的时，当存在脏数据时，可能导致类型转换函数运行失败，进而导致查询失败。

### 将字符串、小数转换为整数

>?OrZero 的输入仅支持字符串，不支持传入数值。

|函数|说明|入参类型|返回值类型|
|----|----|----|----|
|toInt32(expr)|将一个数值或代表数值的字符串转换为整型Int32|数值：Float32、Float64、Boolean；<br>代表数值的字符串：String，如`'123'`|整型Int32|
|toInt32OrZero(expr)|将一个字符串转换为整型Int32，若转换失败，则返回 0。|String|整型Int32|
|toInt64(expr)|将一个数值或代表数值的字符串转换为整型Int64|数值：Float32、Float63、Boolean；<br>代表数值的字符串：String，如`'123'`|整型Int64|
|toInt64OrZero(expr)|将一个字符串转换为整型Int64，若转换失败，则返回 0。|String|整型Int64|
|toUInt32|将一个数值或代表数值的字符串转换为整型UInt32|数值：Float32、Float64、Boolean；<br>代表数值的字符串：String，如`'123'`|整型UInt32||
|toUInt32OrZero|将一个字符串转换为整型UInt32，若转换失败，则返回 0.|String|整型UInt32|
|toUInt64|将一个数值或代表数值的字符串转换为整型UInt64|数值：Float32、Float64、Boolean；<br>代表数值的字符串：String，如`'123'`|整型UInt64|
|toUInt64OrZero|将一个字符串转换为整型UInt64，若转换失败，则返回 0.|字符串|整型UInt64|

### 将字符串、整数转换为小数

|函数|说明|入参类型|返回值类型|
|----|----|----|----|
|toFloat32|将一个数值或代表数值的字符串转换为浮点数 Float32。|数值：Int32、UInt32、Int64、UInt64、Boolean；<br>代表数值的字符串：String，如`'123.1'`|浮点型Float32|
|toFloat32OrZero|将一个字符串转换为Float32，若转换失败，则返回0。|String|浮点型Float32|
|toFloat64|将一个数值或代表数值的字符串转换为浮点数 Float32。|数值：Int32、UInt32、Int64、UInt64、Boolean；<br>代表数值的字符串：String，如`'123.1'`|浮点型Float64|
|toFloat64OrZero|将一个字符串转换为Float64，若转换失败，则返回0。|String|浮点型Float64|

### 将字符串、整数转换为日期（Date）或日期时间（DateTime）

|函数|说明|入参类型|返回值类型|
|----|----|----|----|
|toDate|将字符串、整数转换为 Date 格式。|Int32、UInt32、Int64、UInt64、String|Date|
|toDateOrZero|将字符串转换为 Date 格式，当转换失败时，返回最小的Date值（即1970-01-01）。|String|Date|
|toDateTime|将字符串转换为 DateTime 格式。|Int32、UInt32、Int64、UInt64、String|DateTime|
|toDateTimeOrZero|将字符串转换为 DateTime 格式，当转换失败时，返回一个`1970-01-01 08:00:00`。|String|DateTime|
|parseDateTimeBestEffort|将字符串解析为 DateTime 格式，适合具有特殊格式的日期字符串。|String|DateTime|

toDate、toDateTime 支持将字符串转换为 Date 或 DateTime 格式，支持的字符串格式如下：
```
YYYY-MM-DD
YYYY-MM-DD hh:mm:ss
```
如果需要转换其他日期格式的字符串，建议使用 parseDateTimeBestEffort。

toDate、toDateTime 支持将整数转换为 Date 或 DateTime 格式：
- 使用 toDate，整数会被解析为 Unix 时间戳天数，返回对应的 Date 日期；使用 toDateTime，整数会被解析为 Unix 时间戳秒数，返回对应的 DateTime 日期时间。
- 当整数大于或等于65536时，使用 toDate，整数会被解析为 Unix 时间戳秒数，并向前取整返回最近的 Date 日期。

### 数字、日期转换为字符串

|函数|说明|入参类型|返回值类型|
|----|----|----|----|
|toString|将数字、日期转换为字符串|Int32、UInt32、Int64、UInt64、Float32、Float64、Boolean、Date、DateTime|String|


示例：
```
toString(32) ---- '32'
toString(0.001) ---- '0.001'
toString(toDate(1668328645)) ---- '2022-11-13'
toString(toDateTime(1668328645)) ---- '2022-11-13 16:37:25'
```
