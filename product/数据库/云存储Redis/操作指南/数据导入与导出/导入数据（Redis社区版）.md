## crs-port 简介
云数据库 Redis（Redis 版）支持通过 crs-port 工具进行实例数据导入导出：
- 支持导入 Redis 4.0 及以下版本的 RDB 文件至 Redis 2.8 主从版、4.0 集群版。
- 支持导出 Redis 2.8 单机版、主从版的数据。

**crs-port 工具下载**：[crs-port（Linux 版）](		https://main.qcloudimg.com/raw/8d28dd072a60f1a4b7ed3bc0fe5a3d16/crs-port)

## 前提条件
 - 使用工具前需先清空目标 Reids 实例，否则会出现`【ERROR】 restore error: ERR Target key name is busy. for key: xxx `报错。
 - 如果有其他客户端正写入数据到该实例中（可以清空实例后，观察监控中的 QPS 指标来判断），需停止其他的写入。
 - 需要确保执行脚本的机器时间正确，否则可能导致数据不一致。
 - 用 crs-port 导入的服务器务必保证内存配置大于导出实例的已用内存数据大小，例如源实例已用量20GB，导出 RDB 文件会压缩为12GB，需要服务器配置大于20GB。

## 导入 RDB 文件
导入命令：
``` 
crs-port restore -n 16 -i /data/dump.rdb -t 192.168.0.1:6379 -A pwd
```

参数说明：
- -n：并发数，该值建议取 CPU 总核数的2倍到4倍。
- -i：指定导入文件所在路径。
- -t：要导入的目标 Reids 实例的 IP 和端口。
- -A：目标 Reids 实例的链接密码。
- --setdb=N：指定导入到目标实例的某个库中，N 的范围 [0 - 15]。
- --filterdb=N：指定导入源文件中某个库的数据到目标实例，N 的范围 [0 - 15]。

>?
- 出现`【ERROR】 restore error: ERR Target key name is busy. for key: xxx `时，表示该 Key 已经存在于数据库中，出现报错后数据将不会回滚，建议再次发起导入之前操作清理数据。
- crs-port 只支持整个实例导出，如需指定库，添加导入参数： --filterdb=N。
- dump RDB 文件后文件会被压缩，因此得到的 RDB 文件会比当前使用量小。

## dump RDB 文件
从云数据库 Redis 实例的导出数据为 RDB 文件（仅支持 Redis 2.8 单机版、2.8 主从版），命令格式如下：
``` 
crs-port dump -n 16 -f 192.168.0.1:6379 -P pwd -o /data/dump.rdb
```

参数说明：
- -n ：并发数，该值建议取 CPU 总核数的2倍到4倍。
- -f ：源 Redis 服务的 IP 和端口。
- -P ：源 Redis 服务的密码，如无密码，可不指定该参数。
- -o ：指定文件输出路径。

