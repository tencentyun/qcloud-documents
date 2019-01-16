
云数据库 Redis（CKV 版）提供数据导入工具 [redis-import-rdb（Linux 版本）](https://main.qcloudimg.com/raw/2b60883d002b00f4814daf80c2335ba3/redis-import-rdb)，工具支持导入 Redis 4.0 及以下版本的 RDB 数据。

## 操作步骤
1. 通过`BGSAVE`或`SAVE`命令生成 RDB 文件，推荐使用`BGSAVE`命令备份数据，使用`SAVE`命令会导致整个 Redis 服务在完成备份前不可用。
2. 登录 [控制台](https://console.cloud.tencent.com/redis)，单击实例名称进入实例详情页。
3. 单击右上角的【清空实例】清空实例数据，如果不清空目标实例，会导致数据导入失败。
4. 使用 redis-import-rdb 工具导入 RDB 文件中的数据。
示例：
```
   ./redis-import-rdb  -dip 192.168.1.2 -dport 6379 -dauth 654321 -client 200 -rdb ./dump.rdb
```
参数说明如下：
    - -dip：云数据库 Redis 的 IP 地址。
    - -dport：云数据库 Redis 的端口（默认为6379）。
    - -dauth：云数据库 Redis 的密码。
    - -client：导入数据的并发线程数量，根据导入数据决定（建议设置为10）。
    - -rdb：RDB 文件路径。
    - -support_multi_db：该参数为0表示将所有 DB 的数据导入至 DB 0，非0表示将数据导入至原有的 DB。
    


