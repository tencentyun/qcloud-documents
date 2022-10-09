
## 迁移原理

将 PIKA 中的数据在线迁移到 Redis，并支持全量和增量同步。使用 [pika-migrate](https://github.com/Qihoo360/pika/tree/v3_2_7_migrate) 工具，将工具虚拟为 PIKA 的从库，然后从主库获取到数据转发给 Redis，同时支持增量同步，实现在线热迁的功能。

1. [pika-migrate](https://github.com/Qihoo360/pika/tree/v3_2_7_migrate) 通过 dbsync 请求获取主库全量 DB 数据，以及当前 DB 数据所对应的 binlog 点位。
2. 获取到主库当前全量 DB 数据之后，扫描 DB，将 DB 中的数据打包转发给 Redis。
3. 通过之前获取的 binlog 的点位向主库进行增量同步, 在增量同步的过程中，将从主库获取到的 binlog 重组成 Redis 命令，转发给 Redis。

## 适用版本

适用 PIKA 3.2.0及以上版本，单机模式且只使用了单 DB。若 PIKA 版本低于3.2.0，需将内核版本升级至 3.2.0。具体信息，请参见 [升级 PIKA 内核版本至3.2.0](https://github.com/Qihoo360/pika/wiki/如何升级到Pika3.1或3.2)。

## 注意事项

- PIKA 支持不同数据结构采用同名 Key，但是 Redis 不⽀持，所以在有同 Key 数据的场景下，以第⼀个迁移到 Redis 数据结构为准，其他同名 Key 的数据结构会丢失。
- 该工具只支持热迁移单机模式下，并且只采⽤单 DB 版本的 PIKA，如果是集群模式，或者是多 DB 场景，⼯具会报错并且退出。
- 为了避免由于主库 binlog 被清理导致该⼯具触发多次全量同步向 Redis 写入脏数据，工具自身做了保护，在第⼆次触发全量同步时会报错退出。

##  迁移步骤

1. 在 PIKA 主库上执行如下命令，让 PIKA 主库保留10000个 binlog 文件。
```
config set expire-logs-nums 10000 
```
> ?
> - pika-port 将全量数据写入到 Redis 这段时间可能耗时很长，而导致主库原先 binlog 点位被清理。需要在 PIKA 主库上保留10000个 binlog ⽂件，确保后续该⼯具请求增量同步的时候，对应的 binlog 文件还存在。
> - binlog 文件占用磁盘空间，可以根据实际情况确定保留 binlog 的数量。
2. 修改迁移工具的配置文件 pika.conf 中的如下参数。
![](https://qcloudimg.tencent-cloud.cn/raw/3646268c10c0c2f605550dbc3d176dc7.png)
 - **target-redis-host**：指定 Redis 的 IP 地址。
 - **target-redis-port**：指定 Redis 的端口号。
 - **target-redis-pwd**：指定 Redis 默认账号的密码。
 - **sync-batch-num**：指定 pika-migrate 接收到主库的 sync-batch-num 个数据⼀起打包发送给 Redis，提升转发效率。
 - **redis-sender-num**：指定 redis-sender-num 个线程用于转发数据包。转发命令通过 Key 的哈希值将数据分配到不同的线程发送，无需担心多线程发送导致数据错乱的问题。
3. 在工具包的路径下执行如下命令，启动 pika-migrate 工具，并查看回显信息。
```
pika -c pika.conf
```
4. 执行如下命令，将迁移工具伪装成 Slave，向主库请求同步，并观察是否有报错信息。
```
slaveof ip port force
```
5. 确认主从关系建立成功之后，pika-migrate 同时向目标 Redis 转发数据。执行如下命令，查看主从同步延迟。可在主库写入⼀个特殊的 Key，然后在 Redis 侧查看是否可立即获取到该 Key，判断数据同步完毕。
```
info Replication
```

