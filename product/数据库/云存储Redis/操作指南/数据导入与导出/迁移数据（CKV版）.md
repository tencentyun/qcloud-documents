
云数据库 Redis（CKV 版）提供数据迁移工具 [redis-migration（Linux 版）](https://main.qcloudimg.com/raw/7f7f185d6cb83179e3e2fd0ddbe27c21/redis-migration)，工具支持迁移 Redis 4.0 及以下版本的 RDB 数据。

## 前提条件
确保源实例支持`sync`命令或`psync`命令，如果不支持将无法进行数据迁移。
## 操作步骤

1. 登录 [控制台](https://console.cloud.tencent.com/redis)，单击实例名称进入实例详情页。
2. 单击右上角的【清空实例】清空实例数据，如果不清空目标实例，会导致数据迁移失败。
2. 使用 redis-migration 工具迁移源实例数据。
示例：    
```
   ./redis-migration -sip 192.168.1.1 -sport 6379 -sauth 123456 -dip 192.168.1.2 -dport 6379 -dauth 654321 -client 200 -datapath /data 
```
参数说明如下：    
    - -sip：需要进行迁移的源 Redis 服务 IP 地址。
    - -sport：需要进行迁移的源 Redis 服务端口。
    - -dip：目标云数据库 Redis 的 IP 地址。
    - -dport：目标云数据库 Redis 的端口（默认为6379）。
    - -dauth：目标云数据库 Redis 的密码。
    - -client：导入数据的并发线程数量，根据导入数据决定（建议设置为10）。
    - -datapath：本地存放 RDB 文件和 AOF 文件的目录，确保磁盘空间足够存放数据。

