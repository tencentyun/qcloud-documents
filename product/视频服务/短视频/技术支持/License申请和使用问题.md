[](id:que0)
### 关于 License 版本问题？
短视频 SDK 分基础版和企业版，从4.5版本开始需要 License，基础版只需要短视频的 License（TXUgcSDK.licence），企业版还同时需要 Pitu 的 License（YTFaceSDK.licence），把 License 放到工程目录，并修改为对应的名字即可。

4.9版本开始 License 使用方式有改变，可以选择是否把 License 打包到项目中。使用时需要调用 setLicenceURL：key：接口设置 License 的 url 和 key。
>!4.5 - 4.7版本的 SDK 不支持 License 自动续期，4.9版本开始才支持自动续期。4.9的 SDK 可以兼容之前的 Licence（url 和 key 不能传 null，可以随便传个字符串），但是新的 License 无法在4.9之前的 SDK 上使用。


[](id:que1)
### 测试 License 到期后是否可以延期？

您可以免费申请测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。到期后请尽快 [购买正式 License](https://cloud.tencent.com/document/product/266/50290#.E8.B4.AD.E4.B9.B0.E6.AD.A3.E5.BC.8F.E7.89.88-license)。

> !试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
>
> - 当申请测试开始时间为 `2021-08-12 10:28:41`，则14天后到期时间为 `2021-08-26 10:28:41`。
> - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2021-09-09 10:28:41`；若在试用期14天结束后申请续期，申请续期的时间为 `2021-08-30 22:26:20`，则续期的到期时间为 `2021-09-13 22:26:20`。


[](id:que2)
### 测试 License 能否更改 Android 的 PackageName 和 iOS 的 BundleID?
测试 License 支持更改，在 [云点播控制台](https://console.cloud.tencent.com/vod/license/video) 选择测试 License 信息右上角，单击**编辑**即可进行修改。

[](id:que3)
### 正式 License 能否更改 Android 的 PackageName 和 iOS 的 BundleID?
当前版本，正式 License **不能**更改 PackageName 和 BundleID，后续版本会加以支持。

[](id:que4)
### License 可以同时支持多个 App 吗？
一个 License 只能对应一个 PackageName 和 BundleID，不支持多个 App。

[](id:que5)
### License 应该如何确认绑定关系（Android 的 PackageName 和 iOS 的 BundleID）?
在填写时用户需要确认绑定正式上架 App Store 的 iOS 所对应的 Bundle ID 和正式上架应用市场 Android 的 Package Name。

[](id:que6)
### 续期 License 时出现“license not exist”问题，如何解决？
您可登录**云点播控制台**>**License 管理** >**[SDK License](https://console.cloud.tencent.com/vod/license/video)**根据以下方式排查：
1. 请确认是否在**管理员**页面进行 License 绑定续期。
![](https://main.qcloudimg.com/raw/446b60171da15bee7b10537ea2f63f32.png)
2. 如果您是在**非管理员**页面下进行操作，请联系**管理员**协助您进行 License 变更操作。

[](id:que7)
### License 无法添加/新增，如何解决？
- 确认是否有可绑定的资源包。进入**云点播控制台**>**[资源包](https://console.cloud.tencent.com/vod/assets/packages)**，确认您的账号下是否有可绑定的点播流量 10T、50T、200T 或 1PB 资源包中的一种。
- 查看绑定页面是否为**管理员**页面，请选择管理员页面进行绑定。

[](id:que8)
### License 校验失败，如何排查？
建议您可以参考以下几点进行排查：
- 确认您的 License 是否在有效期内。
- 确认 License 信息里的 Package Name 是否与项目里面的包名一致。
- 确认 License 中的 LicenseUrl 协议是否为 HTTPS。

>? 若上述方法无法解决您的问题，建议**卸载应用重新安**装或 [提工单](https://console.cloud.tencent.com/workorder/category) 解决。 


[](id:que9)
### 没有 bundleid，Android 端是不是无法使用 License？
bundleid 类似于 Android 端的 package name，若您不集成 iOS 端，可随意填写，不使用即可。

[](id:que10)
### 精简版的短视频 SDK，想升级成基础版 License，要怎么操作？
购买点播流量资源包 50TB、200TB 或 1PB 获取基础版 License 使用权。
> ?目前只支持短视频 License 由精简版升级至基础版，升级的 License 为对应的资源包赠送的 License 规格。

[](id:que11)
### 个人购买的短视频 SDK License 可以用于企业吗？
短视频 SDK 暂仅支持购买所在账号进行使用，暂无个人实名认证以及企业实名认证的限制。

[](id:que12)
### 为什么我的子账户已经授权了直播和点播所有权限，但是还是无法访问 License 控制台相关界面？
#### 问题截图：
<img src="https://main.qcloudimg.com/raw/7423d2e7912de344052c7891629d528b.png" width=400px>

#### 问题解析：
新版 SDK License 本次升级更新了接口（详情请参见 [新旧 License 说明](https://cloud.tencent.com/document/product/1449/56980#.E6.96.B0.E6.97.A7-license-.E5.8C.BA.E5.88.AB)），需要主账号为子账号独立进行重新授权策略后方可访问 License 控制台页面。
- 若您仅需要提供子账号查询 License 的权限，请授权 QcloudVCUBEReadOnlyAccess 策略。
- 若您需要提供子账号所有 License 操作权限，请授权 QcloudVCUBEFullAccess 策略。

为用户/用户组关联策略以授权相关操作权限的关联指引请参见 [策略授权管理](https://cloud.tencent.com/document/product/598/10602)。

>? License 界面所有功能操作已独立于云直播、云点播策略外，即原 QcloudVODFullAccess、QcloudLIVEFullAccess 策略已不包含 License 相关接口，需按照上述说明单独授权。

[](id:que13)
### 为什么接收不到 License 到期等相关消息通知？
短视频 License 用于腾讯云视立方·音视频终端引擎管理功能模块的授权解锁，您可以通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端引擎，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。短视频正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。
