

### 数据导入说明
云数据库 Redis-CKV 引擎提供数据导入工具(linux 版本) [redis-import-rdb](https://main.qcloudimg.com/raw/2b60883d002b00f4814daf80c2335ba3/redis-import-rdb)，工具支持导入 Redis 4.0 以及 4.0 版本以下的 RDB 数据，数据的导入流程步骤分为三步：

- 通过 BGSAVE 或者 SAVE 命令生成 RDB 文件，推荐使用 BGSAVE 命令备份数据，因为 SAVE 命令会在完成备份前会使整个 Redis 服务不可用；
- 清空目标实例，可用通过云数据库 Redis 控制台右上角的【清空实例】按钮清空实例数据，如果不清空目标实例，数据导入会失败；
- 使用 redis-import-rdb 工具导入 RDB 文件中的数据，工具参数说明如下：

    - -dip，云数据 Redis 的 IP 地址；
    - -dport，云数据 Redis 的端口（默认是 6379）；
    - -dauth，云数据 Redis 的密码；
    - -client，导入数据的并发线程数量，根据导入数据决定（默认情况建议设置为 10）；
    - -rdb，RDB文件路径；
    - -support_multi_db，该参数为 0 表示将所有 DB 的数据导入到 DB 0，非 0 表示将数据导入到原有的 DB；
    
    
- 工具使用示例：    
```
   ./redis-import-rdb  -dip 192.168.1.2 -dport 6379 -dauth 654321 -client 200 -rdb ./dump.rdb
```



### 数据迁移说明
云数据库 Redis-CKV 引擎提供数据导入工具(linux 版本) [redis-migration](https://main.qcloudimg.com/raw/7f7f185d6cb83179e3e2fd0ddbe27c21/redis-migration)，工具支持迁移 Redis 4.0 以及 4.0 版本以下的 RDB 数据，数据的迁移流程步骤分为三步：
- 确保源实例支持 sync 命令或者 psync 命令，如果不支持将无法进行数据迁移；
- 清空目标实例，可用通过云数据库 Redis 控制台右上角的【清空实例】按钮清空实例数据，如果不清空目标实例，数据导入会失败；
- 使用 redis-migration 工具迁移源实例据，工具参数说明如下：
    
    - -sip，需要进行迁移的源 Redis 服务 IP 地址；
    - -sport，需要进行迁移的源 Redis 服务端口；
    - -dip，云数据 Redis 的 IP 地址；
    - -dport，云数据 Redis 的端口（默认是 6379）；
    - -dauth，云数据 Redis 的密码；
    - -client，导入数据的并发线程数量，根据导入数据决定（默认情况建议设置为 10）；
    - -datapath，本地存放 RDB 文件和 AOF 文件的目录，确保磁盘空间足够存放数据；
- 工具使用示例：    
```
   ./redis-migration -sip 192.168.1.1 -sport 6379 -sauth 123456 -dip 192.168.1.2 -dport 6379 -dauth 654321 -client 200 -datapath /data 
```
