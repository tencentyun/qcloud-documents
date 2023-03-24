[](id:toc)
通过阅读本文，您可以了解集成 Flutter SDK 的方法。

## 环境要求

| 环境  | 版本 |
|---------|---------|
| Flutter | IM SDK 最低要求 Flutter 2.2.0版本，TUIKit 集成组件库最低要求 Flutter 2.10.0 版本。|
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 支持平台

我们致力于打造一套支持 Flutter 全平台的即时通信 IM SDK 及 TUIKit，帮助您一套代码，全平台运行。

| 平台 | 无 UI SDK ([tencent_cloud_chat_sdk](https://pub.dev/packages/tencent_cloud_chat_sdk)) | 含 UI 及基础业务逻辑 TUIKit ([tencent_cloud_chat_uikit](https://pub.dev/packages/tencent_cloud_chat_uikit)) |
|---------|---------|---------|
| iOS | 支持 | 支持 |
| Android | 支持 | 支持 |
| [Web](#web) | 支持，4.1.1+2版本起 | 支持，0.1.5版本起 |
| [macOS](#pc) | 支持，4.1.9版本起 | 支持，2.0.0 版本起 |
| [Windows](#pc) | 支持，4.1.9版本起 | 支持，2.0.0 版本起 |
| [混合开发](https://cloud.tencent.com/document/product/269/83153) （将 Flutter SDK 添加至现有原生应用） | 5.0.0版本起支持 | 1.0.0版本起支持 |

>? Web/macOS/Windows 平台需要简单的几步额外引入，详情请查看本文 [拓展更多平台](#more)。

## 体验 Demo

在开始接入前，您可以体验我们的 DEMO，快速了解腾讯云 IM Flutter 跨平台 SDK 及 TUIKit 的能力。

**以下各版本 DEMO，均由同一 Flutter 项目引入TUIKit 制作打包而成。** Desktop(macOS/Windows)平台，SDK 已支持，DEMO 将于近期上线。

<table style="text-align:center; vertical-align:middle; max-width: 800px">
  <tr>
    <th style="text-align:center;">移动端 APP</th>
    <th style="text-align:center;">WEB - H5</th>
  </tr>
  <tr>
    <td><div style="display: flex; justify-content: center; align-items: center; flex-direction: column; padding-top: 10px">iOS/Android APP，自动判断平台下载<img style="max-width:200px; margin: 20px 0 20px 0" src="https://qcloudimg.tencent-cloud.cn/raw/ca2aaff551410c74fce48008c771b9f6.png"/></div></td>
    <td><div style="display: flex; justify-content: center; align-items: center; flex-direction: column; padding-top: 10px">手机扫码体验在线Web版DEMO<img style="max-width:200px; margin: 20px 0 20px 0" src="https://qcloudimg.tencent-cloud.cn/raw/3c79e8bb16dd0eeab35e894a690e0444.png"/></div></td>
  </tr>
</table>

## 前序工作

1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 参照 [创建并升级应用](https://cloud.tencent.com/document/product/269/32577) 创建应用，并记录好 `SDKAppID`。
3. 在 [IM 控制台](https://console.cloud.tencent.com/im) 选择您的应用，在左侧导航栏依次点击 **辅助工具**->**UserSig 生成&校验** ，创建两个 UserID 及其对应的 UserSig，复制`UserID`、`签名（Key）`、`UserSig`这三个，后续登录时会用到。
![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

>? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是由服务器端生成，并提供面向 App 的接口，在需要 `UserSig` 时由 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

[](id:part2)

## 选择合适的方案集成 Flutter SDK

IM 提供了三种方式来集成，您可以选择最合适的方案来集成：

| 集成方式  | 适用场景 |
|---------|---------|
| [使用 DEMO 修改](#part3) | IM Demo 是一个完整的聊天 App，代码已开源，如果您需要实现聊天类似场景，可以使用 Demo 进行二次开发。 可立即 [体验 Demo](https://cloud.tencent.com/document/product/269/36852)。 |
| [含 UI 集成](#part4) | IM 的 UI 组件库`TUIKit`提供了通用的 UI 组件，例如会话列表、聊天界面和联系人列表等，开发者可根据实际业务需求通过该组件库快速地搭建自定义 IM 应用。**推荐优先使用该方案**。 |
| [自实现 UI 集成](#part5) | 如果 TUIKit 不能满足您应用的界面需求，或者您需要比较多的定制，可以使用该方案。 |

为帮助您更好的理解 IM SDK 的各 API，我们还提供了[API Example](https://github.com/TencentCloud/tc-chat-sdk-flutter/tree/main/example)，演示各 API 的调用及监听的触发。

[](id:part3)

## 方案一：使用 Demo 修改

### 跑通 Demo

1. 下载 Demo 源码、安装依赖：
```shell
# Clone the code
git clone https://github.com/TencentCloud/tc-chat-demo-flutter.git

# Install dependencies
flutter pub get
```
2. 运行 Demo 项目：
```shell
#启动demo项目，请替换SDK_APPID、KEY两个参数
flutter run --dart-define=SDK_APPID={YOUR_SDKAPPID} --dart-define=ISPRODUCT_ENV=false --dart-define=KEY={YOUR_KEY}
```
>?
>
>- `--dart-define=SDK_APPID={YOUR_SDKAPPID}` 其中`{YOUR_SDKAPPID}`需替换成您自己应用的 SDKAppID。
>- `--dart-define=ISPRODUCT_ENV=false` 对开发生产环境做判断，如您是开发环境请用 false。
>- `--dart-define=KEY={YOUR_KEY}` 其中`{YOUR_KEY}`需替换成 [第一部分：创建测试用户](#part1) 中的`密钥（Key）`信息。
>

#### 也可以使用 IDE 运行：（可选步骤）

<dx-tabs>
::: Android 平台[](id:android)
1. 在 Android Studio 中安装 Flutter 和 Dart 插件。
 - Mac 平台：打开插件设置（在 v3.6.3.0 以上的系统打开 Preferences > Plugins）=> 选择 Flutter 插件并点击 安装 => 当弹出安装 Dart 插件提示时，点击 Yes => 当弹出重新启动提示时，点击 Restart。
 - Linux 或者 Windows 平台：打开插件设置 (位于 File > Settings > Plugins)= > 选择 Marketplace (扩展商店)，选择 Flutter plugin 然后点击 Install (安装)。
![](https://qcloudimg.tencent-cloud.cn/raw/481bc19b55b40051daa8e669325cd123.png)
2. 打开项目并获取依赖。
在 Android Studio 中打开 `im-flutter-uikit` 目录。
![](https://qcloudimg.tencent-cloud.cn/raw/b22a52c14373a222f9bf55e79b04f12b.png)
并在该路径执行命令安装依赖。
```shell
flutter pub get
```
3. 配置环境变量。
在右上角运行按钮旁，鼠标单击 `main.dart`，配置 `Edit Configurations`。
![](https://qcloudimg.tencent-cloud.cn/raw/e2db56849e86dab8f6f0ccb4d3374fce.png)
在弹出窗口中，配置 `Additional run args`，输入环境变量（SDKAPPID等信息）。如：
```shell
# 请替换SDK_APPID、KEY两个参数
--dart-define=SDK_APPID={YOUR_SDKAPPID} --dart-define=ISPRODUCT_ENV=false --dart-define=KEY={YOUR_KEY}
```
![](https://qcloudimg.tencent-cloud.cn/raw/f022441399d2d6057b86e489593768ad.png)
4. 创建Android模拟器。
启动您刚安装好的模拟器，并选中其。
![](https://qcloudimg.tencent-cloud.cn/raw/e3aebdd2f6018c8f1fa10d5b5fb62c79.png)
单击界面右上角 Device Manager，完成 Create devices，创建模拟器。如果您需要使用 Google FCM 推送能力，建议最好安装支持 Google Play Store 的设备。
![](https://qcloudimg.tencent-cloud.cn/raw/9db005b86f9ffa1052826fe5e11d219a.png)
5. 运行项目。
根据需要，单击下图左侧 Run ，或右侧 Debug，以运行项目。
![](https://qcloudimg.tencent-cloud.cn/raw/7b0d4d008f71e1d0d805c9fb3a5de437.png)
>?UI 可能会有部分调整更新，请以最新版为准。
:::
::: iOS 平台[](id:ios)

1. 在 Xcode 中打开 `im-flutter-uikit/ios`目录。
![](https://qcloudimg.tencent-cloud.cn/raw/16b555ebe0c2caa77f13ac3b42b20a24.png)
2. 连接 iPhone 真机，单击 **Build And Run**，iOS 工程等待编译完成，会有新窗口弹出 Xcode 工程。
3. 打开 iOS 工程，设置主 Target 的 Signing & Capabilities（需要苹果开发者账号），让项目可以在 iPhone 真机上运行。
4. 启动项目，在真机上进行 Demo 的调试。
![](https://qcloudimg.tencent-cloud.cn/raw/911935cf419e4298edb45cd93bf10852.png)
:::
</dx-tabs>

#### Demo 代码结构概览

>? 我们 Demo 的 UI 及业务逻辑部分，使用 Flutter TUIKit。Demo 层本身仅用于构建 App，处理导航跳转及调用实例化 TUIKit 中各个组件。

|  文件夹  | 介绍 |
|---------|---------|
| lib | 程序核心目录 |
| lib/i18n | 国际化相关代码。这里的国际化，不包含 TUIKit 本身的国际化能力和国际化词条，您可按需引入 |
| lib/src | 项目主体目录 |
| lib/src/pages | 本 Demo 几个重点导航页。项目初始化完成后，由 `app.dart` 负责展示加载动画，并判断登录态，将用户引导至 `login.dart` 或 `home_page.dart`。用户登录后，会将登录信息通过 `shared_preference` 插件，存储至本地。以后每次启动应用，若在本地发现原来的登录信息，则自动使用该信息进行登录，若无或登录失败，则引导至登录页。自动登录过程中，用户还在 `app.dart` ，可看到加载动画。`home_page.dart`含一个底部 Tab，支撑本 Demo 的四个主功能页的切换。 |
| lib/utils | 一些工具函数类 |

基本上，`lib/src` 内每个 dart 文件引入了一个 TUIKit 组件，在文件内，实例化组件后，即可渲染页面。

主要文件如下：

|  lib/src 主要文件  | 文件介绍 |
|---------|---------|
| add_friend.dart | 申请添加好友页面，使用 `TIMUIKitAddFriend` 组件|
| add_group.dart | 申请入群页面，使用 `TIMUIKitAddGroup` 组件|
| blacklist.dart| 黑名单列表页面，使用 `TIMUIKitBlackList` 组件 |
| chat.dart | 主聊天页面，使用全套TUIKit聊天能力，使用 `TIMUIKitChat` 组件 |
| chatv2.dart | 主聊天页面，使用原子化能力，使用 `TIMUIKitChat` 组件 |
| contact.dart | 联系人页面 ，使用 `TIMUIKitContact` 组件|
| conversation.dart | 会话列表界面，使用 `TIMUIKitConversation` 组件 |
| create_group.dart | 发起群聊页面，纯Demo实现，未使用组件 |
| group_application_list.dart | 入群申请列表页面，使用 `TIMUIKitGroupApplicationList` 组件 |
| group_list.dart | 群列表页面，使用 `TIMUIKitGroup` 组件  |
| group_profile.dart | 群资料及群管理页面，使用 `TIMUIKitGroupProfile` 组件 |
| newContact.dart | 联系人好友申请页面，使用 `TIMUIKitNewContact` 组件 |
| routes.dart | Demo 的路由，导航至登录页 `login.dart` 或主页面 `home_page.dart`。 |
| search.dart | 全局搜索及会话内搜索页面，使用 `TIMUIKitSearch`（全局搜索） 及 `TIMUIKitSearchMsgDetail`（会话内搜索） 组件 |
| user_profile.dart | 用户信息及关系链维护页面，使用 `TIMUIKitProfile` 组件|

大部分 TUIKit 组件需要传入导航跳转方法，因此需要 Demo 层处理 `Navigator` 。

以上介绍了我们的 Demo，您可以直接直接修改它二次开发，或参照它实现您的业务需求。

[](id:part4)

## 方案二：含 UI 集成，使用 TUIKit 组件库，半天完成 IM 能力植入

TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，它提供了一些通用的 UI 组件，例如会话列表、聊天界面和联系人列表等，开发者可根据实际业务需求通过该组件库快速地搭建自定义 IM 应用。参见 [TUIKit 图文介绍](https://cloud.tencent.com/document/product/269/70747)。

本部分为快速使用 TUIKit 介绍，详细入门指引可参见 [TUIKit 集成基础功能](https://cloud.tencent.com/document/product/269/70746)。

![](https://qcloudimg.tencent-cloud.cn/raw/f140dd76be01a65abfb7e6ba2bf50ed5.png)

### 前提条件

您已经完成创建 Flutter 项目，或有可以基于的 Flutter 项目。

### 接入步骤

#### 配置权限

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

#### 初始化

1. 在您应用启动时，初始化 TUIKit。
2. 请务必保证先执行 [`TIMUIKitCore.getInstance()`](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitCore/getInstance.html) ，再调用初始化函数 [`init()`](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitCore/init.html) ，并将您的`sdkAppID`传入。
3. 为方便您获取API报错及建议提醒用户的提示语，此处建议挂载一个 onTUIKitCallbackListener 监听，[详见此部分](https://cloud.tencent.com/document/product/269/70746#onTUIKitCallbackListener)。

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
     onTUIKitCallbackListener:  (TIMCallback callbackValue){}, // [建议配置，详见此部分](https://cloud.tencent.com/document/product/269/70746#onTUIKitCallbackListener)
     listener: V2TimSDKListener());
   super.initState();
 }
}
```

>?请在本步骤 await 初始化完成后，才可执行后续步骤。

#### 登录测试账户

1. 此时，您可以使用最开始的时候，在控制台生成的测试账户，完成登录验证。
2. 调用 [`_coreInstance.login`](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitCore/login.html) 方法，登录一个测试账户。

```dart
import 'package:tencent_cloud_chat_uikit/tencent_cloud_chat_uikit.dart';

final CoreServicesImpl _coreInstance = TIMUIKitCore.getInstance();
_coreInstance.login(userID: userID, userSig: userSig);
```

>? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是由服务器端生成，并提供面向 App 的接口，在需要 `UserSig` 时由 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

#### 实现：会话列表页面

您可以以会话列表作为您的 IM 功能首页，其涵盖了与所有有聊天记录的用户及群聊的会话。

<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/279da6d5d41ec1ce0b0cf7fca9a697b8.jpg" />

请创建一个 `Conversation` 类，`body` 中使用 [`TIMUIKitConversation`](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitConversation/) 组件，渲染会话列表。

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

#### 实现：会话聊天页面

该页面由顶部主体聊天历史记录及底部发送消息模块组成。
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/0c361254fa5117f7580f39e8b523e472.png" />

请创建一个 `Chat` 类，`body` 中使用 [`TIMUIKitChat`](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitChat/) 组件，渲染聊天页面。

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

#### 实现：用户详情页面

该页面默认，可在只传入一个 `userID` 的情况下，自动根据是否是好友，生成用户详情页。

请创建一个 `UserProfile` 类，`body` 中使用 [`TIMUIKitProfile`](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitProfile/) 组件，渲染用户详情及关系链页面。

>? 如果您希望自定义该页面，请优先考虑使用 [`profileWidgetBuilder`](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitProfile/ProfileWidgetBuilder.html) 传入需自定义的profile组件并配合 `profileWidgetsOrder` 确定纵向排列顺序；如果无法满足，才可使用 `builder` 。

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



#### 更多能力

您还可以继续使用以下 TUIKit 插件快速实现完整 IM 功能。

- [TIMUIKitContact](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitContact/)：联系人列表页面。
- [TIMUIKitGroupProfile](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitGroupProfile/)：群资料页面，使用方式与 `TIMUIKitProfile` 基本一致。
- [TIMUIKitGroup](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitGroup/): 群列表界面。
- [TIMUIKitBlackList](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitBlackList/)：黑名单列表界面。
- [TIMUIKitNewContact](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/TIMUIKitNewContact/)：联系人（好友）申请列表。如需在外部显示小红点，可使用 `TIMUIKitUnreadCount` 小红点组件，其会自动挂载监听。
- [本地搜索](https://cloud.tencent.com/document/product/269/79121)：`TIMUIKitSearch` 全局搜索组件，支持全局搜索联系人/群组/聊天记录，也支持使用 `TIMUIKitSearchMsgDetail` 在特定会话中搜索聊天记录。两种模式取决于是否传入 `conversation`。

UI 组件全貌可参见 [本图文概览](https://cloud.tencent.com/document/product/269/70747) 或 [详细文档](https://comm.qq.com/im/doc/flutter/uikit-sdk-api/)。

[](id:part5)

## 方案三：自实现 UI 集成

### 前提条件

您已经完成创建 Flutter 项目，或有可以基于的 Flutter 项目。

### 接入步骤

#### 安装 IM SDK

[本节详细文档](https://cloud.tencent.com/document/product/269/75286)

使用如下命令，安装 Flutter IM SDK 最新版本。

在命令行执行：

```shell
flutter pub add tencent_cloud_chat_sdk
```

>?
> 如果您的项目还同时需要用于 [Web](#web) 或 [桌面端(macOS、Windows)](#pc)，一些额外的步骤是需要的，具体情况各自的链接。

#### 完成 SDK 初始化

[本节详细文档](https://cloud.tencent.com/document/product/269/75293)

调用`initSDK`，完成 SDK 初始化。

将您的 `sdkAppID` 传入。

```Dart
import 'package:tencent_cloud_chat_sdk/enum/V2TimSDKListener.dart';
import 'package:tencent_cloud_chat_sdk/enum/log_level_enum.dart';
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';
TencentImSDKPlugin.v2TIMManager.initSDK(
  sdkAppID: 0, // Replace 0 with the SDKAppID of your IM application when integrating
  loglevel: LogLevelEnum.V2TIM_LOG_DEBUG, // Log
  listener: V2TimSDKListener(),
);
```

在本步骤，您可以针对 IM SDK 挂载一些监听，主要包括网络状态及用户信息变更等，详情可参见 [该文档](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimSDKListener/V2TimSDKListener-class.html)。

#### 登录测试账户

[本节详细文档](https://cloud.tencent.com/document/product/269/75296)

此时，您可以使用最开始的时候，在控制台生成的测试账户，完成登录验证。

调用`TencentImSDKPlugin.v2TIMManager.login`方法，登录一个测试账户。

当返回值`res.code`为0时，登录成功。

```dart
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';
V2TimCallback res = await TencentImSDKPlugin.v2TIMManager.login(
  userID: userID,
  userSig: userSig,
);
```

>? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是将 `UserSig` 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 `UserSig` 时由您的 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

#### 发送消息

[本节详细文档](https://cloud.tencent.com/document/product/269/75317)

此处以发送文本消息举例，其流程为：

1. 调用 `createTextMessage(String)`创建一个文本消息。
2. 根据其返回值，拿到消息 ID。
3. 调用 `sendMessage()` 发送该ID的消息。`receiver`可填入您此前创建的另一个测试账户 ID。发送单聊消息无需填入`groupID`。

代码示例：

```dart
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';

V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
      await TencentImSDKPlugin.v2TIMManager
          .getMessageManager()
          .createTextMessage(text: "The text to create");

String id = createMessage.data!.id!; // The message creation ID

V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin.v2TIMManager
      .getMessageManager()
      .sendMessage(
          id: id, // Pass in the message creation ID to
          receiver: "The userID of the destination user",
          groupID: "The groupID of the destination group",
          );
```

>?如果发送失败，可能是由于您的 sdkAppID 不支持陌生人发送消息，您可至控制台开启，用于测试。
>
> [请单击此链接](https://console.cloud.tencent.com/im/login-message)，关闭好友关系链检查。

#### 获取会话列表

[本节详细文档](https://cloud.tencent.com/document/product/269/75368)

在上一个步骤中，完成发送测试消息，现在可登录另一个测试账户，拉取会话列表。
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/e2fdd7632ebc0c5cde68c91afa914201.jpg" />

获取会话列表的方式有两种：

1. 监听长连接回调，实时更新会话列表。
2. 请求 API，根据分页一次性获取会话列表。

常见应用场景为：

在启动应用程序后立即获取会话列表，然后监听长连接以实时更新会话列表的变化。

##### 一次性请求会话列表

为了获取会话列表，需要维护`nextSeq`，记录当前位置。

```dart
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';

String nextSeq = "0";

getConversationList() async {
  V2TimValueCallback<V2TimConversationResult> res = await TencentImSDKPlugin
      .v2TIMManager
      .getConversationManager()
      .getConversationList(nextSeq: nextSeq, count: 10);

  nextSeq = res.data?.nextSeq ?? "0";
}
```

此时，您可以看到您在上一步中，使用另一个测试账号，发来消息的会话。

##### 监听长链接实时获取会话列表

您在此步骤中，需要先在 SDK 上挂载监听，然后处理回调事件，更新 UI。

1. 挂载监听。
```dart
await TencentImSDKPlugin.v2TIMManager
      .getConversationManager()
      .setConversationListener(
        listener: new V2TimConversationListener(
          onConversationChanged: (List<V2TimConversation> list){
            _onConversationListChanged(list);
    },
          onNewConversation:(List<V2TimConversation> list){
            _onConversationListChanged(list);
    },
```
2. 处理回调事件，将最新的会话列表展示在界面上。
```dart
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';

List<V2TimConversation> _conversationList = [];

_onConversationListChanged(List<V2TimConversation> list) {
  for (int element = 0; element < list.length; element++) {
    int index = _conversationList.indexWhere(
        (item) => item!.conversationID == list[element].conversationID);
    if (index > -1) {
      _conversationList.setAll(index, [list[element]]);
    } else {
      _conversationList.add(list[element]);
    }
  }
```

#### 接收消息

[本节详细文档](https://cloud.tencent.com/document/product/269/75320)

通过腾讯云 IM Ffltter SDK 接收消息有两种方式：

1. 监听长连接回调，实时获取消息变化，更新渲染历史消息列表。
2. 请求 API，根据分页一次性获取历史消息。

常见应用场景为：

1. 界面进入新的会话后，首先一次性请求一定数量的历史消息，用于展示历史消息列表。
2. 监听长链接，实时接收新的消息，将其添加进历史消息列表中。

##### 一次性请求历史消息列表

每页拉取的消息数量不能太大，否则会影响拉取速度。建议此处设置为20左右。

您应该动态记录当前页数，用于下一轮请求。

示例代码如下：

```dart
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';

  V2TimValueCallback<List<V2TimMessage>> res = await TencentImSDKPlugin
      .v2TIMManager
      .getMessageManager()
      .getGroupHistoryMessageList(
        groupID: "groupID",
        count: 20,
        lastMsgID: "",
      );

  List<V2TimMessage> msgList = res.data ?? [];

  // here you can use msgList to render your message list
    }
```

##### 监听长链接实时获取新消息

历史消息列表初始化后，新消息来自长链接 `V2TimAdvancedMsgListener.onRecvNewMessage`。

`onRecvNewMessage`回调被触发后，您可以按需将新消息添加进历史消息列表中。

绑定监听器示例代码如下：

```dart
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';

final adVancesMsgListener = V2TimAdvancedMsgListener(
onRecvNewMessage: (V2TimMessage newMsg) {
  _onReceiveNewMsg(newMsg);
},
/// ... other listeners related to message
);

TencentImSDKPlugin.v2TIMManager
    .getMessageManager()
    .addAdvancedMsgListener(listener: adVancesMsgListener);
```

此时，您已基本完成 IM 模块开发，可以发送接收消息，也可以进入不同的会话。

您可以继续完成 [群组](https://cloud.tencent.com/document/product/269/75697)，[用户资料](https://cloud.tencent.com/document/product/269/75418)，[关系链](https://cloud.tencent.com/document/product/269/75421)，[离线推送](https://cloud.tencent.com/document/product/269/75430)，[本地搜索](https://cloud.tencent.com/document/product/269/75438) 等相关功能开发。

详情可查看 [自实现 UI 集成 SDK 文档](https://cloud.tencent.com/document/product/269/75260)。

## 高阶功能集成

### 使用更多插件丰富 Flutter IM 使用体验

除 SDK 及 TUIKit 本体基础功能外，我们还提供了四个选装插件，帮助您丰富 IM 能力。

- [消息推送插件](https://cloud.tencent.com/document/product/269/74605)：支持厂商原生离线推送能力及在线推送能力，并支持推送您的其他业务消息，帮助您提高消息触达率。
- [音视频通话插件](https://cloud.tencent.com/document/product/269/72485)：支持类似微信的 一对一/群组 音视频 通话。
- [地理位置消息插件](https://cloud.tencent.com/document/product/269/80881)：提供选取位置/发送位置及解析展示位置消息的能力。
- [自定义表情插件](https://cloud.tencent.com/document/product/269/80882)：TUIKit0.1.5版本后，无自带表情包，需要使用此插件，快速简便集成表情能力。支持 Emoji Unicode 编码及自定义图片表情。集成代码可参考我们的 [Demo](https://github.com/TencentCloud/tc-chat-demo-flutter/blob/main/lib/src/pages/app.dart)。

>?如果您有好的想法及建议，欢迎随时 [联系我们](https://cloud.tencent.com/online-service?from=doc_269&source=PRESALE)。

[](id:more)

## 拓展更多平台

腾讯云IM for Flutter 相关SDK默认支持 Android / iOS平台， 如果您需要拓展更多平台（ Web/Desktop ），请参考本部分。

### Flutter for Web支持[](id:web)

我们的 SDK，TUIKit(tencent_cloud_chat_uikit) 0.1.5版本，无 UI SDK(tencent_cloud_chat_sdk) 4.1.1+2 版本起，可完美兼容 Web 端。

相比 Android 和 iOS 端，需要一些额外步骤。如下：

#### 升级 Flutter 3.x 版本

Flutter 3.x 版本 针对 Web 性能做了较多优化，强烈建议您使用其来开发 Flutter Web 项目。

#### 引入 Flutter for Web 增补SDK

```dart
flutter pub add tencent_im_sdk_plugin_web
```

#### 引入 JS

>?如果您现有的 Flutter 项目不支持 Web，请在项目根目录下运行 `flutter create .` 添加 Web 支持。
>

进入您项目的 `web/` 目录，使用 `npm` 或 `yarn` 安装相关JS依赖。初始化项目时，根据屏幕指引，进行即可。

```shell
cd web

npm init

npm i tim-js-sdk

npm i tim-upload-plugin
```

打开 `web/index.html` ，在 `<head> </head>` 间引入这JS文件。如下：

```html
<script src="./node_modules/tim-upload-plugin/index.js"></script>
<script src="./node_modules/tim-js-sdk/tim-js-friendship.js"></script>
```

![](https://qcloudimg.tencent-cloud.cn/raw/a4d25e02c546e0878ba59fcda87f9c76.png)

### Flutter for Desktop(PC) 支持[](id:pc)

我们的无 UI SDK(tencent_cloud_chat_sdk) 4.1.9 版本起，可完美兼容 macOS、Windows 端。相比 Android 和 iOS 端，需要一些额外步骤。如下：

#### 升级 Flutter 3.x 版本

从 Flutter 3.0 版本起，才可用于打包 desktop 端，因此，如需使用，请升级至 Flutter 3.x 版本。

#### 引入 Flutter for Desktop 增补 SDK

```dart
flutter pub add tencent_im_sdk_plugin_desktop
```

#### macOS修改

打开 `macos/Runner/DebugProfile.entitlements` 文件。

在 `<dict></dict>` 中，加入如下 `key-value` 键值对。

```
<key>com.apple.security.app-sandbox</key>
<false/>
```

## 可选操作：开通内容审核功能
在消息发送、资料修改场景中，很有可能会扩散不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。


## 常见问题

### iOS 端 Pods 依赖无法安装成功

#### **尝试方案一：**配置运行后，如果报错，可以单击 **Product** > **Clean Build Folder**，清除产物后重新 `pod install` 或 `flutter run`

![](https://qcloudimg.tencent-cloud.cn/raw/d495b2e8be86dac4b430e8f46a15cef4.png)

#### **尝试方案二：**手动删除 `ios/Pods` 文件夹，及 `ios/Podfile.lock` 文件，并执行如下命令，重新安装依赖

1. 搭载新款 Apple Silicon 的 Mac 设备，如 M1。
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

### 佩戴 Apple Watch 时，真机调试 iOS 报错

![](https://qcloudimg.tencent-cloud.cn/raw/1ffcfe39a18329c86849d7d3b34b9a0e.png)

请将您的 Apple Watch 调整至飞行模式，并将 iPhone 的蓝牙功能通过 `设置 => 蓝牙` 彻底关闭。

重新启动 Xcode（若打开），并重新 `flutter run` 即可。

### Flutter 环境问题

如您需得知 Flutter 的环境是否存在问题，请运行 Flutter doctor 检测 Flutter 环境是否装好。

### 使用 Flutter 自动生成的项目，引入TUIKit 后，运行 Android 端报错

![](https://qcloudimg.tencent-cloud.cn/raw/d95efdd4ae50f13f38f4c383ca755ae7.png)

1. 打开 `android\app\src\main\AndroidManifest.xml`，根据如下，补全 `xmlns:tools="http://schemas.android.com/tools"` / `android:label="@string/android_label"` 及 `tools:replace="android:label"`。
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="替换成您的 Android 端包名"
    xmlns:tools="http://schemas.android.com/tools">
    <application
        android:label="@string/android_label"
        tools:replace="android:label"
        android:icon="@mipmap/ic_launcher" // 指定一个 icon 路径
        android:usesCleartextTraffic="true"
        android:requestLegacyExternalStorage="true">
```
2. 打开 `android\app\build.gradle`，补全 `defaultConfig` 中 `minSdkVersion` 及 `targetSdkVersion`。
```gradle
defaultConfig {
  applicationId "" // 替换成您的Android端包名
  minSdkVersion 21
  targetSdkVersion 30
}
```

### 错误码如何查询？

- IM SDK 的 API 层面错误码，请查看 [该文档](https://cloud.tencent.com/document/product/269/1671)。
- TUIKit 的场景码，用于界面弹窗提示，通过 [onTUIKitCallbackListener 监听](https://cloud.tencent.com/document/product/269/70746#callback) 获得。全部场景码清单，请查看 [该文档](https://cloud.tencent.com/document/product/269/70746#infoCode)。

## 联系我们

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)
