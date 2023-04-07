## 什么是 TUIKit

Flutter TUIKit 是基于 Flutter IM SDK 实现的一套 UI 组件，其中包含会话、聊天、关系链、群组及本地搜索等功能。

基于本套 UI 组件和内置的 IM 业务逻辑，您可以像搭积木一样，快速地在您 App 中，引入即时通信及用户关系链管理等模块。

**接入前，您可以通过 [我们的 DEMO](https://cloud.tencent.com/document/product/269/70747#demo)，快速在线体验 TUIKit 各项能力。**

>? 本含 TUIKit tencent_cloud_chat_uikit 已开源，您可引入 [在线版本](https://pub.dev/packages/tencent_cloud_chat_uikit)，也可 [GitHub fork](https://github.com/TencentCloud/chat-uikit-flutter) 后本地引入使用。

目前包含的一级组件如下：

- [TIMUIKitCore](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitCore/readme.html) 核心
- [TIMUIKitConversation](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitConversation/TIMUIKitConversation-Implementation.html) 会话列表
- [TIMUIKitChat](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChat-Implementation.html) 聊天区域，发送消息+历史消息列表
- [TIMUIKitContact](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitContact/TIMUIKitContact-Implementation.html) 联系人列表
- [TIMUIKitProfile](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitProfile/TIMUIKitProfile-Implementation.html) 用户资料查看及关系链管理
- [TIMUIKitGroupProfile](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitGroupProfile/TIMUIKitGroupProfile-Implementation.html) 群资料展示与管理
- [TIMUIKitGroup](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitGroup/TIMUIKitGroup-Implementation.html) 我的群聊
- [TIMUIKitBlackList](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitBlackList/TIMUIKitBlackList-Implementation.html) 黑名单
- [TIMUIKitNewContact](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitNewContact/TIMUIKitNewContact-Implementation.html) 新的联系人申请
- [TIMUIKitSearch](https://cloud.tencent.com/document/product/269/79121) 本地搜索，支持全局搜索及会话内搜索

![](https://qcloudimg.tencent-cloud.cn/raw/f140dd76be01a65abfb7e6ba2bf50ed5.png)

>?上图 TUIKit 界面语言支持自动或手动在 **简体中文/繁体中文/英文/日语/韩语** 间切换。国际化界面语言用法详情，或新增其他语言包，[可参考本文档](https://cloud.tencent.com/document/product/269/84481)。

## 环境要求

|     环境    | 版本                                                               |
| ------- | ------------------------------------------------------------------ |
| Flutter | 最低要求 Flutter 2.10.0 版本。                                     |
| Android | Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。 |
| iOS     | Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。       |

## 支持平台

| 平台  | 支持状态 |
|---------|---------|
| iOS  | 支持 |
| Android  | 支持 |
| [Web](#web)  | 支持，0.1.5版本起 |
| macOS  | 支持，2.0.0 版本起 |
| Windows  | 支持，2.0.0 版本起 |
| [混合开发](https://cloud.tencent.com/document/product/269/83153) （将 Flutter SDK 添加至现有原生应用） | 1.0.0版本起支持 |

>? Web/macOS/Windows 平台需要简单的几步额外引入，详情请参见 [拓展更多平台](https://cloud.tencent.com/document/product/269/68823#.E6.8B.93.E5.B1.95.E6.9B.B4.E5.A4.9A.E5.B9.B3.E5.8F.B0)。

## 前提条件

1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 帐号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 参照 [创建并升级应用](https://cloud.tencent.com/document/product/269/32577) 创建应用，并记录好 `SDKAppID`。
3. 在 [IM 控制台](https://console.cloud.tencent.com/im) 选择您的应用，在左侧导航栏依次单击 **辅助工具** > **UserSig 生成&校验** ，创建两个 UserID 及其对应的 UserSig，复制`UserID`、`签名（Key）`、`UserSig`这三个，后续登录时会用到。
![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

## 接入步骤

如下会介绍如何使用 Flutter TUIKit 快速构建一个简单的即时通信应用。

### 步骤1：创建 Flutter 应用并添加权限

请参见 [Flutter 文档](https://flutter.cn/docs/get-started/test-drive?tab=terminal) 快速创建一个 Flutter 应用。

#### 配置权限[](id:permission)

由于 TUIKit 运行，需要拍摄/相册/录音/网络等权限，需要您在 Native 的文件中手动声明，才可正常使用相关能力。

**Android**

打开 `android/app/src/main/AndroidManifest.xml` ，在 `<manifest></manifest>`中，添加如下权限。

```xml
    <uses-permission
        android:name="android.permission.INTERNET"/>
    <uses-permission
        android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission
        android:name="android.permission.FOREGROUND_SERVICE"/>
    <uses-permission
        android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission
        android:name="android.permission.VIBRATE"/>
    <uses-permission
        android:name="android.permission.ACCESS_BACKGROUND_LOCATION"/>
    <uses-permission
        android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission
        android:name="android.permission.READ_EXTERNAL_STORAGE"/>
    <uses-permission
        android:name="android.permission.CAMERA"/>
```

**iOS**

打开 `ios/Podfile` ，在文件末尾新增如下权限代码。

```
post_install do |installer|
  installer.pods_project.targets.each do |target|
    flutter_additional_ios_build_settings(target)
    target.build_configurations.each do |config|
          config.build_settings['GCC_PREPROCESSOR_DEFINITIONS'] ||= [
            '$(inherited)',
            'PERMISSION_MICROPHONE=1',
            'PERMISSION_CAMERA=1',
            'PERMISSION_PHOTOS=1',
          ]
        end
  end
end
```

>?如您需要用到推送能力，还需要添加推送相关权限，详情可查看 [Flutter 厂商消息推送插件集成指南](https://cloud.tencent.com/document/product/269/75430)。

#### 安装 IM TUIkit

我们的 TUIkit 已经内含 IM SDK，因此仅需安装`tencent_cloud_chat_uikit`，不需要再安装基础 IM SDK。

```shell
#在命令行执行：
flutter pub add tencent_cloud_chat_uikit
```

如果您的项目需要支持 Web，请在执行后续步骤前，[查看 Web 兼容说明章节](#web)，引入 JS 文件。

### 步骤2：初始化[](id:init)

1. 在您应用启动时，初始化 IM。
2. 请务必保证先执行 [`TIMUIKitCore.getInstance()`](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitCore/getInstance.html) ，再调用初始化函数 [`init()`](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitCore/init.html) ，并将您的`sdkAppID`传入。
3. 为方便您获取API报错及建议提醒用户的提示语，此处建议挂载一个 onTUIKitCallbackListener 监听，[详见此部分](#callback)。

示例代码如下，[全部初始化参数可参考此文档](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitCore/init.html)。

```dart
/// main.dart
import 'package:tencent_cloud_chat_uikit/tencent_cloud_chat_uikit.dart';

final CoreServicesImpl _coreInstance = TIMUIKitCore.getInstance();
  @override
 void initState() {
   _coreInstance.init(
     sdkAppID: 0, // Replace 0 with the SDKAppID of your IM application when integrating
     // language: LanguageEnum.en, // 界面语言配置，若不配置，则跟随系统语言
     loglevel: LogLevelEnum.V2TIM_LOG_DEBUG,
     onTUIKitCallbackListener:  (TIMCallback callbackValue){}, // [建议配置，详见此部分](https://cloud.tencent.com/document/product/269/70746#callback)
     listener: V2TimSDKListener());
   super.initState();
 }
}
```

>!请在本步骤 await 初始化完成后，才可执行后续步骤。

#### 登录测试账户

1. 此时，您可以使用最开始的时候，在控制台生成的测试账户，完成登录验证。
2. 调用 [`_coreInstance.login`](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitCore/login.html) 方法，登录一个测试账户。

```dart
import 'package:tencent_cloud_chat_uikit/tencent_cloud_chat_uikit.dart';

final CoreServicesImpl _coreInstance = TIMUIKitCore.getInstance();
_coreInstance.login(userID: userID, userSig: userSig);
```

>? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是由服务器端生成，并提供面向 App 的接口，在需要 `UserSig` 时由 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

### 步骤3：实现 - 会话列表页面

您可以以会话列表作为您的 IM 功能首页，其涵盖了与所有有聊天记录的用户及群聊的会话。

<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/279da6d5d41ec1ce0b0cf7fca9a697b8.jpg" />

请创建一个 `Conversation` 类，`body` 中使用 [`TIMUIKitConversation`](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitConversation/TIMUIKitConversation-Implementation.html) 组件，渲染会话列表。

您仅需传入一个 `onTapItem` 事件的处理函数，用于跳转至具体会话聊天页的导航。关于 `Chat` 类，会在下一步讲解。

```dart
import 'package:flutter/material.dart';
import 'package:tencent_cloud_chat_uikit/tencent_cloud_chat_uikit.dart';

class Conversation extends StatelessWidget {
const Conversation({Key? key}) : super(key: key);
@override
Widget build(BuildContext context) {
return Scaffold(
  appBar: AppBar(
    title: const Text(
      "Message",
      style: TextStyle(color: Colors.black),
    ),
  ),
  body: TIMUIKitConversation(
    onTapItem: (selectedConv) {
      Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => Chat(
              selectedConversation: selectedConv,
            ),
          ));
    },
  ),
);
}
}
```

### 步骤4：实现 - 会话聊天页面

该页面由顶部主体聊天历史记录及底部发送消息模块组成。
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/0c361254fa5117f7580f39e8b523e472.png" />

请创建一个 `Chat` 类，`body` 中使用 [`TIMUIKitChat`](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChat-Implementation.html) 组件，渲染聊天页面。

您最好传入一个 `onTapAvatar` 事件的处理函数，用于跳转至联系人的详细信息页。关于 `UserProfile` 类，会在下一步讲解。

```dart
import 'package:flutter/material.dart';
import 'package:tencent_cloud_chat_uikit/tencent_cloud_chat_uikit.dart';

class Chat extends StatelessWidget {
final V2TimConversation selectedConversation;
const Chat({Key? key, required this.selectedConversation}) : super(key: key);
String? _getConvID() {
return selectedConversation.type == 1
    ? selectedConversation.userID
    : selectedConversation.groupID;
}
@override
Widget build(BuildContext context) {
return TIMUIKitChat(
  conversationID: _getConvID() ?? '', // groupID or UserID
  conversationType: selectedConversation.type ?? 1, // Conversation type
  conversationShowName: selectedConversation.showName ?? "", // Conversation display name
  onTapAvatar: (_) {
        Navigator.push(
            context,
            MaterialPageRoute(
             builder: (context) => UserProfile(userID: userID),
        ));
  }, // Callback for the clicking of the message sender profile photo. This callback can be used with `TIMUIKitProfile`.
);
}
```

### 步骤5：实现 - 用户详情页面

该页面默认，可在只传入一个 `userID` 的情况下，自动根据是否是好友，生成用户详情页。

请创建一个 `UserProfile` 类，`body` 中使用 [`TIMUIKitProfile`](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitProfile/TIMUIKitProfile-Implementation.html) 组件，渲染用户详情及关系链页面。

>? 如果您希望自定义该页面，请优先考虑使用 [`profileWidgetBuilder`](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitProfile/ProfileWidgetBuilder.html) 传入需自定义的 profile 组件并配合 `profileWidgetsOrder` 确定纵向排列顺序；如果无法满足，才可使用 `builder` 。

<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/5f2e67ffb31adc738165e2c4ce58218c.jpg" />

```dart
import 'package:flutter/material.dart';
import 'package:tencent_cloud_chat_uikit/tencent_cloud_chat_uikit.dart';

class UserProfile extends StatelessWidget {
    final String userID;
    const UserProfile({required this.userID, Key? key}) : super(key: key);

    @override
    Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
       title: const Text(
         "Message",
         style: TextStyle(color: Colors.black),
       ),
     ),
     body: TIMUIKitProfile(
          userID: widget.userID,
     ),
    );
  }
}
```

此时，您的应用已经可以完成消息收发，管理好友关系，展示用户详情及展示会话列表。

### 步骤6: 音视频通话
### 1 添加依赖
音视频通话功能依赖TUICallKit,首先在工程中完成对TUICallKit依赖，在工程的配置文件pubspec.yaml文件中添加依赖：

```
dependencies:
  tencent_calls_uikit:
```
#### 2 音视频通话功能
在TIMUIKit中已经集成了音视频通话功能，TUIKit通过插件查询功能检测当前工程是否已经完成对TUICallKit的依赖，若存在音视频通话组件，则在TIMUIKitChat和TIMUIKitProfile中会出现音视频通话的相关功能按钮。

![](https://qcloudimg.tencent-cloud.cn/raw/13ba2d71c18c9f1ab7e915e1eaa3347c.png)

此时，您的应用便可使用音视频通话功能。


### 附加1：TUIKit 的更多能力

您还可以继续使用以下 TUIKit 组件快速实现完整 IM 功能。

- [TIMUIKitContact](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitContact/TIMUIKitContact-Implementation.html)：联系人列表页面。
- [TIMUIKitGroupProfile](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitGroupProfile/TIMUIKitGroupProfile-Implementation.html)：群资料页面，使用方式与 `TIMUIKitProfile` 基本一致。
- [TIMUIKitGroup](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitGroup/TIMUIKitGroup-Implementation.html)：群列表界面。
- [TIMUIKitBlackList](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitBlackList/TIMUIKitBlackList-Implementation.html)：黑名单列表界面。
- [TIMUIKitNewContact](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitNewContact/TIMUIKitNewContact-Implementation.html)：联系人（好友）申请列表。如需在外部显示小红点，可使用 `TIMUIKitUnreadCount` 小红点组件，其会自动挂载监听。
- [本地搜索](https://cloud.tencent.com/document/product/269/79121)：`TIMUIKitSearch` 全局搜索组件，支持全局搜索联系人/群组/聊天记录，也支持使用 `TIMUIKitSearchMsgDetail` 在特定会话中搜索聊天记录。两种模式取决于是否传入 `conversation`。

UI 组件全貌可参见 [本全览文档](https://cloud.tencent.com/document/product/269/70747) 或 [详细文档](https://comm.qq.com/im/doc/flutter/zh/TUIKit/readme.html)。

[](id:controller)

### 附加2：[选装] 使用 Controller 控制 TUIKit

>? 建议在 tencent_cloud_chat_uikit 0.1.5 及以后版本中使用本功能。

通过上述步骤的快速集成，您已经可以搭建一套可用的 IM 模块。如果您有其他额外的控制操作需求，可以使用组件配套的 controller 完成。

使用场景如，在会话列表页面中，您可自定义会话 item 的侧滑菜单，提供置顶会话/删除会话/删除历史消息等功能；抑或是发送消息，满足您的额外消息发送需求，例如通过您自行开发的送礼界面发送一条礼物消息。

目前我们提供三个 controller，如下：

| 组件                                                                                                                               | 控制器                                                                                                                                  | 功能                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [TIMUIKitChat](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChat-Implementation.html)                         | [TIMUIKitChatController](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChatController.html)                         | 刷新历史消息列表/更新单条消息/手动发送额外的消息/为消息设置自定义字段 等                                                                     |
| [TIMUIKitConversation](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitConversation/TIMUIKitConversation-Implementation.html) | [TIMUIKitConversationController](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitConversation/TIMUIKitConversationController.html) | 获取及刷新会话列表/会话置顶/设置会话的草稿/清空会话内所有消息/删除会话/滚动到特定会话 等                                                                    |
| [TIMUIKitProfile](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitProfile/TIMUIKitProfile-Implementation.html)                | [TIMUIKitProfileController](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitProfile/TIMUIKitProfileController.html)                | 删除联系人好友/置顶当前联系人的会话/将用户加入黑名单/修改被加好友方式/更新联系人备注名/设置联系人消息免打扰/添加联系人好友/更新自己的资料 等 |

他们的使用方式一致，以 [TIMUIKitChatController](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChatController.html) 举例用法。完整代码可[参考DEMO](https://github.com/TencentCloud/tc-chat-demo-flutter/blob/main/lib/src/chat.dart)。

1. 在使用到 [TIMUIKitChat](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChat-Implementation.html) 的类中，实例化一个 [TIMUIKitChatController](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChatController.html) 对象。
<dx-codeblock>
:::  dart
final TIMUIKitChatController _chatController = TIMUIKitChatController();
:::
</dx-codeblock>
2. 将此对象传入 [TIMUIKitChat](https://comm.qq.com/im/doc/flutter/zh/TUIKit/TIMUIKitChat/TIMUIKitChat-Implementation.html)  的 `controller` 参数中。
<dx-codeblock>
:::  dart
@override
Widget build(BuildContext context) {
  return TIMUIKitChat(
    controller: _chatController,
  // ...其他参数
 );
}
:::
</dx-codeblock>
3. 在这个类中，即可使用控制器，完成自定义操作。例如发送一条地理位置消息：
<dx-codeblock>
:::  dart
_sendLocationMessage(String desc, double longitude, double latitude) async {
    final locationMessageInfo = await sdkInstance.v2TIMMessageManager
        .createLocationMessage(
        desc: desc,
        longitude: longitude,
        latitude: latitude);
    final messageInfo = locationMessageInfo.data!.messageInfo;
    _chatController.sendMessage(
        receiverID: _getConvID(),
groupID:_getConvID(),
        convType: _getConvType(),
        messageInfo: messageInfo);
}
:::
</dx-codeblock>

### 附加3：[选装] 使用更多插件丰富 TUIKit 使用体验

除 TUIKit 本体基础功能外，我们还提供了四个选装插件，帮助您丰富 IM 能力。

- [消息推送插件](https://cloud.tencent.com/document/product/269/74605)：支持厂商原生离线推送能力及在线推送能力，并支持推送您的其他业务消息，帮助您提高消息触达率。
- [音视频通话插件](https://cloud.tencent.com/document/product/269/72485)：支持类似微信的 一对一/群组 音视频 通话。
- [位置消息插件](https://cloud.tencent.com/document/product/269/80881)：提供选取位置/发送位置及解析展示位置消息的能力。
- [自定义表情插件](https://cloud.tencent.com/document/product/269/80882)：0.1.5版本后， TUIKit 无自带表情包，需要使用此插件，快速简便集成表情能力。支持 emoji unicode 编码及自定义图片表情。集成过程可参考我们的 [Demo](https://github.com/TencentCloud/tc-chat-demo-flutter/blob/main/lib/src/pages/app.dart)。

>?更多实用的插件正在开发中，如果您有好的想法及建议，欢迎随时 [联系我们](https://cloud.tencent.com/online-service?from=doc_269&source=PRESALE)。

## Flutter for Web 支持[](id:web)

TUIKit(tencent_cloud_chat_uikit) 0.1.5版本起，可完美兼容 Web 端。

相比 Android 和 iOS 端，需要一些额外步骤。如下：

### 引入 JS

>?如果您现有的 Flutter 项目不支持 Web，请在项目根目录下运行 `flutter create .` 添加 Web 支持。

进入您项目的 `web/` 目录，使用 `npm` 或 `yarn` 安装相关JS依赖。初始化项目时，根据屏幕指引，进行即可。

```shell
cd web

npm init

npm i tim-js-sdk

npm i tim-upload-plugin
```

打开 `web/index.html` ，在 `<head> </head>` 间引入JS文件。如下：

```html
<script src="./node_modules/tim-upload-plugin/index.js"></script>
<script src="./node_modules/tim-js-sdk/tim-js-friendship.js"></script>
```

![](https://qcloudimg.tencent-cloud.cn/raw/a4d25e02c546e0878ba59fcda87f9c76.png)

## 常见问题

### Android 端报错 `compileSdkVersion` 不合适怎么办？

1. 请在您项目的 `pubspec.yaml` 文件中，指定确保如下两个插件的版本。

```yaml
  video_thumbnail: ^0.5.3
  permission_handler: ^10.0.0
  flutter_local_notifications: 9.7.0
```

2. 修改 `android/app/build.gradle` 文件，保证 `android => compileSdkVersion 33`。

```gradle
android {
  compileSdkVersion 33
  ...
}
```

3. 执行如下命令，重新安装 Android 端依赖。

```shell
flutter pub cache clean
flutter pub get
```

### 在 Flutter 2.x 上，Android 构建报错 `Codepoint 984472 not found in font, aborting.` 怎么办？

![](https://qcloudimg.tencent-cloud.cn/raw/017362112bb49e5ac2d94d76699b068a.png)

在您的编译命令中，加入 `--no-tree-shake-icons`。如：

```shell
flutter build apk --no-tree-shake-icons --dart-define=SDK_APPID={您的SDKAPPID}
```

### iOS 端 Pods 依赖无法安装成功怎么办？

#### **尝试方案一：**配置运行后，如果报错，可以单击 **Product** > **Clean Build Folder**，清除产物后重新 `pod install` 或 `flutter run`

![](https://qcloudimg.tencent-cloud.cn/raw/d495b2e8be86dac4b430e8f46a15cef4.png)

#### **尝试方案二：**手动删除 `ios/Pods` 文件夹，及 `ios/Podfile.lock` 文件，并执行如下命令，重新安装依赖

1. 搭载新款 Apple Silicon 的Mac设备，如 M1。
![](https://qcloudimg.tencent-cloud.cn/raw/dd87d8ff05aec0ecad461f12ef6c3020.png)

```shell
cd ios
sudo arch -x86_64 gem install ffi
arch -x86_64 pod install --repo-update
```

2. 搭载老款 Intel 芯片的 Mac 设备。

```shell
cd ios
sudo gem install ffi
pod install --repo-update
```

### 佩戴 Apple Watch 时，真机调试 iOS 报错怎么办？

![](https://qcloudimg.tencent-cloud.cn/raw/1ffcfe39a18329c86849d7d3b34b9a0e.png)

请将您的 Apple Watch 调整至飞行模式，并将 iPhone 的蓝牙功能通过 `设置 => 蓝牙` 彻底关闭。

重新启动 Xcode（若打开），并重新 `flutter run` 即可。

### Flutter 环境问题如何确认？

如您需得知 Flutter 的环境是否存在问题，请运行 Flutter doctor 检测 Flutter 环境是否装好。

### 使用 Flutter 自动生成的项目，引入 TUIKit 后，运行 Android 端报错怎么办？

![](https://qcloudimg.tencent-cloud.cn/raw/d95efdd4ae50f13f38f4c383ca755ae7.png)

1. 打开 `android\app\src\main\AndroidManifest.xml`，根据如下，补全 `xmlns:tools="http://schemas.android.com/tools"` / `android:label="@string/android_label"` 及 `tools:replace="android:label"`。
<dx-codeblock>
:::  xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="替换成您的 Android 端包名"
    xmlns:tools="http://schemas.android.com/tools">
    <application
        android:label="@string/android_label"
        tools:replace="android:label"
        android:icon="@mipmap/ic_launcher" // 指定一个 icon 路径
        android:usesCleartextTraffic="true"
        android:requestLegacyExternalStorage="true">
:::
</dx-codeblock>
2. 打开 `android\app\build.gradle`，补全 `defaultConfig` 中 `minSdkVersion` 及 `targetSdkVersion`。
<dx-codeblock>
:::  gradle
defaultConfig {
  applicationId "" // 替换成您的Android端包名
  minSdkVersion 21
  targetSdkVersion 30
}
:::
</dx-codeblock>

### 如果国际化界面语言？

国际化界面语言用法详情，或新增其他语言包，[可参考本文档](https://cloud.tencent.com/document/product/269/84481)。

### 如何获取 API 接口调用报错/Flutter 层报错/弹窗提示信息？[](id:callback)

请在初始化 TUIKit 时，挂载 `onTUIKitCallbackListener` 监听。

该监听用于返回包括：SDK API 错误 / Flutter 报错 / 一些可能需要弹窗提示用户的场景信息。

通过`TIMCallbackType`确定类型。

示例代码如下。您可以根据您的业务需要，修改以下代码，自定义提醒用户的逻辑，包括但不限于弹窗/横幅等。

```dart
final CoreServicesImpl _coreInstance = TIMUIKitCore.getInstance();

final isInitSuccess = await _coreInstance.init(
  onTUIKitCallbackListener: (TIMCallback callbackValue){
    switch(callbackValue.type) {
      case TIMCallbackType.INFO:
        // Shows the recommend text for info callback directly
        Utils.toast(callbackValue.infoRecommendText!);
        break;
      case TIMCallbackType.API_ERROR:
        //Prints the API error to console, and shows the error message.
        print("Error from TUIKit: ${callbackValue.errorMsg}, Code: ${callbackValue.errorCode}");
        if (callbackValue.errorCode == 10004 && callbackValue.errorMsg!.contains("not support @all")) {
            Utils.toast(imt("当前群组不支持@全体成员"));
        }else{
          Utils.toast(callbackValue.errorMsg ?? callbackValue.errorCode.toString());
        }
        break;
      case TIMCallbackType.FLUTTER_ERROR:
      default:
        // prints the stack trace to console or shows the catch error
        if(callbackValue.catchError != null){
          Utils.toast(callbackValue.catchError.toString());
        }else{
          print(callbackValue.stackTrace);
        }
    }
  },
);
```

下面，分别介绍这三种类型的回调：

#### SDK API 错误（`TIMCallbackType.API_ERROR`）

该场景下，提供 SDK API 原生`errorMsg`及`errorCode`。

[错误码请参考该文档](https://cloud.tencent.com/document/product/269/1671)

#### Flutter 报错（`TIMCallbackType.FLUTTER_ERROR`）

该错误由监听 Flutter 原生抛出异常产生，提供错误发生时的`stackTrace`(来自`FlutterError.onError`)或`catchError`(来自 try-catch)。

#### 场景信息（`TIMCallbackType.INFO`）

建议根据实际情况，将这些信息弹窗提示用户。

具体提示规则和弹窗样式可由您决定。

提供`infoCode`场景码帮助您确定当前的场景，及默认的提示推荐语`infoRecommendText`。

您可直接弹窗提示我们的推荐语，也可根据场景码自定义推荐语。推荐语语言使用系统语言语言或您指定的语言，请勿根据推荐语来判断场景。

**场景码规则如下：**

场景码由七位数组成，前五位数确定场景发生的组件，后两位确定具体的场景表现。

| 场景码开头 | 对应的组件             |
| ---------- | ---------------------- |
| 66601      | `TIMUIKitAddFriend`    |
| 66602      | `TIMUIKitAddGroup`     |
| 66603      | `TIMUIKitBlackList`    |
| 66604      | `TIMUIKitChat`         |
| 66605      | `TIMUIKitContact`      |
| 66606      | `TIMUIKitConversation` |
| 66607      | `TIMUIKitGroup`        |
| 66608      | `TIMUIKitGroupProfile` |
| 66609      | `TIMUIKitNewContact`   |
| 66610      | `TIMUIKitGroupProfile` |
| 66611      | `TIMUIKitNewContact`   |
| 66612      | `TIMUIKitProfile`      |
| 66613      | `TIMUIKitSearch`       |
| 66614      | 通用组件               |

**全部场景码清单如下：**[](id:infoCode)

| 场景码 `infoCode` | 推荐提示语 `infoRecommendText`                               | 场景描述                                                                    |
| ----------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------- |
| 6660101           | 好友申请已发送                                               | 用户申请添加其他用户为联系人                                                |
| 6660102           | 该用户已是好友                                               | 用户申请添加其他已是好友的用户为好友时，触发 `onTapAlreadyFriendsItem` 回调 |
| 6660201           | 群申请已发送                                                 | 用户申请加入需要管理员审批的群聊                                            |
| 6660202           | 您已是群成员                                                 | 用户申请加群时，判断用户已经是当前群成员，触发 `onTapExistGroup` 回调       |
| 6660401           | 无法定位到原消息                                             | 当用户需要跳转至@消息或者是引用消息时，在消息列表中查不到目标消息           |
| 6660402           | 视频保存成功                                                 | 用户在消息列表，点开视频消息后，选择保存视频                                |
| 6660403           | 视频保存失败                                                 | 用户在消息列表，点开视频消息后，选择保存视频                                |
| 6660404           | 说话时间太短                                                 | 用户发送了过短的语音消息                                                    |
| 6660405           | 发送失败,视频不能大于 100MB                                  | 用户试图发送大于 100MB 的视频                                               |
| 6660406           | 图片保存成功                                                 | 用户在消息列表，点开图片大图后，选择保存图片                                |
| 6660407           | 图片保存失败                                                 | 用户在消息列表，点开图片大图后，选择保存图片                                |
| 6660408           | 已复制                                                       | 用户在弹窗内选择复制文字消息                                                |
| 6660409           | 暂未实现                                                     | 用户在弹窗内选择非标功能                                                    |
| 6660410           | 其他文件正在接收中                                           | 用户点击下载文件消息时，前序下载任务还未完成                                |
| 6660411           | 正在接收中                                                   | 用户点击下载文件消息                                                        |
| 6660412           | 视频消息仅限 mp4 格式                                        | 用户发送了一条非 mp4 格式的视频消息                                         |
| 6660413           | 已加入待下载队列，其他文件下载中                                                   | 已加入待下载队列，其他文件下载中                                         |
| 6661001           | 无网络连接，无法修改                                         | 当用户试图在无网络环境下，修改群资料                                        |
| 6661002           | 无网络连接，无法查看群成员                                   | 当用户试图在无网络环境下，修改群资料                                        |
| 6661003           | 成功取消管理员身份                                           | 用户将群内其他用户移除管理员                                                |
| 6661201           | 无网络连接，无法修改                                         | 当用户试图在无网络环境下，修改自己或联系人的资料                            |
| 6661202           | 好友添加成功                                                 | 在资料页添加其他用户为好友，并自动添加成功，无需验证                        |
| 6661203           | 好友申请已发出                                               | 在资料页添加其他用户为好友，对方设置需要验证                                |
| 6661204           | 当前用户在黑名单                                             | 在资料页添加其他用户为好友，对方在自己的黑名单内                            |
| 6661205           | 好友添加失败                                                 | 在资料页添加其他用户为好友，添加失败，可能是由于对方禁止加好友              |
| 6661206           | 好友删除成功                                                 | 在资料页删除其他用户为好友，成功                                            |
| 6661207           | 好友删除失败                                                 | 在资料页删除其他用户为好友，失败                                            |
| 6661401           | 输入不能为空                                                 | 当用户在录入信息时，输入了空字符串                                          |
| 6661402           | 请传入离开群组生命周期函数，提供返回首页或其他页面的导航方法 | 用户退出群或解散群时，为提供返回首页办法                                    |
| 6661403           | 设备存储空间不足，建议清理，以获得更好使用体验               | 在login成功后，会自动检测设备存储空间，如果不足1GB，会提示存储空间不足      |

## 联系我们[](id:contact)

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)
