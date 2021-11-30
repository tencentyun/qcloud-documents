## 功能介绍
**主播 PK** 是在秀场直播场景中经常使用的一种吸引热度的方式，两个分处不同房间的主播可以相互分屏连麦（视频通话），主播与主播之间的延迟可以达到 500ms 以内，而观众在不需要切换流地址的情况下，就可以在原来的 CDN 直播流中看到主播 PK 的效果。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/9985984163972441ebbe3ad79b265136.jpg" />

## LiveRoom
主播 PK 是 **LiveRoom** 组件的一项基本功能（LiveRoom 还支持观众同主播连麦），它分成 Client 和 Server 两个部分：

- **终端部分（Client）**
LiveRoom 组件的终端部分是对腾讯视频云 LiteAVSDK（主要用于音视频，包括 TXLivePusher、TXLivePlayer 等接口） 和 LiteIMSDK （主要用于收发消息，包括 TIMManager 和 TIMConversation 等接口）的封装。直接使用 LiteAVSDK 和 LiteIMSDK 实现直播 + 主播PK功能是非常耗时耗力的，但通过 LiveRoom 组件，您可以直接调用 createRoom，enterRoom 和 leaveRoom 等接口就可以完成您想要的直播 + 主播PK功能。
 
- **后台部分（Server）**
RoomService 是 LiveRoom 对应的后台组件，其职责有两个：一是房间管理（直播间的增、删、改、查）和成员管理（维护房间里有几个人正在推流，主要是连麦场景下使用，主播PK场景暂未使用）；二是对腾讯云直播服务、实时音视频服务以及 IM 云通讯服务的控制（主要通过腾讯云的后台 REST API 进行调用）。

