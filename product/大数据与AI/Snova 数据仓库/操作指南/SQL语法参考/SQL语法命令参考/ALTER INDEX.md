更改一个索引的定义。

## 概要

```sql
ALTER INDEX name RENAME TO new_name
 
ALTER INDEX name SET TABLESPACE tablespace_name
 
ALTER INDEX name SET ( FILLFACTOR = value )
 
ALTER INDEX name RESET ( FILLFACTOR )
```

## 描述
ALTER INDEX 更改一个现有索引的定义。有几种子形式：

**RENAME**
更改索引的名称。对存储的数据没有影响。

**SET TABLESPACE** 
将索引的表空间更改为指定的表空间，并将与索引关联的数据文件移动到新的表空间。另见 CREATE TABLESPACE。

**SET FILLFACTOR** 
更改索引的索引方法特定的存储参数。内置索引方法都要接受一个独有参数：FILLFACTOR。索引的 fillfactor 是一个百分比，用于确定索引方法将如何填充索引页。此命令不会立即修改索引内容。使用 REINDEX 重建索引以获得所需的效果。

**RESET FILLFACTOR**
将 FILLFACTOR 重置为默认值。与 SET 一样，可能需要 REINDEX 来完全更新索引。

## 参数
name
要修改的现有索引的名称（可选方案限定）。

new_name
索引的新名称。

tablespace_name
要移动索引的表空间。

FILLFACTOR
索引的填充因子是一个百分比，用于确定索引方法将如何填充索引页。对于 B 树，在初始索引编译期间，还会在右侧扩展索引（最大键值）时将页面填充到此百分比。如果页面随后变得完全充满，它们将被分割，导致索引效率逐渐下降。
B 树使用默认填充因子90，但是可以选择从10到100的任何值。如果表是静态的，那么 fillfactor 为100对最小化索引的物理大小是最好的，但是对于需要大量更新的表，较小的填充因子对最小化页分割来说是有利的。其他索引方法使用不同但大致相似的填充因子，默认填充因子因方法而异。

## 注意
这些操作也可以使用 ALTER TABLE。
不允许更改系统目录索引的任何部分。

## 示例
重命名现有索引：
```sql
ALTER INDEX distributors RENAME TO suppliers;
```

将索引移动到不同的表空间：
```sql
ALTER INDEX distributors SET TABLESPACE fasttablespace;
```

要更改索引的填充因子（假设 index 方法支持它）：
```sql
ALTER INDEX distributors SET (fillfactor = 75);
REINDEX INDEX distributors;
```

## 兼容性
ALTER INDEX 是一个数据库扩展。

## 另见
CREATE INDEX、REINDEX、ALTER TABLE
