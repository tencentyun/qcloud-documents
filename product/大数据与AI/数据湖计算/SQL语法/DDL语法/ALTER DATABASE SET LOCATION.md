## 说明
- 支持内核：Presto。
- 用途：修改数据库的存储路径。

## 标准语法
```
ALTER (DATABASE|SCHEMA) database_name SET LOCATION hdfs_path
```
## 参数
`[database_name]`：数据库名称。


## 示例
```
ALTER DATABASE db01 SET LOCATION 'cosn:///new/path'
```
