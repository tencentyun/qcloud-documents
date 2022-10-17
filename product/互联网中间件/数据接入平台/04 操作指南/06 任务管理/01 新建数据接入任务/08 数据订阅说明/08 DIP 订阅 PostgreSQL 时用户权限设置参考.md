## 背景

在使用 DIP 订阅 Postgresql 数据库时，需要给 **连接管理** 中配置的 PostgreSQL 用户分配相应的权限。只有拥有相应权限的用户从被允许的主机访问数据库时，才能够进行消息的同步。

本文从用户权限设置以及主机访问权限设置两方面进行说明。

## 用户权限设置

权限赋予是分 decode 插件的，不同插件需要的权限不一样。

### 使用 decoderbufs 插件时用户权限设置

通过超级用户登录 PostgreSQL，新建一个角色，给角色赋予至少 `REPLICATION` 和 `LOGIN` 两种权限。

赋予权限：

```
 CREATE ROLE userName REPLICATION LOGIN;
```

<dx-alert infotype="explain" title="">
超级用户默认拥有必要的权限，如果是超级用户，大部分无需赋予上面权限。但出于安全考虑不建议使用超级用户。
</dx-alert>



### 使用 pgoutput 插件时用户权限设置



<dx-alert infotype="notice" title="">
pgoutput 插件需要连接管理配置的用户拥有超级用户权限。
</dx-alert>


**第一步：** 验证用户是否拥有超级用户权限

```
// 登录postgresql，执行 \du 命令查看用户权限
postgres=# \du
Role name  | List of roles Attributes
 admin     | Superuser                                                  
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS 
 slave     | Replication

 // 如果配置的用户不包含 Superuser 权限，需要进行授权
postgres=# ALTER USER userName WITH SUPERUSER;
```

**第二步：** 用户拥有超级用户权限后，按照以下步骤进行授权
connector pgoutput插件通过订阅 postgresql 节点上的 publication 来获取变更事件，您可以在启动 connector 前手动创建 publication，也可以授予配置的用户创建 publication 的权限。
赋予用户以下权限：`Replication`、`CREATE`、`SELECT`

```
CREATE ROLE userName REPLICATION LOGIN;

GRANT CREATE ON DATABASE databaseName TO userName;

GRANT SELECT ON TABLE tableName TO userName;
```

连接管理中配置的用户需要拥有订阅的表的所有者权限，可通过以下方式授予用户表的所有者权限：

```
1. 创建 replication group
 CREATE ROLE <replication_group>;
2. 将表的所有者加入到 replication group
 GRANT REPLICATION_GROUP TO <original_owner>; 
3. 将 connector 用户添加到 replication group
 GRANT REPLICATION_GROUP TO <replication_user>; 
4. 将表的所有者权限转移到 replication group
 ALTER TABLE <table_name> OWNER TO REPLICATION_GROUP; 
```

## 主机访问权限设置（自建集群需要配置）

您需要配置数据库允许 connector 的主机访问，通过配置 `pg_hba.conf` 文件来设置相应的策略, `pg_hba.conf` 详细介绍可参见 [pg_hba.conf](https://www.postgresql.org/docs/10/auth-pg-hba-conf.html)。配置文件格式如下：

```
host    databaseName    userName     11.163.0.0/16         md5
host    databaseName    userName    11.163.0.0/16        trust
```
