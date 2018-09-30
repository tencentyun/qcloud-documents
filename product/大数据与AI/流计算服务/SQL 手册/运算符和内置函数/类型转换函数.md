类型转换函数的函数名和功能描述如下：

| 函数名	| 功能描述 | 
| ----- | ----- |
| CAST(value AS type)	| 将某个值转为 type 类型，例如 CAST(`hello` AS VARCHAR) 会将 `hello` 字段转为 VARCHAR 类型。|
| TO_TIMESTAMP(string, simple_format) | 以 Java 的 SimpleDateFormat 支持的时间格式化模板 simple_format 将 string 字符串格式化为 SCS 内部支持的 timestamp 类型的时间戳。<br>例如 TO_TIMESTAMP(ts, ‘yyyy-MM-dd HH:mm:ss’)|
| DATE_FORMAT_SIMPLE(timestamp, simple_format | 将 timestamp 类型的字段以 Java 的 SimpleDateFormat 支持的时间格式化模板转为字符串形式。<br>例如 DATE_FORMAT_SIMPLE(ts, ‘yyyy-MM-dd HH:mm:ss’) |
| DATE_FORMAT(timestamp, format) | 使用与 MySQL 兼容的模板 format 来格式化时间戳为字符串（与 DATE_FORMAT_SIMPLE 的区别在于采用 MySQL 的格式化语法而非 Java SimpleDateFormat 的格式化语法）。<br>使用方式与 MySQL 的 date_parse() 函数相同。<br>例如 DATE_FORMAT(ts, ‘%Y, %d %M’) 返回字符串 ‘2017, 05 May’ |
