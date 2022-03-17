## 命名空间

Namespace=QCE/APIGATEWAY 

## 指标名称

| 指标英文名 | 指标中文名   | 指标含义                                                     | 计算方式                     | 单位 |
| ------------- | ------------------------------------------------------------ | ---------------------------- | ---- | ---- |
| NumOfReq | 请求数        | 经过 API 网关的请求数量                                        | 按照所选择的时间粒度统计求和 | 次   |
| SuccReq | 有效调用次数  | 经过 API 网关的有效调用请求数量	 | 按照所选择的时间粒度统计求和                           |   次   |
| OutTraffic | 外网出流量    | API 网关所发出的公网数据包的流量	 | 按照所选择的时间粒度统计求和                           |  MB    |
| InTraffic | 内网出流量    | API 网关所发出的内网数据包的流量                              | 按照所选择的时间粒度统计求和 | MB   |
| ResponseTime | 响应时间      | API 网关对请求作出响应的时间                                  | 按照所选择的时间粒度的平均值 | ms   |
| ClientError | 前台错误数    | 客户端发送到 API 网关的请求是非法请求，如鉴权不通过或者超过限流值的错误个数 | 按照所选择的时间粒度统计求和 | 次   |
| ServerError | 后台错误数    | API 网关将消息转发到后端服务，后端服务返回大于等于400错误状态码的个数 | 按照所选择的时间粒度统计求和 | 次   |
| ConcurrentConnections | 并发连接数    | API 网关当前长连接的数量                                      | 按照所选择的时间粒度的平均值 | 条   |
| Serviceservererror404 | 后台404错误数 | 请求后端服务失败，请求所希望的资源未被在后端服务器上发现，此类错误个数的统计 | 按照所选择的时间粒度统计求和 | 次   |
| Serviceservererror502 | 后台502错误数 | API 网关尝试执行后端请求时，从后端服务器接收到无效的响应，此类错误个数的统计 | 按照所选择的时间粒度统计求和 | 次   |

> ?
> - API 网关监控指标支持所有维度，您可根据相关 [维度说明](#weidu) 进行监控指标的维度筛选。
> - 每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度及维度信息。

## 各维度对应参数总览

| 参数名称                       | 维度名称        | 维度解释                      | 格式                                     |
| ------------------------------ | --------------- | ----------------------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | serviceId       | API 网关服务 ID 的维度名称     | 输入 String 类型维度名称：serviceId       |
| Instances.N.Dimensions.0.Value | serviceId       | 具体的 API 网关服务 ID         | 输入具体服务 ID，例如：service-12345jy    |
| Instances.N.Dimensions.1.Name  | environmentName | 环境维度名称                  | 输入 String 类型维度名称：environmentName |
| Instances.N.Dimensions.1.Value | environmentName | 具体环境名称                  | 输入环境名称，例如：release、test、repub |
| Instances.N.Dimensions.2.Name  | apiId/key       | apiId 或者 secretKey 的维度名称 | 输入 String 类型维度名称：apiId/key        |
| Instances.N.Dimensions.2.Value | apiId/secretId  | 具体的 apiId 或者 secretId      | 输入具体的 apiId 或者 secretId          |

[](id:weidu)

## 维度说明

</span>

 API 网关提供了获取以下三种级别监控数据的组合 ：环境维度、API 维度、密钥对（SecretId 和 SecretKey）维度。

以下为 API 网关的三种维度组合的查询方式 ：

#### 1.  环境维度，入参取值

&Namespace=QCE/APIGATEWAY
&Instances.N.Dimensions.0.Name=serviceId
&Instances.N.Dimensions.0.Value=serviceId 的值
&Instances.N.Dimensions.1.Name=environmentName
&Instances.N.Dimensions.1.Value=环境名

#### 2.  API 维度，入参取值

&Namespace=QCE/APIGATEWAY
&Instances.N.Dimensions.0.Name=serviceId
&Instances.N.Dimensions.0.Value=serviceId 的值
&Instances.N.Dimensions.1.Name=environmentName
&Instances.N.Dimensions.1.Value=环境名
&Instances.N.Dimensions.2.Name=apiId
&Instances.N.Dimensions.2.Value=API 的 ID

#### 3. 密钥对维度，入参取值（需要开启白名单）

&Namespace=QCE/APIGATEWAY
&Instances.N.Dimensions.0.Name=serviceId
&Instances.N.Dimensions.0.Value=serviceId 的值
&Instances.N.Dimensions.1.Name=environmentName
&Instances.N.Dimensions.1.Value=为环境名
&Instances.N.Dimensions.2.Name=key
&Instances.N.Dimensions.2.Value=密钥对的 secretid
