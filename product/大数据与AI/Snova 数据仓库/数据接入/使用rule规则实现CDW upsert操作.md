**背景**: CDW(云数据仓库)底层是基于greenplum6来构建，postgresql内核为9.4版本，目前并不能很好支持postgresql的insert .. on conflict特性,所以对于upsert场景需要采用额外的方式来进行处理，这里提供一种利用postgresql rule特性来进行upsert的方法:

**rule规则介绍:**

PostgreSQL规则系统允许在更新、插入、删除 时执行一个其它的预定义动作。简单的说，规则就是在指定表上执行指定动作 的时候，将导致一些额外的动作被执行。另外，一个`INSTEAD` 规则可以用另外一个命令取代特定的命令，或者令完全不执行该命令。规则 还可以用于实现表视图。规则实际上只是一个命令转换机制，或者说命令宏。 这种转换发生在命令开始执行之前。

详细信息可以参考:[rule使用手册](https://m.php.cn/manual/view/20779.html)

**upsert rule**

如果需要实现upsert的操作，那么需要这样一条规则:当进行insert操作的时候，判断是否已经有相应的记录，如果存在记录则改为进行update操作，如果不存在记录则进行正常insert操作

下面以一个数据库实例来进行说明:

创建一个测试数据库

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

然后需要给表增加rule规则

```
create rule r1 as on insert to my_test where ff(NEW.id) do instead update my_test set num1=NEW.num1,num2=NEW.num2,str1=NEW.str1,str2=NEW.str2 where id=NEW.id;
```

这里可以看到这条rule命令的含义就是针对insert操作，如果新的insert语句的id是存在，那么就直接用新insert里面的值update原来的数据，语句中的NEW.XXX，就新insert语句的值，操作完成后可以看到

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

数据表中存在rule规则，接着进行insert操作，如果id存在，那么不会因为主键约束报错，而是进行update操作

**使用注意:**

rule规则使用存在一定局限，如下所示

1.因为exists对于insert批量插入处理不完善，如果语句没有设置唯一约束或者主键约束，可能在insert批量插入时产生重复数据，尽量避免使用批量insert，使用时也要避免需要判断upsert的字段不重复，或者对需要判断的字段增加唯一约束,例如:

```
insert into my_test (id,num1,num2,str1,str2)values(1,2,1.0,'111','555'),(1,3,2.0,'111','666');
```

这种批量操作，如果id没有主键约束，那么可能执行后存在重复数据

2.rule不支持COPY语句，COPY语句效果和insert 批处理类似，都可能导致重复数据

3.rule用法在设置update规则的时候如果设置了

```
update my_test set num1=NEW.num1,num2=NEW.num2,str1=NEW.str1,str2=NEW.str2
```

但是insert语句没有传num1和num2字段，这两个字段更新后会为空值，导致原数据丢失，这里要注意！
