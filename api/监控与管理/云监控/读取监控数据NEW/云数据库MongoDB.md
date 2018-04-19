## 1. 接口描述

接口：GetMonitorData

获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。 

接口调用频率限制为：50次/秒，500次/分钟。 单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。

若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。

查询文档数据库MongoDB产品监控数据，入参取值如下：
Namespace：qce/cmongo
Dimensions.N.target：视查询维度而定

下面来说明下Dimensions.N.target 的取值。
腾讯云提供的MongoDB是集群服务，通过本API可以查询“整个集群”、“某个副本集”、“某个节点”三个维度的监控数据。
其中：
“整个集群”代表了您所购买的某一个MongoDB实例，这个维度可以查询整个实例的读写请求次数、容量使用率、超时请求等。
“某个副本集”维度可查询集群下的某一个副本集内部的容量使用率和主从延迟。副本集实例本身只包含一个副本集，分片实例的每一片都是一个副本。
“某个节点”维度可以查询集群内的任意节点的CPU、内存等信息。

Dimensions.N.target 取值参照表

| 取值类型  | 取值示例                                     | 描述                                       |
| ----- | ---------------------------------------- | ---------------------------------------- |
| 实例ID  | cmgo-6ielucen                            | 实例ID一个MongoDB实例的唯一标识；可以在[MongoDB控制台](https://console.cloud.tencent.com/mongodb)查询到；或者调用MognoDB的API也可以获取 |
| 副本集ID | cmgo-6ielucen_0cmgo-6ielucen_2           | 在实例ID后面拼接 “_索引号”可以得到副本集ID；“索引号”从0开始，最大值为副本集个数-1；副本集实例只有一个副本集，所以固定拼接“_0”即可；分片实例有多个片，每一片都是副本集，举例：第3个片的副本集ID就是拼接“_2” |
| 节点ID  | cmgo-6ielucen_0-node-primarycmgo-6ielucen_1-node-slave0cmgo-6ielucen_3-node-slave2 | 在副本集ID后面拼接“-node-primary”得到该副本集的主节点ID；拼接“-node-slave从节点索引号”可得到对应的从节点的ID，“从节点索引号”从0开始，最大值为从节点个数-1 |

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为GetMonitorData。

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

| 指标                | 含义                       | 单位   | 集群/实例 | dimensions.0.value取值 |
| ----------------- | ------------------------ | ---- | ----- | -------------------- |
| inserts           | 单位时间内写入次数                | 次    | 集群/实例 | 实例ID                 |
| reads             | 单位时间内读取次数                | 次    | 集群/实例 | 实例ID                 |
| updates           | 单位时间内更新次数                | 次    | 集群/实例 | 实例ID                 |
| deletes           | 单位时间内删除次数                | 次    | 集群/实例 | 实例ID                 |
| counts            | 单位时间内ount次数              | 次    | 集群/实例 | 实例ID                 |
| aggregates        | 单位时间内aggregates次数        | 次    | 集群/实例 | 实例ID                 |
| cluster_diskusage | 集群容量使用率                  | %    | 集群/实例 | 实例ID                 |
| success           | 单位时间内成功请求次数              | 次    | 集群/实例 | 实例ID                 |
| delay_10          | 单位时间内成功请求延迟在10ms-50ms次数  | 次    | 集群/实例 | 实例ID                 |
| delay_50          | 单位时间内成功请求延迟在50ms-100ms次数 | 次    | 集群/实例 | 实例ID                 |
| delay_100         | 单位时间内成功请求延迟在100ms以上次数    | 次    | 集群/实例 | 实例ID                 |
| replica_diskusage | 副本集容量使用率                 | %    | 副本集   | 副本集ID                |
| slavedelay        | 主从单位时间内平均延迟              | 秒    | 副本集   | 副本集ID                |
| cpuusage          | CPU使用率                   | %    | 节点    | 节点ID                 |
| memusage          | 内存使用率                    | %    | 节点    | 节点ID                 |
| qr                | Read请求等待队列中的个数           | 个    | 节点    | 节点ID                 |
| qw                | Write请求等待队列中的个数          | 个    | 节点    | 节点ID                 |
| conn              | 连接数                      | 个    | 节点    | 节点ID                 |
| netin             | 网络入流量                    | MB/s | 节点    | 节点ID                 |
| netout            | 网络出流量                    | MB/s | 节点    | 节点ID                 |


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

### 示例1 拉取单个实例监控数据示例

### 5.1查询某个集群/实例大于100ms的请求数

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/cmongo
&MetricName=delay_100
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.target=cmgo-6ielucen
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "target": "cmgo-6ielucen"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "delay_100",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```
### 5.2查询某个副本集的主从延时

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/cmongo
&MetricName=slavedelay
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.target=cmgo-6ielucen_0
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "target": "cmgo-6ielucen_0"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "slavedelay",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```
### 5.3查询某个节点的连接数

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/cmongo
&MetricName=conn
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.target=cmgo-6ielucen0-node-primarycmgo-6ielucen1-node-slave0cmgo-6ielucen_3-node-slave2
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "target": "cmgo-6ielucen0-node-primarycmgo-6ielucen1-node-slave0cmgo-6ielucen_3-node-slave2"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "conn",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```

## 示例2 拉取多个实例监控数据示例

### 场景描述

查询多个集群/实例大于100ms的请求数

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/cmongo
&MetricName=delay_100
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.target=cmgo-aaaaaa
&Dimensions.1.target=cmgo-bbbbb
&Dimensions.2.target=cmgo-ccccc
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "target": "cmgo-aaaaaa"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "target": "cmgo-bbbbb"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "target": "cmgo-ccccc"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "delay_100",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```