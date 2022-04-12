## 读取
### 配置参数说明

| 参数 | 说明 | 
|---------|---------|
| 数据源	| 选择已经配置好的 MySQL 数据源，此处仅支持 MySQL Binlog 方式同步（如果未配置数据源，请单击右侧的**新建数据源**，进入**项目管理 > 数据源管理**页面进行新建）<br> ![](https://qcloudimg.tencent-cloud.cn/raw/748208bc5dbcb4ca87c22725a3b38f20.png)| 
| 表	| 选择当前数据源下需要同步的表名称。MySQL 同步支持实现分库分表的场景，配置的库和表会在该任务中同时进行实时同步（分库分表中的数据表的 Schema 请保持一致，以避免执行报错）| 
| 格式	| 指定 MySQL 日志编码格式。当前版本支持 UTF-8、GBK、LATIN1、UTF8MB4四种格式| 

### 字段类型转换

| Kafka Schema 设定数据类型 | 同步任务转换类型 | 
|---------|---------|
| TINYINT	| TINYINT| 
| SMALLINT	| SMALLINT| 	
| INT	| INT	| 
| BIGINT	| BIGINT	| 
| FLOAT	| FLOAT	| 
| DOUBLE	| DOUBLE| 	
| DECIMAL	| DECIMAL	| 
| BOOLEAN	| BOOLEAN	| 
| DATE	| DATE	| 
| TIMESTAMP	| TIMESTAMP	| 
| CHAR(n)	| CHAR(n)| 	
| STRING	| STRING| 	
| BYTES	| BYTES| 	

## 分库分表
通过单击**分库分表**可以选择多个不同数据库下需要执行数据读取任务的库表，每次点击都会生成新的库表选择框，但分库分表需要保证所有表 schema 一致。
![](https://qcloudimg.tencent-cloud.cn/raw/ab18663115d320f642f8d768dccef28e.png)
