## 数字类型
数字类型由2、4或8字节的整数以及4或8字节的浮点数和可选精度小数组成。TDSQL-A PostgreSQL版 列存表支持如下数字类型：

| **名字**         | **存储尺寸** | **描述**           | **范围**                                     |
| ---------------- | ------------ | ------------------ | -------------------------------------------- |
| smallint         | 2字节        | 小范围整数         | -32768 到 +32767                             |
| integer          | 4字节        | 整数的典型选择     | -2147483648 到 +2147483647                   |
| bigint           | 8字节        | 大范围整数         | -9223372036854775808 到 +9223372036854775807 |
| decimal          | 可变         | 用户指定精度，精确 | 最高小数点前131072位，以及小数点后16383位    |
| numeric          | 可变         | 用户指定精度，精确 | 最高小数点前131072位，以及小数点后16383位    |
| real             | 4字节        | 可变精度，不精确   | 6位十进制精度                                |
| double precision | 8字节        | 可变精度，不精确   | 15位十进制精度                               |
| smallserial      | 2字节        | 自动增加的小整数   | 1 到 32767                                     |
| serial           | 4字节        | 自动增加的整数     | 1 到 2147483647                                |
| bigserial        | 8字节        | 自动增长的大整数   | 1 到 9223372036854775807                       |

## 货币类型
money 类型存储固定小数精度的货币数字：

| **名字** | **存储尺寸** | **描述** | **范围**                                     |
| -------- | ------------ | -------- | -------------------------------------------- |
| money    | 8字节        | 货币额   | -92233720368547758.08 到 +92233720368547758.07 |

## 字符类型
TDSQL-A PostgreSQL版 列存表支持如下字符类型：
- character varying(n) 和 character(n) 类型， 其中 n 是一个正整数。两种类型都可以存储最多 n 个字符长的串。
- text 类型，可以存储任何长度的串。
- name 类型，用于在内部系统目录中存储标识符并且不是给一般用户使用的。该类型长度当前定为64字节（63可用字符加结束符），但在 C 源代码应该使用常量 NAMEDATALEN 引用。这个长度是在编译的时候设置的（因而可以为特殊用途调整），缺省的最大长度在以后的版本可能会改变。
- "char"（注意引号）类型，和 char(1) 不一样，它只用了一个字节的存储空间。它在系统内部用于系统目录当做简化的枚举类型用。

| **名字**                          | **描述**                     |
| --------------------------------- | ---------------------------- |
| character  varying(n), varchar(n) | 有限制的变长                 |
| character(n), char(n)             | 定长，空格填充               |
| text                              | 1GB                          |
| "char"                            | 1字节，单字节内部类型        |
| numeric                           | 64字节，用于对象名单内部类型 |

## 二进制数据类型
bytea 数据类型允许存储二进制串:

| **名字** | **存储尺寸**               | **描述**     |
| -------- | -------------------------- | ------------ |
| bytea    | 1或4字节外加真正的二进制串 | 变长二进制串 |

## 日期类型
TDSQL-A PostgreSQL版 列存表支持 SQL 中所有的日期和时间类型：

| **名字**                         | **存储尺寸** | **描述**                     | **最小值**    | **最大值**    | **解析度**   |
| -------------------------- | ------------ | --------------------- | ------------- | ------------- | ------------ |
| timestamp [ (p) ] [ without time zone ] | 8字节        | 包括日期和时间（无时区）     | 4713 BC       | 294276 AD     | 1微秒 / 14位 |
| timestamp [ (p) ] with time zone   | 8字节        | 包括日期和时间，有时区       | 4713 BC       | 294276 AD     | 1微秒 / 14位 |
| date                                     | 4字节        | 日期（没有一天中的时间）     | 4713 BC       | 5874897 AD    | 1日          |
| time [ (p) ] [ without time zone ]      | 8字节        | 一天中的时间（无日期）       | 0:00:00       | 24:00:00      | 1微秒 / 14位 |
| time [ (p) ] with time zone   | 12字节       | 仅仅是一天中的时间，带有时区 | 00:00:00+1459 | 24:00:00-1459 | 1微秒 / 14位 |
| interval [ fields ] [ (p) ]     | 16字节       | 时间间隔                     | -178000000年  | 178000000年   | 1微秒 / 14位 |

## 布尔类型
TDSQL-A PostgreSQL版 提供标准的 SQL 类型 boolean，boolean 可以有多个状态：“true（真）”、“false（假）”和第三种状态“unknown（未知）”，未知状态由 SQL 空值表示。

