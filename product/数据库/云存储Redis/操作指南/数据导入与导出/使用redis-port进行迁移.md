## 工具介绍
[下载 redis-port（Linux 64 位）](https://redis-doc-2020-1254408587.cos.ap-guangzhou.myqcloud.com/redis-port.tgz)

redis-port 是一组开源工具集合，主要用于 Redis 节点间的数据库同步、数据导入、数据导出，支持 Redis 的跨版本数据迁移，工具集中包括以下工具：
- redis-sync：支持在 Redis 实例之间进行数据迁移。
- redis-restore：支持将 Redis 的备份文件（RDB）导入到指定 Redis 实例。
- redis-dump：支持将 Redis 的数据备份为 RDB 格式文件。
- redis-decode：支持将 Redis 备份文件（RDB）解析为可读的文件。

## 兼容版本
- 支持源 Redis 2.8、3.0、3.2、4.0 版本。
- 支持目标实例为 Redis 2.8、3.0、3.2、4.0 版本，以及云数据库的所有版本，包括 Redis 内存版、CKV 版。


## 使用 redis-sync 在线迁移
**redis-sync 工具迁移原理**
- 工具分为两大模块，模拟成复制节点从源实例同步数据，以及将复制的数据翻译成写入命令更新到目标实例。
- 复制数据分为两个阶段，全量同步阶段和增量同步阶段。

**参数说明**：
- -n：并发写入的任务数量，建议不设置或者设置为 CPU 核心数量 * 2。
- -m：源实例地址，格式为`"password"@ip:port`，免密码认证下格式为`ip:port`。
- -t：目标实例地址，格式为`"password"@ip:port`，免密码认证下格式为`ip:port`。
- --tmpfile=FILE：临时文件名称。
- --tmpfile-size=SIZE：临时文件最大长度。
- --help：查看帮助命令。

**示例**：
```
./redis-sync -m 127.0.0.1:6379 -t "xxx2018"@10.0.5.8:6379
```

**输出日志**：
```
[root@VM_5_16_centos bin]# ./redis-sync -m 127.0.0.1:6379 -t "xxx2018"@10.0.5.8:6379
2019/02/21 09:56:00 sync.go:76: [INFO] sync: master = "127.0.0.1:6379", target = "xxx2018@10.0.5.8:6379"
2019/02/21 09:56:01 sync.go:103: [INFO] +
2019/02/21 09:56:01 sync.go:109: [INFO] sync: runid = "f63e2ad58e2fcc15c8cc122f15778389a012c1a4", offset = 18576271
2019/02/21 09:56:01 sync.go:110: [INFO] sync: rdb file = 9063349 (8.64mb)
2019/02/21 09:56:01 sync.go:208: [INFO] sync: (r/f,s/f,s) = (read,rdb.forward,rdb.skip/rdb.forward,rdb.skip)
2019/02/21 09:56:02 sync.go:250: [INFO] sync: rdb = 9063349 - [100.00%] (r/f,s/f,s)=(1703936/71754,0/0,0) ~ (1.62mb/-,-/-,-) ~ speed=(1.62mb/71754,0/0,0)
2019/02/21 09:56:03 sync.go:250: [INFO] sync: rdb = 9063349 - [100.00%] (r/f,s/f,s)=(3407872/153850,0/0,0) ~ (3.25mb/-,-/-,-) ~ speed=(1.62mb/82096,0/0,0)
2019/02/21 09:57:54 sync.go:250: [INFO] sync: rdb = 9063349 - [100.00%] (r/f,s/f,s)=(80487526/411969,0/1587212,0) ~  (76.76mb/-,-/-,-) ~ speed=(0/0,0/0,0)
```

**使用说明**：
- 目标实例的 db 数量要求大于源实例的 db 数量，否则迁移将失败。
- 如果迁移中途因为网络中断或者其他原因断开，需要先清空目标实例然后再次执行迁移，否则可能出现脏数据。
- 迁移的进度，日志显示 "sync: rdb = 9063349 - [100.00%]" 该内容表示全量数据已经完成同步，正在进行增量数据同步，"speed=(0/0,0/0,0)" 表示增量数据已经完成同步。
- 停止迁移，通过 Ctrl+C 命令或者其他方式终止工具的执行，即可停止数据同步。

## 使用 redis-restore 导入数据
redis-restore 工具支持将 Redis 的备份文件（RDB）导入到指定 Redis 实例，同时也支持导入 AOF 文件，支持 Redis 2.8、3.0、3.2、4.0 版本的 RDB 文件格式。

**参数说明**：
- -n：并发写入的任务数量，建议不设置或者设置为 CPU 核心数量 * 2。
- -i：RDB 文件路径。
- -t：目标实例地址，格式为`"password"@ip:port`，免密码认证下格式为`ip:port`。
- -a：AOF 文件路径。
- --db=DB：备份文件导入 Redis 目标实例的 DB ID，须和源实例 DB ID 保持一致。
- --unixtime-in-milliseconds=EXPR：导入数据的同时更新 Key 过期时间值。
- --help：查看帮助命令。

**示例**：
```
./redis-restore dump.rdb -t 127.0.0.1:6379
```


## 使用 redis-dump 备份数据
redis-dump 支持将 Redis 的数据备份成 RDB 文件，同时还支持备份 AOF 增量数据。
>?腾讯云数据库 Redis 暂时不支持使用 redis-dump 工具进行备份，您可以使用 Redis 数据库控制台或者 API 进行数据备份和下载；以及使用 redis-dump 工具来备份您自建的 Redis 实例。

**参数说明**：
- -n：并发写入的任务数量，建议不设置或者设置为 CPU 核心数量 * 2。
- -m：Redis 实例地址，格式为`"password"@ip:port`，免密码认证下格式为`ip:port`。
- -o：备份输出的 RDB 文件路径。
- -a：备份输出的 AOF 文件路径。
- --help：查看帮助。

**示例**：
```
./redis-dump  127.0.0.1:6379 -o dump.rdb
```

