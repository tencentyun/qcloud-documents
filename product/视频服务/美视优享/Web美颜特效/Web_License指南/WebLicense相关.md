[](id:w1)
### 测试版 License 和正式 License 有何区别？
- **测试版 License** 是赠送给您用来短期开发体验的，有14天有效期，可以续期一次，合计28天。功能和正式版 License 并无区别，都可以授权对应 Domain 和 WeChatAppId 使用。
- **正式版 License** 是您通过购买获得（推广期间可以 [免费申请](https://cloud.tencent.com/apply/p/9fuh8sv6fl)），有效期比较长，是您正式环境长期使用的 License。一个项目下的测试版 License 和正式版 License，只要其中一个在有效期内就可以使用。

>! 一个用户最多只能申请10次测试版 License。

[](id:w2)
### 如何开通正式版 License？
要开通正式版 License 需要购买 License 资源（推广期间可以 [免费申请](https://cloud.tencent.com/apply/p/9fuh8sv6fl)），申请通过后会获得正式版 License 资源），后续按照 [**License 申请与购买**](https://cloud.tencent.com/document/product/616/71368) 完成绑定后可以开通。

[](id:w3)
### 后续如何续期？
首次申请可以获得半年的 License，半年后可视推广情况继续免费申请或者购买获得 License 资源，然后续期即可继续使用。

[](id:w4)
### SDK 接入后报错（referer 或者 WeChatAppId 不匹配）？
请检查您控制台的 Domain 或者 WeChatAppId 配置是否与您实际使用的 Web 域名或 WeChatAppId 匹配，Web 域名如果有特殊端口（除80和443）需要加上端口号。

[](id:w5)
### Token 和 LicenseKey 有何区别？
- **Token** 是 SDK 调用腾讯服务接口的鉴权凭证，用来确定您的身份不会被伪造。
- **LicenseKey** 是您在 **Web 网站**或者**微信小程序**上使用 **Web 美颜特效**的授权 key。
