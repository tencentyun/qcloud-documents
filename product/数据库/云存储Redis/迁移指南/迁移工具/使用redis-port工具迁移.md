
### 工具介绍
[redis-port下载（linux64位）](https://main.qcloudimg.com/raw/4fc8ab232a2ffaeb534b2f6b4dbdcbf0.tgz)

redis-port是一组开源工具开源工具集合，主要用于Redis节点间的数据库同步、数据导入、数据导出，支持Redis的跨版本数据迁移，工具集中包括以下工具：

- redis-sync，该工具支持在Redis实例之间进行数据迁移；
- redis-resotre，该工具支持将Redis的备份文件（RDB）导入到指定Redis实例；
- redis-dump，该工具支持将Redis的数据备份为RDB格式文件；
- redis-decode，该工具支持将Redis备份文件（RDB）解析为可读的文件；

#### 兼容版本
- 支持源Redis 2.8，3.0，3.2，4.0版本；
- 支持目标实例为Redis 2.8，3.0，3.2，4.0版本，以及云数据库的所有版本（包括Redis 2.8标准版、Redis 4.0集群版、CKV 标准版、CKV集群版）；


#### 使用redis-sync进行在线迁移

> redis-sync工具迁移原理：工具分为两大模块，模拟成复制节点从源实例同步数据，以及将复制的数据翻译成写入命令更新到目标实例。复制数据分为两个阶段，全量同步阶段以及增量同步阶段；

- 参数说明：
```
    -n 并发写入的任务数量，建议不设置或者设置为CPU核心数量 * 2;
    -m 源实例地址，格式为 "password@ip:port"
    -t 目标实例地址，格式为 "password@ip:port"
    --tmpfile=FILE，临时文件名称
    --tmpfile-size=SIZW，临时文件最大长度；
    --help 查看帮助命令

    参考：
    redis-sync -m 127.0.0.1:6379 -t 192.17.1.1:6379

    输出日志：
    [root@VM_5_16_centos bin]# ./redis-sync -m 127.0.0.1:6379 -t xxx2018@10.0.5.8:6379
    2019/02/21 09:56:00 sync.go:76: [INFO] sync: master = "127.0.0.1:6379", target = "Passwd2018@10.0.5.8:6379"
    2019/02/21 09:56:01 sync.go:103: [INFO] +
    2019/02/21 09:56:01 sync.go:109: [INFO] sync: runid = "f63e2ad58e2fcc15c8cc122f15778389a012c1a4", offset = 18576271
    2019/02/21 09:56:01 sync.go:110: [INFO] sync: rdb file = 9063349 (8.64mb)
    2019/02/21 09:56:01 sync.go:208: [INFO] sync: (r/f,s/f,s) = (read,rdb.forward,rdb.skip/rdb.forward,rdb.skip)
    2019/02/21 09:56:02 sync.go:250: [INFO] sync: rdb = 9063349 - [100.00%] (r/f,s/f,s)=(1703936/71754,0/0,0) ~ (1.62mb/-,-/-,-) ~ speed=(1.62mb/71754,0/0,0)
    2019/02/21 09:56:03 sync.go:250: [INFO] sync: rdb = 9063349 - [100.00%] (r/f,s/f,s)=(3407872/153850,0/0,0) ~ (3.25mb/-,-/-,-) ~ speed=(1.62mb/82096,0/0,0)
    2019/02/21 09:57:54 sync.go:250: [INFO] sync: rdb = 9063349 - [100.00%] (r/f,s/f,s)=(80487526/411969,0/1587212,0) ~  (76.76mb/-,-/-,-) ~ speed=(0/0,0/0,0)
```

- 使用说明：
    - 目标实例的db数据要求大于源实例的db数量，否则迁移将失败；
    - 如果迁移中途因为网络中断或者其他原因断开，需要先清空目标实例然后再次执行迁移，否则可能出现脏数据；
    - 迁移的进度，日志显示"sync: rdb = 9063349 - [100.00%]"该内容表示全量数据已经完成同步，正在进行增量数据同步，"speed=(0/0,0/0,0)"表示增量数据已经完成同步；
    - 停止迁移，通过Ctrl+C命令或者其他方式终止工具的执行，即可停止数据同步；

#### 使用redis-restore工具进行数据导入
redis-restore工具支持将Redis的备份文件（RDB）导入到指定Redis实例，同时也支持导入AOF文件，支持Redis2.8、3.0、3.2、4.0版本的RDB文件格式；

- 参数说明：
```
    -n 并发写入的任务数量，建议不设置或者设置为CPU核心数量 * 2;
    -i RDB文件路径；
    -t 目标实例地址，格式为 "password@ip:port";
    -a AOF文件路径；
    --db=DB 导入的DB id，默认为和源实例保持一致；
    --unixtime-in-milliseconds=EXPR 导入数据的同时更新Key过期时间值；
    --help 查看帮助命令

    参考：
    ./redis-restore dump.rdb -t 127.0.0.1:6379
```

#### 使用redis-dump工具进行数据备份

redis-dump支持将Redis的数据备份成RDB文件，同时还支持备份AOF增量数据。
> 腾讯云数据库Redis暂时不支持使用redis-dump工具进行备份，您可以使用Redis数据库控制台或者API进行数据备份和下载；您可以使用redis-dump工具来备份您自建的Redis实例。

- 参数说明：
```
    -n 并发写入的任务数量，建议不设置或者设置为CPU核心数量 * 2;
    -m Redis实例地址，格式为 "password@ip:port";
    -o 备份输出的RDB文件路径
    -a 备份输出的AOF文件路径
    --help 查看帮助

    参考：
    redis-dump    127.0.0.1:6379 -o dump.rdb
```



