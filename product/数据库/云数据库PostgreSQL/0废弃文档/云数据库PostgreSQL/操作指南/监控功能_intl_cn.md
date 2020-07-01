## 性能监控
为方便用户查看和掌握实例的运行信息，PostgreSQL提供了丰富的性能监控项，用户可进入PostgreSQL管理控制台对应【实例管理】-【系统监控】查看。

## `pg_stat_statements`
您还可以通过[`pg_stat_statements`](https://www.postgresql.org/docs/9.4/static/pgstatstatements.html)视图查询pg详细性能指标。

## 已提供监控指标
|指标名称|指标api|指标含义|指标单位|
|------|------|-------|-------|
|CPU利用率|cpu|实例CPU使用率，由于在闲时采用灵活的CPU限制策略，CPU利用率可能大于100%|%|
|已用存储空间|storage|实例占用磁盘的可用空间|GB|
|磁盘IOPS|iops|实例的IOPS（每秒的请求次数)|次/秒|
|输入流量|in_flow|实例读写输入的流量|KB/秒|
|输出流量|out_flow|实例读写输出的流量|KB/秒|
|连接数|connections|实例的活跃连接历史变化趋势|个|
|请求数|read_write_calls|读写（增删改查）请求每分钟总数|次/分钟|
|读请求数|read_calls|读请求每分钟总数|次/分钟|
|写请求数|write_calls|写请求每分钟总数|次/分钟|
|其他请求数|other_calls|除了读和写以外的请求总数（如Drop），按分钟累加|次/分钟|
|缓冲区缓存命中率|hit_percent|数据缓存命中率|%|
|平均执行时延|sql_runtime_avg|所有SQL请求的平均执行时间，不包含事务里面的SQL。|ms|
|最长TOP10执行时延|sql_runtime_avg|执行时间最长的top10的SQL的平均值|ms|
|最短TOP10执行时延|sql_runtime_min|执行时间最短的top10的SQL的平均值|ms|
|剩余XID数量|remain_xid|剩余的Transaction Id数量，Transaction Id最大有2^32个，小于1000000建议手工执行vacuum full。|个|
|主备XLOG同步差异|xlog_diff|每分钟采样，主备XLOG的同步的大小差异，代表着同步的延迟，越小越好。|byte|


