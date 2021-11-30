## 背景说明
云数据仓库 PostgreSQL 底层是基于 greenplum6 来构建，postgresql 内核为9.4版本，目前并不能很好支持 postgresql 的 `insert .. on conflict` 特性，所以对于 upsert 场景需要采用额外的方式来进行处理，这里提供一种利用 postgresql rule 特性来进行 upsert 的方法。

## 规则介绍
PostgreSQL 规则系统允许在更新、插入、删除时执行一个其它的预定义动作。简单的说，规则就是在指定表上执行指定动作的时候，将导致一些额外的动作被执行。另外，一个`INSTEAD`规则可以用另外一个命令取代特定的命令，或者完全不执行该命令。规则还可以用于实现表视图。规则实际上只是一个命令转换机制，或者说命令宏。这种转换发生在命令开始执行之前。

详细信息可参考 [rule 使用手册](https://www.postgresql.org/docs/9.4/sql-createrule.html)。

## upsert rule
如果需要实现 upsert 的操作，那么需要这样一条规则：当进行 insert 操作时，判断是否已经有相应的记录，如果存在记录则改为进行 update 操作，如果不存在记录则进行正常 insert 操作。

下面以一个数据库实例来进行说明：

创建一个测试数据库。
```
CREATE TABLE my_test(
   id integer,
   num1 integer,
   num2 decimal,
   str1 varchar(20),
   str2 text,
   PRIMARY KEY(id)
) distributed by (id);
```
然后给表增加 rule 规则。
```
create rule r1 as on insert to my_test where exists (select 1 from e t1 where t1.id=NEW.id limit 1) do instead update my_test set num1=NEW.num1,num2=NEW.num2,str1=NEW.str1,str2=NEW.str2 where id=NEW.id;
```
这条 rule 命令的含义就是针对 insert 操作，如果新的 insert 语句的 id 是存在，那么就直接用新 insert 里面的值 update 原来的数据，语句中的 NEW.XXX，即新 insert 语句的值，操作完成后可以看到。数据表中存在 rule 规则，接着进行 insert 操作，如果 id 存在，那么不会因为主键约束报错，而是进行 update 操作。
```
\d my_test
                                   Table "public.my_test"
 Column |         Type          | Collation | Nullable |               Default               
--------+-----------------------+-----------+----------+-------------------------------------
 id     | integer               |           | not null | nextval('my_test_id_seq'::regclass)
 num1   | integer               |           |          | 
 num2   | numeric               |           |          | 
 str1   | character varying(20) |           |          | 
 str2   | text                  |           |          | 
Indexes:
    "my_test_pkey" PRIMARY KEY, btree (id)
Rules:
    r1 AS
    ON INSERT TO my_test
   WHERE (EXISTS ( SELECT 1
	 FROM my_test my_test_1
 	WHERE my_test_1.id = new.id
	 LIMIT 1)) DO INSTEAD  UPDATE my_test SET num1 = new.num1, num2 = new.num2, str1 = new.str1, str2 = new.str2
```


## 使用注意
rule 规则使用存在一定局限，如下所示：
1. 因为 exists 对于 insert 批量插入处理不完善，如果语句没有设置唯一约束或者主键约束，可能在 insert 批量插入时产生重复数据，应尽量避免使用批量 insert，使用时也要避免需要判断 upsert 的字段不重复，或者对需要判断的字段增加唯一约束。例如下面这种批量操作，如果 id 没有主键约束，那么可能执行后存在重复数据。
```
insert into my_test (id,num1,num2,str1,str2)values(1,2,1.0,'111','555'),(1,3,2.0,'111','666');
```
2. rule 不支持 COPY 语句，COPY 语句效果和 insert 批处理类似，都可能导致重复数据。
3. 在设置 update 规则时，如果设置了 rule 用法，但是 insert 语句没有传 num1 和 num2 字段，这两个字段更新后会为空值，导致原数据丢失。
```
update my_test set num1=NEW.num1,num2=NEW.num2,str1=NEW.str1,str2=NEW.str2
```
