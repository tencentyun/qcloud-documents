## 直播场景下的 IM 需求

直播显然成为互联网当下最热的领域之一。对于任意一个直播系统，无外乎都是由音视频系统与 IM 系统组成的。IM 在直播系统中的主要作用是实现观众与主播、观众与观众之间的文字互动，互动内容包括普通文本消息、表情消息、点赞消息、进退房间消息和红包打赏消息等。

云通信针对直播领域的多人聊天需求提供了一套完整的解决方案：AVChatRoom（也称为互动直播聊天室）。

**AVChatRoom 基本能力包括**：

* 基本的消息分发能力
* 聊天室人数无上限
* 支持 Native App 和 H5
* 支持匿名（即无需注册帐号并登录）接收消息
>**注意：**
AVChatRoom成员人数没有上限，但如果预估群成员人数会超过1万人，需提前联系腾讯云客服或商务工作人员，申请服务资源。 

除了最基本的消息分发能力，直播场景对 IM 还存在很多特殊需求，例如：如何下发用户加退群通知，并且确保在人数很多的情况下控制加退群通知的下发频率？如何在消息中携带发消息用户的身份信息，包括昵称、头像、身份、头衔等？如何对 IM 消息进行控制？云通信充分考虑了直播场景的这些特殊需求，并都给出了完整的解决方案。

云通信提供了 Native App 和 H5 两种模式下的 Demo 及其源码。基于云通信完善的能力以及丰富的参考样本，您可以花费最少的人力来完成直播系统中 IM 功能的集成并快速上线。

## 直播系统与 IM 系统的一般集成架构