| **名字** | **存储字节** | **描述**     |
| -------- | ------------ | ------------ |
| boolean  | 1字节        | 状态为真或假 |

## 几何类型
几何数据类型表示二维的空间物体。TDSQL-A PostgreSQL版 列存表支持如下几种几何类型：

| **名字** | **存储尺寸** | **表示**                 | **描述**                |
| -------- | ------------ | ------------------------ | ----------------------- |
| point    | 16字节       | 平面上的点               | (x,y)                   |
| line     | 32字节       | 无限长的线               | {A,B,C}                 |
| lseg     | 32字节       | 有限线段                 | ((x1,y1),(x2,y2))       |
| box      | 32字节       | 矩形框                   | ((x1,y1),(x2,y2))       |
| path     | 16+16n字节   | 封闭路径（类似于多边形） | ((x1,y1),…)             |
| path     | 16+16n字节   | 开放路径                 | [(x1,y1),…]             |
| circle   | 24字节       | 圆                       | <(x,y),r>(中心点和半径) |

## 网络地址类型
网络地址类型是用于存储 IPv4、IPv6 和 MAC 地址的数据类型，用这些数据类型存储网络地址比用纯文本类型好，因为这些类型提供了输入错误检查以及特殊的操作符和函数。

| **名字** | **存储尺寸** | **描述**              |
| -------- | ------------ | --------------------- |
| cidr     | 7或19字节    | IPv4 和 IPv6 网络        |
| inet     | 7或19字节    | IPv4 和 IPv6 主机及网络  |
| macaddr  | 6字节        | MAC 地址               |
| macaddr8 | 8字节        | MAC 地址（EUI-64 格式） |

## 位串类型
位串就是1和0的串。它们可以用于存储和可视化位掩码。
支持两种类型的 SQL 位类型：bit(*n*) 和 bit varying(*n*)，其中 *n* 是一个正整数。
- bit 类型的数据必须准确匹配长度 *n*；试图存储短些或者长一些的位串都是错误的。
- bit varying 数据是最长 *n* 的变长类型，更长的串会被拒绝。
写一个没有长度的 bit 等效于 bit(1)，没有长度的 bit varying 则意味着没有长度限制。

示例：
```
postgres=# CREATE TABLE bit_test (col1 int,col2 BIT(3), col3 BIT VARYING(5))WITH(ORIENTATION=column);
CREATE TABLE
postgres=# INSERT INTO bit_test VALUES(1,B'101', B'00');
INSERT 0 1
postgres=# INSERT INTO bit_test VALUES(2,B'10'::bit(3), B'101');
INSERT 0 1
postgres=# SELECT * FROM bit_test;
 col1 | col2 | col3 
------+------+------
  1 | 101 | 00
  2 | 100 | 101
(2 rows)
```

## 文本搜索类型
TDSQL-A PostgreSQL版 提供两种数据类型：tsvector 和 tsquery，用来支持全文搜索。全文搜索是一种在自然语言的文档集合中，搜索以定位那些最匹配一个查询的文档的活动。

tsvector 类型表示一个为文本搜索优化的形式下的文档，一个 tsvector 值是一个排序的可区分词位列表，词位是被正规化合并了同一个词的不同变种的词，排序和去重是在输入期间自动完成的。

示例：
```
postgres=# SELECT 'a fat cat sat on a mat and ate a fat rat'::tsvector;
           tsvector           
----------------------------------------------------
 'a' 'and' 'ate' 'cat' 'fat' 'mat' 'on' 'rat' 'sat'
(1 row)
postgres=# SELECT $$the lexeme '  ' contains spaces$$::tsvector;
         tsvector         
-------------------------------------------
 '  ' 'contains' 'lexeme' 'spaces' 'the'
(1 row)
```
tsquery 类型表示一个文本查询。一个 tsquery 值存储要用于搜索的词位，并且使用布尔操作符`&（AND）、|（OR）`和`!（NOT）`来组合它们，还有短语搜索操作符`<->（FOLLOWED BY）`。也有一种 FOLLOWED BY 操作符的变体`<N>`，其中 N 是一个整数常量，它指定要搜索的两个词位之间的距离。`<->`等效于`<1>`。

圆括号可以被用来强制对操作符分组。如果没有圆括号，`!（NOT）`的优先级最高，其次是`<->（FOLLOWED BY）`，然后是`&（AND）`，最后是`|（OR）`。

