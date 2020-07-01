云监控为云数据库 Redis 提供以下监控指标：

| 指标中文名       | 指标英文名            | 指标采集方式（Linux下含义）                         | 指标统计方式                    | 单位    |
| ----------- | ---------------- | ---------------------------------------- | ------------------------- | ----- |
| cache命中率    | cache_hit_ratio  | 1分钟取内取 keyspace_misses、keyspace_hits通过如下计算 （1- keyspace_misses/keyspace_hits）* 100% 得出。不再维护该指标 | 每分钟采集，5分钟粒度数据是按最近5分钟内平均值  | %     |
| get命令数      | cmdstat_get      | 1分钟内 get 命令请求数                           | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| getbit命令数   | cmdstat_getbit   | 1分钟内 getbit 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| getrange命令数 | cmdstat_getrange | 1分钟内 getrange 命令请求数                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hget命令数     | cmdstat_hget     | 1分钟内 hget 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hgetall命令数  | cmdstat_hgetall  | 1分钟内 hgetall 命令请求数                       | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hmget命令数    | cmdstat_hmget    | 1分钟内 hmget 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hmset命令数    | cmdstat_hmset    | 1分钟内 hmset 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hset命令数     | cmdstat_hset     | 1分钟内 hset 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hsetnx命令数   | cmdstat_hsetnx   | 1分钟内 hsetnx 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| lset命令数     | cmdstat_lset     | 1分钟内 lset 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| mget命令数     | cmdstat_mget     | 1分钟内 mget 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| mset命令数     | cmdstat_mset     | 1分钟内 mset 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| msetnx命令数   | cmdstat_msetnx   | 1分钟内 msetnx 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| set命令数      | cmdstat_set      | 1分钟内 set 命令请求数                           | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setbit命令数   | cmdstat_setbit   | 1分钟内 setbit 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setex命令数    | cmdstat_setex    | 1分钟内 setex 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setnx命令数    | cmdstat_setnx    | 1分钟内 setnx 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setrange命令数 | cmdstat_setrange | 1分钟内 setrange 命令请求数                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| 每秒执行命令数     | qps              | 1分钟内命令总数除以60                             | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | 次/秒钟  |
| 连接数         | connections      | 1分钟内连接数总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 个     |
| cpu利用率      | cpu_us           | CPU处于非空闲状态的百分比，取/proc/stat数据计算得出         | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | %     |
| 内网入流量       | in_flow          | 1分钟内入流量总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | Mb/分钟 |
| key总数       | keys             | 1分钟内key数量的最大值                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | 个     |
| 内网出流量       | out_flow         | 1分钟内出流量总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | Mb/分钟 |
| 所有get命令数    | stat_get         | 1分钟内 get, hget, hgetall, hmget, mget, getbit, getrange 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| 所有set命令数    | stat_set         | 1分钟内 set, hset, hmset, hsetnx, lset, mset, msetnx, setbit, setex, setrange, setnx 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| 已使用容量       | storage          | 1分钟内已使用容量的最大值                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | MB/分钟 |
| 容量使用率       | storage_us       | 1分钟内已使用容量的百分比最大值                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | %     |



有关更多如何使用 云存储Redis  的监控指标内容，可以查看云监控 API 中的 [云存储 Redis 接口文档](https://cloud.tencent.com/document/product/248/11009)。
