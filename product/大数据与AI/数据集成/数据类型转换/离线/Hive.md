## 读取

| Hive 数据类型 | 内部类型 | 
|---------|---------|
| TINYINT，SMALLINT，INT，BIGINT| 	Long| 
| FLOAT，DOUBLE	| Double| 
| String，CHAR，VARCHAR，STRUCT，MAP，ARRAY，UNION，BINARY| 	String| 
| BOOLEAN| 	Boolean| 
| Date，TIMESTAMP	| Date| 

## 写入

| 内部类型 | Hive 数据类型 |
|---------|---------|
| Long	| TINYINT，SMALLINT，INT，BIGINT| 
| Double	| FLOAT，DOUBLE| 
| String	| String，CHAR，VARCHAR，STRUCT，MAP，ARRAY，UNION，BINARY| 
| Boolean| 	BOOLEAN| 
| Date	| Date，TIMESTAMP| 
