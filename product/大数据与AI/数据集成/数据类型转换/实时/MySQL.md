## 读取

| MySQL 类型 | 内部类型 | 说明 |
|---------|---------|---------|
| TINYINT	| TINYINT	| -|
| SMALLINT，TINYINT，UNSIGNED	|SMALLINT	|-|
| INT，MEDIUMINT，SMALLINT，UNSIGNED| 	INT| -| 
|BIGINT，INT UNSIGNED	| BIGINT	| -| 
| BIGINT，UNSIGNED	| DECIMAL(20, 0)	| -| 
| REAL，FLOAT| 	FLOAT	| -| 
| DOUBLE	| DOUBLE	| -| 
| NUMERIC(p, s)，DECIMAL(p, s)where p <= 38		| DECIMAL(p, s)| -| 
| NUMERIC(p, s)，DECIMAL(p, s)where 38 < p <= 65	| STRING	| MySQL 中 DECIMAL 数据类型的精度最高为 65，而 inlong 内部使用 DECIMAL 的精度限制为 38。所以如果您定义一个精度大于38的十进制列，您应该把它映射到 STRING，以避免精度损失|
| BOOLEAN，TINYINT(1)，BIT(1)	| BOOLEAN	| -| 
| DATE	| DATE	| -| 
| TIME [(p)]	| TIME [(p)]	| -| 
| TIMESTAMP [(p)]，DATETIME [(p)]	| TIMESTAMP [(p)]	| -| 
| CHAR(n)	| CHAR(n)	| -| 
| VARCHAR(n)	| VARCHAR(n)	| -| 
| BIT(n)| 	BINARY(⌈n/8⌉)	| -|
BINARY(n)| 	BINARY(n)|	-| 
| VARBINARY(N)	| VARBINARY(N)	| -| 
| TINYTEXT，TEXT，MEDIUMTEXT，LONGTEXT	| STRING	| -| 
| TINYBLOB，BLOB，MEDIUMBLOB，LONGBLOB	| BYTES	| 目前，对于 MySQL 中的 BLOB 数据类型，仅支持长度不大于 2,147,483,647(2 * 31 - 1) 的 blob| 
|YEAR	|INT	|-	|
|ENUM		|STRING		|-	|
| JSON	| STRING	| JSON 数据类型会在 Flink 中转换为 JSON 格式的 STRING| | 
| SET	| ARRAY<STRING>| 	由于 MySQL 中的 SET 数据类型是一个可以有零个或多个值的字符串对象，所以它应该总是映射到一个字符串数组| 

## 写入

| 内部类型 | MySQL 类型 | 
|---------|---------|
| TINYINT	| TINYINT| 
| SMALLINT	| SMALLINT，TINYINT UNSIGNED| 
| INT	| INT，MEDIUMINT，SMALLINT UNSIGNED| 
| BIGINT	| BIGINT，INT UNSIGNED| 
| DECIMAL(20, 0)	| BIGINT UNSIGNED| 
| FLOAT	| FLOAT| 
| DOUBLE	| DOUBLE，DOUBLE PRECISION| 
| DECIMAL(p, s)	| NUMERIC(p, s)，DECIMAL(p, s)| 
| BOOLEAN| 	BOOLEAN，TINYINT(1)| 
| DATE	| DATE| 
| TIME [(p)][WITHOUT TIMEZONE]	| TIME [(p)]| 
| TIMESTAMP [(p)][WITHOUT TIMEZONE]	| DATETIME [(p)]| 
| STRING	| CHAR(n)，VARCHAR(n)，TEXT| 
| BYTES	| BINARY，VARBINARY，BLOB| 
| ARRAY	| -| 

