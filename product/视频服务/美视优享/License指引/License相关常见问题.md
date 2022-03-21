在使用 License 的过程中，您可能会遇见以下问题，可以参考本文的解答。
[](id:TE_License)
## 腾讯特效 License 相关
[](id:q1)
### 腾讯特效 License 与 腾讯特效 SDK 的关系？
腾讯特效 License 可以理解是为获取腾讯特效 SDK 功能授权所需要的密钥和路径，而腾讯特效 SDK 是为了更好的使用整个服务所特定的软件包、软件框架、操作系统等建立应用软件时的开发工具集合。腾讯特效 SDK 的 License 信息是由一对 Key 和LicenseURL 组成，获取生效授权的 Key 和 LicenseURL 并填入到 SDK 中相应位置，便能启用腾讯特效功能。

[](id:q2)
### 如何获取腾讯特效正式版 License？
若您需要在您的业务中使用腾讯特效 SDK 功能，您可参见计费概述，根据您的需求选择 SDK 套餐进行购买。通过购买相应的 SDK 套餐获取腾讯特效 License 解锁授权，在腾讯云视立方控制台进行绑定，使用相应的功能。具体操作请参见 [购买正式版 License](https://cloud.tencent.com/document/product/616/65879)。

[](id:q3)
### 腾讯特效 License 的有效期是多长？过期后如何更新腾讯特效 License？
- **腾讯特效测试版 License**：的有效期是审批通过后，从签发 License 之日开始往后计算一个月（28天）的时长。比如您在2022年01月01日申请了测试版 License，2022年01月02日申请通过审批并自动签发了 License，测试版 License 将在2022年01月31日的00:00:00过期。
- **腾讯特效正式版 License**：的有效期是审批通过后，从签发 License 之日开始往后计算一年（365天）的时长。比如您在2022年01月01日申请了正式版 License，2022年01月02日申请通过审批并自动签发了 License，正式版 License 将在2023年01月03日的00:00:00过期。
正式版 License 过期后需要重新购买新的 License 进行续期，正式版 License 续期指引，请参见 [续期正式 License](https://cloud.tencent.com/document/product/616/65879#renewal)。

[](id:q4)
### 签发后的腾讯特效 License 支持修改包名吗？
- **腾讯特效测试版 License** 能更改 Android 的 Package Name 和 iOS 的 Bundle ID。
具体操作：进入 [**腾讯云视立方控制台**](https://console.cloud.tencent.com/vcube) > **测试版授权**，单击测试版 License 信息右侧的 **编辑**，进入编辑页面即可修改 Android 的 Package Name 和 iOS 的 Bundle ID。

- **腾讯特效正式版 License** 一旦添加绑定后，是不支持更改 Package Name 和 Bundle ID。

[](id:q5)
### 腾讯特效 License 支持的包名个数是多少？授权台数是多少？
每添加一个 License 会支持 Bundle ID 和 Package Name 两个不同的包名，整个账号可以添加的 License 数量是没有限制的。目前 License 对授权终端的台数也是没有限制的。

[](id:q6)
### 腾讯特效 SDK 如何升降级？
腾讯特效 SDK 一共提供了 10 个版本，各版本功能差异请参见 [计费概述](https://cloud.tencent.com/document/product/616/36807)。您可以在腾讯特效正式版 License 到期之后，选择购买切换为更符合您场景需求的版本。当前 License 仍在有效期内时，我们不支持 SDK 的升降级切换。

腾讯特效测试版 License 是统一签发的最高级版本 S1 - 04 的授权，您可以测试腾讯特效 SDK 的全功能。测试期结束前，您可以更换为与您使用场景匹配的正式版腾讯特效 SDK 和腾讯特效 License。


[](id:Web_License)
## 美颜特效 Web License 相关
[](id:w1)
### 测试版 Web License 和正式版 Web License 有何区别？

- **测试版 Web License**：是赠送给您用来短期开发体验的，**有14天有效期，可以续期一次，合计有28天**。功能上和正式版 Web License 并无区别，都可以授权对应 Domain 和 WeChatAppId 使用。
- **正式版 Web License**：是您通过购买获得（推广期间可以申请内测资源），有效期比较长，是您正式环境长期使用的 License。一个项目下的测试版 Web License 和正式版 Web License，其中只要有一个在有效期内就可以使用。

>! 一个用户最多只能申请10此测试 License。

[](id:w2)
### 如何开通正式版 Web License？

需要购买 Web License 资源（推广期间可以免费申请 [视立方·Web 美颜特效](https://cloud.tencent.com/apply/p/9fuh8sv6fl)），申请通过够会获得正式版 Web License 资源，后续按照  [License 申请与购买](https://tcloud-doc.isd.com/document/product/616/71368?!preview&!editLang=zh#formal) 完成绑定后可以开通。

[](id:w3)
### SDK 接入后报错（referer 或者 WeChatAppId 不匹配）？
请检查您控制台的 Domain 或者 WeChatAppId 配置是否与您实际使用的 Web 域名或 WeChatAppId 匹配，Web 域名如果有特殊端口（除80和443）需要加上端口号

[](id:w3)
### Token 和 LicenseKey 有何区别？
- Token 是 SDK 调用腾讯服务接口的鉴权凭证，用来确定您的身份不会被伪造。
- LicenseKey 是您在您的 **Web 网站**或者**微信小程序**上使用特效功能的授权。
