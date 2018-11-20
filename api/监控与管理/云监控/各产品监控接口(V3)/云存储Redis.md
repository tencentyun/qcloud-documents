## 1. 接口描述

接口：GetMonitorData

获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。 

接口调用频率限制为：50次/秒，500次/分钟。 单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。

若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。

查询云存储Redis产品监控数据，入参取值如下：
Namespace：qce/redis
Dimensions.N.redis_uuid：实例的uuid

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetMonitorData。

### 2.1输入参数

| 参数名称         | 是否必选 | 类型              | 描述                                       |
| ------------ | ---- | --------------- | ---------------------------------------- |
| Namespace    | 是    | String          | 命名空间，每个云产品会有一个命名空间                       |
| MetricName   | 是    | String          | 指标名称，具体名称见2.2                            |
| Period       | 否    | Integer         | 监控统计周期。默认为取值为300，单位为s                    |
| StartTime    | 否    | Timestamp       | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| EndTime      | 否    | Timestamp       | 结束时间，默认为当前时间。 endTime不能小于startTime       |
| Dimensions.N | 是    | Array of String | 实例对象的维度组合                                |

### 2.2 指标名称

每个指标的统计粒度（Period）可取值不一定相同，可通过[DescribeBaseMetrics](https://cloud.tencent.com/document/api/248/15679)接口获取每个接口支持的统计粒度。

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


## 3. 输出参数

| 参数名称       | 类型             | 描述                                       |
| ---------- | -------------- | ---------------------------------------- |
| MetricName | String         | 监控指标                                     |
| StartTime  | Timestamp      | 数据点起始时间                                  |
| EndTime    | Timestamp      | 数据点结束时间                                  |
| Period     | Integer        | 数据统计周期                                   |
| DataPoints | Array of Float | 监控数据列表                                   |
| RequestId  | String         | 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。 |

## 4. 错误码表

| 错误代码             | 描述                 |
| ---------------- | ------------------ |
| InternalError    | 内部错误               |
| InvalidParameter | 参数错误（包括参数格式、类型等错误） |

## 5. 示例

## 示例1 拉取单个实例监控数据示例

### 场景描述

拉取某个云存储Redis某段时间内统计周期为5分钟的缓存命中率监控数据

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/redis
&MetricName=cache_hit_ratio
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.redis_uuid=crs-ifmymj41
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "redis_uuid": "crs-ifmymj41"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "cache_hit_ratio",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```

## 示例2 拉取多个实例监控数据示例

### 场景描述

拉取三个云存储Redis某段时间内统计周期为5分钟的缓存命中率监控数据

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/cvm
&MetricName=cache_hit_ratio
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.redis_uuid=crs-aaaaaa
&Dimensions.1.redis_uuid=crs-bbbbb
&Dimensions.2.redis_uuid=crs-ccccc
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "redis_uuid": "crs-aaaaaa"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "redis_uuid": "crs-bbbbb"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "redis_uuid": "crs-ccccc"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "cache_hit_ratio",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```