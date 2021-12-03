## 聚合函数

COS Select 支持以下聚合函数：

| 函数名          | 参数类型                    | 返回类型                                                     |
| :-------------- | :-------------------------- | :----------------------------------------------------------- |
| AVG(expression) | INT，FLOAT，DECIMAL         | 入参为整型时返回 DECIMAL，入参为浮点型时返回 FLOAT，其余情况下返回值与入参一致 |
| COUNT           | -                           | INT                                                          |
| MAX(expression) | INT，DECIMAL                | 返回值与入参一致                                             |
| MIN(expression) | INT，DECIMAL                | 返回值与入参一致                                             |
| SUM(expression) | INT，FLOAT，DOUBLE，DECIMAL | 入参为整型时返回 INT，入参为浮点型时返回 FLOAT，其余情况下返回值与入参一致|

## 条件函数

COS Select 支持以下条件函数。

### COALESCE

COALESCE 函数按顺序判断输入的参数，并返回第一个非空的参数值。如果输入参数中不包含非空参数，则函数返回 null 值。

#### 语法

```sql
COALESCE ( expression, expression, ... )
```

> ?expression 参数支持传入 INT、String、Float 类型数值、数组或者嵌套函数。

#### 示例

```shell
COALESCE(1)                -- 1
COALESCE(1, null)          -- 1
COALESCE(null, null, 1)    -- 1
COALESCE(missing, 1)       -- 1
COALESCE(null, 'string')   -- 'string'
COALESCE(null)             -- null
COALESCE(null, null)       -- null
COALESCE(missing)          -- null
COALESCE(missing, missing) -- null
```

### NULLIF

NULLIF 函数判断两个传入的参数之间的差异，如果两个入参均为相同的值，则返回 NULL，否则返回第一个入参的值。

#### 语法

```sql
NULLIF ( expression1, expression2 )
```

> ? expression 参数支持传入 INT、String、Float 类型数值、数组或者嵌套函数。

#### 示例

```shell
NULLIF(1, 2)             -- 1
NULLIF(1, '1')           -- 1
NULLIF(1, NULL)          -- 1
NULLIF(1, 1)             -- null
NULLIF(1.0, 1)           -- null
NULLIF(missing, null)    -- null
NULLIF(missing, missing) -- null
NULLIF([1], [1])         -- null
NULLIF(NULL, 1)          -- null
NULLIF(null, null)       -- null
```

## 转换函数

COS Select 支持以下转换函数。

### CAST

CAST 函数可以将一种实例转化为另一种实例。这个实例可以是数值，也可以是可以计算成某个确定数值的函数。

#### 语法

```shell
CAST ( expression AS data_type )
```

