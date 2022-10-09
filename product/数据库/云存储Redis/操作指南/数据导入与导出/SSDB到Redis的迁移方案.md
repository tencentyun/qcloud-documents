## 迁移原理

- 基于 Golang 开发的 [Siphon](https://github.com/imneov/ssdb-port) 迁移工具，将其伪装为 SSDB 的 Slave，进行数据订阅，并同步数据到 Redis。
- Siphon  启动时会自动连接到 SSDB Server，进行 Key 寻址，从起始位置开始同步，直至存量的数据全部同步完成后再同步增量数据，即工具启动后会建立一个长连接通道保持运行。

## 工具及版本说明

- 迁移工具：[Siphon](https://github.com/imneov/ssdb-port)，适用于所有 SSDB 内核版本。
- 若 SSDB 涉及大 Key 或者过亿级别的 Key，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请已改造过的版本 Siphon-V2，提升数据同步效率。

> ?改造后的工具解决了原生版本存在同步效率低下问题，尤其是大 Key 同步，像 hash 数据和 zset 这类数据，大概提升12倍的同步效率。

## 注意事项

SSDB 单实例模式，迁移到 Redis 集群版时，存在逻辑兼容性问题，如跨 slot 事务、pipeline 管道等。

## 迁移步骤

1. 收集执行迁移命令所需配置的参数，如下所示。
 - -p：指定并发线程数。
 - -f：指定 SSDB 服务器地址。
 - -t：指定 Redis 服务器地址。
 - -T：指定 Redis 数据库的密码。
2. 使用 siphon_v2 sync 启动迁移工具，并查看迁移日志。
```
./siphon_v2 sync -p 1 –f X.X.X.X:8888 -t X.X.X.x:6379 –T XXX
```
执行命令后显示的状态如下：
 - **Copy Start**：表示开始启动全量数据同步。
 - **Copy Stop**：表示全量数据同步结束。
3. 进程不退出，等待新数据的生成并进行增量同步到 Redis。

