DLC 通过一套标准 SQL 语法几乎可以无缝在 DLC Serverless Spark 和 DLC Serverless Presto 引擎上运行。元数据和分析语法、函数，基本兼容 Hive 和 Spark 语法，支持自定义函数。
系统内置函数支持范围可参考 [统一函数](https://cloud.tencent.com/document/product/1342/76992)，如您需要使用 Presto 内置函数，使用方式及函数支持范围参见 [Presto 内置函数](https://cloud.tencent.com/document/product/1342/76993) 。
如您需要在数据湖计算中对外部 Iceberg 表进行数据查询分析，部分语法与原生表存在差异，具体可参见 [Iceberg 外部表与原生表语法差异](https://cloud.tencent.com/document/product/1342/81053)。

DLC 支持的语法如下表所示：

| 用途 | 语法 | 
|---------|---------|
| 查询数据表建表信息	| [SHOW CREATE TABLE](https://cloud.tencent.com/document/product/1342/61733)|
| 查询数据库中的视图| 	[SHOW VIEWS](https://cloud.tencent.com/document/product/1342/61771)|
| 查询表属性| 	[SHOW TBLPROPERTIES](https://cloud.tencent.com/document/product/1342/61777)|
| 查询数据库中的所有表和视图| 	[SHOW TABLES](https://cloud.tencent.com/document/product/1342/61780)| 
| 查询数据表分区信息| 	[SHOW PARTITIONS](https://cloud.tencent.com/document/product/1342/61784)|
| 展示视图创建语句|[ SHOW CREATE VIEW](https://cloud.tencent.com/document/product/1342/61785)|
| 展示在该元数据中定义的所有数据库| [SHOW DATABASES](https://cloud.tencent.com/document/product/1342/61786)	|
|查询数据表列信息	|[SHOW COLUMNS IN TABLE](https://cloud.tencent.com/document/product/1342/61787)|
|查看视图列信息	|[SHOW COLUMNS IN VIEW](https://cloud.tencent.com/document/product/1342/81052)|
| 删除视图	| [DROP VIEW](https://cloud.tencent.com/document/product/1342/61788) |
| 删除元数据表| [DROP TABLE](https://cloud.tencent.com/document/product/1342/61789)	|
| 更新分区信息| 	[MSCK REPAIR TABLE](https://cloud.tencent.com/document/product/1342/61790) |
| 删除数据库	| [DROP DATABASE](https://cloud.tencent.com/document/product/1342/61791) |
| 新建数据库| 	[CREATE DATABASE](https://cloud.tencent.com/document/product/1342/61792) |
| 新建数据表	| [CREATE TABLE](https://cloud.tencent.com/document/product/1342/61793)| 
| 将 select 结果创建为视图| [CREATE VIEW AS](https://cloud.tencent.com/document/product/1342/61796)	| 
| 数据库属性变更| [ALTER DATABASE SET DBPROPERTIES](https://cloud.tencent.com/document/product/1342/61797)	| 
| 数据库存储位置变更| [ALTER DATABASE SET LOCATION](https://cloud.tencent.com/document/product/1342/61799)	| 
| 数据表属性变更| [ALTER TABLE SET TBLPROPERTIES	](https://cloud.tencent.com/document/product/1342/61800)| 
| 数据表存储位置变更|[ ALTER TABLE SET LOCATION	](https://cloud.tencent.com/document/product/1342/61801)| 
| 向数据表添加列| [ALTER TABLE ADD COLUMNS](https://cloud.tencent.com/document/product/1342/61802)	| 
| 对数据表新增分区信息| [ALTER TABLE ADD PARTATION](https://cloud.tencent.com/document/product/1342/61804)	| 
| 删除数据表分区信息| [ALTER TABLE DROP PARTITION](https://cloud.tencent.com/document/product/1342/61805)	| 
| 对 Iceberg 表添加分区字段| 	[ALTER TABLE ADD PARTITION FIELD](https://cloud.tencent.com/document/product/1342/74174)| 
| 删除 Iceberg 表分区字段	| [ALTER TABLE DROP PARTITION FIELD](https://cloud.tencent.com/document/product/1342/74175)| 
|删除数据表某个字段|[ALTER TABLE DROP COLUMN](https://cloud.tencent.com/document/product/1342/81172)|
|对数据表新增列|[ALTER TABLE ADD COLUMN AFTER/FIRST](https://cloud.tencent.com/document/product/1342/81173)|
|修改视图名称|	[ALTER VIEW RENAME TO](https://cloud.tencent.com/document/product/1342/81175)|
|修改视图属性|	[ALTER VIEW SET TBLPROPERTIES](https://cloud.tencent.com/document/product/1342/81176)|
| 查看数据表列信息及元数据信息| [DESCRIBE TABLE](https://cloud.tencent.com/document/product/1342/61806)	| 
| 查看视图的列信息| [DESCRIBE VIEW](https://cloud.tencent.com/document/product/1342/61807)	| 
| 创建函数	| [CREATE FUNCTION](https://cloud.tencent.com/document/product/1342/61808) | 
|查看创建函数语法	|[SHOW FUNCTION](https://cloud.tencent.com/document/product/1342/81177)|
|展示执行 sql 的逻辑或物理计划	|[EXPLAIN](https://cloud.tencent.com/document/product/1342/82413)|
| 删除函数| [DROP FUNCTION](https://cloud.tencent.com/document/product/1342/61809)	| 
| 查看数据库属性	| [DESCRIBE DATABASE](https://cloud.tencent.com/document/product/1342/61811) | 
| 对数据表进行统计	|[ ANALYZE TABLES](https://cloud.tencent.com/document/product/1342/71414) | 
| 删除指定数据	| [DELETE STATEMENT](https://cloud.tencent.com/document/product/1342/61763) | 
| 插入一行数据	| [INSERT STATEMENT ](https://cloud.tencent.com/document/product/1342/61988)| 
| 替换一行数据| [INSERT OVERWRITE](https://cloud.tencent.com/document/product/1342/61990)	| 
|行级数据更新操作，可用于替换 INSERT OVERWRITE 操作	|[MERGE INTO](https://cloud.tencent.com/document/product/1342/81178)|
| 数据查询| [SELECT STATEMENT](https://cloud.tencent.com/document/product/1342/61991)	| 
| 将查询结果插入数据表| [INSERT INTO](https://cloud.tencent.com/document/product/1342/73084)	| 
| 删除 Iceberg 表的数据	| [DELETE STATEMENT](https://cloud.tencent.com/document/product/1342/74176)| 

相关查询保留字参见：[保留字](https://cloud.tencent.com/document/product/1342/61765)。
