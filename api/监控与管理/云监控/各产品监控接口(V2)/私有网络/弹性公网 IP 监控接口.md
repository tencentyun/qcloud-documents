## 接口描述
域名：`monitor.api.qcloud.com`
接口：GetMonitorData

弹性公网 IP（Elastic IP，EIP）简称弹性 IP 地址或弹性 IP，是可以独立申请的公网 IP 地址，支持与 CVM/NAT 网关实例的动态绑定和解绑。

查询弹性公网 IP 产品监控数据，入参取值如下：
namespace：qce/lb
维度名称取值：eip
dimensions.0.name=eip
dimensions.0.value 为弹性公网 IP 的唯一 ID

## 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详细请参阅 [公共请求参数](https://cloud.tencent.com/document/product/248/4478) 文档。其中，此接口的 Action 字段为 GetMonitorData。

### 输入参数
| 参数名称           | 必选 | 类型     | 输入内容             | 描述                                                         |
| ------------------ | ---- | -------- | -------------------- | ------------------------------------------------------------ |
| namespace          | 是   | String   | qce/lb               | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏 |
| metricName         | 是   | String   | 具体的指标名称       | 指标名称，详细请见本文 [指标名称](#name) 列表                                    |
| dimensions.0.name  | 是   | String   | eip                  | 入参为弹性公网 IP 的 ID                                         |
| dimensions.0.value | 是   | String   | 具体的弹性公网 IP 的 IP 地址 | 调用 [DescribeAddresses](https://cloud.tencent.com/document/product/215/16702) 接口获取的 AddressIp 字段 |
| period             | 否   | Int      | 60/300               | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变，输入参数时可参考 [指标名称](#name) 列表 |
| startTime          | 否   | Datetime | 起始时间             | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| endTime            | 否   | Datetime | 结束时间             | 结束时间，默认为当前时间， endTime 不能小于 startTime          |

<span id="name"></span>
### 指标名称
| 指标名称       | 含义       | 单位  | 维度 |
| -------------- | ---------- | ----- | ---- |
| vip_outtraffic | 外网出带宽 | Mbps  | eip  |
| vip_intraffic  | 外网入带宽 | Mbps  | eip  |
| vip_outpkg     | 出包量     | 个/秒 | eip  |
| vip_inpkg      | 入包量     | 个/秒 | eip  |

## 输出参数
| 参数名称   | 类型     | 描述                            |
| ---------- | -------- | ------------------------------- |
| code       | Int      | 错误码，0：成功，其他值表示失败 |
| message    | String   | 返回信息                        |
| startTime  | Datetime | 起始时间                        |
| endTime    | Datetime | 结束时间                        |
| metricName | String   | 指标名称                        |
| period     | Int      | 监控统计周期                    |
| dataPoints | Array    | 监控数据列表                    |

## 错误码
| 错误代码 | 错误描述       | 英文描述                             |
| -------- | -------------- | ------------------------------------ |
| -502     | 资源不存在     | OperationDenied.SourceNotExists      |
| -503     | 请求参数有误   | InvalidParameter                     |
| -505     | 参数缺失       | InvalidParameter.MissingParameter    |
| -507     | 超出限制       | OperationDenied.ExceedLimit          |
| -509     | 错误的维度组合 | InvalidParameter.DimensionGroupError |
| -513     | DB操作失败     | InternalError.DBoperationFail        |

## 示例
### 输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="https://cloud.tencent.com/document/product/248/4478">公共请求参数</a> 
&namespace=qce/lb
&metricName=vip_intraffic
&dimensions.0.name=eip
&dimensions.0.value=192.168.1.100
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

### 输出
```
{     
    "code": 0,
    "message": "",
    "MetricName": "vip_intraffic",
    "StartTime": "2018-04-11 15:10:00",
    "EndTime": "2018-04-11 15:20:00",
    "Period": 300,
    "DataPoints": [
        0.003,
        0.003,
        0.003
    ]
}
```