示例：
```
postgres=# SELECT 'fat & rat'::tsquery;
  tsquery  
---------------
 'fat' & 'rat'
(1 row)
postgres=# SELECT 'fat & (rat | cat)'::tsquery;
     tsquery     
---------------------------
 'fat' & ( 'rat' | 'cat' )
(1 row)
postgres=# SELECT 'fat:ab & cat'::tsquery;
   tsquery   
------------------
 'fat':AB & 'cat'
(1 row)
```

## UUID 类型
数据类型 uuid 存储由 RFC 4122、ISO/IEC 9834-8:2005 以及相关标准定义的通用唯一标识符（UUID）（某些系统将这种数据类型引用为全局唯一标识符 GUID）。这种标识符是一个128位的量，它由一个精心选择的算法产生，该算法能保证在已知空间中，任何其他使用相同算法的人能够产生同一个标识符的可能性非常非常小。因此，对于分布式系统，这些标识符相比序列生成器而言提供了一种很好的唯一性保障，序列生成器只能在一个数据库中保证唯一。

一个 UUID 被写成一个小写十六进制位的序列，该序列被连字符分隔成多个组：首先是一个8位组，接下来是三个4位组，最后是一个12位组。总共的32位（十六进制位）表示了128个二进制位。一个标准形式的 UUID 类似于：
```
a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11
```

## XML 类型
XML 数据类型可以被用来存储 XML 数据。相比直接在一个 text 域中存储 XML 数据的优势在于，它会检查输入值的结构是不是良好，并且有支持函数用于在其上执行类型安全的操作。使用这种数据类型要求在安装时用 configure --with-libxml 选项编译。

XML 类型可以存储结构良好（如 XML 标准所定义）的“文档”，以及“内容”片段，它们由 XML 标准中的 XMLDecl? content 产品所定义。粗略地看，这意味着内容片段中可以有多于一个的顶层元素或字符节点。表达式 xmlvalue IS DOCUMENT 可以被用来评估一个特定的 XML 值是一个完整文档或者仅仅是一个文档片段。

## JSON 类型
JSON 数据类型是用来存储 JSON（JavaScript Object Notation）数据。这种数据也可以被存储为 text，但是 JSON 数据类型的优势在于，能强制要求每个被存储的值符合 JSON 规则。也有很多 JSON 相关的函数和操作符可以用于存储在这些数据类型中的数据。

JSON 数据类型有两种：json 和 jsonb。它们几乎接受完全相同的值集合作为输入，主要的实际区别之一是效率。
- json 数据类型存储输入文本的精准拷贝，处理函数必须在每次执行时必须重新解析该数据。
- jsonb 数据被存储在一种分解好的二进制格式中，它在输入时要稍慢一些，因为需要做附加的转换。但是 jsonb 在处理时要快很多，因为不需要解析。jsonb 也支持索引。

由于 json 类型存储的是输入文本的准确拷贝，其中可能会保留在语法上不明显的、存在于记号之间的空格，还有 JSON 对象内部的键的顺序。还有，如果一个值中的 JSON 对象包含同一个键超过一次，所有的键/值对都会被保留（处理函数会把最后的值当作有效值）。相反，jsonb 不保留空格、不保留对象键的顺序并且不保留重复的对象键。如果在输入中指定了重复的键，只有最后一个值会被保留。
通常，除非有特别特殊的需要（如遗留的对象键顺序假设），大多数应用应该更愿意把 JSON 数据存储为 jsonb。
示例：
```
postgres=# SELECT '5'::json;
 json 
------
 5
(1 row)

postgres=# SELECT '[1, 2, "foo", null]'::json;
    json     
---------------------
 [1, 2, "foo", null]
(1 row)

postgres=# SELECT '{"foo": [true, "bar"], "tags": {"a": 1, "b": null}}'::json;
            json             
-----------------------------------------------------
 {"foo": [true, "bar"], "tags": {"a": 1, "b": null}}
(1 row)
postgres=# SELECT '{"foo": {"bar": "baz"}}'::jsonb @> '{"foo": {}}'::jsonb;
 ?column? 
----------
 t
(1 row)

postgres=# SELECT '{"foo": {"bar": "baz"}}'::jsonb @> '{"bar": "baz"}'::jsonb;
 ?column? 
----------
 f
(1 row)
```

