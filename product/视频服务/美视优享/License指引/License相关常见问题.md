在使用 License 的过程中，您可能会遇见以下问题，可以参考本文的解答。

[](id:q1)
###  License 与 SDK 的关系？
License 可以理解是为获取 SDK 功能授权所需要的密钥和路径，而 SDK 是为了更好的使用整个服务所特定的软件包、软件框架、操作系统等建立应用软件时的开发工具集合。腾讯特效 SDK 的 License 信息是由一对 Key 和LicenseURL 组成，获取生效授权的 Key 和 LicenseURL 并填入到 SDK 中相应位置，便能启用美颜特效功能。

[](id:q2)
###  SDK 的升降级？
腾讯特效 SDK 一共提供了 10 个版本，各版本功能差异请参见 [计费概述](待定)，您可以在正式版 License 到期之后，选择购买切换为更符合您场景需求的版本。当前 License 仍在有效期内时，我们不支持 SDK 的升降级切换。

测试版 License 是统一签发的最高级版本 S1 - 04 的授权，您可以测试 SDK 的全功能。测试期结束前，您可以更换为与您使用场景匹配的正式版 SDK 和 License。

[](id:q3)
###  关于 License 的有效期？
**测试版 License** 的有效期是审批通过后，从签发 License 之日开始往后计算一个月（28天）的时长。例如您在2021年11月1日号申请了测试版 License，2021年11月2日申请通过审批并自动签发了 License，测试版 License 将在2021年11月30日00:00:00过期。

**正式版 License** 的有效期是审批通过后，从签发 License 之日开始往后计算一年（365天）的时长。例如您在2021年12月1日号申请了正式版 License，2021年12月2日申请通过审批并自动签发了 License，正式版 License 将在2022年12月2日00:00:00过期。

[](id:q4)
###  签发后的 License 支持修改包名吗？
测试版 License 能更改 Android 的 Package Name 和 iOS 的 Bundle ID。

具体操作：进入 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) > 测试版授权，单击测试版 License 信息右侧的 **编辑**，进入编辑页面即可修改 Android 的 Package Name 和 iOS 的 Bundle ID。

正式版 License 一旦添加绑定后，是不支持更改 Package Name 和 Bundle ID。

[](id:q5)
###  License 支持的包名个数是多少？授权台数是多少？
每添加一个 License 会支持 Bundle ID 和 Package Name 两个不同的包名，整个账号可以添加的 License 数量是没有限制的。目前 License 对授权终端的台数也是没有限制的。

[](id:q6)
### License 的有效期是多长？过期后如何更新 License？
- **测试版 License**：的有效期是审批通过后，从签发 License 之日开始往后计算一个月（28天）的时长。比如您在2022年01月01日申请了测试版 License，2022年01月02日申请通过审批并自动签发了 License，测试版 License 将在2022年01月31日的00:00:00过期。
- **正式版 License**：的有效期是审批通过后，从签发 License 之日开始往后计算一年（365天）的时长。比如您在2022年01月01日申请了正式版 License，2022年01月02日申请通过审批并自动签发了 License，正式版 License 将在2023年01月03日的00:00:00过期。
正式版 License 过期后需要重新购买新的 License 进行续期，正式版 License 续期指引，请参见 [续期正式 License](https://cloud.tencent.com/document/product/616/65879#renewal)。


