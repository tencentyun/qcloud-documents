
### 云 API 的应用场景有哪些？

物联网开发平台提供云 API 服务，便于用户通过 API 方式快速开发基于物联网的各行业垂直应用。通常共享租赁场景、智慧园区、智慧酒店公寓、能耗管理监控、工业设备管理等垂直物联网应用可以基于云 API 进行管理、控制设备。例如可以创建产品、创建设备、远程控制设备、查询设备状态、固件升级等。

### 云 API 是否支持在线调试工具？

支持。腾讯云提供了统一的 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=iotexplorer&Version=2019-04-23&Action=UploadFirmware&SignVersion=) 在线调试工具，无需进行签名验证，用户填写必要参数即可在线调试物联网开发平台开放的云 API。

### 云 API 调用或调试时选择哪个 Region？

物联网开发平台中国区公有云云 API 目前开放的是广州区域，在行业垂直应用调用云 API 或使用 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=iotexplorer&Version=2019-04-23&Action=UploadFirmware&SignVersion=) 工具调试云 API 时，请将 Region 设置为“ap-guangzhou” 。

### 云 API 调用时的 SecretId 与 SecretKey 从哪里获取？

腾讯云 API 会对每个访问请求进行身份验证，即每个请求都需要在公共请求参数中包含签名信息（Signature）以验证请求者身份。 签名信息由安全凭证生成，安全凭证包括 SecretId 和 SecretKey；若用户还没有安全凭证，请前往 [云API密钥](https://console.cloud.tencent.com/cam/capi) 页面申请，否则无法调用云 API 接口。

### 云 API 是否有多语言 SDK？

云 API 提供了 Python、Java、PHP、Go、NodeJS、.NET、C++、Ruby 版本的 SDK，可选择合适的 SDK 集成到用户的垂直行业应用系统中。
 
