## 读取

| SQLServer 类型 | 内部类型 | 
|---------|---------|
|char(n)|	CHAR(n)|
| varchar(n)，nvarchar(n)，nchar(n)	| VARCHAR(n)| 
| text，ntext，xml	| STRING| 
| decimal(p, s)，money，smallmoney	| DECIMAL(p, s)| 
| numeric | NUMERIC| 
| REAL，FLOAT	| FLOAT| 
| bit	| BOOLEAN| 
| int	| INT| 
| tinyint	| TINYINT| 
| smallint| 	SMALLINT| 
| time (n)	| TIME (n)| 
| bigint	| BIGINT| 
| date	| DATE| 
| datetime2，datetime，smalldatetime	| TIMESTAMP(n)| 
| datetimeoffset	| TIMESTAMP_LTZ(3)| 

## 写入

| 内部类型 | SQLServer 类型 |
|---------|---------|
| CHAR(n)	| char(n)| 
| VARCHAR(n)	| varchar(n)，nvarchar(n)，nchar(n)| 
| STRING	| text，ntext，xml| 
| BIGINT	| BIGINT，BIGSERIAL| 
| DECIMAL(p, s)	| decimal(p, s)，money，smallmoney| 
| NUMERIC	| numeric| 
| FLOAT| 	float，real| 
| BOOLEAN	| bit| 
| INT| 	int| 
| TINYINT| 	tinyint| 
| SMALLINT| 	smallint| 
| BIGINT	| bigint| 
| TIME(n)	| time(n)| 
| TIMESTAMP(n)| 	datetime2，datetime，smalldatetime| 
| TIMESTAMP_LTZ(3)| 	datetimeoffset| 
