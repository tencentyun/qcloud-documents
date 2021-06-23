## 1. 接口描述

接口：GetMonitorData<br>
接口请求域名： `monitor.tencentcloudapi.com`

获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。 

接口调用频率限制为：20次/秒，1200次/分钟。 单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。

若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。

查询云数据库Redis监控数据，入参取值如下：<br>
&Namespace= QCE/REDIS<br>
&Instances.N.Dimensions.0.Name=redis_uuid<br>
&Instances.N.Dimensions.0.Value 为实例的 uuid<br>

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/document/api/248/4478) 文档。

### 2.1输入参数

#### 2.1.1 输入参数总览

| 参数名称    | 是否必选 | 类型                                                         | 描述                                                         |
| ----------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Action      | 是       | String                                                       | 公共参数，本接口取值：GetMonitorData                         |
| Version     | 是       | String                                                       | 公共参数，本接口取值： 2018-07-24                            |
| Region      | 否       | String                                                       | 公共参数，表示查询的是哪个地域实例的监控数据；支持的地域可查看云服务器支持的 [地域列表](https://cloud.tencent.com/document/api/213/15692) |
| Namespace   | 是       | String                                                       | 命名空间，每个云产品会有一个命名空间，API 3.0接口版本的必须是大写，如：  QCE/REDIS |
| MetricName  | 是       | String                                                       | 指标名称，具体名称见2.2                                      |
| Instances.N | 是       | Array of [Instance](https://cloud.tencent.com/document/product/248/30354) | 实例对象的维度组合                                           |
| Period      | 否       | Integer                                                      | 监控统计粒度。默认为取值为300，单位为s                       |
| StartTime   | 否       | Timestamp                                                    | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| EndTime     | 否       | Timestamp                                                    | 结束时间，默认为当前时间。 endTime 不能小于 startTime        |

#### 2.1.2 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释      | 格式                                     |
| ------------------------------ | ---------- | ------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | redis_uuid | 实例的 ID     | String类型维度名称：redis_uuid           |
| Instances.N.Dimensions.0.Value | redis_uuid | 具体实例的 ID | 输入实例的具体redis实例 ID，如crs-123456 |

### 2.2 指标名称

每个指标对应的统计粒度（Period）及维度（dimension）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度及维度信息。

| 指标中文名     | 指标英文名      | 指标采集方式（Linux下含义）                                  | 指标统计方式                                     | 单位    |
| -------------- | --------------- | ------------------------------------------------------------ | ------------------------------------------------ | ------- |
| cache命中率    | CacheHitRatio   | 1分钟取内取 keyspace_misses、keyspace_hits通过如下计算 （1- keyspace_misses/keyspace_hits）* 100% 得出。不再维护该指标 | 每分钟采集，5分钟粒度数据是按最近5分钟内平均值   | %       |
| get命令数      | CmdstatGet      | 1分钟内 get 命令请求数                                       | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| getbit命令数   | CmdstatGetbit   | 1分钟内 getbit 命令请求数                                    | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| getrange命令数 | CmdstatGetrange | 1分钟内 getrange 命令请求数                                  | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| hget命令数     | CmdstatHget     | 1分钟内 hget 命令请求数                                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| hgetall命令数  | CmdstatHgetall  | 1分钟内 hgetall 命令请求数                                   | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| hmget命令数    | CmdstatHmget    | 1分钟内 hmget 命令请求数                                     | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| hmset命令数    | CmdstatHmset    | 1分钟内 hmset 命令请求数                                     | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| hset命令数     | CmdstatHset     | 1分钟内 hset 命令请求数                                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| hsetnx命令数   | CmdstatHsetnx   | 1分钟内 hsetnx 命令请求数                                    | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| lset命令数     | CmdstatLset     | 1分钟内 lset 命令请求数                                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| mget命令数     | CmdstatMget     | 1分钟内 mget 命令请求数                                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| mset命令数     | CmdstatMset     | 1分钟内 mset 命令请求数                                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| msetnx命令数   | CmdstatMsetnx   | 1分钟内 msetnx 命令请求数                                    | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| set命令数      | CmdstatSet      | 1分钟内 set 命令请求数                                       | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| setbit命令数   | CmdstatSetbit   | 1分钟内 setbit 命令请求数                                    | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| setex命令数    | CmdstatSetex    | 1分钟内 setex 命令请求数                                     | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| setrange命令数 | CmdstatSetrange | 1分钟内 setrange 命令请求数                                  | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| 每秒执行命令数 | Qps             | 1分钟内命令总数除以60                                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | 次/秒钟 |
| 连接数         | Connections     | 1分钟内连接数总和                                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 个      |
| cpu利用率      | CpuUs           | CPU处于非空闲状态的百分比，取 /proc/stat数据计算得出         | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | %       |
| 内网入流量     | InFlow          | 1分钟内入流量总和                                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | Mb/分钟 |
| key总数        | Keys            | 1分钟内key数量的最大值                                       | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | 个      |
| 内网出流量     | OutFlow         | 1分钟内出流量总和                                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | Mb/分钟 |
| 所有get命令数  | StatGet         | 1分钟内 get, hget, hgetall, hmget, mget, getbit, getrange 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| 所有set命令数  | StatSet         | 1分钟内 set, hset, hmset, hsetnx, lset, mset, msetnx, setbit, setex, setrange, setnx 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和     | 次/分钟 |
| 已使用容量     | Storage         | 1分钟内已使用容量的最大值                                    | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | MB/分钟 |
| 容量使用率     | StorageUs       | 1分钟内已使用容量的百分比最大值                              | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | %       |



## 3. 输出参数

| 参数名称   | 类型                  | 描述                                                         |
| ---------- | --------------------- | ------------------------------------------------------------ |
| MetricName | String                | 监控指标                                                     |
| StartTime  | Timestamp             | 数据点起始时间                                               |
| EndTime    | Timestamp             | 数据点结束时间                                               |
| Period     | Integer               | 数据统计粒度                                                 |
| DataPoints | Array of PointsObject | 监控数据列表                                                 |
| RequestId  | String                | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId |

## 4. 错误码表

| 错误代码 | 错误描述       | 英文描述                             |
| -------- | -------------- | ------------------------------------ |
| -502     | 资源不存在     | OperationDenied.SourceNotExists      |
| -503     | 请求参数有误   | InvalidParameter                     |
| -505     | 参数缺失       | InvalidParameter.MissingParameter    |
| -507     | 超出限制       | OperationDenied.ExceedLimit          |
| -509     | 错误的维度组合 | InvalidParameter.DimensionGroupError |
| -513     | DB操作失败     | InternalError.DBoperationFail        |

## 5. 示例

### 示例1

拉取某个云数据库 Redis 某段时间内统计粒度为60秒的连接数监控数据。

#### 输入示例

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace= QCE/REDIS
&MetricName=Connections
&Period=60
&StartTime=2019-06-04T00:00:00+08:00
&EndTime=2019-06-04T00:05:00+08:00
&Instances.0.Dimensions.0.Name=redis_uuid
&Instances.0.Dimensions.0.Value=crs-123456
&<公共请求参数>
```

#### 输出示例

```
{
  "Response": {
    "StartTime": "2019-06-04 00:00:00",
    "EndTime": "2019-06-04 00:05:00",
    "Period": 60,
    "MetricName": "Connections",
    "DataPoints": [
      {
        "Dimensions": [
          {
            "Name": "redis_uuid",
            "Value": "crs-123456"
          }
        ],
        "Timestamps": [
          1557304800,
          1557304860,
          1557304920,
          1557304980,
          1557305040,
          1557305100
        ],
        "Values": [
          3,
          3,
          4.5,
          3,
          3
        ]
      }
    ],
    "RequestId": "0ea9aeee-3bf8-46a0-b594-c2b9e1b7f0bf"
  }
}
```

### 示例2 

拉取某个云数据库 Redis 某段时间内统计粒度为60秒的连接数监控数据。

#### 输入示例

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace= QCE/REDIS
&MetricName=Connections
&Period=60
&StartTime=2019-06-04T00:00:00+08:00
&EndTime=2019-06-04T00:05:00+08:00
&Instances.0.Dimensions.0.Name=redis_uuid
&Instances.0.Dimensions.0.Value=crs-123456
&Instances.1.Dimensions.0.Name=redis_uuid
&Instances.1.Dimensions.0.Value=crs-1234567
&<公共请求参数>
```

#### 输出示例

```
{
  "Response": {
    "StartTime": "2019-06-04 00:00:00",
    "EndTime": "2019-06-04 00:05:00",
    "Period": 60,
    "MetricName": "Connections",
    "DataPoints": [
      {
        "Dimensions": [
          {
            "Name": "redis_uuid",
            "Value": "crs-123456"
          }
        ],
        "Timestamps": [
          1557304800,
          1557304860,
          1557304920,
          1557304980,
          1557305040,
          1557305100
        ],
        "Values": [
          3,
          3,
          4.5,
          3,
          3
        ]
      },
      {
        "Dimensions": [
          {
            "Name": "redis_uuid",
            "Value": "crs-1234567"
          }
        ],
        "Timestamps": [
          1557304800,
          1557304860,
          1557304920,
          1557304980,
          1557305040,
          1557305100
        ],
        "Values": [
          3,
          3,
          4.5,
          3,
          3
        ]
      }
    ],
    "RequestId": "0ea9aeee-3bf8-46a0-b594-c2b9e1b7f0bf"
  }
}
```
