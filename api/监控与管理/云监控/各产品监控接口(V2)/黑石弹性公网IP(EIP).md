## 1. 接口描述

域名：monitor.api.qcloud.com
接口：GetMonitorData

查询黑石弹性公网IP(EIP)监控数据，入参取值如下：
namespace：qce/bm_lb
dimensions.0.name=vip
dimensions.0.value为要查询的 EIP 的地址信息

| 英文   | 中文含义                                     |
| ---- | ---------------------------------------- |
| vip  | 弹性公网IP地址，可以通过查询 EIP 列表接口 [DescribeEipBm](https://cloud.tencent.com/document/product/386/6671) 查看自己账户已申请的 EIP 列表 |

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 GetMonitorData。

### 2.1 输入参数

| 参数名称               | 必选   | 类型       | 输入内容           | 描述                                       |
| ------------------ | ---- | -------- | -------------- | ---------------------------------------- |
| namespace          | 是    | String   | qce/bm_lb        | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称        | 指标名称，具体名称见2.2                            |
| dimensions.0.name  | 是    | String   | vip            | 入参为要查询的 EIP 的地址信息                          |
| dimensions.0.value | 是    | String   | 具体要查询的EIP的地址信息 | 输入具体 vip                                  |
| period             | 否    | Int      | 60/300         | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标详情列表。 |
| startTime          | 否    | Datetime | 起始时间           | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| endTime            | 否    | Datetime | 结束时间           | 结束时间，默认为当前时间。 endTime不能小于startTime       |


### 2.2 指标名称
> 当前黑石弹性公网 IP 监控维度的取值周期为300秒（period参数），暂不支持更细粒度的数据获取。

| 指标名称           | 含义    | 单位   | 纬度   |
| -------------- | ----- | ---- | ---- |
| eip_outtraffic | 外网出带宽 | Mbps | vip  |
| eip_intraffic  | 外网入带宽 | Mbps | vip  |
| eip_outpkg     | 外网出包量 | 个/秒  | vip  |
| eip_inpkg      | 外网入包量 | 个/秒  | vip  |


## 3. 输出参数

| 参数名称       | 类型       | 描述                  |
| ---------- | -------- | ------------------- |
| code       | Int      | 错误码，0：成功，其他值表示失败 |
| message    | String   | 返回信息                |
| startTime  | Datetime | 起始时间                |
| endTime    | Datetime | 结束时间                |
| metricName | String   | 指标名称                |
| period     | Int      | 监控统计周期              |
| dataPoints | Array    | 监控数据列表              |


## 4. 错误码表

| 错误代码 | 错误描述    | 英文描述                                 |
| ---- | ------- | ------------------------------------ |
| -502 | 资源不存在   | OperationDenied.SourceNotExists      |
| -503 | 请求参数有误  | InvalidParameter                     |
| -505 | 参数缺失    | InvalidParameter.MissingParameter    |
| -507 | 超出限制    | OperationDenied.ExceedLimit          |
| -509 | 错误的维度组合 | InvalidParameter.DimensionGroupError |
| -513 | DB操作失败  | InternalError.DBoperationFail        |

## 5. 示例

**输入**

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>
&namespace=qce/bm_lb
&metricName=eip_outpkg
&dimensions.0.name=vip
&dimensions.0.value=115.115.115.115
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
&period=300
</pre>

**输出**

```shell
{
    "code": 0,
    "message": "",
    "metricName": "eip_outpkg",
    "startTime": "2016-06-28 14:10:00",
    "endTime": "2016-06-28 14:20:00",
    "period": 300,
    "dataPoints": [
        30,
        35,
        40
    ]
}
```
