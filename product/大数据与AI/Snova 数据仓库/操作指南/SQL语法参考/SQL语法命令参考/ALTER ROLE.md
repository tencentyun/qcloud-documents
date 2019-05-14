更改一个数据库角色（用户或组）。

## 概要

```sql
ALTER ROLE name RENAME TO newname
 
ALTER ROLE name SET config_parameter {TO | =} {value | DEFAULT}
 
ALTER ROLE name RESET config_parameter
 
ALTER ROLE name RESOURCE QUEUE {queue_name | NONE}
 
ALTER ROLE name [ [WITH] option [ ... ] ]
```

其中option可以是：

```sql
      SUPERUSER | NOSUPERUSER
    | CREATEDB | NOCREATEDB
    | CREATEROLE | NOCREATEROLE
    | CREATEEXTTABLE | NOCREATEEXTTABLE 
      [ ( attribute='value'[, ...] ) ]
           where attributes and value are:
           type='readable'|'writable'
           protocol='gpfdist'|'http'
    | INHERIT | NOINHERIT
    | LOGIN | NOLOGIN
    | CONNECTION LIMIT connlimit
    | [ENCRYPTED | UNENCRYPTED] PASSWORD 'password'
    | VALID UNTIL 'timestamp'
    | [ DENY deny_point ]
    | [ DENY BETWEEN deny_point AND deny_point]
    | [ DROP DENY FOR deny_point ]
```

## 描述
ALTER ROLE更改数据库角色的属性。此命令有几种变体：

**RENAME** 
更改角色的名称。数据库超级用户可以重命名任何角色。角色有CREATEROLE特权可以重命名非超级用户角色。无法重命名当前会话用户（以其他用户身份连接重命名角色）。因为MD5加密的密码使用角色名称作为密钥，如果密码为MD5加密，则重命名角色将清除其密码。

**SET | RESET** 
更改指定配置参数的角色的会话默认值。 每当角色随后启动新会话时，指定的值将成为会话默认值，覆盖服务器配置文件中存在的任何设置（postgresql.conf）。
对于没有LOGIN权限的角色，会话默认值没有任何效果。
普通角色可以更改自己的会话默认值。
超级用户可以更改任何人的会话默认值。 
有CREATEROLE特权的角色可以更改非超级用户角色的默认值。参考“数据库管理员指南”获取有关所有用户可设置的配置参数的信息。

**RESOURCE QUEUE** 
将角色分配给工作负载管理资源队列。在发出查询时，角色将受到分配资源队列的限制。指定NONE将角色分配给默认资源队列。一个角色只能属于一个资源队列。对于没有LOGIN 特权的角色，会话默认值没有任何作用。参考**CREATE RESOURCE QUEUE**获取更多信息。

**WITH** 
更改在**CREATE ROLE**中指定的角色的许多属性。命令中未提及的属性保留其以前的设置。数据库超级用户可以更改任何这些设置的任何角色。角色有CREATEROLE权限可以更改任何这些设置，但只能用于非超级用户角色。普通角色只能改变自己的密码。

## 参数

name
角色的名称，其属性将被更改。

newname
角色的新名称。

config_parameter=value
将指定配置参数的此角色的会话默认值设置为给定值。如果值为DEFAULT或者如果RESET被使用时，角色特定的变量设置被删除，因此该角色将在新会话中继承系统范围的默认设置。使用RESET ALL清除所有特定于角色的设置。 

queue_name
要分配用户级角色的资源队列的名称。 只有有LOGIN特权的角色可以分配给资源队列。要从资源队列中取消分配角色并将其置于默认资源队列中，请指定NONE。角色只能属于一个资源队列。

SUPERUSER | NOSUPERUSER
CREATEDB | NOCREATEDB
CREATEROLE | NOCREATEROLE
CREATEEXTTABLE | NOCREATEEXTTABLE [(attribute='value')]
如果CREATEEXTTABLE 被指定， 允许定义的角色创建外部表。如果没被指定，默认类型是可读并且默认协议是gpfdist 。NOCREATEEXTTABLE（默认）拒绝角色有创建外部表的能力。 注意使用的外部表file或execute协议只能由超级用户创建。

INHERIT | NOINHERIT
LOGIN | NOLOGIN
CONNECTION LIMIT connlimit
PASSWORD password
ENCRYPTED | UNENCRYPTED
VALID UNTIL 'timestamp'
这些子句通过CREATE ROLE改变了原来设置的角色属性。

DENY deny_point
DENY BETWEEN deny_point AND deny_point
DENY 和DENY BETWEEN关键字设置了在登录时强制执行的基于时间的约束。DENY设置一天或一天的时间来拒绝访问。DENY BETWEEN设置访问被拒绝的间隔。两者都使用以下格式的参数 deny_point：

```sql
DAY day [ TIME 'time' ]
```

deny_point两部分参数使用以下格式：

对于day：

```sql
{'Sunday' | 'Monday' | 'Tuesday' |'Wednesday' | 'Thursday' | 'Friday' | 
'Saturday' | 0-6 }
```

对于time：

{ 00-23 : 00-59 | 01-12 : 00-59 { AM | PM }}

DENY BETWEEN子句使用两种deny_point参数。

```sql
DENY BETWEEN deny_point AND deny_point
```

有关基于时间的约束和示例的更多信息，参考“数据库管理员指南”中的“管理角色和特权”。

DROP DENY FOR deny_point
该DROP DENY FOR子句从角色中删除基于时间的约束。它使用上述的deny_point 参数。

有关基于时间的约束和示例的更多信息，参考“数据库管理员指南”中的“管理角色和特权”。

## 注解
使用GRANT和REVOKE用于添加和删除角色成员资格。
使用此命令指定未加密的密码时，必须小心。密码将以明文形式发送到服务器，也可能会记录在客户端的命令历史记录或服务器日志中。 该psql命令行客户端包含一个元命令\password可用于安全地更改角色的密码。

还可以将会话默认值与特定数据库而不是角色绑定。如果存在冲突，则特定于角色的设置将覆盖数据库特定的设置。参考 ALTER DATABASE。

更改角色的密码：

```sql
ALTER ROLE daria WITH PASSWORD 'passwd123';
```

更改密码失效日期：

```sql
ALTER ROLE scott VALID UNTIL 'May 4 12:00:00 2015 +1';
```

使密码永久有效：

```sql
ALTER ROLE luke VALID UNTIL 'infinity';
```

赋予角色创建其他角色和新数据库的能力：

```sql
ALTER ROLE joelle CREATEROLE CREATEDB;
```

给角色一个非默认设置 maintenance_work_mem参数：

```sql
ALTER ROLE admin SET maintenance_work_mem = 100000;
```

将角色分配给资源队列：

```sql
ALTER ROLE sammy RESOURCE QUEUE poweruser;
```

授予创建可写外部表的角色权限：

```sql
ALTER ROLE load CREATEEXTTABLE (type='writable');
```

更改角色在星期日不允许登录访问：

```sql
ALTER ROLE user3 DENY DAY 'Sunday';
```

改变角色以消除星期日不允许登录访问的约束：

```sql
ALTER ROLE user3 DROP DENY FOR DAY 'Sunday';
```

## 兼容性
ALTER ROLE语句是一个数据库扩展。

## 另见
CREATE ROLE、DROP ROLE、SET、CREATE RESOURCE QUEUE、GRANT、REVOKE