![](//mccdn.qcloud.com/static/img/9de5ecdca24d44477b0e925156cc3588/image.png)

## 云通信直播场景 Demo

### Demo 应用商店体验

**Native App：**

云通信直播聊天室的相关 Demo 在应用商店上架名为“随心播”，该 App 是基于云通信以及腾讯云另一款产品“[互动直播](https://cloud.tencent.com/product/ilvb.html)”开发而成。单击下载 [ Android 版 Demo（应用宝）](http://sj.qq.com/myapp/detail.htm?apkName=com.tencent.qcloud.suixinbo)，或者扫描以下二维码。

![](//mccdn.qcloud.com/static/img/55b65132442aa62465730bc0b20a1c7b/image.png)

单击下载[ iOS 版 Demo（App Store）](https://itunes.apple.com/cn/app/sui-xin-bo/id1037944078?mt=8)，或者扫描以下二维码。

![](//mccdn.qcloud.com/static/img/25abd38be30a88cdaf6eedb975be02e7/image.png)

**H5 Demo：**

为了确保 H5 Demo 的简洁，我们仅在 Demo 中集成了 IM 相关功能，并未包含视频功能。单击体验 [ H5 Demo](http://avc.qcloud.com/demo/webim/biggroup/mobile/index.html)，或者扫描以下二维码。

![](//mccdn.qcloud.com/static/img/a188f7fd653c8237b362a7adea1f63b1/image.png)

### Demo 源码下载与代码导读

- 下载 Android SDK
	- [查看 GitHub Android 源码与导读 >>](https://github.com/zhaoyang21cn/Android_Suixinbo)
	-	[单击下载 Android SDK >>](https://mc.qcloudimg.com/static/archive/e8389820ad5dc3b40cf3dc689d3f5432/Android_Suixinbo-master.zip)
- 下载 iOS SDK
	- [查看 GitHub iOS 源码下载与导读 >>](https://github.com/zhaoyang21cn/iOS_Suixinbo)
	- [单击下载 iOS SDK >>](https://mc.qcloudimg.com/static/archive/8015331b15c58c29ce01d303fff00ee7/iOS_Suixinbo-master.zip)
- [H5 源码下载与导读 >>](/doc/product/269/H5直播聊天室DEMO指引)

## 直播聊天室接入指引


直播场景的聊天室主要包括如下几大类核心操作：

* 创建聊天室（包括主播创建聊天室和 App 后台通过 REST API 创建聊天室）
* 观众申请加入聊天室（包括匿名加入聊天室）
* 观众在聊天室中发言
* App 接收聊天消息

### 集成准备工作

本小节我们将引导您如何从零开始在直播 App 中集成聊天服务。在真正开始集成 IMSDK 之前，您必须完成一些接入准备工作，包括：应用接入和用户体系集成。在完成这两步之后，您需要将 SDK 集成到您的 App 中，然后才能开始调用直播聊天室相关的 SDK 接口。

**应用接入**

详细请参阅 [应用接入指引](/doc/product/269/应用接入指引)。

**用户体系集成**

云通信提供 [独立模式](/doc/product/269/独立模式) 和 [托管模式](/doc/product/269/托管模式) 两种用户体系集成。

- 如果您的 App 自主维护用户的注册、用户身份的验证，则应当使用[独立模式](/doc/product/269/独立模式)。
- 如果您只是想快速开发一个 App 原型，云通信可以为您提供一套符合业界通用安全标准的用户体系，用户的注册、用户身份的验证将全部由云通信提供，此时应当选用 [托管模式](/doc/product/269/托管模式)。

**客户端集成**

客户端集成是将 IMSDK 集成到您的 App 中，详细请参阅以下接口中的描述：

* [Android 客户端集成](/doc/product/269/概述（Android%20SDK）)
* [iOS 客户端集成](/doc/product/269/概述（iOS%20SDK）)
* [Windows C++ 客户端集成](/doc/product/269/概述（Windows%20SDK）)

### 创建直播聊天室

接下来您便可以通过 SDK 提供的接口来实现直播聊天室。通过 IMSDK 创建直播聊天室(AVChatRoom)，详细请参阅以下接口中的描述：

* [Android 创建群组](/doc/product/269/群组管理（Android%20SDK）#.E5.88.9B.E5.BB.BA.E5.86.85.E7.BD.AE.E7.B1.BB.E5.9E.8B.E7.BE.A4.E7.BB.84)
* [iOS 创建群组](/doc/product/269/群组管理（iOS%20SDK）#.E5.88.9B.E5.BB.BA.E5.86.85.E7.BD.AE.E7.B1.BB.E5.9E.8B.E7.BE.A4.E7.BB.84)
* [Windows C++ 创建群组](/doc/product/269/群组管理（Windows%20SDK）#.E5.88.9B.E5.BB.BA.E5.86.85.E7.BD.AE.E7.B1.BB.E5.9E.8B.E7.BE.A4.E7.BB.84)

通过 REST API 创建直播聊天室，详细请参阅 [REST API：创建群组](/doc/product/269/创建群组)。

### 申请加入聊天室

通过 IMSDK 申请加入聊天室，详细请参阅以下接口中的描述：

* [Android 申请加群](/doc/product/269/群组管理（Android%20SDK）#.E7.94.B3.E8.AF.B7.E5.8A.A0.E5.85.A5.E7.BE.A4.E7.BB.84)
* [iOS 申请加群](/doc/product/269/群组管理（iOS%20SDK）#.E7.94.B3.E8.AF.B7.E5.8A.A0.E5.85.A5.E7.BE.A4.E7.BB.84)
* [Windows C++ 申请加群](/doc/product/269/群组管理（Windows%20SDK）#.E7.94.B3.E8.AF.B7.E5.8A.A0.E5.85.A5.E7.BE.A4.E7.BB.84)

>**注意：**
>用户加入 AVChatRoom 后，如果发生异常登出 `logout` 或者 App 进程崩溃 `crash` 的情况，在重新上线 `login` 或者重启 App 进程后，需要再次调用申请加群才能继续在原来的 AVChatRoom 中收发消息。

### 收发消息

通过 IMSDK 收发消息，详细请参阅以下接口中的描述：

* [Android 消息收发](/doc/product/269/消息收发（Android%20SDK）)
* [iOS 消息收发](/doc/product/269/消息收发（iOS%20SDK）)
* [Windows C++ 消息收发](/doc/product/269/消息收发（Windows%20SDK）)

通过 REST API 发送消息，详细请参阅 [REST API：在群组中发送普通消息](/doc/product/269/在群组中发送普通消息)。

## 直播场景一些 IM 相关特殊需求的实现方法

### 聊天室成员进出通知
当聊天室中有用户进入或者离开时，云通信后台会下发成员进出通知。

新用户入群通知，详细请参阅以下接口中的描述：

* [Android 用户入群通知](/doc/product/269/群组管理（Android%20SDK）#.E7.94.A8.E6.88.B7.E5.8A.A0.E5.85.A5.E7.BE.A4.E7.BB.84.E9.80.9A.E7.9F.A5)
* [iOS 用户入群通知](/doc/product/269/群组管理（iOS%20SDK）#.E7.94.A8.E6.88.B7.E5.8A.A0.E5.85.A5.E7.BE.A4.E7.BB.84)
* [Windows C++ 用户入群通知](/doc/product/269/群组管理（Windows%20SDK）#.E7.94.A8.E6.88.B7.E5.8A.A0.E5.85.A5.E7.BE.A4.E7.BB.84)

用户退群通知，详细请参阅以下接口中的描述：

* [Android 用户退群通知](/doc/product/269/群组管理（Android%20SDK）#.E7.94.A8.E6.88.B7.E9.80.80.E5.87.BA.E7.BE.A4.E7.BB.84)
* [iOS 用户退群通知](/doc/product/269/群组管理（iOS%20SDK）#.E7.94.A8.E6.88.B7.E9.80.80.E5.87.BA.E7.BE.A4.E7.BB.84)
* [Windows C++ 用户退群通知](/doc/product/269/群组管理（Windows%20SDK）#.E7.94.A8.E6.88.B7.E9.80.80.E5.87.BA.E7.BE.A4.E7.BB.84)

云通信后台会对用户进出聊天室的消息进行频率控制，详细请参阅 [消息优先级与频率控制](https://cloud.tencent.com/doc/product/269/%E7%BE%A4%E7%BB%84%E6%B6%88%E6%81%AF%E7%BB%BC%E8%BF%B0#7.5-.E6.B6.88.E6.81.AF.E4.BC.98.E5.85.88.E7.BA.A7.E4.B8.8E.E9.A2.91.E7.8E.87.E6.8E.A7.E5.88.B6)。

### 获取观看直播的用户列表
直播 App 有时需要展示当前用户列表。单个 AVChatRoom 本身支持的用户数量无上限，但是只能够获取到部分群成员列表，最多为 300 个成员。

通过 IMSDK 获取群成员列表，详细请参阅以下接口中的描述：

* [Android 获取群成员列表](/doc/product/269/群组管理（Android%20SDK）#.E8.8E.B7.E5.8F.96.E7.BE.A4.E6.88.90.E5.91.98.E5.88.97.E8.A1.A8)
* [iOS 获取群成员列表](/doc/product/269/群组管理（iOS%20SDK）#.E8.8E.B7.E5.8F.96.E7.BE.A4.E6.88.90.E5.91.98.E5.88.97.E8.A1.A8)
* [Windows C++ 获取群成员列表](/doc/product/269/群组管理（Windows%20SDK）#.E8.8E.B7.E5.8F.96.E7.BE.A4.E6.88.90.E5.91.98.E5.88.97.E8.A1.A8)

### 获取观看直播的人数
AVChatRoom 的人数统计并不是实时的，有 1 分钟左右的时延。App 管理后台通过 REST API 接口获取当前群人数，详细请参阅 [获取群组资料](https://cloud.tencent.com/doc/product/269/1616)（回包中的 `MemberNum` 字段）。

IMSDK 获取当前群人数，详细请参阅以下接口中的描述：：

* [Android 获取群组资料](/doc/product/269/群组管理（Android%20SDK）#4.-.E8.8E.B7.E5.8F.96.E7.BE.A4.E7.BB.84.E8.B5.84.E6.96.99)
* [iOS 获取群组资料](/doc/product/269/群组管理（iOS%20SDK）#4.-.E8.8E.B7.E5.8F.96.E7.BE.A4.E8.B5.84.E6.96.99)
* [Windows C++ 获取群组资料](/doc/product/269/群组管理（Windows%20SDK）#4.-.E8.8E.B7.E5.8F.96.E7.BE.A4.E8.B5.84.E6.96.99)

>**注意：**
>- AVChatRoom 针对大规模直播场景，在人数统计上是以“有收发消息的动作”来衡量，统计结果存在时延且不完全准确。在人数较少的场景（比如只有几十人）下，统计的偏差会比较明显。
>- 通过 H5 匿名接收 IM 消息的用户也会被计入聊天室人数中。但由于这些用户没有登录，不可能在用户列表中得到展示。

### 在聊天室中下发自定义消息

云通信的消息原生支持文本、图片、语音、表情等。如果 App 存在一些特殊的消息需求（例如点赞消息、红包消息等），可以通过云通信的自定义消息实现。

通过 IMSDK 发送自定义消息，详细请参阅以下接口中的描述：

- [Android 发送自定义消息](/doc/product/269/消息收发（Android%20SDK）#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81)
- [iOS 发送自定义消息](/doc/product/269/消息收发（iOS%20SDK）#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81)
- [Windows C++ 发送自定义消息](/doc/product/269/消息收发（Windows%20SDK）#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81)

通过 REST API 发送自定义消息，详细请参阅 [REST API：在群组中发送普通消息](/doc/product/269/在群组中发送普通消息#.E8.AF.B7.E6.B1.82.E5.8C.85.E7.A4.BA.E4.BE.8B)。

>**注意：**
>- 如果需要使用云通信的脏字过滤功能，请注意自定义消息的结构设计，详细请参阅 [敏感词（脏字）过滤](/doc/product/269/4104#.E6.95.8F.E6.84.9F.E8.AF.8D.EF.BC.88.E8.84.8F.E5.AD.97.EF.BC.89.E8.BF.87.E6.BB.A4)。
>- 为方便调试，建议 App 使用 JSON 来组织自定义字段。不建议使用二进制数据。

### 消息优先级与频率控制
当 AVChatRoom 中的人数较多时，发消息的用户可能会非常多，导致一秒之内产生的消息量非常大。消息频率过高，会对云通信服务后台和App 的渲染造成压力，也会加大客户端流量。此外，如果 App 界面的消息滚动速率过快，可能导致用户无法看清消息。

基于上述考虑，云通信会对单个 AVChatRoom 中的消息进行频率控制。详细请参阅 [消息优先级与频率控制](/doc/product/269/群组消息综述#.E6.B6.88.E6.81.AF.E4.BC.98.E5.85.88.E7.BA.A7.E4.B8.8E.E9.A2.91.E7.8E.87.E6.8E.A7.E5.88.B6)。

### 聊天室禁言与全局禁言
某些用户可能会在聊天室中发送广告或者其它不良信息，此时可以考虑将该用户禁言。禁言分为两个维度：

- **群组维度的禁言：**用户在指定群内无法发言，即使退群再加群也不例外。群主和管理员具备此权限。
- **全局维度的禁言：**用户在所有群组中都不能发言，同时也不能发送单聊消息。仅 App 管理员具备该权限。

通过 IMSDK 实现群内禁言，详细请参阅以下接口中的描述：

* [Android 对群成员进行禁言](/doc/product/269/群组管理（Android%20SDK）#.E5.AF.B9.E7.BE.A4.E6.88.90.E5.91.98.E8.BF.9B.E8.A1.8C.E7.A6.81.E8.A8.80)
* [iOS 对群成员进行禁言](/doc/product/269/群组管理（iOS%20SDK）#.E5.AF.B9.E7.BE.A4.E6.88.90.E5.91.98.E8.BF.9B.E8.A1.8C.E7.A6.81.E8.A8.80)
* [Windows C++ 对群成员进行禁言](/doc/product/269/群组管理（Windows%20SDK）#.E4.BF.AE.E6.94.B9.E7.BE.A4.E5.91.98.E4.BF.A1.E6.81.AF)

通过 REST API 实现群内禁言，详细请参阅 [REST API：批量禁言和取消禁言](/doc/product/269/批量禁言和取消禁言)。

通过 REST API 获取群内被禁言用户的列表，详细请参阅 [REST API：获取群组被禁言用户列表](/doc/product/269/获取群组被禁言用户列表)。

通过 REST API 设置全局禁言，详细请参阅 [设置全局禁言](/doc/product/269/4230)。

通过 REST API 查询全局禁言，详细请参阅 [查询全局禁言](/doc/product/269/4229)。

### 敏感词（脏字）过滤
所谓脏字过滤，是指 App 可以在云通信后台配置一批敏感词，如果云通信后台在用户发送的消息中检测到这些敏感词，则拒绝下发该消息，并向发送者返回错误码 `80001`。

脏字的增删查改，详细请参阅以下接口中的描述：

- [REST API：查询APP自定义脏字](/doc/product/269/查询APP自定义脏字)
- [REST API：添加APP自定义脏字](/doc/product/269/添加APP自定义脏字)
- [REST API：删除APP自定义脏字](/doc/product/269/删除APP自定义脏字)

>**注意：**
>- 云通信已经默认配置了政治类、色情类的脏字，能够满足这两方面的大多数过滤需求，App 只需要配置业务场景相关的脏字即可。例如，电商类 App 只需要配置『假货』、『刷单』等业务类脏字即可。
>- 默认情况下，云通信后台只会对消息格式中的文本消息进行脏字过滤（TIMTextElem，详细请参阅 [消息格式描述](/doc/product/269/消息格式描述)），如果 App 使用自定义消息格式（TIMCustomElem，详细请参阅 [消息格式描述](/doc/product/269/消息格式描述)），云通信后台无法进行过滤。因此，App 最好在设计之初就确保将需要进行脏字过滤的文本放到 TIMTextElem 中。对于 App 已经使用了自定义消息格式，且已经上线，可以联系云通信客服，将消息格式提供给云通信的技术人员。云通信后台可以据此解析 App 的自定义消息中的文本信息，并进行脏字过滤。

### 其他消息控制策略
除了禁言与脏字过滤之外，云通信还提供了其他消息控制策略，例如群内发言之前回调。另外，如果您的控制策略较为特殊，可以联系云通信客服提出需求，云通信可以为您定制开发消息控制策略。详细请参阅以下接口中的描述：

- [第三方回调简介](/doc/product/269/第三方回调简介)
- [第三方回调接入指引](/doc/product/269/第三方回调接入指引)
- [群内发言之前回调](/doc/product/269/群内发言之前回调)

### 在消息中携带用户身份信息
群消息在下发给客户端时，除了会携带消息内容本身，还会携带消息发送者的信息，默认会携带如下字段：发送者的昵称、发送者的头像、发送者在群内的群名片。如果您的 App 在云通信中配置了 [用户维度的自定义字段](/doc/product/269/用户资料和好友关系综述#.E7.94.A8.E6.88.B7.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99)、[群维度的自定义字段](/doc/product/269/群组系统#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)（AVChatRoom 不支持群成员维度的自定义字段），亦可在消息中携带这些信息。默认下不会携带自定义字段，如有需要请根据 [工单模板](/doc/product/269/云通信配置变更需求工单#.E7.BE.A4.E4.B8.8B.E8.A1.8C.E6.B6.88.E6.81.AF.E5.B8.A6.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)提交工单进行处理。

>**注意：**
>如果要在消息中携带发送者昵称、头像，必须将这两个信息导入云通信的用户资料。

通过 App 设置设置用户资料，详细请参阅以下接口中的描述：

- [Android 用户资料](/doc/product/269/用户资料与关系链（Android%20SDK）)
- [iOS 用户资料](/doc/product/269/用户资料与关系链（iOS%20SDK）)
- [Windows C++ 用户资料](/doc/product/269/用户资料与关系链（Windows%20SDK）)
- [Web 用户资料](/doc/product/269/用户资料（Web%20SDK）)

通过 REST API 查询/设置用户资料，详细请参阅 [REST API：拉取用户资料](/doc/product/269/拉取资料) 和 [REST API：设置用户资料](/doc/product/269/设置资料)。

除此之外，使用独立模式的 App 还可以在通过 REST API 导入帐号的同时设置用户资料，详细请参阅 [REST API：独立模式帐号同步](/doc/product/269/独立模式帐号同步接口)。

### 客户端压力测试
如果要对客户端在 AVChatRoom 下的消息收发性能进行测试，详细请参阅 [压测工具](/doc/product/269/4287#.E7.BE.A4.E5.86.85.E5.8F.91.E9.80.81.E6.B6.88.E6.81.AF.E5.8E.8B.E5.8A.9B.E6.B5.8B.E8.AF.95.E8.84.9A.E6.9C.AC.E4.BD.BF.E7.94.A8.E8.AF.B4.E6.98.8E)。

## 从 ChatRoom 迁移到 AVChatRoom
AVChatRoom 和 ChatRoom 主要有以下区别：

* 面向的应用场景不同——ChatRoom 适用于群组规模中等（数百人及以下级别）、成员进出不太频繁（每秒进出成员在个位数）的场景；AVChatRoom 是专门为了大型直播设计的，适用于人数众多（千级以上）、成员进出频繁（每秒数十人以上进出）的场景。
* AVChatRoom 的优点——单个群支持人数无上限、支持 [H5](/doc/product/269/4105)、支持匿名收群消息、消息可靠性更高、客户端收消息开销更小。
* AVChatRoom 的缺点——为了更好支持大型直播，AVChatRoom 在一些次要功能点上做了让步，包括只能拉取到部分成员列表（最多 300 人）、不能移除成员（可以通过禁言来实现近似目的）、不能邀请用户入群（创建时也不能邀请，只能由用户主动申请入群）、不能修改群成员资料、不能设置管理员、不能获取完整成员列表、不能拉取历史消息。

>**版本要求**
>- IMSDK 1.9 或以上版本（下面称为新版本，1.9 之前的称为老版本）可以支持 AVChatRoom。
>- 对于老版本，后台实现了有限制的兼容逻辑，最多允许 1000 个老版本用户加入一个 AVChatRoom 群组，超出部分的老版本申请加群请求会返回 `10014`（群已满员）错误码，新版本客户端加群不受人数限制。
>- Web SDK 需使用 [直播聊天室](https://cloud.tencent.com/doc/product/269/4105) 专用接口，[通用](https://cloud.tencent.com/doc/product/269/4196) 接口无法支持 AVChatRoom。

因此，我们建议将 ChatRoom 用于直播场景的用户迁移到 AVChatRoom。IMSDK 与后台已经做了充分的兼容逻辑，开发者唯一需要做的事情是：在创建群组时，指定群组形态为 AVChatRoom。除此之外，其他逻辑一概不需要改变。即使对于已经发布的老版本客户端，依然可以加入到 AVChatRoom 并接收消息。

## 其他相关的通信能力

### 全员消息推送

云通信针对不同的应用场景，提供了 **App 消息推送服务** 和 **在线成员广播大群** 两种解决方案：

* 直播场景下，高价值礼物送出时，App 后台有可能会需要向**全体在线用户**下发消息，俗称『大喇叭消息』。云通信为此场景专门提供了 [在线成员广播大群](/document/product/269/7949)，该方案也支持非登录在线用户接收广播消息。

* 需要向 **全体成员** （包含不在线用户）推送 APP 通知时，则需要选用 [消息推送服务](/document/product/269/4119)，除此之外，该方案还支持向全部用户中满足特定条件的用户推送消息，即按用户的标签、属性进行推送。

### 面向单个/一批用户的系统通知

如果 App 后台需要向单个/一批用户发送系统通知，可以参考 [REST API 发送消息](/doc/product/269/单发单聊消息) 和 [REST API 批量发单聊消息](/doc/product/269/批量发单聊消息)。

### App 接收消息

IMSDK 接收消息都是通过统一回调接口 `onNewMessage` 返回，通过 `onNewMessage` 回调获得消息后，能根据消息获取相应的会话。详细请参阅以下接口中的描述：

- [Android 新消息通知](/doc/product/269/初始化（Android%20SDK）#.E6.96.B0.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5)
- [iOS 新消息通知](/doc/product/269/初始化（iOS%20SDK）#2.-.E6.96.B0.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5)
- [Windows 新消息通知](/doc/product/269/初始化（Windows%20%20SDK）#4.-.E6.96.B0.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5)
- [WebSDK 初始化新消息回调](/doc/product/269/初始化（Web%20SDK）)
