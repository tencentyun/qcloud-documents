## 操作场景
TSW 本身不提供 Go 语言客户端采集，但可兼容通过 Skywalking 的 Go2Sky 接入应用，向TSW后端上报数据。TSW 目前已支持将 Skywalking 上报的数据转换成自身兼容的 Opentracing 格式，在服务调用监控、调用链、依赖拓扑等功能上，功能可与使用 TSW 自有 Agent 保持一致。

## 操作流程
#### 1. 获取接入点和 Token
在 [TSW 控制台](https://console.cloud.tencent.com/tsw)的【服务监控】>【服务列表】中，单击【接入服务】，选择 Go 语言与 Skywalking 的数据采集方式。您可在下方的获取接入点和 Token 中找到私网接入点与您的个人 Token。

#### 2. 接入埋点
参考 [Go2Sky 文档](https://github.com/SkyAPM/go2sky)，自行对 Go 的跨服务调用埋点。
Go 语言应用在使用 Skywalking 上报数据时有一定改造成本，您需要改造少量业务代码以完成接入埋点。

#### 3. 修改上报配置
将 reporter 的 serverAddr 修改为 TSW 的接入点，将 reporter 的 auth 修改为 Token。

#### 4. 重启服务，开始上报数据

## 接入验证
向应用发送请求，在收到响应后，在 TSW 控制台查看调用数据。
您可以在1分钟内通过【链路追踪】>【调用链查询】>【[Span查询](https://console.cloud.tencent.com/tsw/trace?rid=1&tab=span)】查找调用详情。监控曲线与统计数据将在1分钟后开始正常显示。

（完善中）
操作流程步骤2中的改造详情举例


