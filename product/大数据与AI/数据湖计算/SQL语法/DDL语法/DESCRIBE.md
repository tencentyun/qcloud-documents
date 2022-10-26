## 说明
- 支持内核：Presto、SparkSQL。
- 用途：查看数据库属性。

## 标准语法
```
DESCRIBE SCHEMA|DATABASE [EXTENDED] DB_NAME
```
## 参数
- `SCHEMA|DATABASE`：指定库为 SCHEMA 或者 DATABASE。
- `EXTENDED`：该库是否为 EXTENDED。


## 示例
```
DESCRIBE DATABASE db_name;
DESCRIBE DATABASE EXTENDED db_name;
```
