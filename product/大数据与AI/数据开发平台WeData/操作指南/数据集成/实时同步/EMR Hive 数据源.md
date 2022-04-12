## 写入
### 参数信息说明

| 参数 | 说明 | 
|---------|---------|
| 数据源	| 选择项目下绑定的 EMR Hive 数据源| 
|目标 DB	| 选择当前数据源下需要同步的数据库名称| 
| 目标表名	| 选择当前数据源下需要同步的表名称，可单击**一键生成目标表**根据源表结构快速构建 Hive 表| 


### 字段类型转换

| Kafka Schema 设定数据类型 | 同步任务转换类型 | 
|---------|---------|
| TINYINT	| TINYINT| 
| SMALLINT	| SMALLINT| 
| INT	| INT	| 
| BIGINT	| BIGINT| 	
| FLOAT| 	FLOAT	| 
| DOUBLE	| DOUBLE	| 
| DECIMAL	| DECIMAL| 	
| BOOLEAN	| BOOLEAN	| 
| DATE| 	DATE	| 
| TIMESTAMP| 	TIMESTAMP	| 
| CHAR(n)	| CHAR(n)	| 
| STRING| 	STRING| 	
| BYTES	| BYTES	| 
