定义访问特权。

## 概要

```sql
GRANT { {SELECT | INSERT | UPDATE | DELETE | REFERENCES | 
TRIGGER | TRUNCATE } [,...] | ALL [PRIVILEGES] }
    ON [TABLE] tablename [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { {USAGE | SELECT | UPDATE} [,...] | ALL [PRIVILEGES] }
    ON SEQUENCE sequencename [, ...]
    TO { rolename | PUBLIC } [, ...] [WITH GRANT OPTION]
 
GRANT { {CREATE | CONNECT | TEMPORARY | TEMP} [,...] | ALL 
[PRIVILEGES] }
    ON DATABASE dbname [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { EXECUTE | ALL [PRIVILEGES] }
    ON FUNCTION funcname ( [ [argmode] [argname] argtype [, ...] 
] ) [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { USAGE | ALL [PRIVILEGES] }
    ON LANGUAGE langname [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { {CREATE | USAGE} [,...] | ALL [PRIVILEGES] }
    ON SCHEMA schemaname [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { CREATE | ALL [PRIVILEGES] }
    ON TABLESPACE tablespacename [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT parent_role [, ...] 
    TO member_role [, ...] [WITH ADMIN OPTION]
 
GRANT { SELECT | INSERT | ALL [PRIVILEGES] } 
    ON PROTOCOL protocolname
    TO username
```

## 描述
GRANT 命令由两种基本的变体：一种授予在一个数据库对象（表、列、视图、外部表、序列、数据库、外部数据包装器、外部服务器、函数、过程语言、方案或表空间）上的特权，另一个授予一个角色中的成员关系。

**在数据库对象上的 GRANT**
这种 GRANT 命令的变体将一个数据库对象上的指定特权交给一个或多个角色。如果有一些已经被授予，这些特权会被加入到它们之中。

关键词 PUBLIC 指示特权要被授予给所有角色，包括那些可能稍后会被创建的角色。PUBLIC 可以被认为是一个被隐式定义的总是包含所有角色的组。任何特定角色都将具有直接授予给它的特权、授予给它作为成员所在的任何角色的特权以及被授予给 PUBLIC 的特权。

如果指定了WITH GRANT OPTION，特权的接收者可以接着把它授予给其他人。如果没有授权选项，接收者就不能这样做。授权选项不能被授予给 PUBLIC。

没有必要把权限授予给一个对象的拥有者（通常就是创建该对象的用户）， 因为拥有者默认具有所有的特权。删除一个对象或者以任何方式修改其定义的权力是不被当作一个可授予特权的，它被固化在拥有者中，并且不能被授予和撤回。拥有者也隐式地拥有该对象的所有授权选项。

会把某些类型的对象上的默认特权授予给 PUBLIC。默认不包括对表、方案以及表空间的公共访问；CONNECT 特权以及数据库中对 TEMP 表的创建特权；函数的 EXECUTE 特权；语言的 USAGE 特权。对象的拥有者当然可能 revoke 这些特权。

**角色上的 GRANT**
GRANT 命令的这种变体把一个角色中的成员关系授予一个或者多个其他角色。一个角色中的成员关系是有意义的，因为它会把授予给一个角色的特权带给该角色的每一个成员。

如果指定了 WITH ADMIN OPTION ，成员接着可以把该角色中的成员关系授予给其他用户，也可以撤回该角色中的成员关系。 数据库超级用户能够授予或撤回任何角色中任何人的成员关系。具有CREATEROLE 特权的角色能够授予或者撤回任何非超级用户角色中的成员关系。

和特权的情况不同，一个角色中的成员关系不能被授予 PUBLIC。

**协议上的 GRANT**
当创建一个用户协议后，指定 specify CREATE TRUSTED PROTOCOL 能够允许任何一个除了其拥有者来访问它。如果协议是不可信的，用户不能给任何其他用户通过该协议来读或者写数据。当一个 TRUSTED 协议被创建后，可以用 GRANT 命令指定哪些用户可以访问它。
- 为了让一个用户能够创建带有可信协议的外部可读表，使用：
```sql
GRANT SELECT ON PROTOCOL protocolname TO username
```
- 为了让一个用户能够创建带有可信协议的外部可写表，使用：
```sql
GRANT INSERT ON PROTOCOL protocolname TO username
```
- 为了让一个用户能够创建带有可信协议的外部可读且可写表，使用：
```sql
GRANT ALL ON PROTOCOL protocolname TO username
```

## 参数
SELECT
允许从指定表、视图或序列的任何列或者列出的特定列进行 SELECT，还允许使用 COPY TO。对于序列，这个特权也允许使用 ccurrval 函数。

INSERT
允许 INSERT 一个新行到指定表中。还允许 COPY FROM。

