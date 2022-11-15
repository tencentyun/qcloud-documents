本文为您介绍通过云 API 接口拉取 TDSQL-C MySQL 版对应指标的监控数据，详细操作和更多示例请参见 [拉取指标监控数据](https://cloud.tencent.com/document/api/248/31014)。

## 接口描述
传入 TDSQL-C MySQL 版的命名空间、对象维度描述和监控指标即可获得相应的监控数据。
接口调用频率限制为：20次/秒，1200次/分钟。单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。
若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。
默认接口请求频率限制：20次/秒。

## 输入参数
以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/248/30346)。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Action | 是 | String | 公共参数，本接口取值：GetMonitorData |
| Version | 是 | String | 公共参数，本接口取值：2018-07-24 |
| Region | 是 | String | 公共参数，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/248/30346#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) |
| Namespace | 是 | String | 命名空间，如 QCE/cynosdb_mysql。详细命名空间说明请参阅 [监控指标](https://cloud.tencent.com/document/product/248/45106) |
| MetricName | 是 | String | 指标名称，如 CPUUsagerate（CPU 利用率），仅支持单指标拉取 |
| Instances.N | 是 | Array of Instance | 实例对象的维度组合，格式为 key-value 键值对形式的集合。不同类型的实例字段完全不同，TDSQL-C MySQL 版的维度组合请参见 [监控指标](https://cloud.tencent.com/document/product/248/45106) |
| Period | 否	 | Integer | 监控统计周期，如60。默认为取值为300，单位为s |
| StartTime | 否	 | Timestamp ISO8601 | 起始时间，如2021-07-15T19:51:23+08:00 |
| EndTime | 否 | Timestamp ISO8601 | 结束时间，如2021-07-15T20:51:23+08:00，默认为当前时间。 EndTime 不能小于 StartTime |

## 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| Period | Integer | 	统计周期 |
| MetricName | String | 指标名 |
| DataPoints | Array of DataPoint | 数据点数组 |
| StartTime | Timestamp ISO8601 | 开始时间 |
| EndTime | Timestamp ISO8601 | 结束时间 |
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId |

## 示例
拉取某个 TDSQL-C MySQL 版实例某段时间内统计周期为5分钟的 CPU 利用率监控数据。
**输入示例**
```
POST / HTTP/1.1
Host: monitor.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: GetMonitorData
<公共请求参数>

{
    "Namespace": "QCE/cynosdb_mysql",
    "MetricName": "CPuUsageRate",
    "Period": 3600,
    "Instances": [
        {
            "Dimensions": [
                {
                    "Name": "InstanceId",
                    "Value": "cynosdbmysql-ins-edpn3t6b"
                }
            ]
        }
    ],
    "StartTime": "2022-07-15T10:00:00",
    "EndTime": "2022-07-15T15:00:00"
}
```
**输出示例**
```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": [
          {
            "Name": "InstanceId",
            "Value": "cynosdbmysql-ins-edpn3t6b"
          }
        ],
        "Timestamps": [
          1657850400,
          1657854000,
          1657857600,
          1657861200,
          1657864800
        ],
        "Values": [
          0.26,
          0.24,
          0.23,
          0.26,
          0.24
        ]
      }
    ],
		"EndTime": "2022-07-15 15:00:00",
		"MetricName": "CPuUsageRate",
		"Period": 3600,
    "RequestId": "71c72744-bec5-49d0-b42c-433609ab4166"
		 "StartTime": "2022-07-15 10:00:00"
  }
}
```

