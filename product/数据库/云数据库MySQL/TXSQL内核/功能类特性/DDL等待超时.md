## 功能介绍
DDL 等待超时功能支持在获得 MDL 元数据锁前则 DDL 操作等待超时。

## 适用场景
该功能适用于线上 ALTER TABLE 操作时，可能会系统正常运行的场景。

## 使用说明
可以通过在操作语句时添加关键字参数来实现功能，支持以下 DDL 操作：
- ALTER TABLE `table` [NO_WAIT | WAIT [n]] `command`;                       
- DROP TABLE `table` [NO_WAIT | WAIT [n]];                                  
- TRUNCATE TABLE `table` [NO_WAIT | WAIT [n]];                              
- OPTIMIZE TABLE `table` [NO_WAIT | WAIT [n]];                              
- RENAME TABLE `table_src` [NO_WAIT | WAIT [n]] TO `table_dst`;             
- CREATE INDEX `index` ON `table.columns` [NO_WAIT | WAIT [n]];             
- CREATE FULLTEXT INDEX `index` ON `table.columns` [NO_WAIT | WAIT [n]];    
- CREATE SPATIAL INDEX `index` ON `table.columns` [NO_WAIT | WAIT [n]];     
- DROP INDEX `index` ON `table` [NO_WAIT | WAIT [n]];

NO_WAIT: the DDL would return immediately, and print                        
"ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction;"
if it has to wait for a metadata lock;                                      
                                                                                
WAIT [n]: n is the wait time in seconds for a metadata lock before the DDL  
returns and raises error message;          