![](https://mc.qcloudimg.com/static/img/5a153aa265f6b41dbd88126d786c47e7/image.png)


<h2 id="Client"> 终端对接 </h2>

#### step1: 下载 SDK 开发包

| 平台 | 编程语言 | SDK 下载 | API 文档 | 
|:-------:|:-------:| :-------:| :-------:|
| iOS    | Objective-C | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#iOS) | [API 文档](https://cloud.tencent.com/document/product/454/14730) | 
| Android | java  | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Android) |  [API 文档](https://cloud.tencent.com/document/product/454/14642) | 


- LiteAV SDK 位于 ZIP 包解压后的 SDK 文件夹中，用于实现音视频相关功能
- LiteIM SDK 位于 ZIP 包解压后的 SDK 文件夹中，用于实现 IM 通讯相关功能
- LiveRoom  位于 ZIP 包解压后的 Demo \ liveroom 文件夹中，代码开源，方便您进行调试和定制。


<h4 id="CLIENT_LOGIN"> step2: 登录（login） </h4>
LiveRoom 单靠一个终端的组件无法独自运行，它依赖一个后台服务为其实现房间管理和状态协调，这个后台服务我们称之为**房间服务**（RoomService）。而要使用这个房间服务，LiveRoom 就需要先进行**登录**（login）。

阅读 [RoomService](#Server) 可以了解 login 函数的几个参数应该如何填写。

#### step3: 获取房间列表（getRoomList）
不管是主播还是观众，都需要有一个房间列表，调用 LiveRoom 的 **getRoomList** 接口可以获取到该列表。列表中每一个房间都有其对应的 roomInfo，是在 createRoom 时传入的，推荐您将 roomInfo 定义为 json 格式，这样可以有很强的扩展性。

> 如果您希望使用自己的房间列表，这一步可以省略，但是需要您在 step 4 中自行指定 roomID，且全局不能有重复。

#### step4: 主播开播（createRoom）
主播要开播，需要先调用 LiveRoom 的 **startLocalPreview** 接口开启本地摄像头预览，该函数需要传入一个 view 对象，该对象用于显示摄像头的视频影像。这期间 LiveRoom 会申请摄像头使用权限，同时，主播也可以对着摄像头调整一下美颜和美白的具体效果。

之后，通过调用 **createRoom ** 接口，LiveRoom 会在后台的房间列表中新建一个直播间，同时主播端会进入推流模式。

> **参数roomID**
> 如果您在调用 createRoom 时不填写 roomId，后台会为您分配一个 roomID， 并通过 createRoom 的回调接口返回给您。如果您希望自己管理房间列表，roomID 可以由您的服务器分配，那么只需要在调用 createRoom 时填写您后台分配的 roomId 即可。

#### step5: 观看直播（enterRoom）
观众通过 LiveRoom 的 **enterRoom** 接口可以进入直播间观看视频直播，enterRoom 函数需要传入一个 view 对象，用于显示直播流的视频影像。

另外，进入房间后，调用 LiveRoom 的 **getAudienceList** 接口可以获取观众列表，这里的列表不是全量数据，如果少于30 个人就全部返回，如果多于 30 个人，就只返回新进入的 30 个人。（出于性能方面的考虑， 而且 UI 界面上最多能也就能放下 10 个头像。）

#### step6: 主播PK（sendPKRequest）
主播PK是两个房间的主播在直播的同时，互相拉取对方的视频流，建立实时视频通话互动，每个房间的观众都可以看到两个主播互动的过程，流程图如下：

![](https://main.qcloudimg.com/raw/099b6f684e2372dc8b861378eacb25f0.jpg)

##### a. 选择目标主播
调用 getOnlinePusherList 获取当前正在直播的主播列表，回调函数 GetOnlinePusherListCallback 返回在线主播的详细信息，包含昵称、头像、用户ID等；然后显示一个 UI 列表，以便选择一个主播进行PK。

##### b. 启动 PK
- 第一步（主播一）：调用 **sendPKRequest** ，向主播二发起 PK 请求。
- 第二步（主播二）：会收到 **onRecvPKRequest** 回调通知，之后可以展示一个 UI 提示，询问主播二要不要接受 PK。
- 第三步（主播二）：可以调用 **acceptPKRequest** 接受 PK 请求，也可以调用 **rejectPKRequest** 拒绝 PK 请求；如果接受了 PK 请求，请同时调用 startPlayPKStream 播放主播一的视频流。
- 第四步（主播一）：通过 **RequestPKCallback** 可以了解到 PK 请求是否被接受。
- 第五步（主播一）：如果 PK 请求被接受，请调用 **startPlayPKStream** 播放主播二的视频流。

> 函数 startPlayPKStream 除了完成拉流播放的功能；同时会触发后台混流，即把对方主播的视频流叠加到自己的流上。普通观众不需要重新拉流，可以自动观看到两个主播PK的视频画面。

##### c. 结束 PK
主播PK过程中，任何一方都可以主动结束PK，假设主播一主动结束PK

- 第六步（主播一）：调用 **sendPKFinishRequest** ，向主播二发起结束 PK 的请求；同时调用 **stopPlayPKStream** 结束播放主播二的视频流。
- 第七步（主播二）：会收到 **onRecvPKFinishRequest** 回调通知。
- 第八步（主播二）：调用 **stopPlayPKStream** 结束播放主播一的视频流。

> 函数 stopPlayPKStream 除了结束播放视频流，同时会取消后台混流。普通观众不需要重新拉流，可以自动切换到直播模式。

#### step7: 弹幕消息（sendMsg）
LiveRoom 自带了消息发送接口，可以通过 **sendRoomTextMsg** 函数发送普通的文本消息（用来弹幕），也可以通过 **sendRoomCustomMsg** 发送自定义消息（用于点赞，送花等等）。

通过 RoomListenerCallback 里的 **onRecvRoomTextMsg** 和 **onRecvRoomCustomMsg** 可以收取聊天室里别人发来的文本消息和自定义消息。

> ** <font color='red'> ATTENTION </font> **
> 
> 腾讯云 IM 每秒钟最多可以收取 40 条以上的消息，如果您要把所有这些消息都按照接收频率刷新到屏幕 UI 上，那您的直播体验一定是非常卡顿的，这里一定要注意刷新频率控制。
>
>有太多的客户在测试期间顺顺利利，APP一上线就卡的不行，都是这个原因导致的。

<h2 id="Server"> 后台对接 </h2>

**LiveRoom 为什么需要 login？** 

LiveRoom 单靠一个终端的组件无法独自运行，它依赖一个后台服务为其实现房间管理和状态协调，这个后台服务我们称之为**房间服务**（RoomService）。而要使用这个房间服务，LiveRoom 就需要先进行**登录**（login）。

**login 有很多参数需要填写，我应当如何填写这些参数呢？**

如下表格中列举了三种填写方案，每种方案都有其适用场景：方案一只能用于调试；方案二适合快速上线；方案三适合自行定制；

| 参数名 | 方案一（纯测试方案） | 方案二（腾讯云RoomService） | 方案三（自建RoomService） |
| :-------:| :-------:| :-------: | :-------:|
| serverDomain | 使用腾讯云 RoomService<br> `https://room.qcloud.com/weapp`<br>`/live_room` | 使用腾讯云 RoomService<br> `https://room.qcloud.com/weapp`<br>`/live_room` ，需要提前 [配置](#TencentRoom) | [自行部署](#SelfRoom) RoomService<br> `https://[yourcompany]/weapp`<br>`/live_room` |
| sdkAppID | 通过测试地址获取<br> `https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug` | 自行填写，[如何获取？](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) | 自行填写，[如何获取？](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) |
| accType | 通过测试地址获取<br> `https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug` | 自行填写，[如何获取？](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) | 自行填写，[如何获取？](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) | 
| userID | 通过测试地址获取<br> `https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug` | 您来指定，比如 9527 | 您来指定，比如 9527 | 
| userSig | 通过测试地址获取<br>`https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug`  | 您的服务器生成，[如何生成？](https://cloud.tencent.com/document/product/454/14548) | 您的服务器生成，[如何生成？](https://cloud.tencent.com/document/product/454/14548)| 
| **账号归属** | 账号为腾讯云测试账号 | 账号为您名下的账号 | 账号为您名下的账号 | 
| **账号限制** | 每天 10：00 - 22：00 可用 | 无限制，但不支持定制 | 无限制，且您可以进行定制| 
| **适用场景** | 前期终端研发调试使用 | 产品上线初期阶段 | 产品进入上升期 |

<h3 id="DebugRoom"> 方案一：纯调试方案 </h3>

该方案使用腾讯云为方便客户调试而统一提供的测试账号，仅适合调试期间使用，每天 10：00 - 22：00 这个时间段可用。

#### step1. 配置RoomService
serverDomain 填写  `https://room.qcloud.com/weapp/live_room` 即可。

#### step2. 获得 login 所需参数
通过测试地址（ `https://room.qcloud.com/weapp/utils/get_login_info_debug`）获取相关参数


<h3 id="TencentRoom"> 方案二：使用腾讯云RoomService </h3>

该方案使用您自己的腾讯云账号 + 腾讯云自行部署的 RoomService 服务，所以在使用前，您需要先对 RoomService 进行配置。

 ![](https://mc.qcloudimg.com/static/img/32d0a7583f62eb51a2dc0290f8c23afd/image.png)

#### step1. 配置RoomService
腾讯云 RoomService 地址为

``` 
https://room.qcloud.com/weapp/live_room 
```

点击 [RoomTool.zip](http://dldir1.qq.com/hudongzhibo/mlvb/RoomTool.zip) 下载腾讯云 RoomService 后台配置工具，这是一个基于 Node.js 的配置工具，需要您在使用前 [安装](http://nodejs.cn/download/) Node.js 。配置工具压缩包中包含的 pdf 和 PPT 有详细的配置说明，这里仅简要概括一下各个配置项的含义和作用。

| 配置项 | 作用 | 获取方案 |
|---------|---------|---------|
| 直播（live）appID | 腾讯云直播服务基于 appID 区分客户身份 | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_APPID) |
| 直播（live）APIKey | 腾讯云直播服务的后台 REST API，采用 APIKey 进行安全保护 | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_API_SECRECT) |
| 云通讯（IM）sdkAppID | 腾讯云通讯服务用 sdkAppID 区分 IM 客户身份 | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) |
| 云通讯（IM）accountType | 曾用于区分 APP 类型，现仅出于兼容性原因而保留 | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) |
| 云通讯（IM）administrator | RoomService 使用了 IM REST API 发送房间里的系统消息，而 IM REST API 接口需要您填写管理员名称。 |  [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ADMIN)  |
| 云通讯（IM）privateKey | RoomService 使用 privateKey 用于签发管理员（administrator）的 usersig，进而能够调用 IM REST API 发送房间里的系统消息。  |  [DOC](https://cloud.tencent.com/document/product/454/7953#IM_PRIKEY)  |
| 云通讯（IM）publicKey | RoomService 使用 publicKey 用于确认终端用户的登录身份。 | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_PRIKEY) |

#### step2. 获得 login 所需参数
RoomService 需要终端调用 `login(serverDomain, sdkAppID, accType, userID, userSig)`  登录成功后才能使用，其中前四个信息都可以在客户端写死，但是 UserSig 必须由您的后台服务器签发，因为让 Client 计算 UserSig 就需要将签名私钥写在终端的代码里，这会有私钥被 hack 窃取的安全风险。

RoomService 所使用的 UserSig 的签发同 IM 云通讯服务是一样的，所以同一个 UserSig 既可以用来登录 IM，又可以用来登录 RoomService，您可以参考文档 [派发UserSig](https://cloud.tencent.com/document/product/454/14548) 进行接入。

<h3 id="SelfRoom"> 方案三：自建RoomService后台 </h3>

该方案使用您自己的腾讯云账号 + 您自己部署的房间服务，所以您可以对内部的逻辑进行修改和定制。

#### step1. 下载源码 & 修改配置 & 部署
在 [CODE](https://cloud.tencent.com/document/product/454/7873#Server) 下载 RoomService 后台源码，源码包分成三个目录，其中 live_room 下的源码是您需要关注的。

下载到源码后，解压并找到 live_room 文件夹下面的 config.js 文件，这里有几个个配置项需要修改。配置项跟方案一中的基本类似，可以参考方案一中的 step1 进行配置。区别在于，在方案二中您不需要用 RoomService 配置工具，而是直接修改本地源码即可。

![](https://main.qcloudimg.com/raw/74512dcd5d06edac59b4d051da94e75f.png)

| 配置项 | 作用 | 获取方案 |
|---------|---------|:-------:|
| 直播（live）pushSecretKey | 用于计算推流 URL 的防盗链签名，必须要配置 | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_PUSH_SECRECT) |
| 直播（live）APIKey | 腾讯云直播服务的后台 REST API，采用 APIKey 进行安全保护 | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_API_SECRECT) |

之后，您可以将其部署到您自己的后台服务器上，并将服务器的外网 URL 告知您的终端研发工程师，因为他/她在调用终端的 [login](#CLIENT_LOGIN) 函数时需要指定 RoomService 的后台地址，例如：

``` 
https://[www.yourcompany.com]/weapp/live_room 
```

#### step2. 获得 login 所需参数
第一步完成之后，相当于您已经拥有了一个自己的 RoomService，但这个自己的 RoomService 还是基于 `sdkAppID, accType, userID, userSig`  这四个信息进行身份鉴权的（您也可以替换成您期望的身份鉴权方案），所以您同样需要参考文档 [生成UserSig](https://cloud.tencent.com/document/product/454/14548) 并给 Client 派发登录签名。

> RoomService 后台源码中，`logic\im_mgr.js` 内部的 getSig 函数是 node.js 版本的 UserSig 生成示例代码， java 和 php 版本的我们稍后放出。



## 实现原理
### 1. 两种“通道”

腾讯云采用了两套通道实现直播+主播PK功能，其中直播采用标准的 （RTMP + FLV ）协议，走标准CDN线路，没有并发观看人数的限制，且带宽成本很低，但延迟一般在2s以上。主播PK采用私有的 UDP 协议，走特殊专线线路，延迟一般在500ms左右，但最多支持10人同时视频通话，且单路费用高于普通直播。

![](https://main.qcloudimg.com/raw/ca3441a2671fda6b336edf9921b4cd8a.png)


|  通道            |  直播通道   |     主播PK通道      |
| :--------------:  | :-----: | :-----------: | 
| 通讯延迟       |  >=2s |  500ms左右 |
| 底层协议       |  RTMP/HTTP-FLV |  私有UDP协议 |
| 价格/费用      |  [按带宽计费](https://cloud.tencent.com/document/product/454/8008#LVB) |  [按时长计费](https://cloud.tencent.com/document/product/454/8008#ACC) |
| 最高并发      |  无上限 |  <=10人 |
| TXLivePusher      |  setVideoQuality 为 SD、HD、FHD |  setVideoQuality 为 MAIN_PUBLISHER |
| TXLivePlayer      |  PLAY_TYPE_LIVE_FLV |  PLAY_TYPE_LIVE_RTMP_ACC |
| 播放URL      |  普通 FLV 地址 |  带防盗链签名的 RTMP 地址 |

 
### 2. 内部原理
您完全不需要了解 LiveRoom 的内部原理便可轻松接入，但是如果您确实感兴趣，可以通过下图了解其内部运作机制。
<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/ffd2a4d21728c43b516fb9d3311f90e3.gif" />
