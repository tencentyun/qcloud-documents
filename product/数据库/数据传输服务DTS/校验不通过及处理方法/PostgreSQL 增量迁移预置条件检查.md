## 检查详情
当迁移类型选择增量迁移时，需要对如下条件进行检查，否则校验失败。
- 源和目标库的主版本号需要为 PostgreSQL 10.x 之前。
- 源实例的 `wal_level` 必须为 `logical`。
- 目标库 `max_replication_slots` 和 `max_wal_senders` 参数需要大于待迁移的数据库总数。
- 目标实例的 `max_worker_processes` 必须大于 `max_logical_replication_workers` 的值。
- 待迁移表中不能存在 unlogged table，否则无法迁移。

## 修护方法
如果版本不符合要求，请升级版本。修改参数 `wal_level`，`max_replication_slots`，`max_worker_processes` 和 `max_wal_senders` 的方法如下。

1. 登录源数据库。
>?
>- 如源数据库为自建数据库，需要登录至数据库的运行服务器上，进入数据库数据主目录中，一般为 $PGDATA。
>- 如源数据库为其他云数据库，请使用相关云平台的参数修改方法。
>- 如需要修改目标实例的参数，请通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 处理。
2. 找到 postgresql.conf 文件，打开此文件，修改`wal_level`。
```
wal_level = logical
```
3. 修改完成后，重启数据库实例。
4. 登录至数据库实例中，使用以下命令查看参数值是否设置正确：
```
postgres=> select name,setting from pg_settings where name='wal_level';
   name    | setting 
-----------+---------
 wal_level | logical
(1 row)
postgres=> select name,setting from pg_settings where name='max_replication_slots';
         name          | setting 
-----------------------+---------
 max_replication_slots | 10
(1 row)
postgres=> select name,setting from pg_settings where name='max_wal_senders';
      name       | setting 
-----------------+---------
 max_wal_senders | 10
(1 row)
```
5. 重新执行校验任务。

