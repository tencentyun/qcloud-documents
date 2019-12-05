定义一个新的数据库角色（用户或组）。

## 概要

```sql
CREATE ROLE name [[WITH] option [ ... ]]
```

其中 option 可以是：

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
    | [ ENCRYPTED | UNENCRYPTED ] PASSWORD 'password'
    | VALID UNTIL 'timestamp' 
    | IN ROLE rolename [, ...]
    | ROLE rolename [, ...]
    | ADMIN rolename [, ...]
    | RESOURCE QUEUE queue_name
    | [ DENY deny_point ]
    | [ DENY BETWEEN deny_point AND deny_point]
```

## 描述

CREATE ROLE 添加了一个新的角色到数据库系统。角色是一个实体，可以拥有数据库对象并且有数据库权利。角色可以是用户、组或者两者都是，这取决于它是怎么用的。用户必须有 CREATEROLE 权限或者是超级用户才能用此命令。

注意角色是在系统层级定义的，对数据系统所有数据库都有效。

## 参数

name
新角色的名字。

SUPERUSER
NOSUPERUSER
如果指定了 SUPERUSER，该定义的角色将是个超级用户，该超级用户重写数据库中的所有限制。超级用户状态是危险的，应当在仅真正需要的时候才去用。用户自己必须是超级用户才能创建新的超级用户。默认是 NOSUPERUSER。

CREATEDB
NOCREATEDB
如果指定了 CREATEDB，被定义的角色将被允许定义一个新数据库。NOCREATEDB（默认是）将会禁止掉用户创建数据库的能力。

CREATEROLE
NOCREATEROLE
如果指定了 CREATEDB，该被定义的角色将被允许创建新的角色，修改其他角色和删除其他角色。 NOCREATEROLE（默认值）将会禁止掉用户创建或修改（除了他们自己的）角色的能力。

CREATEEXTTABLE
NOCREATEEXTTABLE
如果指定了 CREATEEXTTABLE，被定义的角色将被允许创建外部表。该默认的类型是 readable，如果没有指定，则默认的协议是 gpfdist。NOCREATEEXTTABLE（默认值）禁止掉了角色创建外部表的能力。注意使用 file 或 execute 协议的外部表只能由超级用户创建。

INHERIT
NOINHERIT
如果指定，INHERIT （默认值）允许角色使用该直接或间接所属所有角色的数据库权利。使用 NOINHERIT，其他角色的成员资格仅通过 SET ROLE 授予到其他角色。

LOGIN
NOLOGIN
如果指定，LOGIN 允许该角色登录数据库，使用 LOGIN 属性的角色可以被认为是一个用户。使用 NOLOGIN（默认值）的角色对管理数据库非常有用，可以被认为是组。

CONNECTION LIMIT connlimit
该角色所能创建的最大并发连接数。默认值-1表示没有限制。

PASSWORD password
为使用 LOGIN 属性的角色设置用户密码。如果用户没有打算使用密码授权，用户可以省略该属性。如果没有指定密码，该密码将被置为 null，并且对该用户来说密码授权始终无效。null 密码可选择性的写明为 PASSWORD NULL。

ENCRYPTED
UNENCRYPTED
这些关键字控制密码是否加密存储在系统目录中（如果没一个指定，则默认行为由配置参数 password_encryption 决定）。如果提供的密码字符串已经是 MD5 加密的格式，则无论是否指定了 ENCRYPTED 或 UNENCRYPTED 都会按原样加密存储（因为系统不能解密指定加密的密码字符串）。这允许在转储/恢复期间重新加载加密的密码。

注意老客户端可能缺乏对 MD5 认证机制的支持，系统需要该机制来和存储的密码一起工作。

VALID UNTIL 'timestamp'
该 VALID UNTIL 子句设置了日期和时间，在此时间日期之后角色的密码不再有效。如果省略了该子句，则密码将永远不会过期。

IN ROLE rolename
将新角色添加为命令角色们的成员。请注意无法添加管理员新角色；使用单独的 GRANT 的命令可以做到。

ROLE rolename
将命名的角色添加为该角色的成员，将该角色变成一个组。

ADMIN rolename
该 ADMIN 子句像 ROLE，但是命令的角色将被添加到新角色中 WITH ADMIN OPTION，给他们能授予其他用户该组成员的权利。

RESOURCE QUEUE queue_name
该新的用户级角色被分配到的资源队列名称。仅带有 LOGIN 权利的角色能被分配到资源队列。该特殊的关键字 NONE 意味着该角色被分配到默认的资源队列，一个角色只能被分配到一个资源队列。
带有 SUPERUSER 属性的角色免于资源队列的限制。对于一个超级用户角色来说，查询总是立即运行而不顾资源队列施加的限制。

DENY deny_point
DENY BETWEEN deny_point AND deny_point
DENY 和 DENY BETWEEN 关键字设置了基于时间的限制，该限制在登录的时候被强制。DENY 设置了天或天和时间来拒绝访问。DENY BETWEEN 设置了访问拒绝后的间隔。两个都用参数 deny_point ，该参数有以下格式：

```sql
DAY day [ TIME 'time' ]
```

该 deny_point 参数的两个部分使用以下格式：

对于 day：

```sql
{'Sunday' | 'Monday' | 'Tuesday' |'Wednesday' | 'Thursday' | 'Friday' | 
'Saturday' | 0-6 }
```

对于 time：

```sql
{ 00-23 : 00-59 | 01-12 : 00-59 { AM | PM }}
```

该 DENY BETWEEN 子句使用两个 deny_point 参数：

```sql
DENY BETWEEN deny_point AND deny_point
```

更多关于基于时间的限制的信息和例子，请参阅“数据库管理员指南”中的“管理角色和权限”。

## 注意

添加删除角色成员（管理组）最偏爱的方式就是使用 GRANT和 REVOKE。

VALID UNTIL 子句仅对密码定义了一个期限时间，而不是对角色。当使用非基于密码授权方式登录时，该期限时间是不生效的。

该 INHERIT 属性控制可授权权限的继承（数据库对象和角色成员资格的访问权限）。它不适用与由 CREATE ROLE 和 ALTER ROLE 设置的特殊角色属性。例如拥有 CREATEDB 权限的角色，即使设置了 INHERIT，也不会授予 CREATEDB 的权限。以下权限不会继承，必须在每个角色上设置属性，包括：SUPERUSER、CREATEDB、CREATEROLE、CREATEEXTTABLE、LOGIN 和 RESOURCE QUEUE。

该 INHERIT 属性是默认的为了向后兼容。在先前数据库的发行版中，用户通常访问他们所属组的所有权限。但是，NOINHERIT 提供了一个与 SQL 标准中指定语义更合适的匹配。

小心使用 CREATEROLE 权限。对于一个 CREATEROLE 角色，并没有一个继承的概念。这意味着即使一个角色没有特定的权限，也允许创建其他角色，它可以轻松地创建具有不同于其自己权限的其他角色（除了使用超级用户创建角色）。例如，如果角色具有 CREATEROLE 权限但是不具有 CREATEDB 权限，它可以创建一个带有 CREATEDB 权限的角色。因此，将具有 CREATEROLE 权限的角色视为几乎具有超级用户角色。

该 CONNECTION LIMIT 选项从来不对超级用户执行。

当使用此命令指定一个未加密的密码时候，必须小心。该密码将以明文形式发送到服务器，也可能会记录在客户端的命令历史记录或服务器日志中。然而，客户端程序 createuser 发送加密的密码。此外，psql 还包含一个命令 \password，可以用来安全的更改密码。

## 示例
创建一个可以登录的角色，但是不给密码：

```sql
CREATE ROLE jonathan LOGIN;
```

创建一个属于资源队列的角色：

```sql
CREATE ROLE jonathan LOGIN RESOURCE QUEUE poweruser;
```

创建一个带密码的角色，改密码有效期到2016年底（CREATE USER 和 CREATE ROLE 相同除了前者暗示了 LOGIN）：

```sql
CREATE USER joelle WITH PASSWORD 'jw8s0F4' VALID UNTIL '2017-01-01';
```

创建一个可以创建 db 和管理其他角色的角色：

```sql
CREATE ROLE admin WITH CREATEDB CREATEROLE;
```

创建一个不允许在星期天登录的角色：

```sql
CREATE ROLE user3 DENY DAY 'Sunday';
```

## 兼容性

SQL 标准定了用户和角色的概念，但是把他们视为不同的概念并且让所有定义用户的命令由数据库实现指定。在数据库中，用户和角色被统一为单个类型的对象。因此，角色有比标准中更多的可选属性。

CREATE ROLE 在 SQL 标准中，但是该标准只需要语法：

```sql
CREATE ROLE name [WITH ADMIN rolename]
```

允许多个初始管理员和 CREATE ROLE 的所有其他选项，是数据库扩展。

由 SQL 标准指定的行为和给与用户 NOINHERIT 属性最为接近，然而角色则赋予 INHERIT 属性。

## 另见

SET ROLE、ALTER ROLE、DROP ROLE、GRANT、REVOKE、CREATE RESOURCE QUEUE
