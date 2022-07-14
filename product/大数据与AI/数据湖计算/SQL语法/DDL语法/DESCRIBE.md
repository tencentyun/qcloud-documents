返回表的列信息以及元数据信息。
## 语法
```
DESCRIBE SCHEMA|DATABASE [EXTENDED] DB_NAME;
```
## 参数
- SCHEMA|DATABASE：指定库为 SCHEMA 或者 DATABASE。
- EXTENDED：该库是否为 EXTENDED。

## 示例
```
DESCRIBE DATABASE db_name;
DESCRIBE DATABASE EXTENDED db_name;
```
