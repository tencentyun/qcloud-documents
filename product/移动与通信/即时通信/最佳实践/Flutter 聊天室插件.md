## 前言
本文以 [Tencent Cloud AV Chat Room](https://pub.dev/packages/tencent_cloud_av_chat_room) 插件为基础，结合 [直播 Flutter SDK](https://cloud.tencent.com/document/product/454/71673) 实现的直播业务场景.

## Tencent Cloud AV Chat Room

`Tencent Cloud AV Chat Room` 是基于 [Tencent Cloud Chat SDK](https://pub.dev/packages/tencent_cloud_chat_sdk) 并围绕聊天互动场景业务实现的 UI 组件。

您可通过该组件快速实现一个包含**千万级互动**的应用。

<p align="center">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/6bf8f0570d62121a5d1a7296a8f36073.jpg">
</p>

[](id:msg)
## 使用介绍

### 前置条件

- 已 [注册](https://www.tencentcloud.com/zh/document/product/378/17985) 腾讯云账号并完成 [身份验证](https://www.tencentcloud.com/zh/document/product/378/3629)。
- 参照 [创建并升级应用](https://www.tencentcloud.com/zh/document/product/1047/34577) 创建应用，并记录好 `SDKAppID`。
- 在 [IM 控制台](https://console.tencentcloud.com/im) 选择您的应用，在左侧导航栏依次点击 辅助工具->UserSig 生成&校验 ，创建 UserID 及其对应的 `UserSig`，复制`UserID`、`签名（Key）`、`UserSig`这三个，后续登录时会用到。
- 创建一个 Flutter 应用。
- 在 pubspec.yaml 文件中的 dependencies 下添加 tencent_cloud_av_chat_room。或者执行如下命令：

```
/// step 1:
flutter pub add tencent_cloud_av_chat_room

/// step 2:
flutter pub get
```

### 步骤1：初始化并登录 IM

初始化并登录 IM 有两种方式:

- **组件外部**：整个应用初始化并登录一次即可。
- **组件内部**：通过配置的方式将参数传入组件内部。
  如若您在现有 IM flutter 项目中集成该插件，可跳过该步骤。

##### 组件外部(推荐)

在您创建的 flutter 应用中初始化 IM, 注意 IM 应用只需初始化一次即可。如若在现有 IM 项目中集成可跳过该步骤。

```dart
import 'package:tencent_av_chat_room_kit/tencent_cloud_chat_sdk_type.dart';

class _MyHomePageState extends State<MyHomePage> {
	 final int _sdkAppID = 0; // 前置条件中创建的IM应用SDKAppID
	 final String _loginUserID = ""; // 前置条件中的UserID
	 final String _userSig = ""; // 前置条件中的UserSig
	@override
	void initState() {
		super.initState();
		_initAndLoginIm();
	  }

	_initAndLoginIm() async {
		await TencentImSDKPlugin.v2TIMManager.initSDK(
			sdkAppID: _sdkAppID,
			loglevel: LogLevelEnum.V2TIM_LOG_ALL,
			listener: V2TimSDKListener());
		TencentImSDKPlugin.v2TIMManager
          .login(userID: _loginUserID, userSig: _userSig);
	}
}
```

##### 组件内部

您也可将`SDKAppID`、`UserSig`、`UserID`通过配置的方式传入组件内部进行 IM 的初始化和登录。

```dart
import 'package:tencent_cloud_av_chat_room/tencent_cloud_av_chat_room.dart';

class _TencentAVChatRoomKitState extends State<TencentCloudAVChatRoom> {
	final int _sdkAppID = 0; // 前置条件中创建的IM应用SDKAppID
	final String _loginUserID = ""; // 前置条件中的UserID
	final String _userSig = ""; // 前置条件中的UserSig
	@override
  	Widget build(BuildContext context) {
		return TencentCloudAVChatRoom(
			config: TencentCloudAvChatRoomConfig(
				loginUserID: _loginUserID, sdkAppID: _sdkAppID, userSig: _userSig));
	}
}
```

### 步骤2：使用组件

在您合适的模块中使用该组件。

```dart
import 'package:tencent_cloud_av_chat_room/tencent_cloud_av_chat_room.dart';

class _TencentAVChatRoomKitState extends State<TencentCloudAVChatRoom> {
	final int _sdkAppID = 0; // 前置条件中创建的IM应用SDKAppID
	final String _loginUserID = ""; // 前置条件中的UserID
	final String _userSig = ""; // 前置条件中的UserSig
	@override
  	Widget build(BuildContext context) {
		return TencentCloudAVChatRoom(
			data: TencentCloudAvChatRoomData(anchorInfo: AnchorInfo()),
			config: TencentCloudAvChatRoomConfig(
				loginUserID: _loginUserID, sdkAppID: _sdkAppID, userSig: _userSig, avChatRoomID: ''));
	}
}
```

### 可选操作：开通内容审核功能
在聊天室场景中，用户很可能会发送不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。



## 配合腾讯云视立方搭建直播间

直播在生活中可谓是无处不在，越来越多的企业、开发者们正在搭建自己的直播平台。下面会介绍如何与腾讯云视立方搭建一个直播间。
直播间主要包含直播和互动两部分，直播部分我们会采用腾讯云视立方移动直播来实现直播拉流, 画面播放等。互动采用本插件来实现直播点赞、送礼、弹幕收发等。

本文相关代码均可在 [Github](https://github.com/TencentCloud/chat-demo-flutter/tree/main/lib/src/pages/live_room) 中下载查看。

### 直播拉流和画面播放

直播 SDK 是腾讯云视立方产品家族的子产品之一。直播 SDK 支持直播推流、拉流、主播观众互动连麦、主播跨房 PK 等能力，为用户提供稳定、极速的直播终端服务。
参见 [直播 Flutter SDK 标准直播拉流](https://cloud.tencent.com/document/product/454/71673) 实现直播拉流和画面播放功能。

**1: 设置 License**

```dart
// live.dart
class Live extends StatefulWidget {
  const Live({Key? key}) : super(key: key);

  @override
  State<Live> createState() => _LiveState();
}

class _LiveState extends State<Live> {
	...
	@override
	void initState() {
		super.initState();
		setupLicense();
	}

	/// 腾讯云License管理页面(https://console.cloud.tencent.com/live/license)
	setupLicense() {
		// 当前应用的License LicenseUrl
		final licenseUrl = "";
		// 当前应用的License Key
		final licenseKey = "";
		V2TXLivePremier.setLicence(licenseUrl, licenseKey);
	}
	...
}
```

**2: 直播拉流、画面播放**

```dart
// live_player.dart
...
class _LivePlayState extends State<LivePlayer> {
	...
	@override
	void initState() {
		super.initState();
		initPlayer();
	}
	initPlayer() async {
		_livePlayer = await V2TXLivePlayer.create();
	}

	@override
	void dispose() {
		super.dispose();
		_livePlayer.destroy();
	}

	@override
	Widget build(BuildContext context) {
		return Container(
			color: Colors.black.withOpacity(0.7),
			child: V2TXLiveVideoWidget(
				onViewCreated: (viewId) async {
				_localViewId = viewId;
				startPlay();
				},
			),
		);
	}

	void startPlay() async {
		if (_isPlaying) {
			return;
		}
		if (_localViewId != null) {
			debugPrint("_localViewId $_localViewId");
			var code = await _livePlayer.setRenderViewID(_localViewId!);
			if (code != V2TXLIVE_OK) {
				debugPrint("StartPlay error： please check remoteView load");
			}
		}
		var url = widget.playUrl;
		debugPrint("play url: $url");
		var playStatus = await _livePlayer.startLivePlay(url);
		debugPrint("play status: $playStatus");
		if (playStatus != V2TXLIVE_OK) {
		setState(() {
			_onError = true;
		});
		debugPrint("play error: $playStatus url: $url");
			return;
		}
		await _livePlayer.setPlayoutVolume(100);
		setState(() {
			_isPlaying = true;
		});
	}
}
```

### 直播互动(点赞、送礼、弹幕收发)

直播互动在直播场景中尤为重要。用户通过弹幕、送礼等方式与主播进行互动。
接下来参见 [使用介绍](#msg) 来集成本插件。

**1：初始化、登录 IM**

我们在插件外部登录 IM,通常整个应用程序只需要初始化和登录 IM 一次即可。

```dart
import 'package:tencent_av_chat_room_kit/tencent_cloud_chat_sdk_type.dart';

class _MyHomePageState extends State<MyHomePage> {
	 final int _sdkAppID = 0; // 前置条件中创建的IM应用SDKAppID
	 final String _loginUserID = ""; // 前置条件中的UserID
	 final String _userSig = ""; // 前置条件中的UserSig
	@override
	void initState() {
		super.initState();
		_initAndLoginIm();
	  }

	_initAndLoginIm() async {
		await TencentImSDKPlugin.v2TIMManager.initSDK(
			sdkAppID: _sdkAppID,
			loglevel: LogLevelEnum.V2TIM_LOG_ALL,
			listener: V2TimSDKListener());
		TencentImSDKPlugin.v2TIMManager
          .login(userID: _loginUserID, userSig: _userSig);
	}
}
```

**2：使用插件**

```dart
// live_room.dart

class LiveRoom extends StatelessWidget {
	final String loginUserID;
	final String playUrl;
	final String avChatRoomID = ''; // 一个直播间本质上是所有用户在一个av chat room 类型的群组里面做消息的收发

	LiveRoom({Key? key, required this.loginUserID, required this.playUrl})
      : super(key: key);

	@override
	Widget build(BuildContext context) {
		return Stack(
			children: [
				LivePlayer(playUrl: playUrl), // 直播拉流和画面播放
				TencentCloudAVChatRoom(
					config: TencentCloudAvChatRoomConfig(
						avChatRoomID: avChatRoomID,
						loginUserID: loginUserID, //登录的用户ID
					),
					data: TencentCloudAvChatRoomData(
						isSubscribe: false,
						notification: "直播间公告",
						anchorInfo: AnchorInfo(
							subscribeNum: 200,
							fansNum: 5768,
							nickName: "风雨人生",
							avatarUrl:""
						),
					)
				)
			]
		)
	}
}
```

上面我们通过`Stack Widget`将`LivePlayer(直播)`和`LiveRoom(互动)`通过层叠的方式结合在一起。

**3：如何自定义**

插件本身提供默认的 UI，但是往往在实际的使用过程中，用户都有不同的 UI, 接下来会介绍如何自定义本插件。

```dart
...
@override
	Widget build(BuildContext context) {
		return Stack(
			children: [
				LivePlayer(playUrl: playUrl), // 直播拉流和画面播放
				TencentCloudAVChatRoom(
					...
					TencentCloudAvChatRoomCustomWidgets(
						roomHeaderAction: Container(), // 屏幕右上角显示区域自定义组件, 默认显示的是直播间在线人数
						roomHeaderLeading: Container(), // 屏幕左上角显示区域自定义组件，默认显示的是主播信息
						roomHeaderTag: Container(), // roomHeaderAction 和 roomHeaderLeading 下方，一般用于显示排行榜，热度等。
						onlineMemberListPanelBuilder: (context, id) { // 直播间在线人数点击后展开的面板自定义
							return Container();
						},
						anchorInfoPanelBuilder: (context, id) { // 主播头像点击后展开的面板自定义
							return Container();
						},
						giftsPanelBuilder: (context) { // 屏幕右下方礼物按钮点击后展示的面板自定义
							return Container();
						},
						messageItemBuilder: (context, message, child) { // 弹幕消息自定义
							return Container();
						},
						messageItemPrefixBuilder: (context, message) { // 弹幕消息前缀自定义，一般用于自定义粉丝牌子等
							return Container();
						},
						giftMessageBuilder: (context, message) { // 礼物消息自定义, 从屏幕左侧滑入的礼物消息
							return Container();
						},
						textFieldActionBuilder: ( // 屏幕右下方区域自定义
							context,
						) {
							return [Container()];
						},
						textFieldDecoratorBuilder: (context) { // 屏幕左下方输入框自定义
							return Container();
						}
					)
				)
			]
		)
	}
```

**4：礼物**

送礼在直播场景中是非常重要的场景。本插件默认提供了三种礼物类型的解析, 用户只需要按照特定的格式来发送自定义消息即可在界面上展示礼物消息。本插件默认带的送礼面板只用于展示礼物消息解析的功能，通常礼物是会牵扯到用户计费计量的逻辑，所以需要用户根据自己的业务需求在服务端计费后调用服务端接口发送礼物消息。送礼流程如下:

- 客户端短连接请求到自己的业务服务器，涉及到计费逻辑。
- 计费后，发送人直接看到 XXX 送了 XXX 礼物。（以确保发送人自己看到自己发的礼物，消息量大的时候，可能会触发抛弃策略）
- 计费结算后，调用服务端接口发送发送自定义消息（礼物）
  礼物消息我们通过发送自定义消息来实现。如下定义了三种礼物格式:

```dart
// 礼物带特效(会在屏幕左侧滑入送礼详情并会在屏幕上展示礼物特效(Lottie/SVAGA))
final customInfoRocket = {
	"version": 1.0, // 协议版本号
	"businessID": "flutter_live_kit", // 业务标识字段
	"data": {
		"cmd":
			"send_gift_message", // 必须为send_gift_message
		"cmdInfo": {
		"type": 3, // 礼物类型
		"giftUrl": "", // 礼物图片地址
		"giftCount": 1, // 礼物数量
		"giftSEUrl": "assets/live/rocket.json", // 礼物特效地址，如果是http 开头会加载网络地址
		"giftName": "超级火箭", // 礼物名称
		},
	}
};

// 礼物不带特效(会在屏幕左测滑入)
final customInfoPlane = {
    "version": 1.0, // 协议版本号
    "businessID": "flutter_live_kit", // 业务标识字段
    "data": {
      "cmd":
          "send_gift_message", // 必须为send_gift_message
      "cmdInfo": {
        "type": 2, // 礼物类型
        "giftUrl": "", // 礼物图片地址
        "giftCount": 1, // 礼物数量
        "giftName": "飞机", // 礼物名称
      },
    }
};

// 普通礼物(礼物会展示到弹幕中，不会从屏幕左测滑入和展示特效)
final normalGift = {
    "version": 1.0, // 协议版本号
    "businessID": "flutter_live_kit", // 业务标识字段
    "data": {
      "cmd":
          "send_gift_message", // 必须为send_gift_message
      "cmdInfo": {
        "type": 1, //普通礼物
        "giftUrl": "", // 礼物图片地址
        "giftCount": 1, // 礼物数量
        "giftName": "花", // 礼物名称
        "giftUnits": "朵", // 礼物单位
      },
    }
};
```

**5：主题**
本插件除了自定义外同时提供了`主题`能力，主题分为`颜色`和`字体`两部分。可按照您的需求自定义 [主题](#tencentcloudavchatroomtheme)。

## API Docs

### TencentCloudAvChatRoomData

组件需要使用到的数据，例如主播信息、直播间公告等。

```dart
TencentCloudAvChatRoomData(
	anchorInfo: AnchorInfo(), // 主播信息
	isSubscribe: false, // 是否订阅
	notification: "直播间公告" // 直播间公告
)
```

### TencentCloudAvChatRoomConfig

组件配置信息。

```dart
TencentCloudAvChatRoomConfig(
	avChatRoomID: '', // AV Chat Group. AV Chat Room类型的群ID.[https://cloud.tencent.com/document/product/269/75697]
	loginUserID: '', // 登录用户ID
	sdkAppID: 0, // IM 应用ID
	userSig: '', // 用户ID和secrectKey生成的sig
	barrageMaxCount: 200, // 弹幕最大条数。默认200条，当超出条数后，早些的弹幕会被清除。
	giftHttpBase: '', // 礼物消息http base。
	displayConfig: DisplayConfig() // 可控制界面部分组件的展示与隐藏
)
```

### TencentCloudAvChatRoomController

组件控制器，可在组件外部调用，用于更新数据、发送消息等。

```dart
final controller = TencentCloudAvChatRoomController();
final _needUpdateData = TencentCloudAvChatRoomData(
        anchorInfo: AnchorInfo(), // 主播信息
		isSubscribe: false, // 是否订阅
		notification: "直播间公告" // 直播间公告
	);
final _textString = "我是一条文本消息";

final customInfoRocket = {
	"version": 1.0, // 协议版本号
	"businessID": "flutter_live_kit", // 业务标识字段
	"data": {
		"cmd":
			"send_gift_message", // 指令
		"cmdInfo": { // 指令携带的信息
		"type": 3, // 礼物类型
		"giftUrl": "1e8913f8c6d804972887fc179fa1fbd7.png", // 礼物图片地址
		"giftCount": 1, // 礼物数量
		"giftSEUrl": "assets/live/rocket.json", // 礼物特效地址
		"giftName": "超级火箭", // 礼物名称
		},
	}
};

final customInfoPlane = {
    "version": 1.0, 
    "businessID": "flutter_live_kit", 
    "data": {
      "cmd":
          "send_gift_message",
      "cmdInfo": {
        "type": 2, 
        "giftUrl": "5e175b792cd652016aa87327b278402b.png",
        "giftCount": 1,
        "giftName": "飞机",
      },
    }
};

final customInfoFlower = {
    "version": 1.0, 
    "businessID": "flutter_live_kit", 
    "data": {
      "cmd":
          "send_gift_message", 
      "cmdInfo": {
        "type": 1, 
        "giftUrl": "8f25a2cdeae92538b1e0e8a04f86841a.png",
        "giftCount": 1,
        "giftName": "花",
        "giftUnits": "朵",
      },
    }
};

// 更新传入组件的data信息。
controller.updateData(_needUpdateData);

// 发送文本消息
controller.sendTextMessage(_textString);

// 发送礼物消息, 礼物消息需要按照如上特定的格式。礼物分为三种类型: [1]: 普通礼物 [2]: 礼物不带特效 [3]: 礼物带特效
controller.sendGiftMessage(jsonEncode(customInfoFlower));

// 发送任何类型的消息, [message] 需要自己创建
controller.sendMessage(message);

// 播放特效动画(Lottie, SVGA).
controller.playAnimation("assets/live/rocket.json"):
```

### TencentCloudAvChatRoomCallback

事件回调。

```dart
TencentCloudAvChatRoomCallback(
	onMemberEnter: (memberInfo) {}, // 有人进入直播间
	onRecvNewMessage: (message) {} // 收到弹幕消息
)
```

### TencentCloudAvChatRoomCustomWidgets

自定义组件

```dart
TencentCloudAvChatRoomCustomWidgets(
	roomHeaderAction: Container(), // 屏幕右上角显示区域自定义组件, 默认显示的是直播间在线人数
	roomHeaderLeading: Container(), // 屏幕左上角显示区域自定义组件，默认显示的是主播信息
	roomHeaderTag: Container(), // roomHeaderAction 和 roomHeaderLeading 下方，一般用于显示排行榜，热度等。
	onlineMemberListPanelBuilder: (context, id) { // 直播间在线人数点击后展开的面板自定义
		return Container();
	},
	anchorInfoPanelBuilder: (context, id) { // 主播头像点击后展开的面板自定义
		return Container();
	},
	giftsPanelBuilder: (context) { // 屏幕右下方礼物按钮点击后展示的面板自定义
		return Container();
	},
	messageItemBuilder: (context, message, child) { // 弹幕消息自定义
		return Container();
	},
	messageItemPrefixBuilder: (context, message) { // 弹幕消息前缀自定义，一般用于自定义粉丝牌子等
		return Container();
	},
	giftMessageBuilder: (context, message) { // 礼物消息自定义, 从屏幕左侧滑入的礼物消息
		return Container();
	},
	textFieldActionBuilder: ( // 屏幕右下方区域自定义
		context,
	) {
		return [Container()];
	},
	textFieldDecoratorBuilder: (context) { // 屏幕左下方输入框自定义
		return Container();
	}
)
```

[](id:tcentcloudavchatroomtheme)
### TencentCloudAvChatRoomTheme

主题

```dart
TencentCloudAvChatRoomTheme(
	backgroundColor: Colors.black, // 小部件的背景色,
	hintColor: Colors.red, // hint text 颜色
	highlightColor: Colors.orange, // 高亮颜色
	accentColor: Colors.white, // 前景色
	textTheme: TencentCloudAvChatRoomTextTheme(), // 字体主题
	secondaryColor: Colors.grey, // 次色
	inputDecorationTheme: InputDecorationTheme() // 输入框主题
)
```

### TencentCloudAvChatRoomTextTheme

字体主题

```dart
TencentCloudAvChatRoomTextTheme(
	giftBannerSubTitleStyle: TextStyle(), // 屏幕左侧划入的礼物消息 sub title 字体主题, 礼物名称
	giftBannerTitleStyle: TextStyle(), // 屏幕左侧划入的礼物消息 title 字体主题
	anchorTitleStyle: TextStyle(), // 主播名称字体主题
	anchorSubTitleStyle: TextStyle(), // 点赞字体主题
	barrageTitleStyle: TextStyle(), // 弹幕消息发送人名称主题
	barrageTextStyle: TextStyle() // 弹幕消息内容主题
)
```

## 联系我们

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入 QQ 群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)
