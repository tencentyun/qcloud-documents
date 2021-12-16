[](id:que1)
### 腾讯云视立方 License 是必须购买的吗？

若您下载的腾讯云视立方版本中，包含直播推流（主播开播和主播观众连麦/主播跨房 PK）或短视频（视频录制编辑/视频上传发布）功能模块，应通过购买对应的云服务的资源包免费获取 License 进行解锁。功能模块解锁详情请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

[](id:que2)
### 腾讯云视立方 License 有单独购买入口吗？

不支持单独购买。需购买相应云服务的资源包免费获取 [直播推流 License](https://cloud.tencent.com/document/product/1449/56973#live) 或者 [短视频 License](https://cloud.tencent.com/document/product/1449/56973#video) 的1年有效期（购买日起算1年有效期）。


[](id:que3)
### 腾讯云视立方 License 和功能模块 License 有什么区别？

![](https://main.qcloudimg.com/raw/26c0c8235ae57714ffd008db8be33397.png)

- 腾讯云视立方 License 通过一组 License URL 和 Key 来获取并校验一个应用下功能模块的授权，管理此应用下的直播推流 License（ RTMP 推流和 RTC 推流）和短视频 License（精简版和基础版）功能模块解锁使用。
- 功能模块 License 包含**直播推流 License** 和**短视频 License**，是购买相应云服务资源包免费获取1年使用有效期并解锁功能模块授权。

直播推流 License（ RTMP 推流 + RTC 推流）可用于开启直播推流（主播开播和主播观众连麦/主播跨房 PK）功能模块，短视频 License（精简版/基础版）可用于开启短视频（视频录制编辑/视频上传发布）功能模块。

[](id:que4)
### 短视频精简版 License 和短视频基础版 License 有什么区别？

短视频 License 包括精简版 License 和基础版 License。

- 精简版 License支持视频生成、上传、处理、分发和播放多种功能。
- 基础版 License 在精简版基础上增加滤镜、特效和转场等能力，快速轻松实现基于移动端的短视频应用。

>?
>- 更多功能支持详细说明，请参见 [短视频 License 功能详情](https://cloud.tencent.com/document/product/1449/56980#UGSV_detail)。
>- 美颜特效更多高级美颜、动效贴纸、AI 抠图和绿幕抠图的功能能力暂通过原（移动直播/短视频）企业版 SDK 对外售卖，通过购买原移动直播企业版License、短视频企业版 License 或者短视频企业版 Pro License 后，使用对应的功能。详情请参见 [美颜特效功能概述](https://cloud.tencent.com/document/product/1449/58916)。

[](id:que5)
### 一个账号下能创建多个腾讯云视立方 License 吗？

一个腾讯云视立方·音视频终端引擎项目整体视作一个 License 进行应用管理，一个腾讯云视立方 License 对应一个 Bundle ID 和 Package Name，管理此应用下的直播推流（RTMP 推流 + RTC 推流）和短视频（精简版/基础版）功能模块。

同一个账号下创建腾讯云视立方 License 的数量没有限制，可管理多个应用项目。为了方便用户管理，相同包名的腾讯云视立方 License 建议通过续期的方式延长有效时间。

> ! **Package Name** 为 Android 的包名，**Bundle Id** 为 iOS 的包名。


[](id:que6)
### 相同包名可以创建多个腾讯云视立方 License 吗？

可以，多个腾讯云视立方 License 填写相同的包名不会影响使用，一般不建议创建多个相同包名的 License。

[](id:que7)
### 腾讯云视立方 License 可以修改 Bundle ID 和 Package Name 吗？

腾讯云视立方正式版 License 包名信息不支持修改，腾讯云视立方测试版 License 可编辑更改包名。请您在添加腾讯云视立方正式版 License 先核对包名在应用商店里是否被占用，提交后不支持修改和替换。

[](id:que8)
### 腾讯云视立方 License 何时过期？
- **正式版 License** 的过期时间取决于其绑定的功能模块 License 有效期，任一绑定的功能模块 License 最晚有效期即为正式版 License 的有效期。功能模块 License 的有效期自资源包购买之日计算，1年后到期次日00:00:00止。
- **测试版 License** 可试用14天，免费续期1次，每个功能模块仅可申请一次，长期试用请购买正式版功能模块 License。试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
<dx-alert infotype="explain" title="示例：">
- 当申请测试开始时间为 `2021-08-12 10:28:41`，则14天后到期时间为 `2021-08-26 10:28:41`。
- 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2021-09-09 10:28:41`；若在试用期14天结束后申请续期，申请续期的时间为 `2021-08-30 22:26:20`，则续期的到期时间为 `2021-09-13 22:26:20`。
</dx-alert>


[](id:que9)
### 创建了多个腾讯云视立方 License， License URL 和 License Key 一样吗？

一样。同一个账户下的腾讯云视立方 License 为方便维护和管理，默认 License URL 和 License Key 是一样的。

[](id:que10)
### 关联 License 的资源包是不是只能这个 License 使用？

该账号下的直播播放域名产生的日结流量后付费消耗均可抵扣。资源包关联只是用于同步有效期，里面的流量不限于 License 使用（流量用尽也不影响 License 的使用）。
**例如：**
用户甲是日结流量后付费计费，购买了一个 10TB 直播流量资源包和 50TB 直播流量资源包，分别创建了 License A 和 License B：

- License A 对应的 App 使用的是 `abc.com` 域名播放，产生了 20TB 的播放流量。
- License B 对应的 App 使用的是 `def.com` 域名播放，产生了 30TB 的播放流量。

只要 `abc.com` 和 `def.com` 这两个是属于用户甲云直播账号下直播的播放域名，则可以使用购买的 10TB + 50TB 资源包进行抵扣，抵扣后用户甲的直播流量资源包剩余 10TB 流量。  

[](id:que11)
### 购买直播推流 License 可以用于小程序直播吗？

不支持，直播推流 License 仅支持 iOS 和 Android 端的 App 在使用直播推流（主播开播和主播观众连麦/主播跨房 PK）功能模块时使用。小程序端接入直播功能需要先具备对应的服务类目，详情参见 [方案选择](https://cloud.tencent.com/document/product/1078/37707)。  

[](id:que12)
### 为什么新版 License 升级后，少了一个 License，多了一个可用资源包？

新版 License 增加了重复包名校验逻辑，当多个同类型的 License 绑定了同一组包名（ Bundle ID 和 Package Name ），此时实际上仅一个 License 会生效；我们会解除无效且有效期较短的 License 绑定关系，为您释放无效绑定的资源包，并且被释放的资源包可以绑定新的 License 使用。

示例：
用户 A 以前购买了两个 10 TB 的直播流量资源包（有效期截止时间不同），获赠两个移动直播 License，并分两次绑定了同一组包名（实际上仅一个 License 有效）。在升级为腾讯云视立方 License 后，仅保留了有效期较长的 License 的绑定；另一个有效期较短的 License 被解除绑定关系，10TB 资源包被释放，用户 A 可以再次进行新的 License 绑定。

[](id:que13)
### 为什么子账户打开腾讯云视立方·音视频终端引擎控制台提示未授权？
#### 问题截图：
<img src="https://main.qcloudimg.com/raw/7423d2e7912de344052c7891629d528b.png" width=400px>

#### 问题解析：
音视频终端引擎控制台需要主账号为子账号独立进行授权策略后方可访问控制台页面。
- 若您仅需要提供子账号访问音视频终端引擎控制台只读的权限，请授权 QcloudVCUBEReadOnlyAccess 策略。
- 若您需要提供子账访问音视频终端引擎号所有操作权限，请授权 QcloudVCUBEFullAccess 策略。
为用户/用户组关联策略以授权相关操作权限的关联指引请参见 [策略授权管理](https://cloud.tencent.com/document/product/598/10602)。

#### 相关问题：
- [子账户为什么无法访问直播控制台 License 相关界面？](https://cloud.tencent.com/document/product/454/43500#que16)
- [子账户为什么无法访问点播控制台 License 相关界面？](https://cloud.tencent.com/document/product/266/50296#que12)

[](id:que14)
### 为什么接收不到音视频终端引擎产品和 License 相关消息通知？
您可以通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端引擎，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。