## 数组类型
允许一个表中的列定义为变长多维数组。可以创建任何内建或用户定义的基类、枚举类型或组合类型的数组。
一个数组数据类型可以通过在数组元素的数据类型名称后面加上方括号（[]）来命名。
示例：
```
postgres=# CREATE TABLE sal_emp (
postgres(#   name      text,
postgres(#   pay_by_quarter integer[],
postgres(#   schedule    text[][]
postgres(# )with(orientation=column);
CREATE TABLE
postgres=# INSERT INTO sal_emp
postgres-#   VALUES ('Bill',
postgres(#   '{10000, 10000, 10000, 10000}',
postgres(#   '{{"meeting", "lunch"}, {"training", "presentation"}}');
INSERT 0 1
postgres=# 
postgres=# INSERT INTO sal_emp
postgres-#   VALUES ('Carol',
postgres(#   '{20000, 25000, 25000, 25000}',
postgres(#   '{{"breakfast", "consulting"}, {"meeting", "lunch"}}');
INSERT 0 1
postgres=# SELECT * FROM sal_emp;
 name |   pay_by_quarter    |         schedule         
-------+---------------------------+-------------------------------------------
 Carol | {20000,25000,25000,25000} | {{breakfast,consulting},{meeting,lunch}}
 Bill | {10000,10000,10000,10000} | {{meeting,lunch},{training,presentation}}
(2 rows)
```

另一种符合 SQL 标准的语法是使用关键词 ARRAY，可以用来定义一维数组。
如上示例中 sal_emp 表中 pay_by_quarter 字段可定义为：
```
pay_by_quarter integer ARRAY[4],
```
或者不指定数组尺寸：
```
pay_by_quarter integer ARRAY,
```

## 枚举类型
枚举（enum）类型是由一个静态、值的有序集合构成的数据类型。它们等效于很多编程语言所支持的 enum 类型。枚举类型的一个例子可以是一周中的日期，或者一个数据的状态值集合。
枚举类型可以使用 CREATE TYPE 命令创建，创建后，枚举类型可以像其他类型 一样，在表和函数定义中使用：
示例：
```
postgres=# CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
CREATE TYPE
postgres=# CREATE TABLE person (
postgres(#   name text,
postgres(#   current_mood mood
postgres(# )WITH(ORIENTATION=column);
CREATE TABLE
postgres=# INSERT INTO person VALUES ('Moe', 'happy');
INSERT 0 1
postgres=# SELECT * FROM person WHERE current_mood = 'happy';
 name | current_mood 
------+--------------
 Moe | happy
(1 row)
```

## 复合类型
一个复合类型表示一行或一个记录的结构，它本质上就是一个域名和它们数据类型的列表。
示例：
```
postgres=# CREATE TYPE inventory_item AS (
postgres(#   name      text,
postgres(#   supplier_id   integer,
postgres(#   price      numeric
postgres(# );
CREATE TYPE
postgres=# CREATE TABLE on_hand (
postgres(#   item   inventory_item,
postgres(#   count   integer
postgres(# )WITH(ORIENTATION=column);
CREATE TABLE
postgres=# INSERT INTO on_hand VALUES (ROW('fuzzy dice', 42, 1.99), 1000);
INSERT 0 1
postgres=# SELECT * FROM on_hand;
     item     | count 
------------------------+-------
 ("fuzzy dice",42,1.99) | 1000
(1 row)
```

## 范围类型
范围类型是表达某种元素类型（称为范围的 subtype）一个值的范围的数据类型。例如，timestamp 的范围可以被用来表达一个会议室被保留的时间范围。在这种情况下，数据类型是 tsrange（“timestamp range” 的简写，而 timestamp 是 subtype。subtype 必须具有一种总体的顺序，这样对于元素值是在一个范围值之内、之前或之后就是界线清楚的）。

范围类型非常有用，因为它们可以表达一种单一范围值中的多个元素值，并且可以很清晰地表达诸如范围重叠等概念。用于时间安排的时间和日期范围是最清晰的例子，但是价格范围、一种仪器的量程等也都有用。

TDSQL-A PostgreSQL版 列存表支持如下内建范围类型：
- int4range — integer 的范围
- int8range — bigint 的范围
- numrange — numeric 的范围
- tsrange — 不带时区的 timestamp 的范围
- tstzrange — 带时区的 timestamp 的范围
- daterange — date 的范围

示例：
```
postgres=# CREATE TABLE reservation (room int, during tsrange)WITH(ORIENTATION=column);
CREATE TABLE
postgres=# INSERT INTO reservation VALUES
postgres-#   (1108, '[2010-01-01 14:30, 2010-01-01 15:30)');
INSERT 0 1
postgres=# SELECT * FROM reservation;
 room |          during           
------+-----------------------------------------------
 1108 | ["2010-01-01 14:30:00","2010-01-01 15:30:00")
(1 row)
```
