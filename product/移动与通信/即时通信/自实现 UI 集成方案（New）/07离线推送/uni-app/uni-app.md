## 概述
[TUIOfflinePush](https://ext.dcloud.net.cn/plugin?id=9149) 是 uni-app 平台的腾讯云即时通信 IM Push 插件。目前支持华为、小米、oppo、vivo、魅族等 Android 厂商推送和 iOS 推送。
>!
>- 在没有主动退出登录的情况下，应用退后台、手机锁屏、或者应用进程被用户主动杀掉三种场景下，如果想继续接收到 IM 消息提醒，可以接入即时通信 IM 离线推送。
>- 如果应用主动调用  logout 退出登录，或者多端登录被踢下线，即使接入了 IM 离线推送，也收不到离线推送消息。

## 效果
![](https://qcloudimg.tencent-cloud.cn/raw/ca52cff62e712bbe4e800e4f1e7f0878.png)

## 集成 TUIOfflinePush 跑通离线推送功能

集成 TUIOfflinePush 插件之前，需要申请相关的参数和证书。

### 安卓配置
#### 步骤一：注册应用到厂商推送平台
离线推送功能依赖厂商原始通道，您需要将自己的应用注册到各个厂商的推送平台，得到 AppID 和 AppKey 等参数。目前国内支持的手机厂商有：[小米](https://dev.mi.com/console/doc/detail?pId=68)、[华为](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060)、[OPPO](https://open.oppomobile.com/wiki/doc#id=10195)、[VIVO](https://dev.vivo.com.cn/documentCenter/doc/281)、[魅族](http://open-wiki.flyme.cn/doc-wiki/index#id?129)。
#### 步骤二：IM 控制台配置
请参考 [IM 控制台配置](https://cloud.tencent.com/document/product/269/75428#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E6.B3.A8.E5.86.8C.E5.BA.94.E7.94.A8.E5.88.B0.E5.8E.82.E5.95.86.E6.8E.A8.E9.80.81.E5.B9.B3.E5.8F.B0) 文档，登录腾讯云 [即时通信 IM 控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Favc) ，添加各个厂商推送证书，并将您在步骤一中获取的各厂商的 AppId、AppKey、AppSecret 等参数配置给 IM 控制台的推送证书。
#### 步骤三：IM 控制台跳转参数配置
![](https://qcloudimg.tencent-cloud.cn/raw/60e98388da66e10a6b8e634a9568f48b.png)
### iOS 配置
#### 步骤一：iOS 申请 APNs 证书
向 Apple [申请 APNs 推送证书](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E7.94.B3.E8.AF.B7-apns-.E8.AF.81.E4.B9.A6)，然后 [上传推送证书到 IM 控制台](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E4.B8.8A.E4.BC.A0.E8.AF.81.E4.B9.A6.E5.88.B0.E6.8E.A7.E5.88.B6.E5.8F.B0) 。之后按照如下步骤操作即可快速接入 IM 离线推送。
#### 步骤二：在腾讯云控制台上传第三方推送证书后分配的证书 ID
当您 [上传证书到 IM 控制台](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E4.B8.8A.E4.BC.A0.E8.AF.81.E4.B9.A6.E5.88.B0.E6.8E.A7.E5.88.B6.E5.8F.B0) 后，IM 控制台会为您分配一个证书 ID ，见下图。
<img src="https://qcloudimg.tencent-cloud.cn/raw/15802b097a0347f16a28c1a354ee3ea3.png" style="zoom:40%;" />

### 集成 TUIOfflinePush 插件 
#### 步骤一： **下载 TUIOfflinePush 插件并 <font color=red>本地集成</font>**
   登录uni 原生插件市场，在 [ TUIOfflinePush 插件](https://ext.dcloud.net.cn/plugin?id=9149) 详情页面，下载插件或者使用HBuilderX 导入插件。
	 将插件下载到本地，放入项目 nativeplugins 中，在项目 manifest.json --> App原生插件配置 --> 选择本地插件中勾选 TUIOfflinePush 插件。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/09d6b4f0e8d9cfe0d6dd98903f253371.png)
> - <font color=red>该插件仅支持本地集成，不支持云端集成方式</font>。
#### 步骤二：在项目 manifest.json --> App模块配置 中勾选 Push 模块，不勾选unipush。
![](https://qcloudimg.tencent-cloud.cn/raw/b9847502c3bb6623f09a942a7b5af417.jpeg)
#### 步骤三：在项目中注册 TUIOfflinePush 插件，[注册插件API](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#registerPlugin)。
```
 // v2.22.0 起支持 uni-app 打包 native app 时使用离线推送插件
 // 请注意！应合规要求，在用户同意隐私协议的前提下，登录成功后 SDK 会通过推送插件获取推送 token，并将推送 token 传递至后台（若获取 token 失败则会导致离线推送无法正常使用）
 const TUIOfflinePush = uni.requireNativePlugin("TencentCloud-TUIOfflinePush");
 tim.registerPlugin({
   'tim-offline-push-plugin': TUIOfflinePush,
   'offlinePushConfig': {
		// huawei
		'huaweiBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
		// xiaomi
		'xiaomiBusinessID': '',// 在腾讯云控制台上传第三方推送证书后分配的证书 ID
		'xiaomiAppID': '',// 小米开放平台分配的应用 APPID
		'xiaomiAppKey': '',// 小米开放平台分配的应用 APPKEY
		// meizu
		'meizuBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
		'meizuAppID': '',// 魅族开放平台分配的应用 APPID
		'meizuAppKey': '',// 魅族开放平台分配的应用 APPKEY
		// vivo
		'vivoBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
		// oppo
		'oppoBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
		'oppoAppKey': '',// oppo 开放平台分配的应用 APPID
		'oppoAppSecret': '',//
		// ios
		'iosBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
  }
 });
```
>!
>- 请将 sdk 升级到 [v2.22.0](https://cloud.tencent.com/document/product/269/38492) 或更高版本, v2.22.0 起支持 uni-app 打包 native app 时使用离线推送插件
>- vivo 推送需要在项目 manifest.json 本地插件处配置vivo appId、appKey，如果不需要，可以填写为0，否则可能会编译错误。
>- 华为推送需要将官网下载的 agconnect-services.json 文件放到 nativeplugins/TencentCloud-TUIOfflinePush/android/assets/ 路径下。
>- 集成插件后，sdk 会在 im login 时自动上报 deviceToken，无需其他代码的配置。

#### 步骤四：获取点击推送的内容
```
// 在 App.vue, 生命钩子 onLaunch 中监听
TUIOfflinePush.setOfflinePushListener((data) => {
  console.log('setOfflinePushListener', data);
});
```
#### 步骤五：使用自定义基座打包 uni 原生插件 （**请使用真机运行自定义基座**）。
   该插件只支持本地集成，原生插件调试一个自定义基座，把需要先将原生插件打到真机运行基座里，然后在本地写代码调用调试。

>?自定义基座不是正式版，真正发布时，需要再打正式包。使用自定义基座是无法正常升级替换 APK 的。

## 常见问题

### 收不到离线推送怎么排查？
#### 1、OPPO 手机收不到推送的可能情况
OPPO 安装应用通知栏显示默认关闭，需要确认下开关状态。

#### 2、设备通知栏设置影响
离线推送的直观表现就是通知栏提示，所以同其他通知一样受设备通知相关设置的影响，以华为为a例：

- “手机设置-通知-锁屏通知-隐藏或者不显示通知”，会影响锁屏状态下离线推送通知显示。
- “手机设置-通知-更多通知设置-状态栏显示通知图标”，会影响状态栏下离线推送通知的图标显示。
- “手机设置-通知-应用的通知管理-允许通知”，打开关闭会直接影响离线推送通知显示。
- “手机设置-通知-应用的通知管理-通知铃声” 和 “手机设置-通知-应用的通知管理-静默通知”，会影响离线推送通知铃音的效果。

#### 3、按照流程接入完成，还是收不到离线推送
- 首先在 IM 控制台通过 [离线测试工具](https://console.cloud.tencent.com/im-detail/tool-push-check) 自测下是否可以正常推送。
推送异常情况，设备状态异常，需要检查下 IM 控制台配置各项参数是否正确，再者需要检查下代码初始化注册逻辑，包括厂商推送服务注册和 IM 设置离线推送配置相关逻辑是否正确设置。
推送异常情况，设备状态正常，需要看下是否需要正确填写 channel ID 或者后台服务是否正常。
- 离线推送依赖厂商能力，一些简单的字符可能会被厂商过滤不能透传推送。
- 如果离线推送消息出现推送不及时或者偶尔收不到情况，需要看下厂商的推送限制。

#### 4、iOS 普通消息为什么收不到离线推送
- 首先，请检查下 App 的运行环境和证书的环境是否一致，如果不一致，收不到离线推送。
- 其次，检查下 App 和证书的环境是否为生产环境。如果是开发环境，向苹果申请 deviceToken 可能会失败，生产环境暂时没有发现这个问题，请切换到生产环境测试。

#### 5、iOS 开发环境下，注册偶现不返回 deviceToken 或提示 APNs 请求 token 失败？
此问题现象是由于 APNs 服务不稳定导致的，可尝试通过以下方式解决：
1. 给手机插入 SIM 卡后使用4G网络测试。
2. 卸载重装、重启 App、关机重启后测试。
3. 打生产环境的包测试。
4. 更换其它 iOS 系统的手机测试。

#### 6、iOS 没有 token的原因
1. 模拟器，是不产生 token 的
2. 真机，需要在手机上开启推送的权限
3. 真机，需要添加 push notification 的 enetitemenet

### 厂商推送限制

1、国内厂商都有消息分类机制，不同类型也会有不同的推送策略。如果想要推送及时可靠，需要按照厂商规则设置自己应用的推送类型为高优先级的系统消息类型或者重要消息类型。反之，离线推送消息会受厂商推送消息分类影响，与预期会有差异。
2、另外，一些厂商对于应用每天的推送数量也是有限制的，可以在厂商控制台查看应用每日限制的推送数量。
如果离线推送消息出现推送不及时或者偶尔收不到情况，需要考虑下这里：
- 华为：将推送消息分为服务与通讯类和资讯营销类，推送效果和策略不同。另外，消息分类还和自分类权益有关：
  - 无自分类权益，推送消息厂商还会进行二次智能分类 。
  - 有申请自分类权益，消息分类会按照自定义的分类进行推送。
具体请参见 [厂商描述](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835)。
- vivo：将推送消息分为系统消息类和运营消息类，推送效果和策略不同。系统消息类型还会进行厂商的智能分类二次修正，若智能分类识别出不是系统消息，会自动修正为运营消息，如果误判可邮件申请反馈。另外，消息推送也受日推总数量限制，日推送量由应用在厂商订阅数统计决定。
具体请参见 [厂商描述1](https://dev.vivo.com.cn/documentCenter/doc/359) 或 [厂商描述2](https://dev.vivo.com.cn/documentCenter/doc/156)。
- OPPO：将推送消息分为私信消息类和公信消息类，推送效果和策略不同。其中私信消息是针对用户有一定关注度，且希望能及时接收的信息，私信通道权益需要邮件申请。公信通道推送数量有限制。
具体请参见 [厂商描述1](https://open.oppomobile.com/wiki/doc#id=11227) 或 [厂商描述2](https://open.oppomobile.com/wiki/doc#id=11210)。
- 小米：将推送消息分为重要消息类和普通消息类，推送效果和策略不同。其中重要消息类型仅允许即时通讯消息、个人关注动态提醒、个人事项提醒、个人订单状态变化、个人财务提醒、个人状态变化、个人资源变化、个人设备提醒这8类消息推送，可以在厂商控制台申请开通。普通消息类型推送数量有限制。
具体请参见 [厂商描述1](https://dev.mi.com/console/doc/detail?pId=2422) 或 [厂商描述2](https://dev.mi.com/console/doc/detail?pId=2086)。
- 魅族：推送消息数量有限制。
具体请参见 [厂商描述](http://open.res.flyme.cn/fileserver/upload/file/202201/85079f02ac0841da859c1da0ef351970.pdf)。
- FCM：推送上行消息频率有限制。
<!--具体请参见 [厂商描述](https://firebase.google.com/docs/cloud-messaging/concept-options?hl=zh-cn#upstream_throttling)。-->


## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。 309869925 (技术交流群)