UPDATE
允许对指定表的特定列进行 UPDATE。SELECT ... FOR UPDATE 和 SELECT ... FOR SHARE 也需要该特权（同时也要 SELECT 特权）。对于序列，这个特权允许使用 nextval 和 setval 函数。

DELETE
允许从指定的表中 DELETE 一行。

REFERENCES
这个关键词是可以接受的，尽管现在外键约束在数据库中还不支持。要创建一个外键约束，必须在引用列和被引用列上都有这个特权。

TRIGGER
允许在指定的表上创建触发器。
注解： 数据库不支持触发器。

TRUNCATE
允许在指定表上使用 TRUNCATE 。

CREATE
对于数据库，允许在其中创建新方案。
对于方案，允许在其中创建新的对象。要重命名一个已有对象，用户必须拥有该对象并且具有所在方案的这个特权。
对于表空间，允许在其中创建表、索引，并且允许创建使用该表空间作为默认表空间的数据库（注意撤回这个特权将不会更改现有对象的放置位置）。

CONNECT
允许用户连接到指定数据库。在连接开始时会检查这个特权（除了检查由 pg_hba.conf 施加的任何限制之外）。

TEMPORARY
TEMP
允许在使用指定数据库时创建临时表。

EXECUTE
允许使用指定的函数以及使用在该函数之上实现的任何操作符。这是适用于函数的唯一一种特权类型（这种语法也可用于聚集函数）。

USAGE
对于过程语言，允许使用指定的语言创建函数。这是适用于过程语言的唯一一种特权类型。
对于方案，允许访问包含在指定方案中的对象（假定这些对象的拥有特权要求也满足）。本质上这允许被授权者在方案中“查阅”对象。
对于序列，这种特权允许使用 currval 和 nextval 函数。

ALL PRIVILEGES
一次授予所有的可用特权。在数据库中，PRIVILEGES 关键词是可选的，但是在严格的 SQL 中是要求它的。

PUBLIC
一个特别的组级别的角色，它指示了那些授予给所有角色的特权，包括后来可能会被创建的。

WITH GRANT OPTION
特权接受者可以把该特权授予给其他的用户。

WITH ADMIN OPTION
成员接着可以把该角色中的成员关系授予给其他用户。

## 注解
数据库超级用户可以访问所有对象而不管对象特权的设置。对于该规则的一个例外是视图。访问一个视图中引用的表取决于视图的拥有者而不是当前用户（即使当前用户是超级用户）。

如果一个超级用户选择发出一个 GRANT 或者 REVOKE 命令，该命令将被执行，好像它是由被影响对象的拥有者发出的一样。特别地，通过这样一个命令授予的特权将好像是由对象拥有者授予的一样。对于角色成员关系，该成员关系好像是由该角色本身授予的一样。

GRANT 以及 REVOKE 也可以由一个不是受影响对象拥有者的角色完成，不过该角色是拥有该对象的角色的一个成员，或者是在该对象上持有特权的 WITH GRANT OPTION 的角色的一个成员。在这种情况下，特权将被记录为由实际拥有该对象的角色授予或者是由持有特权的 WITH GRANT OPTION 的角色授予。

授予一个表上的权限不会自动地扩展权限给该表使用的任何序列，包括绑定在 SERIAL 列上的序列。序列上的权限必须被独立设置。

数据库不支持授予或者回收一个表上单独列上的特权。一个可选的方案是在需要赋予的特权的列上创建视图，然后授予视图特权。

使用 psql 的 \z 命令能够获取一个对象上现在存在的特权信息。

## 示例
授予所有角色在表 mytable 上的插入特权：

```sql
GRANT INSERT ON mytable TO PUBLIC;
```

授予所有可以的特权给角色 sally 在视图 topten 上。注意只有在超级用户或者视图 topten 拥有者执行时才会真正的将所有特权都授予，如果执行的是其他用户，那么只会授予角色现在拥有的可进行授予的特权：

```sql
GRANT ALL PRIVILEGES ON topten TO sally;
```

将角色 admins 授予用户 joe：

```sql
GRANT admins TO joe;
```

## 兼容性
在 SQL 标准中， PRIVILEGES 关键词是必需的，但是在数据库中是可选的。SQL 标准不支持在每个命令中设置超过一个对象上的特权。

数据库允许一个用户的拥有者撤回它们拥有的普通特权：一个表拥有者可以通过撤回其自身拥有的 INSERT、UPDATE、DELETE 和 TRUNCATE 特权让该表对它们自己只读。根据 SQL 标准这是不可能发生的。原因在于数据库认为拥有者的特权是由拥有者授予给它们自己的，因此它们也能够撤回它们。在 SQL 标准中，拥有者的特权是有一个假设的实体 *system* 所授予。

SQL 标准允许在一个表的单独列上设置特权。

SQL 标准提供了其他对象类型上的 USAGE 特权：字符集、排序规则、翻译、域。数据库、表空间、方案和语言上的特权都是数据库扩展。

## 另见
REVOKE
