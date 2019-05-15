## 功能介绍

TXLivePusher 和 TXLivePlayer 这两个基础组件可以比较容易的实现推流和拉流功能，但如果想要实现复杂的直播连麦功能，就需要借助我们提供给您的 MLVBLiveRoom 组件，该组件基于腾讯云直播（LVB）和 云通讯（IM）两个 PAAS 服务组合而成，支持：

- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 每一个直播间都有一个不限制房间人数的聊天室，支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。

![](https://main.qcloudimg.com/raw/3e140620deb9058a2e8aba03ab26f280.gif)

## 功能体验

我们提供了 iOS、Android 以及微信小程序三个平台上的直播连麦体验，它们均是使用 MLVBLiveRoom 组件实现的直播加连麦功能：

- **iOS**
  进入 [AppStore](https://itunes.apple.com/cn/app/id1132521667?mt=8) 安装应用“小直播”，注册一个账号即可开始体验。
- **Android**
  下载 [apk](http://dldir1.qq.com/hudongzhibo/xiaozhibo/xiaozhibo.apk) 安装包，安装“小直播”，注册一个账号即可开始体验。
- **微信小程序**
  打开“微信 => 发现 => 小程序”，搜索“腾讯视频云”，点击“手机直播”功能即可体验。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/aacdf8cdfa825f64f34af9c3c3e4154e.jpg" />

## 代码对接

### step1: 下载 LiteAVSDK 和 MLVBLiveRoom 组件

移动直播提供的连麦能力需要依赖三个组件： 

- LiteAVSDK：闭源，负责直播推流，直播拉流，以及连麦视频通话功能。
- TIMSDK：闭源，负责构建直播聊天室，以及聊天室中用户之间的消息传输功能。
- MLVBLiveRoom：开源，基于 LiteAVSDK 和 TIMSDK 搭建一个支持连麦互动和消息互动的“直播间”。

我们已经将上述组件均托管在了 [Github](https://github.com/tencentyun/LiteAVSDK/) 上，clone 下来便可使用，如下是几个关键组件的具体位置：

| 所属平台 |                          LiteAVSDK                           |                            TIMSDK                            |                      MLVBLiveRoom 组件                       |                           示例代码                           |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|   iOS    | [LiteAVSDK](https://github.com/tencentyun/LiteAVSDK/tree/master/iOS/SDK) | [TIMSDK]([LiteAVSDK](https://github.com/tencentyun/LiteAVSDK/tree/master/iOS/SDK)) | [MLVBLiveRoom](https://github.com/tencentyun/LiteAVSDK/tree/master/iOS/Demo/TXLiteAVDemo/LVB/LiveRoom/LiveRoom) | [SimpleCode](https://github.com/tencentyun/LiteAVSDK/tree/master/iOS/Demo/TXLiteAVDemo/LVB/LiveRoom/LiveRoomUI) |
| Android  | [LiteAVSDK](https://github.com/tencentyun/LiteAVSDK/tree/master/Android/SDK) | [TIMSDK]([LiteAVSDK](https://github.com/tencentyun/LiteAVSDK/tree/master/Android/SDK)) | [MLVBLiveRoom](https://github.com/tencentyun/LiteAVSDK/tree/master/Android/Demo/app/src/main/java/com/tencent/liteav/demo/lvb/liveroom) | [SimpleCode](https://github.com/tencentyun/LiteAVSDK/tree/master/Android/Demo/app/src/main/java/com/tencent/liteav/demo/lvb/liveroom/ui) |

### step2: 申请 license 

下载到 LiteAVSDK 后并不能直接使用，因为 SDK 需要 license 授权，阅读 [License 申请](https://cloud.tencent.com/document/product/454/34750) 了解 License 的申请方法和使用方法：

iOS 建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加：

```
[TXLiveBase setLicenceURL:LicenceUrl key:Key];
```

Android 建议在 application 中添加：

```
TXLiveBase.getInstance().setLicence(context, LicenceUrl, Key);
```

### step3: 在应用管理中添加一个新的应用

之后，进入【直播控制台】=>【直播SDK】=>【[应用管理](https://console.cloud.tencent.com/live/license/appmanage)】，点击【创建应用】开始创建一个新的应用。
![](https://main.qcloudimg.com/raw/ccc83c93aa7d85aa1f84ca620ee8f5cb/AppMgr.png)

应用创建完成后要记录好 sdkAppID，这个 ID 会在 step4 中使用到。

> ? 这一步的目的是创建一个 TIM 云通信应用，并将当前直播账号和云通信应用绑定起来，云通信应用能够为小直播 App 提供聊天室和连麦互动的能力。

### step4: 登录到房间服务

MLVBLiveRoom 单靠一个终端的组件无法独自运行，它依赖一个后台服务为其实现房间管理和状态协调，这个后台服务我们称之为**房间服务**（RoomService）。而要使用这个房间服务，MLVBLiveRoom 就需要先进行**登录**（login）。

MLVBLiveRoom 的 login 函数需要指定一些参数，这些参数的填写方式如下：

| 参数       | 类型   | 填写方案                                                     |
| ---------- | ------ | ------------------------------------------------------------ |
| sdkAppID   | 数字   | 当前应用的 AppID，在 step3 中可以获取到                      |
| userID     | 字符串 | 当前用户在您的账号系统中的 ID                                |
| userName   | 字符串 | 用户名（昵称）                                               |
| userAvatar | 字符串 | 用户头像的 URL 地址                                          |
| userSig    | 字符串 | 登录签名，计算方法见 [计算UserSig](https://cloud.tencent.com/document/product/454/14548)。 |

> 由于 login 是一个需要跟后台服务器通讯的过程，所以您的客户端代码不应当在 login 之后立刻调用其他函数，而是应该等待 login 函数的异步回调。

### step5: 获取房间列表（非必需）

不管是主播还是观众，都需要有一个房间间列表，调用 MLVBLiveRoom 的 **getRoomList** 接口可以获得一个简单的房间列表：

- 当主播通过 `createRoom` 创建一个新房间时，房间列表中会相应地增加一条新的房间信息。
- 当主播通过 `exitRoom` 退出房间时，该房间会被从房间列表中移除。
- 列表中每一个房间都有其对应的 roomInfo，是在主播 createRoom 时传入的，推荐您将 roomInfo 定义为 json 格式，这样可以有很强的扩展性。

> 如果您希望使用自己的房间列表，这一步可以省略，但需要您在 step6 中自行指定 roomID，推荐使用主播的 userID 作为 roomID，可以避免房间号重复。

### step6: 主播开播

主播要开播，需要先调用 MLVBLiveRoom 中的 **startLocalPreview** 接口开启本地摄像头预览，该函数需要传入一个 view 对象，该对象用于显示摄像头的视频影像。这期间 MLVBLiveRoom 会申请摄像头使用权限，同时，主播也可以对着摄像头调整一下美颜和美白的具体效果。

之后，调用 **createRoom** 接口，MLVBLiveRoom 会在后台的房间列表中新建一个直播间，同时主播端会进入直播状态。

> 推荐使用主播的 userID 作为 roomID，可以避免房间号重复。如果您不填写 roomId，后台也会为您分配一个 roomID。如果您想要自己管理房间列表，可以先由您的服务器确定 roomID，再通过 createRoom、enterRoom 和 exitRoom 接口使用 MLVBLiveRoom 的连麦能力。

### step7: 观看直播

观众通过 MLVBLiveRoom 中的 **enterRoom** 接口可以进入直播间观看视频直播，enterRoom 函数需要传入一个 view 对象，用于显示直播流的视频影像。

进入房间后，通过调用 **getAudienceList** 接口可以获取观众列表，这里的列表不是全量数据，如果少于30 个人就全部返回，如果多于 30 个人，就只返回新进入的 30 个人（考虑到 UI 上有限的展示需求，返回更多的人数除了会降低列表拉取速度之外，并没有太多实际用处）。

### step8: 弹幕消息

MLVBLiveRoom 包装了 TIMSDK 的消息发送接口，您可以通过 **sendRoomTextMsg** 函数发送普通的文本消息（用来弹幕），也可以通过 **sendRoomCustomMsg** 发送自定义消息（用于点赞，送花等等）。

> ! 腾讯云 IM 的直播聊天室，每秒钟最多可以收取40条的消息，如果您以每秒钟40次以上的速度刷新 UI 上的弹幕界面，很容易导致 CPU 100%，这里需要注意控制刷新频率，避免高频刷新。

### step9: 观众与主播连麦

|  步骤  |    角色    | 详情                                                         |
| :----: | :--------: | :----------------------------------------------------------- |
| 第一步 |    观众    | 观众调用 `requestJoinAnchor()` 向主播发起连麦请求            |
| 第二步 |    主播    | 主播会收到 `MLVBLiveRoomDelegate#onRequestJoinAnchor(AnchorInfo, String)` 通知，之后可以展示一个 UI 提示，询问主播要不要接受连麦。 |
| 第三步 |    主播    | 主播调用 `reponseJoinAnchor()` 确定是否接受观众的连麦请求。  |
| 第四步 |    观众    | 观众会收到 `MLVBLiveRoomDelegate.RequestJoinAnchorCallback` 回调通知，可以得知请求是否被同意。 |
| 第五步 |    观众    | 观众如果请求被同意，则调用 startLocalPreview() 开启本地摄像头，如果 App 还没有取得摄像头和麦克风权限，会触发 UI 提示用户授权摄像头和麦克风的使用权限。 |
| 第六步 |    观众    | 观众然后调用 `joinAnchor()` 正式进入连麦状态。               |
| 第七步 |    主播    | 当观众进入连麦状态后，主播就会收到 `MLVBLiveRoomDelegate#onAnchorEnter(AnchorInfo)` 通知。 |
| 第八步 |    主播    | 主播调用 `startRemoteView()` 就可以看到连麦观众的视频画面。  |
| 第九步 |    观众    | 如果直播间里已经有其他观众正在跟主播进行连麦，那么新加入的这位连麦观众也会收到 `onAnchorJoin()` 通知，用于展示（`startRemoteView()`）其他连麦者的视频画面。 |
| 第九步 | 主播或观众 | 主播或观众随时都可以通过 `quitJoinAnchor()` 接口退出连麦状态，同时，主播还可以通过 `kickoutJoinAnchor()` 接口踢掉连麦观众。 |

> MLVBLiveRoom 在设计上最多支持10人同时连麦，但是出于兼容低端 Android 机和实际体验效果的考虑，建议将同时连麦人数控制在6人以下。

### step10: 主播间跨房间PK

主播间跨房 PK 常被用于活跃直播平台的氛围，提升打赏频率，对平台的主播人数有一定要求。目前常见的主播 PK 玩法是将所有愿意 PK 的主播“圈”在一起，再后台进行随机配对，每次 PK 都有一定时间要求，比如5分钟，超过后即结束 PK 状态。

由于我们暂时未在 MLVBLiveRoom 的房间服务里加入配对逻辑，因此目前仅提供了一个基于客户端 API 接口的简单 PK 流程，您可以通过腾讯云通讯 IM 服务的消息下发 [REST API](https://cloud.tencent.com/document/product/269/2282) 接口，由您的配对服务器，将配对开始、配对结束等指令发送给指定的主播，从而实现服务器控制的目的。如果采用此种控制方式，下述步骤中的第3步实现为默认接受即可。

|  步骤  |   角色    | 详情                                                         |
| :----: | :-------: | :----------------------------------------------------------- |
| 第一步 |  主播 A   | 主播 A 调用 `requestRoomPK()` 向主播 B 发起连麦请求。        |
| 第二步 |  主播 B   | 主播 B 会收到 `MLVBLiveRoomDelegate#onRequestRoomPK(AnchorInfo)` 回调通知。 |
| 第三步 |  主播 B   | 主播 B 调用 `responseRoomPK()` 确定是否接受主播 A 的 PK 请求。如果采用服务器配对的 PK 方案，此处可以默认接受，不需要由主播 B 来决策。 |
| 第四步 |  主播 B   | 主播 B 在接受了主播 A 的请求后，即可调用 `startRemoteView()` 来显示主播 A 的视频画面。 |
| 第五步 |  主播 A   | 主播 A 会收到 `MLVBLiveRoomDelegate.RequestRoomPKCallback` 回调通知，可以得知请求是否被同意，如果请求被同意，则可以调用 `startRemoteView()` 显示主播 B 的视频画面。 |
| 第六步 | 主播 A或B | 主播 A 或 B 均可以通过调用 `quitRoomPK()` 接口结束 PK 状态。 |

## 常见问题

#### 1. 移动直播是不是使用 RTMP 协议进行连麦？

不是的。
腾讯云采用了两种传输通道才实现了直播+连麦功能，其中直播采用标准的 HTTP-FLV 协议，走标准 CDN 线路，没有并发观看人数的限制，且带宽成本很低，但延迟一般在 3s 以上。
连麦则采用了 UDP 协议，走专用加速线路，延迟一般在 500ms 以内，但由于线路成本较高，因此采用连麦时长进行计费。

![](https://main.qcloudimg.com/raw/ca3441a2671fda6b336edf9921b4cd8a.png)

|     通道     |                           直播通道                           |                           连麦通道                           |
| :----------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|   通讯延迟   |                             >=3s                             |                           <=500ms                            |
|   底层协议   |                        HTTP-FLV 协议                         |                           UDP协议                            |
|  价格/费用   | [按带宽计费](https://cloud.tencent.com/document/product/454/8008#LVB) | [按时长计费](https://cloud.tencent.com/document/product/454/8008#ACC) |
|   最高并发   |                            无上限                            |                            <=10人                            |
| TXLivePusher |                setVideoQuality 为 SD、HD、FHD                |       setVideoQuality 为 MAIN_PUBLISHER、SUB_PUBLISHER       |
| TXLivePlayer |                      PLAY_TYPE_LIVE_FLV                      |                   PLAY_TYPE_LIVE_RTMP_ACC                    |
|   播放URL    |                       普通的 FLV 地址                        |                 带防盗链签名的 RTMP-ACC 地址                 |





