移除访问特权。

## 概要

```sql
REVOKE [GRANT OPTION FOR] { {SELECT | INSERT | UPDATE | DELETE 
       | REFERENCES | TRIGGER | TRUNCATE } [,...] | ALL [PRIVILEGES] }
       ON [TABLE] tablename [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] { {USAGE | SELECT | UPDATE} [,...] 
       | ALL [PRIVILEGES] }
       ON SEQUENCE sequencename [, ...]
       FROM { rolename | PUBLIC } [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] { {CREATE | CONNECT 
       | TEMPORARY | TEMP} [,...] | ALL [PRIVILEGES] }
       ON DATABASE dbname [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] {EXECUTE | ALL [PRIVILEGES]}
       ON FUNCTION funcname ( [[argmode] [argname] argtype
                              [, ...]] ) [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] {USAGE | ALL [PRIVILEGES]}
       ON LANGUAGE langname [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [ CASCADE | RESTRICT ]
 
REVOKE [GRANT OPTION FOR] { {CREATE | USAGE} [,...] 
       | ALL [PRIVILEGES] }
       ON SCHEMA schemaname [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] { CREATE | ALL [PRIVILEGES] }
       ON TABLESPACE tablespacename [, ...]
       FROM { rolename | PUBLIC } [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [ADMIN OPTION FOR] parent_role [, ...] 
       FROM member_role [, ...]
       [CASCADE | RESTRICT]
```

## 描述
REVOKE 命令收回之前从一个或者更多角色授予的特权。关键词 PUBLIC 隐式定义的全部角色的组。

特权类型的含义见 **GRANT**。

注意：任何特定角色拥有的特权包括直接授予给它的特权、从它作为其成员的角色中得到的特权，以及授予给 PUBLIC 的特权。因此，例如从 PUBLIC 收回 SELECT 特权并一定意味着所有角色都失去在该对象上的 SELECT 特权，那些直接被授予的或者通过另一个角色被授予的角色仍然会拥有它。

如果指定了 GRANT OPTION FOR ，只会回收该特权的授予选项，特权本身不被回收。否则，特权及其授予选项都会被回收。

如果一个用户持有一个带有授予选项的特权并且把它授予给了其他用户，那么被那些其他用户持有的该特权被称为依赖特权。如果第一个用户持有的该特权或者授予选项正在被收回且存在依赖特权，指定 CASCADE 可以连带回收那些依赖特权，不指定则会导致回收动作失败。 这种递归回收只影响通过可追溯到该 REVOKE 的主体的用户链授予的特权。因此， 如果该特权经由其他用户授予给受影响用户，受影响用户可能实际上还保留有该特权。

在回收一个角色中的成员关系时，GRANT OPTION 被改称为 ADMIN OPTION，但行为是类似的。

## 参数
见**GRANT**部分

## 示例
从 public 收回表 films 的插入特权：

```sql
REVOKE INSERT ON films FROM PUBLIC;
```

从角色 sally 收回视图 topten 上的所有特权，注意实际意味着回收所有当前角色（如果不是超级用户）授予的特权：

```sql
REVOKE ALL PRIVILEGES ON topten FROM sally;
```

从 joe 收回角色 admins 中的成员关系：

```sql
REVOKE admins FROM joe;
```

## 兼容性
**GRANT** 命令的兼容性注解同样适用于 REVOKE。

关键词 RESTRICT 或者 CASCADE 根据标准是必需的，但是数据库假定 RESTRICT 为默认值。

## 另见
GRANT
