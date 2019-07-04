S-QL（Stream Query Language），流式查询语言。这里面的 S 和标准 SQL 中的 S 含义不同。为了便于区分，使用 S-QL 表示 EasyCount 系统中的流式查询语言。
## 语法规范
下表给出 S-QL 的语法规范：
<table align="center">
  <tr>
    <th>语法约定</th>
    <th>语法说明</th>
		<th>示例</th>
		<th>备注</th>
  </tr>
  <tr align="center">
    <td>回车</td>
    <td>代表一条 sql 逻辑结束。</td>
		<td></td>
		<td></td>
  </tr>
	<tr align="center">
    <td>WITH (SELECT ...),(SELECT ...)</td>
    <td>定义临时表，多个临时表直接使用逗号分隔。</td>
		<td>`WITH (SELECT ... FROM...)tmpa, (SELECT ..... FROM .... ) tmpb`</td>
		<td></td>
  </tr>
	 <tr align="center">
    <td>INSERT INTO</td>
    <td>将计算结果写入到结果表。</td>
		<td>`INSERT INTO xxx SELECT .... FROM tmpa, INSERT INTO yyy SELECT ..... FROM tmpb'</td>
		<td></td>
  </tr>
	<tr align="center">
    <td>COORDINATE   BY column_x</td>
    <td>指定按照某个时间字段划分统计窗口，默认值为系统时间。</td>
		<td>`COORDINATE  BY unix_timestamp(dtevetTime, 'yyyy-MM-dd HH：mm：ss')*1000`</td>
		<td>按照 dtevetTime 这个时间字段划分统计窗口。</td>
  </tr>
	 <tr align="center">
    <td>AGGR</td>
    <td>定义普通聚合窗口。</td>
		<td>`WITH AGGR INERVAL 60 SECONDS`（聚合窗口每隔 60 秒做一次统计输出）</td>
		<td rowspan="4">累加窗口和和滑动窗口必须以普通聚合窗口为基础，时间跨度为普通聚合窗口的整数倍。</td>
  </tr>
	<tr align="center">
    <td>ACCU</td>
    <td>定义累加窗口。</td>
		<td>`WITH ACCU INERVAL 120 SECONDS`（累加窗口每隔 120 秒做一次统计输出）</td>
  </tr>
	<tr align="center">
    <td>SW</td>
    <td>定义滑动窗口。</td>
		<td>`WITH SW INERVAL 120 SECONDS` （滑动窗口 120 秒做一次统计输出）</td>
		<td></td>
  </tr>
</table>

以下为一条带有滑动、累加和聚合窗口的 sql 示例：
```
NSERT INTO test_result 
SELECT activityId, count(1) pv, countd_hllp(uiUin ACCU) huv,countd_hllp(uiUin SW) fmuv, from_unixtime(AGGRTIME DIV 1000, "yyyy-MM-dd HH：mm：ss") 
FROM test_src_kafka 
GROUP BY activityId 
COORDINATE BY unix_timestamp(dtevetTime, 'yyyy-MM-dd HH：mm：ss')*1000 WITH AGGR INTERVAL 60 SECONDS 
WITH ACCU INTERVAL 3600 SECONDS 
WITH SW INTERVAL 300 SECONDS
```

通常编写一条 S-QL，可以按照如下步骤进行：
1. 将所有的中间查询结果，通过 WITH 语法，以子查询的方式作为临时表写在最前面，并用英文逗号分隔。
2. 使用 INSERT 语法将计算结果写入目标表，多条 INSERT 语句使用英文逗号分隔。
可见，一条 S-QL 语句支持多个输入，多个输出，用户可以在一条 S-QL 内部充分发挥。S-QL 支持这种操作，主要原因是 EasyCount 系统中提交一条 S-QL 以后，任务将一直运行，其所占用的系统资源一直不会被释放。在系统资源总数固定的条件下，系统能够承载的总任务数目是有限的，因此提交一个 S-QL 需要相当的谨慎，一条 S-QL 应该可以做更多的事情，从总体上减少系统资源的占用。
以下是多条 sql 示例：
```
with (select iActivityId, hllp(uiUin) uvb, from_unixtime(AGGRTIME DIV 1000, "yyyy-MM-dd HH:mm:ss") ts, 
concat_ws('-', 'd', from_unixtime((AGGRTIME DIV 1000), 'yyyy-MM-dd 00:00:00'), cast(iActivityId as string)) dk 
from src 
GROUP BY iActivityId 
COORDINATE BY unix_timestamp(dteventTime, 'yyyy-MM-dd HH:mm:ss')*1000 WITH AGGR INTERVAL 60 SECONDS) tmp, (select iActivityId, hllp_merge(tmp.uvb, dim.uvball) uvball, tmp.dk k, ts 
from tmp 
left join dim on tmp.dk=dim.k) jd 
insert into dim with k as KEY select jd.k k, jd.uvball uvball from jd,
insert into dest select jd.iActivityId, hllp_get(jd.uvball) duv, jd.ts from jd
```

## 数据类型
### 基本数据类型

| 数据类型  | 描述 | 示例 |
|---------|---------|---------|
| TINYINT | 1 字节（8 位）有符号整数 ( 从 -128 到 127 )，后缀 Y 用来表示小范围的数字。 | 10Y |
| SMALLINT | 2 字节（16 位）有符号整数 ( 从 -32,768 到 32,767 ) ，后缀 S 用来表示一个 egular descriptive number。 | 10S |
| INT | 4 字节（32 位）有符号整数 ( 从 -2,147,483,648 到  2,147,483,647 )。 | 10 |
| BIGINT | 8 字节（64 位）有符号整数 ( 从 -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 )，后缀为 L。 | 100L |
| FLOAT | 4 字节（32 位）单精度浮点数，范围在 1.40129846432481707e-45 到 3.40282346638528860e+38 (正负值)。暂时不支持科学计数法，用它来存储会非常接近数字值。 | 1.2345679 |
| DOUBLE | 8 字节（64 位）双精度浮点数，范围在 4.94065645841246544e-324d 到 1.79769313486231570e+308d (正负值)。暂时不支持科学计数法，用它来存储会非常接近数字值。（numeric values） | 1.2345678901234567 |
| DECIMAL 十进制 | DECIMAL 数据类型存储数据的精确值，它的范围在 1-1038 到 1039 -1 之间，默认定义格式是 decimal (10,0)。decimal (a,b) 中 a 代表小数点左边的最大位数，b 代表小数点右边的最大位数。 | DECIMAL (3,2) for 3.14 |
| BINARY | 它只支持与 STRING 类型的转换，反之亦然。 | 1011 |
| BOOLEAN | TRUE 或 FALSE。 | TRUE |
| STRING | 它使用单引号（'）或者双引号（"）来表达包含的字符串。Hive 使用 C 语言格式的字符串，最大溢出大小在 2 G 左右。 | 'Books' 或 "Books" |
| DATE | 用来指定年月日，格式是 YYYY-MM-DD，范围从 0000-01-01 到 9999-12-31。 | '2013-01-01' |
| TIMESTAMP | 从 Hive 0.8.0 开始便支持该类型，它用来描述指定的年，月，日，时，分，秒，毫秒。格式是 YYYY-MM-DD HH：MM：SS[.fff...]。 | '2013-01-01 12：00：01.345' |
### 复杂数据类型
EasyCount 有 3 个主要的复杂数据类型： ARRAY，MAP 和 STRUCT。这些数据类型是建立在基本数据类型基础之上的。STRUCT 是一个 Record 类型，允许包含任意类型的字段。复杂数据类型允许嵌套类型。

| 复杂数据类型 | 描述 | 语法示例 |
|---------|---------|---------|
| ARRAY | 数组是一组具有相同类型和名称的有序变量的集合。这些变量成为数组的元素，每个数组元素有一个编号，而且从 0 开始。例如：fruit[0]='apple'。 | ['apple','orange','mango'] |
| MAP | Map 是一组无序的键值对元组的集合，使用数组表示法可以访问元素。键的类型必须是原子的，值可以是任何类型，同一个映射的键的类型必须相同，值的类型也必须相同。如果某个列的数据类型是 Map，其中 Key->value paris 对应的是 'first'->'John'  和  'last'->'Doe'， 那么可以通过字段名 ['last'] 获取最后一个元素： fruit['last']='Doe'。| map('first', 'John', 'last', 'Doe') |
| STRUCT | 一组命名的字段。字段类型可以不同。STRUCT 和 C 语言中的 struct 或者"对象“类似，都可以通过"点"分隔符访问元素内容。默认情况下，STRUCT 字段名可以是 col1，col2，…… 您可以通过 structs_name.column_name 来访问具体的值： fruit.col1=1。| info struct<<br>name:STRING,<br> age:INT><br>(info.name 获取 name<br>info.age 获取 age )|

## 表达式
表达式是符号和运算符的一种组合，EasycCount 解析引擎处理该组合以获取单个值。简单表达式可以是常量、变量或者函数，可以用运算符将两个或者多个简单表达式联合起来构成更复杂的表达式。
### 通用表达式
通用表达式可以出现在 select 子句中，也可以出现在 where 或者 group by 子句中。
表达式的优先级从高到底如下表所示：

| 表达式 | 说明 | 
|---------|---------|
| IS [NOT] NULL， [NOT] LIKE， [NOT] BETWEEN，[NOT] IN | 是否为空之类判断表达式。 |
| AND、OR | 多个条件之间"且"或者"或"的逻辑关系。 |
### 特殊表达式
FOREACH & EXECUTE 处理复杂数据类型时，可以使用 foreach 和 execute 语法进行循环和迭代处理。
## 函数
EasyCount 内部提供了很多函数给开发者使用，包括数学函数，类型转换函数，条件函数，字符函数，聚合函数，表生成函数等。其中大部分函数继承自 hive,另外也有一部分是 EasycCount 系统的自定义函数。
>** 注明：\_\_innertable(1000)  每个 1000 ms 输出一次，用于测试使用。innertable 中没有真实数据，可以用于验证函数。**

### 数值函数

| 函数名 | 语法 | 返回值类型 | 说明 | 示例 |
|---------|---------|---------|---------|---------|
| 取整函数： round | round(double a) | bigint | 返回 double 类型的整数值部分（遵循四舍五入）。 | `select round(3.1415926) from __innertable(1000)` <br>结果：3 |
| 指定精度取整函数： round | round(double a, int d) | double | 返回指定精度 d 的 double 类型。 | `select round(3.1415926,4) from __innertable(1000)` <br>结果：3.1416  |
| 向下取整函数： floor | floor(double a) | bigint | 返回小于或者等于该 double 变量的最大的整数。 | `select floor(3.1415926) from __innertable(1000)`<br>结果：3  |
| 向上取整函数： ceil | ceil(double a) | bigint | 返回大于或者等于该 double 变量的最小的整数。 | `select ceiling(3.1415926) from __innertable(1000)`<br>结果：4 |
| 向上取整函数：ceiling | ceiling(double a) | bigint | 与 ceil 功能相同。 | `select ceiling(3.1415926) from __innertable(1000)`<br>结果：4 |
| 取随机数函数：rand | rand()，rand(int seed) | double | 返回一个 0 到 1 范围内的随机数。如果指定种子 seed，则会得到一个稳定的随机数序列。 | `select rand() from  __innertable(1000)`<br>结果：0.5577432776034763<br>`select rand(100) from  __innertable(1000)`<br>结果：0.7220096548596434<br>`select rand(100) from  __innertable(1000)`<br>结果：0.7220096548596434 |
| 自然指数函数：exp | exp(double a) | double | 返回自然对数 e 的 a 次方。 | `select exp(2) from __innertable(1000)`<br>结果：7.38905609893065 |
| 自然对数函数：ln | ln(double a) | double | 返回 a 的自然对数。 | `select ln(7.389) from __innertable(1000)`<br>结果：2.0  |
| 以 10 为底对数函数：log10 | log10(double a) | double | 返回以 10 为底的 a 的对数。 | `select log10(100) from __innertable(1000)`<br>结果：2.0  |
| 以 2 为底对数函数：log2 | log2(double a) | double | 返回以 2 为底的 a 的对数。 | `select log2(8) from __innertable(1000)`<br>结果：3.0  |
| 对数函数：log | log(double base, double a) | double | 返回以 base 为底的 a 的对数。 | `select log(4,256) from __innertable(1000)`<br>结果：4.0 |
| 幂运算函数： power | power(double a, double p) | double | 返回 a 的 p 次幂，与 pow 功能相同。 | `select pow(2,4) from __innertable(1000)`<br>结果：16.0 |
| 幂运算函数： pow | pow(double a, double p) | double | 返回 a 的 p 次幂。 | `select power(2,4) from __innertable(1000)`<br>结果：16.0 |
| 开平方函数：sqrt | sqrt(double a) | double | 返回 a 的平方根。 | `select sqrt(16) from __innertable(1000)`<br>结果：4.0 |
| 二进制函数：bin | bin(BIGINT a) | string | 返回 a 的二进制代码表示。 | `select bin(7) from __nnertable(1000)`<br>结果：111 |
| 十六进制函数：hex | hex(BIGINT a) | string | 如果变量是 int 类型，那么返回 a 的十六进制表示；如果变量是 string 类型，则返回该字符串的十六进制表示。 | `select hex(17) from __innertable(1000)`<br>结果：11<br>`select hex(‘abc’) from __innertable(1000)`<br>结果：616263 |
| 进制转换函数：conv | conv(BIGINT num, int from_base, int to_base) | string | 将数值 num 从 from_base 进制转化到 to_base 进制。 | `select conv(17,10,16) from  __innertable(1000)`<br>结果：11  |
| 绝对值函数：abs | abs(double a)  abs(int a) | double | 返回数值 a 的绝对值。 | `select abs(-3.9) from __innertable(1000)`<br>结果：3.9<br>`select abs(10) from __innertable(1000)`<br>结果：10 |
| 正取余函数：pmod | pmod(int a, int b),pmod(double a, double b) | int或double | 返回正的 a 除以 b 的余数。 | `select pmod(9,4) from __innertable(1000)`<br>结果：1<br>`select pmod(-9,4) from __innertable(1000)`<br>结果：3  |
| 正弦函数： sin | sin(double a) | double | 返回 a 的正弦值。 | `select sin(0.8) from __innertable(1000)`<br>结果：0.7173560908995228 |
| 反正弦函数： asin | asin(double a) | double | 返回 a 的反正弦值。 | `select asin(0.7173560908995228) from __innertable(1000)`<br>结果：0.8 |
| 余弦函数： cos | cos(double a) | double | 返回 a 的余弦值。 | `select cos(0.9) from __innertable(1000)`<br>结果：0.6216099682706644 |
| 反余弦函数： acos | acos(double a) | double | 返回 a 的反余弦值。 | `select acos(0.6216099682706644) from __innertable(1000)`<br>结果：0.9 |
| positive 函数： positive | positive(int a)， positive(double a) | int或double | 返回 a。 | `select positive(-10) from __innertable(1000)`<br>结果：-10<br>`select positive(12) from __innertable(1000)`<br>结果：12 |
| negative 函数： negative | negative(int a)，negative(double a) | int或double | 返回 -a。 | `select negative(-5) from __innertable(1000)`<br>结果：5<br>`select negative(8) from __innertable(1000)`<br>结果：-8 |

### 日期函数

| 函数名 | 语法 | 返回值 | 说明 | 示例 |
|---------|---------|---------|---------|---------|
| UNIX时间戳转日期函数：from_unixtime |from_unixtime(bigint unix_timestamp, string format)| string | 转化 UNIX 时间戳（从1970-01-01 00：00：00 UTC 到指定时间的秒数）到当前时区的时间格式。 | `select from_unixtime(1493864893,'yyyy-MM-dd  HH：mm：ss' ) from __innertable(1000)`<br>结果：2017-05-04 10：28：13 |
| 获取当前 UNIX 时间戳函数：unix_timestamp | unix_timestamp() | bigint | 获得当前时区的 UNIX 时间戳。| `select unix_timestamp() from __innertable(1000)`<br>结果：1493864893 |
| 日期转UNIX时间戳函数：unix_timestamp | unix_timestamp(string date) | bigint | 转换格式为 "yyyy-MM-dd HH：mm：ss" 的日期到 UNIX 时间戳。如果转化失败，则返回0。| `select unix_timestamp('2017-05-04 10：28：13') from __innertable(1000)`<br>结果：1493864893 |
| 指定格式日期转UNIX时间戳函数：unix_timestamp | unix_timestamp(string date, string pattern) | bigint | 转换 pattern 格式的日期到 UNIX 时间戳。如果转化失败，则返回 0。 | `select unix_timestamp('20170504 10：28：13','yyyyMMddHH：mm：ss') from 	__innertable(1000)`<br>结果：1493864893 |
| 日期时间转日期函数：to_date | to_date(string timestamp) | string | 返回日期时间字段中的日期部分。 | `select to_date('2017-05-04 10：03：01') from __innertable(1000)`<br>结果：2017-05-04  |
| 日期转年函数： year | year(string date) | int | 返回日期中的年。 | `select year('2013-12-08 10：03：01') from __innertable(1000)`<br>结果：2013<br>`select year('2012-12-08') from __innertable(1000)`<br>结果：2012  |
| 日期转月函数： month | month (string date) | int | 返回日期中的月份。 | `select month('2011-12-08 10：03：01') from __innertable(1000)`<br>结果：12  |
| 日期转天函数： day | day (string date) | int | 返回日期中的天。 | `select day('2017-05-04 10：03：01') from __innertable(1000)`<br>结果：4 |
| 日期转小时函数： hour | hour (string date) | int | 返回日期中的小时。 | `select hour('2017-05-04 10：03：01') from __innertable(1000)`<br>结果：10 |
| 日期转分钟函数： minute | minute (string date) | int | 返回日期中的分钟。 | `select minute('2017-05-04 10：03：01') from __innertable(1000)`<br>结果：3 |
| 日期转秒函数： second | second (string date) | int | 返回日期中的秒。 | `select second('2017-05-04 10：03：01') from __innertable(1000)`<br>结果：1 |
| 日期转周函数：weekofyear | weekofyear (string date) | int | 返回日期在当前的周数。 | `select weekofyear('2011-12-08 10：03：01') from __innertable(1000)`<br>结果：49  |
| 日期比较函数： datediff | datediff(string enddate, string startdate) | int | 返回结束日期减去开始日期的天数。 | `select datediff('2012-12-08','2012-05-09') from __innertable(1000)`<br>结果：213 |
| 日期增加函数： date_add | date_add(string startdate, int days) | string | 返回开始日期 startdate 增加 days 天后的日期。 | `select date_add('2012-12-08',10) from __innertable(1000)`<br>结果：2012-12-18  |
| 日期减少函数： date_sub  | date_sub (string startdate, int days) | string | 返回开始日期 startdate 减少 days 天后的日期。 | `select date_sub('2012-12-08',10) from __innertable(1000)`<br>结果：2012-11-28 |

### 字符串函数

| 函数名 | 语法 | 返回值 | 说明 | 示例 |
|---------|---------|---------|---------|---------|
|  字符串长度函数：length | length(string A) | int | 返回字符串 A 的长度。 | `select length('abcedfg') from __innertable(1000)`<br>结果：7 |
| 字符串反转函数：reverse | reverse(string A) | string | 返回字符串 A 的反转结果。 | `select reverse(abcedfg’) from __innertable(1000)`<br>结果：gfdecba |
| 字符串连接函数：concat | concat(string A, string B…) | string | 返回输入字符串连接后的结果，支持任意个输入字符串。 | `select concat(‘abc’,'def’,'gh’) from __innertable(1000)`<br>结果：abcdefgh |
| 带分隔符字符串连接函数：concat_ws | concat_ws(string SEP, string A, string B…) | string | 返回输入字符串连接后的结果，SEP 表示各个字符串间的分隔符。 | `select concat_ws('-','abc','def','gh') from __innertable(1000)`<br>结果：abc-def-gh |
| 字符串截取函数：substr，substring | substr(string A, int start)，substring(string A, int start) | string | 返回字符串 A 从 start 位置到结尾的字符串。 | `select substr('abcde',3) from __innertable(1000)`<br>结果：cde |
| 字符串截取函数：substr，substring | substr(string A, int start, int len)，substring(string A, int start, int len) | string | 返回字符串 A 从 start 位置开始，长度为 len 的字符串。 | `select substr('abcde',3,2) from __innertable(1000)`<br>结果：cd  |
| 字符串转大写函数：upper，ucase | upper(string A) ，ucase(string A) | string | 返回字符串 A 的大写格式。 | `select upper('abSEd') from __innertable(1000)`<br>结果： ABSED |
| 字符串转小写函数：lower，lcase | lower(string A)， lcase(string A) | string | 返回字符串 A 的小写格式。 | `select lower('abSEd') from __innertable(1000)`<br>结果：absed |
| 去空格函数：trim | trim(string A) | string | 去除字符串两边的空格。 | `select trim(' abc ') from __innertable(1000)`<br>结果：abc |
| 正则表达式替换函数：regexp_replace | regexp_replace(string A, string B, string C) | string | 将字符串 A 中的符合 Java 正则表达式 B 的部分替换为 C。注意，在有些情况		下要使用转义字符,类似 oracle 中的 regexp_replace 函数。 | `select regexp_replace('foobar', 'oo|ar', '-') from __innertable(1000)`<br>结果：f-b- |
| 正则表达式解析函数：regexp_extract | regexp_extract(string subject, string pattern, int index) | string | 将字符串 subject 按照 pattern 正则表达式的规则拆分，返回 index 指定的字符。 | `select regexp_extract('foothebar', 'foo(.*?)(bar)', 1) from__innertable(1000)`<br>结果：the |
| URL 解析函数：parse_url | parse_url(string urlString, string partToExtract [, string keyToExtract]) | string | 返回 URL 中指定的部分。partToExtract 的有效值为：HOST，PATH，QUERY，REF，PROTOCOL， AUTHORITY，FILE 和 USERINFO。 | `select parse_url('http://facebook.com/path1/p.php?k1=v1&k2=v2#Ref1', 'HOST') 	from__innertable(1000)`<br>结果：facebook.com<br>`select parse_url('http://facebook.com/path1/p.php?k1=v1&k2=v2#Ref1', 	'QUERY','k1') from __innertable(1000)`<br>结果：v1 |
| json 解析函数：get_json_object | get_json_object(string json_string, string path) | string | 解析 json 的字符串 json_string，返回 path 指定的内容。如果输入的 json 字符串无效，那么返回 NULL。 | `select  get_json_object('{"fruit":apple,”ower”:”tim”}’,'$.owner')` <br>结果：tim |
| 空格字符串函数：space | space(int n) | string | 返回长度为 n 的空格字符串。 |  |
| 重复字符串函数：repeat | repeat(string str, int n) | string | 返回重复 n 次后的 str 字符串。 | `select repeat('abc',5) from __innertable(1000)`<br>结果：abcabcabcabcabc  |
| 首字符 ascii 函数：ascii | ascii(string str) | int | 返回字符串 str 第一个字符的 ascii 码。 | `select ascii('abcde') from __innertable(1000)`<br>结果：97 |
| 分割字符串函数： split | split(string str, string pat) | array | 按照 pat 字符串分割 str，会返回分割后的字符串数组。 | `select split('abtcdtef','t') from __innertable(1000)`<br>结果：["ab","cd","ef"]  |
| 集合查找函数：find_in_set | find_in_set(string str, string strList) | int | 返回 str 在 strlist 第一次出现的位置，strlist 是用逗号分割的字符串。如果没有找该 str 字符，则返回 0。 | `select find_in_set('ab','ef,ab,de') from __innertable(1000)`<br>结果：2 |

### 条件函数

| 函数名 | 语法 | 返回值 | 说明 | 示例 |
|---------|---------|---------|---------|---------|
| If 函数： if | if(boolean testCondition, T valueTrue, T valueFalseOrNull) | T | 当条件 testCondition 为 TRUE 时，返回 valueTrue；否则返回 valueFalseOrNull。 | `select if(1=2,100,200) from  __innertable(1000)`<br>结果：200<br>`select if(1=1,100,200) from  __innertable(1000)`<br>结果：100 |
| nvl 函数： nvl | nvl(T value, T default_value) | T | 如果 value 值为 NULL 就返回 default_value，否则返回 value。 | `select nvl(null,100) from __innertable(1000)`<br>结果：100 |
| isnull 函数： isnull | isnull(T value) | true 或 false | 如果 value 值为 NULL 就返回 true，否则返回 false。 | `select isnull(null) from __innertable(1000)`<br>结果：true |
| isnull 函数：isnotnull | isnotnull(T value) | true 或 false | 如果 value 值为 NULL 就返回 true，否则返回 false。 | `select isnotnull(null) from __innertable(1000)`<br>结果：false |
| 条件判断函数：CASE | CASE WHEN a THEN \_a [WHEN b THEN \_b]\* [ELSE \_c] END | T | 如果 a 为 TRUE，则返回 \_a；如果 b 为 TRUE，则返回 \_b；否则返回 \_c 。| `select case when 1=2 then 'tom' when 2=2 then 'mary' else'tim' end from __innertable(1000)`<br>结果：mary |

### 类型转换函数

| 函数名 | 语法 | 返回值 | 说明 | 示例 |
|---------|---------|---------|---------|---------|
| 类型转换函数：cast | cast(expr as < type >) | Expected "=" to follow "type" | 返回 array 类型的长度。 | `select cast(1 as bigint) from __innertable(1000)`<br>结果：1 |

### 集合函数

| 标题1 | 标题2 | 标题3 | 标题2 | 标题3 |
|---------|---------|---------|---------|---------|
| Map 类型长度函数： size(Map< K.V >) | size(Map< K.V >) | int | 返回 map 类型的长度。 | `select size(map('100','tom','101','mary')) from __innertable(1000)`<br>结果：2 |
| Array 类型长度函数： size(Array< T >) | size(Array< T >) | int | 返回数组类型的长度。 | `select size(array(‘aa’,’bb’)) from __innertable(1000)`<br>结果：2 |

### 聚合函数

| 函数名 | 语法 | 返回值 | 说明 | 示例 |
|---------|---------|---------|---------|---------|
| 个数统计函数： count | count(col) | int | count(expr) 统计检索出的行的个数，返回指定字段的个数。 |  |
| 总和统计函数： sum | sum(col) | double | sum(col) 统计结果集中 col 的相加的结果；sum(DISTINCT col) 统计结果中 col 不同值相加的结果。 | `select sum(t) from lxw_dual`<br>结果：100 |
| 平均值统计函数： avg | avg(col) | double | avg(col) 统计结果集中 col 的平均值；avg(DISTINCT col) 统计结果中 col 不同值相加的平均值。 | `select avg(t) from lxw_dual`<br>结果：50  |
| 最小值统计函数： min | min(col) | double | 统计结果集中 col 字段的最小值。 | `select min(t) from lxw_dual`<br>结果：20  |
| 最大值统计函数： max | max(col) | double | 统计结果集中 col 字段的最大值。 | `select max(t) from lxw_dual`<br>结果：120 |

### 扩展函数

| 函数名 | 语法 | 返回值 | 说明 |
|---------|---------|---------|---------|
| 个数统计函数：countd，countd_hllp | countd(col)，countd_hllp(col) | int | count(col) 去重统计检索出的行的个数，返回指定字段的个数。该函数为非精确去重统计，精确度在 99.5% 左右。 |
| 去重合并统计函数：hllp_merge | hllp_merge(a,b)，参数为 binary | binary | 去重合并统计函数是将两个二进制集合去重合并生成以一个新的集合。 |
| 获取去重后的结果函数：hllp_get | hllp_get(a) | bigint | 获取去重后的统计结果。 |
> 说明：以上三个函数都是基于 HyperLogLog 算法的实现，为了做大规模去重统计，降低存储空间，精确度上有一点误差。

Sql示例：
```
with (select iActivityId, hllp(uiUin) uvb, from_unixtime(AGGRTIME DIV 1000, "yyyy-MM-dd 	HH:mm:ss") ts, 
concat_ws('-', 'd', from_unixtime((AGGRTIME DIV 1000), 'yyyy-MM-dd 00:00:00'), cast(iActivityId as 	string)) dk 
from src GROUP BY iActivityId 
COORDINATE BY unix_timestamp(dteventTime, 'yyyy-MM-dd HH:mm:ss')*1000 WITH AGGR 	INTERVAL 60 SECONDS) tmp, 
(select iActivityId, hllp_merge(tmp.uvb, dim.uvball) uvball, tmp.dk k, ts from 
	tmp left join dim on tmp.dk=dim.k) jd 
insert into dim with k as KEY select jd.k k, jd.uvball uvball from jd,
insert into dest select jd.iActivityId, hllp_get(jd.uvball) duv, jd.ts from jd
```
以上为 sql 部分，下面是 sql 中使用的表的描述信息。该信息根据用户在页面上库表配置的内容自动生成。
```
[tabledesc-1]
table.name=src
table.fields=iActivityId,int,:dteventTime,string,:uiUin,string,
table.field.splitter=|

[tabledesc-dimtable-tde]
table.name=dim
table.fields=k,string,:uvball,binary,
table.field.key=k

[tabledesc-destination]
table.type=tpg
table.name=dest
table.fields=iActivityId,int,:duv,bigint,:dteventTime,string
```
> 说明：改向配置用户描述每条数据的结构，统计计算过程会根据结构解析每一行数据。
