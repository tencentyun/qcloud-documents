移除一个表。

## 概要
```sql
DROP TABLE [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

## 描述
DROP TABLE 从数据库移除表。只有表拥有者、模式拥有者和超级用户能删除一个表。要清空一个表中的行但是不销毁该表，可以使用 DELETE 或者 TRUNCATE。

DROP TABLE 总是移除目标表的任何索引、规则、触发器和约束。不过，要删除一个被视图或者另一个表的外键约束所引用的表， 必须指定 CASCADE。CASCADE 将会把依赖的视图也完全移除。

## 参数

IF EXISTS
如果该表不存在则不会抛出一个错误，而是发出一个提示。

name
要删除的表的名称（可以是方案限定的）。

CASCADE
自动删除依赖于该表的对象（例如视图），然后删除所有依赖于那些对象的对象。

RESTRICT
如果有任何对象依赖于该表，则拒绝删除它。这是默认值。

## 示例
移除一个名为 mytable 的表：

```sql
DROP TABLE mytable;
```

## 兼容性
DROP TABLE 符合 SQL 标准，不过该标准只允许每个命令删除一个表并且没有 IF EXISTS 选项。

## 另见
CREATE TABLE、ALTER TABLE、TRUNCATE
