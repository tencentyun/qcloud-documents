更改文件空间的定义。

## 概要
```sql
ALTER FILESPACE name RENAME TO newname
 
ALTER FILESPACE name OWNER TO newowner
```

## 描述
ALTER FILESPACE 更改一个文件空间的定义。

用户必须拥有文件空间去 ALTER FILESPACE。要更改所有者，用户还必须是新的角色的直接或间接成员（**超级用户自动拥有这些权限**）。

## 参数
name
现有文件空间的名称。

newname
文件空间的新名称。新名称不能以 pg_ 和 gp_ 开头。为系统文件空间保留。

newowner
文件空间的新所有者。

## 示例
重命名文件空间 myfs为fast_ssd：

```sql
ALTER FILESPACE myfs RENAME TO fast_ssd;
```

更改表空间 myfs 的拥有者：

```sql
ALTER FILESPACE myfs OWNER TO dba;
```

## 兼容性
在 SQL 标准或 PostgreSQL 中没有 ALTER FILESPACE 语句。

## 另见
DROP FILESPACE
