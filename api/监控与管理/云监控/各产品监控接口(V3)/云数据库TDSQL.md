## 1. 接口描述

接口：GetMonitorData

获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。 接口调用频率限制为：50次/秒，500次/分钟。 若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。

查询云数据库TDSQL产品监控数据，入参取值如下：
namespace：qce/tdsql
dimensions.0.name=uuid
dimensions.0.value为实例的uuid

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetMonitorData。

### 2.1输入参数

| 参数名称         | 必选   | 类型              | 输入内容      | 描述                                       |
| ------------ | ---- | --------------- | --------- | ---------------------------------------- |
| Namespace    | 是    | String          | qce/cvm   | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| MetricName   | 是    | String          | 具体的指标名称   | 指标名称，具体名称见2.2                            |
|              |      |                 |           |                                          |
| Dimensions.N | 是    | Array of String | 实例具体的uuid | 实例对象的维度组合                                |
| Period       | 否    | Integer         | 60/300    | 监控统计周期。默认为取值为300，单位为s                    |
| StartTime    | 否    | Timestamp       | 起始时间      | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| EndTime      | 否    | Timestamp       | 结束时间      | 结束时间，默认为当前时间。 endTime不能小于startTime       |
### 2.2 指标名称

每个指标的统计粒度（Period）可取值不一定相同，可通过[DescribeBaseMetrics](https://cloud.tencent.com/document/api/248/15679)接口获取每个接口支持的统计粒度。

| 指标名称                  | 含义           | 单位   |
| --------------------- | ------------ | ---- |
| data_disk_available   | 数据磁盘可用大小     | MB   |
| binlog_disk_available | BINLOG磁盘可用大小 | MB   |
| select_total          | SELECT请求总数   | 次/秒  |
| long_query            | SELECT慢查询数   | 次/秒  |
| update_total          | UPDATE请求总数   | 次/秒  |
| insert_total          | INSERT请求总数   | 次/秒  |
| delete_total          | DELETE请求总数   | 次/秒  |
| mem_available         | 内存可用大小       | GB   |
| disk_iops             | 磁盘IOPS       | 次/秒  |
| conn_active           | 总连接数         | 次/秒  |
| conn_running          | 活跃连接数        | 次/秒  |
| is_master_switched    | 监控是否主备切换     | 无    |
| cpu_usage_rate        | CPU使用率       | %    |


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

拉取某台云数据库TDSQL某段时间内统计周期为5分钟的数据磁盘可用大小监控数据

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/tdsql
&MetricName=data_disk_available
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.uuid=tdsql-0gfryg60
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "uuid": "tdsql-0gfryg60"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "data_disk_available",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```

## 示例2 拉取多个实例监控数据示例

### 场景描述

拉取三台云数据库TDSQL某段时间内统计周期为5分钟的数据磁盘可用大小监控数据

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/tdsql
&MetricName=data_disk_available
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.uuid=tdsql-aaaaaa
&Dimensions.1.uuid=tdsql-bbbbb
&Dimensions.2.uuid=tdsql-ccccc
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "uuid": "tdsql-aaaaaa"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "uuid": "tdsql-bbbbb"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "uuid": "tdsql-ccccc"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "data_disk_available",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```