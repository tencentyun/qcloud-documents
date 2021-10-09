## 命名空间

Namespace=QCE/REDIS

## 监控指标

| 指标中文名       | 指标英文名            | 指标采集方式（Linux下含义）                         | 指标统计方式                    | 单位    | 维度 |
| ----------- | ---------------- | ---------------------------------------- | ------------------------- | ----- | ----- |
| 总请求     | Qps              | 1分钟内命令总数除以60                             | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | 次/秒钟  |redis_uuid|
| 连接数量         | Connections      | 1分钟内连接数总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 个     |redis_uuid|
| CPU使用率      | CpuUs           | CPU处于非空闲状态的百分比，取`/proc/stat`数据计算得出        | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | %     |redis_uuid|
| 入流量       | InFlow          | 1分钟内入流量总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | Mb/分钟 |redis_uuid|
| Key总个数       | Keys             | 1分钟内key数量的最大值                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | 个     |redis_uuid|
| 出流量       | OutFlow         | 1分钟内出流量总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | Mb/分钟 |redis_uuid|
| 读请求    | StatGet         | 1分钟内 get、hget、hgetall、hmget、mget、getbit、getrange 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |redis_uuid|
| 写请求    | StatSet         | 1分钟内 set、hset、hmset、hsetnx、lset、mset、msetnx、setbit、setex、setrange、setnx 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |redis_uuid|
| 内存使用量       | Storage          | 1分钟内已使用容量的最大值                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | MB/分钟 |redis_uuid|
| 内存使用率       | StorageUs       | 1分钟内已使用容量的百分比最大值                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | %     |redis_uuid|

>?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览
| 参数名称               | 维度名称             | 维度解释          | 格式                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| Instances.N.Dimensions.0.Name  | redis_uuid              | 实例 ID 的维度名称 | 输入 String 类型维度名称：redis_uuid |
| Instances.N.Dimensions.0.Value | redis_uuid              | 实例具体 ID   | 输入具体实例 ID，例如：crs-123456 |

## 入参说明

查询云数据库 Redis 监控数据，入参取值如下：
&Namespace= QCE/REDIS
&Instances.N.Dimensions.0.Name=redis_uuid
&Instances.N.Dimensions.0.Value 为实例的 uuid 


