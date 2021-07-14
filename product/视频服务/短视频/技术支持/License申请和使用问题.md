[](id:que0)
### 关于 License 版本问题？
短视频 SDK 分基础版和企业版，从4.5版本开始需要 License，基础版只需要短视频的 License（TXUgcSDK.licence），企业版还同时需要 Pitu 的 License（YTFaceSDK.licence），把 License 放到工程目录，并修改为对应的名字即可。

4.9版本开始 License 使用方式有改变，可以选择是否把 License 打包到项目中。使用时需要调用 setLicenceURL：key：接口设置 License 的 url 和 key。
>!4.5 - 4.7版本的 SDK 不支持 License 自动续期，4.9版本开始才支持自动续期。4.9的 SDK 可以兼容之前的 Licence（url 和 key 不能传 null，可以随便传个字符串），但是新的 License 无法在4.9之前的 SDK 上使用。


[](id:que1)
### 测试 License 到期后是否可以延期？
测试 License 试用期最多28天，不能延期，到期后请尽快 [购买正式 License](https://cloud.tencent.com/document/product/266/50290#.E8.B4.AD.E4.B9.B0.E6.AD.A3.E5.BC.8F.E7.89.88-license)。

[](id:que2)
### 测试 License 能否更改 Android 的 PackageName 和 iOS 的 BundleID?
测试 License 支持更改，在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 选择测试 License 信息右上角，单击【编辑】即可进行修改。

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
您可登录【云点播控制台】>[【短视频 SDK License】](https://console.cloud.tencent.com/vod/license/video)根据以下方式排查：
1. 请确认是否在**管理员**页面进行 License 绑定续期。
![](https://main.qcloudimg.com/raw/9aca1889cc06d22300d031c9a01a7004.png)
2. 如果您是在**非管理员**页面下进行操作，请联系**管理员**协助您进行 License 变更操作。

[](id:que7)
### License 无法添加/新增，如何解决？
- 确认是否有可绑定的资源包。进入【云点播控制台】>【[资源包](https://console.cloud.tencent.com/vod/assets/packages)】，确认您的账号下是否有可绑定的点播流量 10T、50T 或 200T 资源包中的一种。
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
购买点播流量资源包 50TB 或 200TB 获取基础版 License 使用权。
> ?目前只支持短视频 License 由精简版升级至基础版，升级的 License 为对应的资源包赠送的 License 规格。

[](id:que11)
### 个人购买的短视频 SDK License 可以用于企业吗？
短视频 SDK 暂仅支持购买所在账号进行使用，暂无个人实名认证以及企业实名认证的限制。
