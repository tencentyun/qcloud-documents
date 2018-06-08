
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).

### Language structure

**DCDB supports all text formats used by MySQL. The following examples are just for illustration, which does not mean that the DCDB's supported text formats are different from those used by MySQL:**
```
	String Literals
	Numeric Literals
	Date and Time Literals
	Hexadecimal Literals
	Bit-Value Literals
	Boolean Literals
	NULL Values
```
#### String literals

A string literal is a sequence of bytes or characters enclosed in single quotation marks (') or double quotation marks ("). DCDB does not support ANSI_QUOTES SQL MODE. Only string literals rather than identifiers are enclosed in double quotation marks (").
The character set introducer ([_charset_name]'string' [COLLATE collation_name]) is not supported.
Supported escape characters include:
```
	\0: ASCII NUL (X'00') 
	\': Single quotation marks
	\": Double quotation marks
	\b: Backspace character
	\n: Line break
	\r: Carriage return
	Tab
	\z: ASCII 26 (Ctrl + Z)
	\\: Backslash \
	\%: \%
	\_: _
```

#### Numeric literals

Numeric literals include integers, decimal-point numbers, and floating-point numbers.
An integer may include a decimal separator "." and begin with a plus sign "+" or a minus sign "-" to indicate whether it is a positive or negative number.
The exact numeric literal can be expressed as follows: 1, .2, 3.4, -5, -6.78, +9.10.
Scientific notation: 1.2E3, 1.2E-3, -1.2E3, -1.2E-3.

#### Date and time literals

DATE supports the following formats:
```
	'YYYY-MM-DD' or 'YY-MM-DD'
	'YYYYMMDD' or 'YYMMDD'
	YYYYMMDD or YYMMDD
```
For example, '2012-12-31', '2012/12/31', '2012^12^31', '2012@12@31', '20070523', '070523'

DATETIME and TIMESTAMP support the following formats:
```
	'YYYY-MM-DD HH:MM:SS' or 'YY-MM-DD HH:MM:SS'
	'YYYYMMDDHHMMSS' or 'YYMMDDHHMMSS'
	YYYYMMDDHHMMSS or YYMMDDHHMMSS
```
For example, '2012-12-31 11:30:45', '2012^12^31 11+30+45', '2012/12/31 11*30*45', '2012@12@31 11^30^45', 19830905132800

#### Hexadecimal literals

The supported formats are as follows:
```
	X'01AF'
	X'01af'
	x'01AF'
	x'01af'
	0x01AF
	0x01af
```
#### Bit-Value literals

The supported formats are as follows:
```
	b'01'
	B'01'
	0b01
```
#### Boolean literals

The constants TRUE and FALSE are equal to 1 and 0, which are case insensitive.
```
	mysql>  SELECT TRUE, true, FALSE, false;
	+------+------+-------+-------+
	| TRUE | TRUE | FALSE | FALSE |
	+------+------+-------+-------+
	|    1 |    1 |     0 |     0 |
	+------+------+-------+-------+
	1 row in set (0.03 sec)
```
#### NULL values

Null is an absence of a value. It is case insensitive and has the same meaning as \N (case sensitive).
Note that NULL is not the same as 0 or the empty string ('').

