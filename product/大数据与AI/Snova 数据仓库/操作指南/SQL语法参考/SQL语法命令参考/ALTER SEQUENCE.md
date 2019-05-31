更改一个序列发生器的定义。

## 概要

```sql
ALTER SEQUENCE name [INCREMENT [ BY ] increment] 
     [MINVALUE minvalue | NO MINVALUE] 
     [MAXVALUE maxvalue | NO MAXVALUE] 
     [RESTART [ WITH ] start] 
     [CACHE cache] [[ NO ] CYCLE] 
     [OWNED BY {table.column | NONE}]
 
ALTER SEQUENCE name RENAME TO new_name
 
ALTER SEQUENCE name SET SCHEMA new_schema
```

## 描述
ALTER SEQUENCE更改一个现有序列发生器的参数。任何没有被明确设置的参数在ALTER SEQUENCE命中，都要维持他们之前的设置。

用户必须拥有该序列才能使用ALTER SEQUENCE。要更改一个序列的模式，用户还必须拥有新模式上的CREATE特权。 注意超级用户自动拥有所有的特权。

## 参数

name
要修改的序列的名称（可选方案限定）。

increment
子句INCREMENT BY increment是可选的。一个正值将产生一个上升序列，一个负值会产生一个下降序列。如果未被指定，则旧的增量值将被保持。

minvalue
NO MINVALUE
可选的子句MINVALUE minvalue决定一个序列能产生的最小值。如果NO MINVALUE被指定，如果指定了NO MINVALUE，上升序列和下降序列的默认值分别是1和-263-1。如果这些选项都没有被指定，将保持当前的最小值。

maxvalue
NO MAXVALUE
可选子句MAXVALUE maxvalue决定一个序列 能产生的最大值。如果NO MAXVALUE被指定，上升序列和下降序列的默认值分别是263-1和-1。如果这些选项都没有被指定，将保持当前的 最大值。

start
可选子句RESTART WITH更改该序列被记录的开始值。

cache
子句CACHE cache使得序列数字被预先分配并且保存在内存中以便更快的访问。最小值是1（每次只产生一个值，即无缓存）。如果没有指定，旧的缓冲值将被保持。

CYCLE
当一个上升或者下降序列已经达到maxvalue或者minvalue时，可选的CYCLE关键词可以被用来允许该序列绕回。如果达到限制，下一个被生成的数字将分别是minvalue或者maxvalue。

NO CYCLE
如果可选的NO CYCLE关键字被指定，在该序列达到其最大值后对nextval的任何调用将会返回错误。如果CYCLE或NO CYCLE都没有被指定，将维持旧的循环行为。

OWNED BY table.column
OWNED BY NONE
OWNED BY选项导致该序列与一个特定的表列相关联，这样如果该列（或者整个表）被删除，该序列也会被自动删除。 如果指定了关联，这种关联会替代之前为该序列指定的任何关联。被指定的表必须具有相同的拥有者并且与该序列在同一个模式中。OWNED BY NONE可以移除任何现有的关联。

new_name
该序列的新名称。

new_schema
该序列的新模式。

## 注解
为了避免从同一个序列获得数字的并发事务阻塞， ALTER SEQUENCE在该序列生成参数上的效果永远不会被回滚，那些更改立刻生效并且无法逆转。不过OWNED BY、RENAME TO以及SET SCHEMA子句会导致普通目录被更新并且无法被回滚。

ALTER SEQUENCE不会立即影响。nextval影响除当前后端外其他后端中的nextval结果，因为它们有预分配（缓存）的序列值。在注意到序列生成参数被更改之前它们将用尽所有缓存的值。当前会话将被立刻影响。

一些**ALTER TABLE**的变体可以很好的用于序列。例如重命名一个序列利用ALTER TABLE RENAME。

## 示例
重启一个被称为serial的序列在105：

```sql
ALTER SEQUENCE serial RESTART WITH 105;
```

## 兼容性
ALTER SEQUENCE符合SQL标准，OWNED BY、RENAME TO和SET SCHEMA子句除外，它们是数据库的扩展。

## 另见
CREATE SEQUENCE、DROP SEQUENCE、ALTER TABLE
