本文介绍 DTF 在 FMT 模式下支持的 DML 语句类型、SQL 实例，请在使用 FMT 模式时遵循相关的规范。
>!使用 FMT 模式时，客户端与 MySQL 的时区需要保持一致，否则将出现两端数据不一致的问题。

| DML 类型	| SQL 实例	| 语句支持 | 
| --- | --- | --- | 
| INSERT	| INSERT INTO tb1_name (col_name,...)VALUES ({expr \| FAULT},...),(...),...<br> INSERT INTO tb1_nameSET col_name={expr \| DEFAULT}, ...	| 是 | 
| UPDATE	 | UPDATE tb1_nameSET col_name1=expr1 [, col_name2=expr2 ...][WHERE where_definition]	| 是 | 
| DELETE	| DELETE FROM tb1_name [WHERE where_definition]	| 是 |
| SELECT	| SELECT [ALL \| DISTINCT \| DISTINCTROW ]select_expr, ... FROM tb1_name[WHERE where_definition]	| 是 |
| REPLACE	| REPLACE [LOW_PRIORITY \| DELAYED][INTO] tb1_name [(col_name,...)]VALUES ({expr \| DEFAULT},...),(...),...<br> REPLACE  [LOW_PRIORITY \| DELAYED][INTO] tb1_nameSET col_name={expr \| DEFAULT}, ...| 	否 |
| TRUNCATE	| TRUNCATE [TABLE] tb1_name	 | 否 | 

