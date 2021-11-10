删除命名数据库。如果数据库包含表，则必须在运行 drop database 之前删除这些表，或者使用 CASCADE 子句进行级联删除。
## 语法
```
DROP {DATABASE | SCHEMA} [IF EXISTS] database_name [RESTRICT | CASCADE]
```
## 参数
- `[IF EXISTS]`：如果名为 database_name 的库不存在删除就会报错。
- `[RESTRICT|CASCADE]`
 - RESTRICT：如果数据库包含表，则不会删除该数据库，如果不写默写是该模式。
 - CASCADE：会强制删除所有数据库表。

## 示例
```
DROP DATABASE clickstreams;
DROP SCHEMA clickstreams;
DROP DATABASE `DB1` RESTRICT;
DROP DATABASE IF EXISTS `DB1` RESTRICT;
```