> ?
>
> - expression 参数可以是数值、数组、运算符或者可以计算成某个确定数值的 SQL 函数。
> - data_type 参数是转换后的数据类型，例如 INT 类型。目前 COS Select 支持的数据类型，请参见 [数据类型](https://cloud.tencent.com/document/product/436/37639)。

#### 示例

```shell
CAST('2007-04-05T14:30Z' AS TIMESTAMP)
CAST(0.456 AS FLOAT)
```

## 日期函数

COS Select 支持以下日期函数。

### DATE_ADD

DATE_ADD 函数可以为指定时间戳的某个部分（年、月、日、时、分、秒）加上指定时间间隔，并返回一个新的时间戳。

#### 语法

```shell
DATE_ADD( date_part, quantity, timestamp )
```

> ?
> - date_part 参数指定时间戳中需要修改的部分，可以是年、月、日、时、分、秒。
> - quantity 参数代表需要增加的数值，必须为正整数。
> - timestamp 参数为需要修改的时间戳。

#### 示例

```shell
DATE_ADD(year, 5, `2010-01-01T`)                -- 2015-01-01
DATE_ADD(month, 1, `2010T`)                     -- 2010-02T 
DATE_ADD(month, 13, `2010T`)                    -- 2011-02T
DATE_ADD(hour, 1, `2017T`)                      -- 2017-01-01T01:00-00:00
DATE_ADD(hour, 1, `2017-01-02T03:04Z`)          -- 2017-01-02T04:04Z
DATE_ADD(minute, 1, `2017-01-02T03:04:05.006Z`) -- 2017-01-02T03:05:05.006Z
DATE_ADD(second, 1, `2017-01-02T03:04:05.006Z`) -- 2017-01-02T03:04:06.006Z
```

### DATE_DIFF

DATE_DIFF 函数比较两个合法的时间戳并返回两个时间戳的差值，这个差值可以以指定的时间单位显示。当 timestamp1 的 date_part 值比 timestamp2 大时，返回值为正数。反之，则返回负数。

#### 语法

```shell
DATE_DIFF( date_part, timestamp1, timestamp2 )
```

> ?
> - date_part 参数指定两个时间戳比较的时间单位，可以是年、月、日、时、分、秒。
> - timestamp1 参数是输入的第一个时间戳。
> - timestamp2 参数是输入的第二个时间戳。

#### 示例

```shell
DATE_DIFF(year, `2010-01-01T`, `2011-01-01T`)            -- 1
DATE_DIFF(year, `2010T`, `2010-05T`)                     -- 4 
DATE_DIFF(month, `2010T`, `2011T`)                       -- 12
DATE_DIFF(month, `2011T`, `2010T`)                       -- -12
DATE_DIFF(day, `2010-01-01T23:00T`, `2010-01-02T01:00T`) -- 0 
```

### EXTRACT

 EXTRACT 函数从给定的时间戳中，抽取指定时间单位的数值。

#### 语法

```shell
EXTRACT( date_part FROM timestamp )
```

> ?
> - date_part 参数指定需要抽取的时间单位，可以是年、月、日、时、分、秒。
> - timestamp 参数是输入的时间戳。

#### 示例

```shell
EXTRACT(YEAR FROM `2010-01-01T`)                           -- 2010
EXTRACT(MONTH FROM `2010T`)                                -- 1 
EXTRACT(MONTH FROM `2010-10T`)                             -- 10
EXTRACT(HOUR FROM `2017-01-02T03:04:05+07:08`)             -- 3
EXTRACT(MINUTE FROM `2017-01-02T03:04:05+07:08`)           -- 4
EXTRACT(TIMEZONE_HOUR FROM `2017-01-02T03:04:05+07:08`)    -- 7
EXTRACT(TIMEZONE_MINUTE FROM `2017-01-02T03:04:05+07:08`)  -- 8
```

### TO_STRING

TO_STRING 函数可以将时间戳转换成指定格式的时间字符串。

#### 语法

```shell
TO_STRING ( timestamp time_format_pattern )
```

> ?
> - timestamp 参数指定需要转换的时间戳。
> - time_format_pattern 参数指定转换时间格式。

| 格式             | 描述                                                         | 示例                              |
| ---------------- | ------------------------------------------------------------ | --------------------------------- |
| yy             | 2位数年份                                                    | 98                              |
| y             | 4位数年份                                                    | 1998                            |
| yyyy           | 固定4位数年份，不足的以0填充                                 | 0199                            |
| M              | 月份                                                         | 1                              |
| MM             | 固定2位数月份，不足的以0填充                                 | 01                              |
| MMM            | 月份的英文缩写                                               | Jan                             |
| MMMM           | 月份的英文全称                                               | January                         |
| MMMMM          | 月份的首字母缩写                                             | J（不适用于 to_timestamp 函数） |
| d             | 一个月中的某天（1~31）                                       | 1                              |
| dd             | 固定2位数的天数（1~31）                                      | 01                              |
| a             | 早上或者下午的标识（AM/PM）                                  | AM                              |
| h              | 时钟，12小时制                                               | 1                             |
| hh             | 固定2位数的时刻，12小时制                                    | 01                              |
| H              | 时钟，24小时制                                               | 1                              |
| HH             | 固定2位数的时刻，24小时制                                    | 01                             |
| m              | 分钟（00-59）                                               | 1                               |
| mm            | 固定2位数的分钟，24小时制                                    | 01                              |
| s              | 秒钟（00-59）                                                  | 1                               |
| ss            | 固定2位数的时刻，24小时制                                    | 01                              |
| S              | 秒钟的小数部分（精度0.1，范围0.0 - 0.9）                         | 0                              |
|SS             | 秒钟的小数部分（精度0.01，范围0.00 - 0.99）                     | 6                               |
| SSS            | 秒钟的小数部分（精度0.001，范围0.000 - 0.999）                   | 60                              |
| ...              | ...                                                          | ...                               |
| SSSSSSSSS     | 秒钟的小数部分（精度0.000000001，范围0.000000000 - 0.999999999） | 60000000                        |
| n             | 纳秒                                                         | 60000000                        |
| X              | 时钟级的偏移，如果偏移为0则为"Z"                             | +01或者 Z                      |
| XX 或者 XXXX   | 时钟或者分钟级的偏移，如果偏移为0则为"Z"                     | +0100或者 Z                    |
| xxx 或者 xxxxx | 时钟或者分钟级的偏移，如果偏移为0则为"Z"                     | +01:00或者 Z                   |
| x              | 时钟级的偏移                                                 | 1                               |
| xx 或者 xxxx   | 时钟或者分钟级的偏移                                         | 0100                            |
| xxx 或者 xxxxx | 时钟或者分钟级的偏移                                         | 01:00                           |

#### 示例

```shell
TO_STRING(`1998-07-20T20:18Z`,  'MMMM d, y')                    -- "July 20, 1998"
TO_STRING(`1998-07-20T20:18Z`, 'MMM d, yyyy')                   -- "Jul 20, 1998"
TO_STRING(`1998-07-20T20:18Z`, 'M-d-yy')                        -- "7-20-69"
TO_STRING(`1998-07-20T20:18Z`, 'MM-d-y')                        -- "07-20-1998"
TO_STRING(`1998-07-20T20:18Z`, 'MMMM d, y h:m a')               -- "July 20, 1998 8:18 PM"
TO_STRING(`1998-07-20T20:18Z`, 'y-MM-dd''T''H:m:ssX')           -- "1998-07-20T20:18:00Z"
TO_STRING(`1998-07-20T20:18+08:00Z`, 'y-MM-dd''T''H:m:ssX')     -- "1998-07-20T20:18:00Z"
TO_STRING(`1998-07-20T20:18+08:00`, 'y-MM-dd''T''H:m:ssXXXX')   -- "1998-07-20T20:18:00+0800"
TO_STRING(`1998-07-20T20:18+08:00`, 'y-MM-dd''T''H:m:ssXXXXX')  -- "1998-07-20T20:18:00+08:00"
```

### TO_TIMESTAMP

 TO_TIMESTAMP 函数可以将时间字符串转换为时间戳。

#### 语法

```shell
TO_TIMESTAMP ( string )
```

> ?  string 参数为输入的时间字符串。

#### 示例

```shell
TO_TIMESTAMP('2007T')                         -- `2007T`
TO_TIMESTAMP('2007-02-23T12:14:33.079-08:00') -- `2007-02-23T12:14:33.079-08:00`
```

### UTCNOW

 UTCNOW 函数可以返回当前 UTC 制时间戳。

#### 语法

```
UTCNOW()
```

#### 示例

```shell
UTCNOW() -- 2019-01-01T14:23:12.123Z
```

## 字符串函数

COS Select 支持以下字符串函数。

### CHAR_LENGTH, CHARACTER_LENGTH

CHAR_LENGTH 和 CHARACTER_LENGTH 均可以计算字符串中的字符数量，这两个函数名的语义相同。

#### 语法

```shell
CHAR_LENGTH ( string )
```

> ?  string 参数指定需要计算字符数的字符串。

#### 示例

```shell
CHAR_LENGTH('null')      -- 4
CHAR_LENGTH('tencent')   -- 7
```

### LOWER

 LOWER 函数可以将指定字符串中的所有大写字母转换为小写字母，所有非大写字母将保持不变。

#### 语法

```shell
LOWER ( string )
```

> ?  string 参数指定一个需要将大写字母转为小写字母的字符串。

#### 示例

```shell
LOWER('TENcent') -- 'tencent'
```

### SUBSTRING

 SUBSTRING 函数可以返回一个字符串的子串。您可以指定一个索引， SUBSTRING 函数将从这个索引开始，按照指定的子串长度截取原字符串的剩余内容，并将结果返回。

>? 如果输入的字符串只有1个字符，且索引设置大于1，则 SUBSTRING 函数将自动将其切换至1。
>

#### 语法

```shell
SUBSTRING( string FROM start [ FOR length ] )
```

> ?
> - string 参数指定需要截取子串的字符串。
> - start 参数为字符串的某个索引值，指定截取的位置。
> - length 参数指定子串长度，如未特殊指定将截取字符串剩余所有内容。

#### 示例

```shell
SUBSTRING("123456789", 0)      -- "123456789"
SUBSTRING("123456789", 1)      -- "123456789"
SUBSTRING("123456789", 2)      -- "23456789"
SUBSTRING("123456789", -4)     -- "123456789"
SUBSTRING("123456789", 0, 999) -- "123456789" 
SUBSTRING("123456789", 1, 5)   -- "12345"
```

### TRIM

 TRIM 函数可以删除指定字符串首字符前或末字符后的所有字符。默认删除字符为" "。

#### 语法

```shell
TRIM ( [[LEADING | TRAILING | BOTH remove_chars] FROM] string )
```

> ?
> -  string 参数指定需要操作的字符串。
> - `LEADING | TRAILING | BOTH`参数指定需要删除字符串前（LEADING）或者字符串后（TRAILING）或者同时删除（BOTH）的多余字符。
> -  remove_chars 参数指定需要删除何种多余字符。remove_chars 参数可以是一个长度大于1的字符串，TRIM 函数只要在 string 参数前后发现与之匹配的多余字符串均会做删除处理。

#### 示例

```shell
TRIM('       foobar         ')               -- 'foobar'
TRIM('      \tfoobar\t         ')            -- '\tfoobar\t'
TRIM(LEADING FROM '       foobar         ')  -- 'foobar'
TRIM(TRAILING FROM '       foobar         ') -- 'foobar'
TRIM(BOTH FROM '       foobar         ')     -- 'foobar'
TRIM(BOTH '12' FROM '1112211foobar22211122') -- 'foobar'
```

### UPPER

 UPPER 函数可以将所有小写字符转换为大写字符，非小写字符将不会被修改。

#### 语法

```shell
UPPER ( string )
```

> ? string 参数指定需要转换为大写字符的字符串。

#### 示例

```shell
UPPER('tenCENT') -- 'TENCENT'
```

