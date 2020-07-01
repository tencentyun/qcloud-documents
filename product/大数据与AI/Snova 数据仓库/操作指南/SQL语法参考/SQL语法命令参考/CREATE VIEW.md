定义一个新的视图。

## 概要

```sql
CREATE [OR REPLACE] [TEMP | TEMPORARY] VIEW name
       [ ( column_name [, ...] ) ]
       AS query
```

## 描述

CREATE VIEW 定义一个视图查询。该视图没有实际物。相反，每次在查询中引用该视图时，都会运行查询。

CREATE OR REPLACE VIEW 是相似的，但是如果同名的视图已经存在，则会被替换。用户只能使用生成相同列（相同列名称和数据类型）的新查询替换视图。

如果给定了模式名称，则在指定的模式名称中创建视图。否则，在当前的模式中创建该视图。临时视图存在于特殊的模式中，所以创建临时模式时不会给定模式名。该视图的名称与同模式中其他任何视图，表，序列或索引的名称必须不同。

## 参数

TEMPORARY | TEMP
如果指定，该视图创建为临时表。临时表在当前事务结束时自动删除。当临时表存在时，具有相同的名字的永久表在当前会话中不可见，除非他们使用方案限定名来引用。如果视图引用的任何表是临时的话，该视图会创建成一个临时表（不管是否指定 TEMPORARY ）。

name
要创建的表的名字（可选方案限定）。

column_name
可选名字列表用于视图的列。如果没有给定，该列名将从查询中推导而来。

query
SELECT 或 VALUES 命令，二者会提供视图的列和行。

## 注意
数据库中的视图是只读的。该系统不允许在视图上插入、更新或者删除。用户可以通过在视图上创建重写规则到其他表上的适当操作来获得可更新视图的效果。更多信息，请参阅 CREATE RULE。

请注意，视图列的名字和数据类型可以按照用户想要的方式分配。例如：

```sql
CREATE VIEW vista AS SELECT 'Hello World';
```

是两种不好的形式：该列名默认为 ?column?, 而且列的数据类型默认为 unknown。如果用户想在视图的结果中使用字符串文字，请使用以下内容：

```sql
CREATE VIEW vista AS SELECT text 'Hello World' AS hello;
```

视图中引用的表的访问由视图所有者的权限决定的，而不是当前用户（即使当前用户是超级用户）。这在超级用户的情况下可能会令人困惑，因为超级用户通常可以访问所有对象。在视图的这种情况下，如果用户不是视图的所有者，那么即使是超级用户也必须要明确被授予对视图引用表的访问权限才能访问。

但是，视图中调用函数的处理方式与使用视图从查询中直接调用的方式相同。因此，视图的用户必须要有具有调用视图使用的任何函数的权限。

如果用户使用 ORDER BY 子句创建了一个视图，则当用户从视图中执行 SELECT 时将忽略 ORDER BY 子句。

## 示例
创建所有包含 comedy 电影的视图：

```sql
CREATE VIEW comedies AS SELECT * FROM films WHERE kind = 
'comedy';
```

创建一个获取排名前10婴儿的名字：

```sql
CREATE VIEW topten AS SELECT name, rank, gender, year FROM 
names, rank WHERE rank < '11' AND names.id=rank.id;
```

## 兼容性

该 SQL 标准指定了不在数据库中的 CREATE VIEW 语句的一些附加功能。标准完整 SQL 命令的可选子句包括：
- **CHECK OPTION**：该选项和可更新视图有关。将检查视图上所有 INSERT 和 UPDATE 命令来确保数据满足视图定义条件（即新的数据将通过视图可见）。如果不满足条件，则拒绝该更新。
- **LOCAL**：检查视图上的完整性。
- **CASCADED**：检查此视图的和任何从属视图的完整性，假定为 CASCADED 如果不指定 CASCADED 或 LOCAL。

CREATE OR REPLACE VIEW 是数据库语言扩展，临时视图的概念也是如此。

## 另见
SELECT、DROP VIEW
