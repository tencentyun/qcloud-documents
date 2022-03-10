[](id:que10)
### Android 下如何获取 package name？
您可在 Android 工程下的 `Mainfest.xml` 文件中获取，如下所示：
```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
	package="com.huawei.player"
	android:versionCode="20181111"
	android:versionName="1.0">
``` 

[](id:que11)
### iOS 下如何获取 Bundle ID？
iOS 可在工程配置中的`General->Identity`中获取，如下图所示：
![](https://main.qcloudimg.com/raw/56571d560da04bf6563ccae91d32b75a.png)

[](id:que12)
### 测试版 License 到期后是否可以延期？
测试 License 试用期最多28天，初次申请满14天后可延期一次，不支持二次延期，到期后请尽快 [购买正式 License](https://cloud.tencent.com/document/product/454/34750)。
试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。

- 当申请测试开始时间为 `2021-08-12 10:28:41`，则14天后到期时间为 `2021-08-26 10:28:41`。
- 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2021-09-09 10:28:41`；若在试用期14天结束后申请续期，申请续期的时间为 `2021-08-30 22:26:20`，则续期的到期时间为 `2021-09-13 22:26:20`。

[](id:que13)
### 测试版 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
测试版 License 能更改 Android 的 Package Name 和 iOS 的 Bundle ID。
具体操作：进入**云直播控制台**>[**License 管理**](https://console.cloud.tencent.com/live/license)，单击测试版 License 信息右侧的**编辑**，进入编辑页面即可修改 Android 的 Package Name 和 iOS 的 Bundle ID。

[](id:que14)
### 正式版 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
正式版 License 不能更改 Package Name 和 Bundle ID。

[](id:que15)
### License 可以同时支持多个 App 吗？
一个 License 只能对应一个 Package Name 和一个 Bundle ID，若多个 App 使用 SDK 功能，需要购买多个资源包新增多个 License。

[](id:que1)
### 移动直播 License 是必须购买的吗？
移动直播 SDK 的直播推流功能，必须通过购买移动直播 License 进行解锁。
>! 短视频 License 无法解锁移动直播相关功能。


[](id:que2) 
### 移动直播 License 有单独购买入口吗？
不支持单独购买。
- 直播推流 License（原移动直播基础版 SDK License） ：需购买云直播10TB及以上 [流量资源包](https://cloud.tencent.com/document/product/267/34174) 获取一年使用授权。
- 移动直播企业版 SDK License：需 [联系腾讯云商务](https://cloud.tencent.com/apply/p/h1qsz5vhvko) 申请。

[](id:que3)
### 直播推流 License（原移动直播基础版 SDK License） 和移动直播企业版 License 有什么区别？
直播推流 License（原移动直播基础版 SDK License） 即可解锁直播推流和播放功能，以及基础的美颜功能（美白、磨皮等）。
移动直播企业版 License 是在其之上，增加了高级美颜（大眼、瘦脸）、绿幕功能、动效贴纸、AI 抠图等能力，还可以配合美妆和手势素材实现额外的功能。

>?
>- SDK 下载中的3个版本的 SDK 均可用直播推流 License（原移动直播基础版 SDK License） 来解锁直播推流和播放功能。
>- 企业版中的高级美颜相关功能只能通过移动直播企业版 License 来解锁。


[](id:que4)
### 一个账号下能创建多个 License 吗？
同一个账号下创建 License 的数量没有限制。为了方便用户管理，相同包名的 License 建议通过续期的方式延长有效时间。

[](id:que5)
### 相同包名可以创建多个 License 吗？
可以，多个 License 填写相同的包名不会影响使用，不过同时创建多个 License 有效期会各自计算，一般不建议创建多个相同包名的 License。

[](id:que6)
### License 可以修改吗？
移动直播 License 可通过续期来延长有效时间，包名信息不支持修改，请您在添加 License 先核对包名在应用商店里是否被占用，提交后不支持修改和替换。

[](id:que7)
### 为什么我创建了多个 License ，但是 licenseurl 和 key 都是一样的？
同一个账号下移动直播的 licenseurl 和 key 默认是相同的。这样保证了测试 License 、正式 License、不同包名的 License 均可以复用相同的接口信息。

>?不建议使用免费测试的 License 发布到线上运行。您可以通过添加新的正式版 License，即可无需再修改接口中的 licenseurl 和 key，切换到正式版 License。

[](id:que8)
### 关联 License 的资源包是不是只能这个 License 使用？
该账号下的标准直播播放域名产生的日结流量后付费消耗均可抵扣。资源包关联只是用于同步有效期，里面的流量不限于 License 使用（流量用尽也不影响 License 的使用）。
**例如：**
用户甲是日结流量后付费计费，购买了一个10TB标准直播流量包和50TB标准直播流量包，分别创建了 License A 和 License B：
   - License A 对应的 App 使用的是`abc.com`域名播放，产生了20TB的播放流量。
   - License B 对应的 App 使用的是`def.com`域名播放，产生了30TB的播放流量。

只要`abc.com`和`def.com`这两个是属于用户甲云直播账号下标准直播的播放域名，即可使用购买的10TB + 50TB来抵扣，抵扣后用户甲的标准直播流量包剩余10TB流量。  

[](id:que9)
### 购买移动直播 License 可以用于小程序直播吗？
不支持，移动直播 License 仅支持 iOS 和 Android 端的 App 在使用移动直播 SDK 直播功能时使用。小程序端接入直播功能需要先具备对应的服务类目，详情参见 [方案选择](https://cloud.tencent.com/document/product/1078/37707)。  

[](id:que16)
### 为什么我的子账户已经授权了直播和点播所有权限，但是还是无法访问 License 控制台相关界面？
#### 问题截图：
<img src="https://main.qcloudimg.com/raw/7423d2e7912de344052c7891629d528b.png" width=400px>

#### 问题解析：
新版 SDK License 本次升级更新了接口（详情请参见 [新旧 License 说明](https://cloud.tencent.com/document/product/1449/56980#.E6.96.B0.E6.97.A7-license-.E5.8C.BA.E5.88.AB)），需要主账号为子账号独立进行重新授权策略后方可访问 License 控制台页面。
- 若您仅需要提供子账号查询 License 的权限，请授权 QcloudVCUBEReadOnlyAccess 策略。
- 若您需要提供子账号所有 License 操作权限，请授权 QcloudVCUBEFullAccess 策略。

为用户/用户组关联策略以授权相关操作权限的关联指引请参见 [策略授权管理](https://cloud.tencent.com/document/product/598/10602)。

>? License 界面所有功能操作已独立于云直播、云点播策略外，即原 QcloudVODFullAccess、QcloudLIVEFullAccess 策略已不包含 License 相关接口，需按照上述说明单独授权。

[](id:que17)
### 为什么接收不到 License 到期等相关消息通知？
移动直播 SDK 的直播推流 License 用于腾讯云视立方·音视频终端引擎管理功能模块的授权解锁，您可以通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端引擎，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。直播推流正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。
