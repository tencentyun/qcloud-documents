云 API 为腾讯云向外提供服务的接口，应用系统需要根据语言集成对应的 SDK 调用云 API，SDK 的集成方法请参考以下对应链接：
- [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
- [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
- [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
- [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
- [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
- [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)


SDK 的使用流程如下图所示：
<img src="https://main.qcloudimg.com/raw/3abf6af1b8f0f1096619fa0945a3d789.png" alt="img" style="zoom: 33%;" />            

云 API 支持 Fabric 和 BCOS 调用。
## 获取账户信息
使用云 API 调用合约时除了需要网络、合约的相关参数，还需要提供购买 TBaaS 节点的账户信息，包括 SecretId 和 SecretKey。
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 `SecretId` 和 `SecretKey`。

## 调试接口

在应用系统调用接口之前，若需要对接口进行调试，推荐使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=tbaas&Version=2018-04-16&Action=GetInvokeTx)。该工具提供在线调用、签名验证、SDK 代码生成和快速检索接口等能力，能显著降低使用 [TBaaS API](https://cloud.tencent.com/document/product/663/19457) 的难度。仅需要在页面上输入 API 密钥以及 [请求结构](https://cloud.tencent.com/document/product/663/19457) 的必要参数。


