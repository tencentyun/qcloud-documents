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
