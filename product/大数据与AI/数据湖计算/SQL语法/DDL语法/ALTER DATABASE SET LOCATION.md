修改某个数据库的存储位置。
## 语法
```
ALTER DATABASE database_name SET LOCATION cos_path;
```
## 参数
- `[database_name]`：数据库名字。
- `[cos_path]`：Tencent COS 对象存储路径。

## 示例
```
ALTER DATABASE db01 SET LOCATION 'cosn:///new/path'
```
