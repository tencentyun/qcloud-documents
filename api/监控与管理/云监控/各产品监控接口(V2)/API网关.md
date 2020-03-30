## 1. 接口描述

域名：monitor.api.qcloud.com
接口：GetMonitorData

API 网关（API Gateway）是 API 托管服务。提供 API 的完整生命周期管理，包括创建、维护、发布、运行、下线等。您可使用 API Gateway 封装自身业务，将您的数据、业务逻辑或功能安全可靠的开放出来，用以实现自身系统集成、以及与合作伙伴的业务连接
查询API网关产品监控数据，入参取值如下：

qce/apigateway支持以下几种维度组合的查询方式，入参取值如下：

### 1.1 环境维度，入参取值

&namespace=qce/apigateway
&dimensions.0.name=serviceId
&dimensions.0.value serviceId 的值
&dimensions.1.name=environmentName
&dimensions.1.value 为环境名



### 1.2 API 维度，入参取值

&namespace=qce/apigateway
&dimensions.0.name=serviceId
&dimensions.0.value serviceId 的值
&dimensions.1.name=environmentName
&dimensions.1.value 为环境名
&dimensions.2.name=apiid
&dimensions.2.value 为 API 的 ID




### 1.3 密钥对维度，入参取值（需要开启白名单）

&namespace=qce/apigateway
&dimensions.0.name=serviceId
&dimensions.0.value serviceId 的值
&dimensions.1.name=environmentName
&dimensions.1.value 为环境名
&dimensions.2.name=key
&dimensions.2.value 为密钥对的 secretid




## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 GetMonitorData。

### 2.1 输入参数

#### 2.1.1 输入参数总览

| 参数名称               | 必选   | 类型       | 输入内容    | 描述                                       |
| ------------------ | ---- | -------- | ------- | ---------------------------------------- |
| namespace          | 是    | String   | qce/apigateway | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称 | 指标名称，具体名称见2.2                            |
| dimensions.n.name  | 是    | String   | 维度的名称   | 维度的名称，具体维度名称见第2.1.2小节，与 dimensions.n.value 配合使用。 |
| dimensions.n.value | 是    | String   | 对应的维度的值 | 对应的维度的值，具体维度名称见第2.1.2小节，与 dimensions.n.name 配合使用。 |
| period             | 否    | Int      | 60/300  | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标详情列表。 |
| startTime          | 否    | Datetime | 起始时间    | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| endTime            | 否    | Datetime | 结束时间    | 结束时间，默认为当前时间。 endTime 不能小于 startTime       |


#### 2.1.2 各维度对应参数总览

| 参数名称               | 维度名称             | 维度解释          | 格式                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| dimensions.0.name  | serviceId              | API 网关服务 ID      | String 类型维度名称：serviceId              |
| dimensions.0.value | serviceId             | API 网关服务 ID       | 具体 IP 地址      |
| dimensions.1.name  | environmentName | 环境名称        | String 类型维度名称：environmentName |
| dimensions.1.value | environmentName | 环境名称        | 环境名称，release、test、repub                     |
| dimensions.2.name  | apiid/key       | APIid 或者密钥对            | String类型维度名称： apiid/key         |
| dimensions.2.value | apiid/secretid       | APIid 或者密钥对公钥           | 具体的 apiid 或者 secretid（维度为 key）               |


### 2.2 指标名称

| 指标名称（metricName） | 含义    | 单位   |
| ---------------- | ----- | ---- |
| response_time           | 响应时间数据 | ms    |
| client_error         | 前台错误数 | 次    |
| server_error        | 后台错误数   |次 |
| concurrent _connections       | 并发链接数   | 条 |
| out_traffic            | 七层外网出流量   |MB  |
| num_of_req           | 请求次数   | 次  |
| ApiServerError404        | 后台404错误数   |次 |
|ApiServerError502      | 后台502错误数   | 次 |


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
&namespace=qce/apigateway
&metricName=response_time
&dimensions.0.name=serviceId
&dimensions.0.value=serviceIdvalue
&dimensions.1.name=environmentName
&dimensions.1.value=environmentNamevalue
&dimensions.2.name=apiid
&dimensions.2.value=appiidvalue
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

**输出**

```shell
{
	"code": 0,
	"message": "",
	"metricName": "response_time",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		5.6,
		6.5,
		7.7
	]
}
```
