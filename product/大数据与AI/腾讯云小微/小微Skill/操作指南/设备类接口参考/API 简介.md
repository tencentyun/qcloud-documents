Smart Home Skill API 使用 JSON 消息格式与您的技能适配器进行通信。技能适配器作为一个 https 服务可以架设在腾讯云上，也可以架设在您自己的服务器上。该服务以包含 Header 和 Payload 对象的 JSON 格式的请求发送事件到您的技能适配器。您的技能适配器返回 JSON 格式的响应，该响应还包含 Header 和 Payload。用于这些请求和响应的语法是技能适配器指令语言。一个单独的请求或响应就是一个技能适配器指令。在您的技能适配器的代码中，您需要根据指令头以确定 Smart Home Skill API 发送的消息类型。您将使用消息有效内容的详细信息与客户的云连接设备进行通信，并响应指示操作成功或不成功。以下是有关指令结构的一些细节。

## 认证
Smart Home Skill API 遵循 OAuth2.0 规范。从 Smart Home Skill API 发送到技能适配器的每个请求都包含 OAuth 访问令牌。 此外，任何可云控设备的设备云都必须支持授权码授权模式。 确保实施 OAuth 的第三方提供商已经将分配给智能家居技能的 OAuth 重定向地址添加到白名单中。 您可以在开发人员门户上的应用程序的配置页面上找到此 URL。要了解有关腾讯云小微身份验证如何工作的更多信息，请参阅{文档待定}。

## 技能适配器指令
所有技能适配器指令（无论是由 Smart Home Skill API 发送到适配器还是由适配器发送回 Smart Home Skill API）共享相同的基本结构。 技能适配器指令包含两个顶级对象：

*   **Header**
*   **Payload**

另外，两个方向上的技能适配器指令的大小限制都是 128KB。

### Message Headers
指令头具有一组在消息类型中相同的预期字段。 它们描述消息命名空间（namespace），指令名称（name），目标版本（payloadVersion）和唯一消息标识符（messageId）。 以下是典型的 Message Header 的 JSON 示例：
```
{
    "header": {
        "messageId": "9422676d-2356-4aa7-aa88-c642f12bfcd6",
        "name": "DiscoverAppliancesRequest",
        "namespace": "SmartHome.Discovery",
        "payloadVersion": "1"
    }
}
```

header 必须包含以下属性：

| 参数 | 描述 |
| --- | --- |
| messageID | 单个请求或响应的唯一标识符。这用于跟踪目的，技能适配器应该记录此信息，尽管它不应用于支持业务逻辑。来自技能适配器的每条消息都必须填充此字段。任何只包含数字字符及‘-’且长度短于128的字符串都是有效的，但是推荐使用随机数生成的 UUID。 |
| name | 指令的名称，如*DiscoverAppliancesRequest*或*DiscoverAppliancesResponse* |
| namespace | 指令所在的命名空间。 目前的类别有：SmartHome.Discovery、SmartHome.Control、SmartHome.Query |
| payloadVersion | 应用于**Payload**的 API 版本。当前版本为 1，该版本的 payload 格式在本文档中描述。 |

### Message Payload
技能适配器指令的 **Payload** 取决于在 **Header** 中指定的指令的名称，并且 **Payload** 属性将根据请求中包含的指令而有所不同。每个指令类型详细描述有效载荷内容。
以下部分描述不同类型的指令，其预期的 **Payload** 描述和示例。

|任务|类别|指令名称|
|---|----|----|
|  发现已连接设备 | SmartHome.Discovery  | DiscoverAppliancesRequest</br>DiscoverAppliancesResponse |
| 控制连接设备：打开、关闭，更改设置等   | SmartHome.Control  | DecrementColorTemperatureRequest </br> DecrementColorTemperatureConfirmation </br> DecrementPercentageRequest </br>  DecrementPercentageConfirmation </br> DecrementBrightnessRequest </br> DecrementBrightnessConfirmation </br> IncrementColorTemperatureRequest </br> IncrementColorTemperatureConfirmation </br> IncrementPercentageRequest </br> IncrementPercentageConfirmation </br> IncrementTargetTemperatureRequest </br> IncrementTargetTemperatureConfirmation </br> IncrementBrightnessRequest </br> IncrementBrightnessConfirmation </br> SetColorRequest <br> SetColorConfirmation </br> SetColorTemperatureRequest </br> SetColorTemperatureConfirmation </br> SetPercentageRequest </br> SetPercentageConfirmation </br> SetBrightnessRequest </br> SetBrightnessConfirmation </br> SetTargetTemperatureRequest </br> SetTargetTemperatureConfirmation </br> TurnOnRequest </br> TurnOnConfirmation </br> TurnOffRequest </br> TurnOffConfirmation </br>ActivationSenceRequest </br> ActivationSenceConfirmation </br> DeactivateSenceRequest </br> DeactivateSenceConfirmation  |
| 查询连接设备的当前状态  |  SmartHome.Query |  GetTargetTemperatureRequest </br> GetTargetTemperatureResponse </br> GetTemperatureReadingRequest </br> GetTemperatureReadingResponse |
