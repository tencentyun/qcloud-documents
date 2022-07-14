如您需要阅读或下载全量开发文档，请参见 [TDSQL开发指南](https://cloud.tencent.com/document/product/557/7714)。

**TDSQL 支持所有 MySQL 使用的文字格式，此处只是列举，并不代表与 MySQL 有差异**
```
	String Literals
	Numeric Literals
	Date and Time Literals
	Hexadecimal Literals
	Bit-Value Literals
	Boolean Literals
	NULL Values
```

#### String Literals
String Literals 是一个 bytes 或 characters 的序列，两端被单引号'或者双引号"包围，目前 TDSQL 不支持 ANSI_QUOTES SQL MODE，双引号"包围的始终认为是 String Literals，而不是 identifier。
不支持 character set introducer，即 [_charset_name]'string' [COLLATE collation_name] 这种格式。
支持的转义字符：
```
	\0: ASCII NUL (X’00’) 字符
	\‘: 单引号
	\“: 双引号
	\b: 退格符号
	\n: 换行符
	\r: 回车符
	\t: tab 符（制表符）
	\z: ASCII 26 (Ctrl + Z)
	\\: 反斜杠 \
	\%: \%
	\_: _
```

#### Numeric Literals
数值字面值包括 integer 跟 Decimal 类型跟浮点数字面值。
integer 可以包括 . 作为小数点分隔，数字前可以有 - 或者 + 来表示正数或者负数。
精确数值字面值可以表示为如下格式：1, .2, 3.4, -5, -6.78, +9.10.。
科学记数法，如下格式：1.2E3, 1.2E-3, -1.2E3, -1.2E-3。

#### Date and Time Literals
DATE 支持如下格式：
```
	'YYYY-MM-DD' or 'YY-MM-DD'
	'YYYYMMDD' or 'YYMMDD'
	YYYYMMDD or YYMMDD
```
如：'2012-12-31', '2012/12/31', '2012^12^31',  '2012@12@31'  '20070523' , '070523'

DATETIME，TIMESTAMP 支持如下格式：
```
	'YYYY-MM-DD HH:MM:SS' or 'YY-MM-DD HH:MM:SS'
	'YYYYMMDDHHMMSS' or 'YYMMDDHHMMSS'
	YYYYMMDDHHMMSS or YYMMDDHHMMSS
```
如 '2012-12-31 11:30:45', '2012^12^31 11+30+45', '2012/12/31 11*30*45',  '2012@12@31 11^30^45'，19830905132800

#### Hexadecimal Literals
支持格式如下：
```
	X'01AF'
	X'01af'
	x'01AF'
	x'01af'
	0x01AF
	0x01af
```

#### Bit-Value Literals
支持格式如下：
```
	b'01'
	B'01'
	0b01
```

#### Boolean Literals
常量 TRUE 和 FALSE 等于 1 和 0，它是大小写不敏感的。
```
	mysql>  SELECT TRUE, true, FALSE, false;
	+------+------+-------+-------+
	| TRUE | TRUE | FALSE | FALSE |
	+------+------+-------+-------+
	|    1 |    1 |     0 |     0 |
	+------+------+-------+-------+
	1 row in set (0.03 sec)
```

#### NULL Values
NULL 代表数据为空，它是大小写不敏感的，与 \N(大小写敏感) 同义。
需要注意的是 NULL 跟 0 并不一样，跟空字符串 '' 也不一样。
