
通过阅读本文，您可以了解在您现有的 Android / iOS 原生开发项目中，集成腾讯云 IM Flutter 的方法。

有的时候，使用 Flutter 重写您现有的应用程序是不现实的。如果您想在现有 APP 中，使用腾讯云 IM 的能力，推荐采用混合开发方案，即将 Flutter 模块，嵌入您的原生开发 APP 项目中。

**可在很大程度上，降低您的工作量，快速在双端原生 APP 中，植入 IM 通信能力。**

![](https://qcloudimg.tencent-cloud.cn/raw/54adc2b0587f9f30d56e96eb6461b969.png)

## 环境要求

| 环境  | 版本 |
|---------|---------|
| Flutter | SDK 最低要求 Flutter 2.2.0版本，TUIKit 集成组件库最低要求 Flutter 2.10.0 版本。|
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|
|腾讯云IM SDK|[tencent_cloud_chat_sdk](https://pub.dev/packages/tencent_cloud_chat_sdk) 5.0 及以上版本， [tencent_cloud_chat_uikit](https://pub.dev/packages/tencent_cloud_chat_uikit) 1.0 及以上版本。|

## 快速了解

<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/3856-67266?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

>?对于以上的 Demo 项目，源代码可在我们的 [GitHub 仓库](https://github.com/TencentCloud/tencentchat-add-flutter-to-app) 中找到，欢迎查阅。

## 前置知识点

开始之前，您需要了解腾讯云 IM Flutter SDK 及 TUIKit 的用法，及 Flutter-原生混合开发原理。

### 前序工作

1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 参照 [创建并升级应用](https://cloud.tencent.com/document/product/269/32577) 创建应用，并记录好 `SDKAppID`。
3. 在 [IM 控制台](https://console.cloud.tencent.com/im) 选择您的应用，在左侧导航栏依次点击 **辅助工具**->**UserSig 生成&校验** ，创建两个 UserID 及其对应的 UserSig，复制`UserID`、`签名（Key）`、`UserSig`这三个，后续登录时会用到。
![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

>? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是由服务器端生成，并提供面向 App 的接口，在需要 `UserSig` 时由 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

### 腾讯云 IM

#### 总体入门

在开始前，您首先需要了解腾讯云 IM Flutter 的 SDK 构成及使用方式。

主要包括两个 SDK：[无 UI 版本](https://cloud.tencent.com/document/product/269/68823#.E7.AC.AC.E4.BA.94.E9.83.A8.E5.88.86.EF.BC.9A.E8.87.AA.E5.AE.9E.E7.8E.B0-ui-.E9.9B.86.E6.88.90) 及[含UI组件库](https://cloud.tencent.com/document/product/269/70747)。本文将以 [含UI组件库（TUIKit）](https://cloud.tencent.com/document/product/269/70747) 为例，介绍混合开发方案。

**关于腾讯云 IM Flutter 详细用法，可从我们的 [快速入门文档](https://cloud.tencent.com/document/product/269/68823) 看起。**

[](id:modules)

#### 两个模块

腾讯云 IM 主要有两个部分，包括 Chat 聊天模块 和 Call 通话模块。

- Chat 聊天模块主要包括消息收发、会话管理、用户关系管理等。
- Call 通话模块主要包括音视频通话，包括一对一通话和群组多人通话。

### Flutter 混合开发

核心原理是，将 module 形式的 Flutter 项目，打包成 Native 端的可执行程序，嵌入 Native 项目中。因 Flutter module 可以通用，因此仅需编写一次 Flutter module，即可嵌入 Android/iOS APP 中。

当您现有应用需要展示腾讯云IM相关页面时，可加载对应用于承载 Flutter 的 Activity（Android）或 ViewController（iOS）。

当需要两端通信时，如传递当前用户信息，传递音视频通话数据，触发离线推送数据，可采用 [Method Channel](https://docs.flutter.dev/development/platform-integration/platform-channels#channels-and-platform-threading) 方式进行。触发另一端的方法使用 `invokeMethod`，监听另一端发来的方法调用使用 [预挂载的 Method Channel 监听器](https://docs.flutter.dev/development/platform-integration/platform-channels#executing-channel-handlers-on-background-threads)。

[](id:android)

#### 将 Flutter 模块添加至 Android 项目中

[详细学习](https://docs.flutter.dev/development/add-to-app/android/project-setup)

将 Flutter module 添加为 Gradle 中现有应用程序的依赖项。有两种方式可以实现这一点。

##### Android方式一：依赖 Android Archive (AAR)

AAR 机制创建通用的 Android AAR 作为打包 Flutter module 的中介。如果您经常构建，它会增加一个构建步骤。

该选项将 Flutter 库打包为由 AAR 和 POMS 构件组成的通用本地 Maven 存储库。此选项允许您的团队在不安装 Flutter SDK 的情况下构建主机应用程序。然后，您可以从本地或远程存储库中分发构件。

因此，建议在线上生产环境，使用本方案。

**具体步骤:**

1. 在您的Flutter module中，运行：
```shell
flutter build aar
```
2. 然后，按照屏幕上的说明进行集成。
![](https://qcloudimg.tencent-cloud.cn/raw/32e9376de02da10e97a8c54b9ab2b51c.png)
3. 您的应用程序现在将 Flutter 模块作为依赖项包括在内。

##### Android 方式二：依赖Flutter module源代码

源代码子项目机制是一个方便的一键构建过程，但需要 Flutter SDK。这是 Android Studio IDE 插件使用的机制。

此方式可为您的 Android 项目和 Flutter 项目实现一步构建。当您同时处理两个部分并快速迭代时，此选项很方便，但您的团队必须安装 Flutter SDK 才能构建应用程序。

因此，建议在开发测试环境，使用本方案。

**具体步骤:**

1. 将 Flutter module 作为一个子项目，添加至宿主 APP 的 `settings.gradle` 中：
```gradle
// Include the host app project.
include ':app'                                    // assumed existing content
setBinding(new Binding([gradle: this]))                                // new
evaluate(new File(                                                     // new
  settingsDir.parentFile,                                              // new
  'tencent_chat_module/.android/include_flutter.groovy'                // new
))                                                                     // new
```
2. 在您应用中的 `app/build.gradle => dependencies` 中引入对Flutter module的 `implementation`：
```gradle
dependencies {
  implementation project(':flutter')
}
```
3. 您的应用程序现在将Flutter模块作为依赖项包括在内。

[](id:ios)

#### 将 Flutter 模块添加至 iOS 项目中

[详细学习](https://docs.flutter.dev/development/add-to-app/ios/project-setup#embed-the-flutter-module-in-your-existing-application)

有两种方法可以在现有应用程序中嵌入 Flutter。

##### iOS方式一：嵌入 CocoaPods 和 Flutter SDK 集成

使用 CocoaPods 依赖项管理器并安装 Flutter SDK。这种方法要求每个从事项目工作的开发人员都有一个本地安装的 Flutter SDK 版本。

只需在 Xcode 中构建您的应用程序，即可自动运行脚本来嵌入您的 DART 和插件代码。这允许快速迭代最新版本的颤振模块，而无需在 Xcode 之外运行其他命令。

因此，建议在开发测试环境，使用本方案。

**具体步骤:**

1. 将以下代码添加到 Podfile 中：
```
// 上一步构建的Flutter Module的路径
flutter_chat_application_path = '../tencent_chat_module'

load File.join(flutter_chat_application_path, '.ios', 'Flutter', 'podhelper.rb')
```
2. 对于每个需要嵌入 Flutter 的 [Podfile target](https://guides.cocoapods.org/syntax/podfile.html#target)，调用 `install_all_flutter_pods(flutter_chat_application_path)`。
```
target 'MyApp' do
  install_all_flutter_pods(flutter_chat_application_path)
end
```
3. 在 Podfile 的 `post_install` 块中，调用 `flutter_post_install(installer)`，并完成 [腾讯云IM TUIKit](https://cloud.tencent.com/document/product/269/70747) 所需的权限声明，包括麦克风权限/相机权限/相册权限。
```
post_install do |installer|
  flutter_post_install(installer) if defined?(flutter_post_install)
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
执行 `pod install`。
> ?
>
> - 在 `tencent_chat_module/pubspec.yaml` 中更改Flutter插件依赖时，请在Flutter Module目录中运行 `flutter pub get` 以刷新 `podhelper.rb` 脚本读取的插件列表。然后，从您iOS应用程序的根目录，再次执行 `pod install`。
> - 对于 Apple Silicon 芯片 arm64 架构的 Mac电脑，可能需要执行 `arch -x86_64 pod install --repo-update`。
>
> `podhelper.rb` 脚本将您的插件 / `Flutter.framework` / `App.framework` 植入您的项目中。

##### iOS 方式二：在 Xcode 中嵌入 frameworks

为 Flutter 引擎、已编译的 DART 代码和所有 Flutter 插件创建框架。手动嵌入框架，并在 Xcode 中更新现有应用程序的构建设置。

通过手动编辑现有的 Xcode 项目，您可以生成必要的 framework 并将它们嵌入到应用程序中。如果您的团队成员无法在本地安装 Flutter SDK 和 CocoaPods，或者如果您不想在现有应用程序中使用 CocoaPods 作为依赖项管理器，则可以这样做。每次您在您的颤动模块中修改代码时，您都必须运行 `flutter build ios-framework`.

因此，建议在线上环境，使用本方案。

**具体步骤:**

1. 在您的Flutter module中，运行如下代码。下面的示例，假设您想要将framework生成到 `some/path/MyApp/Flutter/`。
```shell
flutter build ios-framework --output=some/path/MyApp/Flutter/
```
2. 在 Xcode 中将生成的 frameworks 集成到您的既有应用中。例如，您可以在 `some/path/MyApp/Flutter/Release/` 目录拖拽 frameworks 到您的应用 target 编译设置的 General > Frameworks, Libraries, and Embedded Content 下，然后在 Embed 下拉列表中选择 “Embed & Sign”。

## 混合开发选型

我们推荐您使用 Flutter Module 方式进行混合开发集成。

在 Native 原生项目中，构建 Flutter 引擎，来承载 Flutter 中的 Chat 及 Call 模块。有关两个模块的介绍，[请看此处](#modules)。

对于 Flutter 引擎的创建管理，目前两种方式：单 Flutter 引擎及多 Flutter 引擎。

| 引擎模式 | 介绍 | 优点 | 缺点 | Demo 源码下载 |
|---------|---------|---------|---------|---------|
| [Flutter单引擎](#single) | Chat 模块和 Call 模块在同一个 Flutter 引擎中承载。 | 方便，所有 Flutter 代码统一维护。 | 由于 Call 插件，在有电话呼入时，需要自动展示来电页面。如果在同一个引擎中，需要强制跳转至 Flutter 所在页面，体验较差。 | [点击下载](https://github.com/TencentCloud/tencentchat-add-flutter-to-app/tree/main/Single%20Flutter%20Engines) |
| [Flutter多引擎](#multiple) | Chat 模块和 Call 模块分别承载于不同的 Flutter 引擎中，使用 Flutter 引擎组来统一管理这两个引擎。 | Call 插件独立存在于一个 Flutter 引擎中，独立页面控制，来电时，直接将该页面弹窗即可，不影响用户当前所在页面，体验较好。 | 通话模块无法最小化成浮窗形式。 | [点击下载](https://github.com/TencentCloud/tencentchat-add-flutter-to-app/tree/main/Multiple%20Flutter%20Engines) |

此外，我们还提供，将腾讯云 IM Native SDK 与 Flutter SDK 结合使用的方案，[适用场景和步骤介绍可查看这里](#native)。[Demo 源码下载](https://github.com/TencentCloud/tencentchat-add-flutter-to-app/tree/main/Initialize%20from%20Native)。

[](id:multiple)

## 方案一：Flutter 多引擎方案（推荐）

本方案中，Chat 和 Call 模块分别独立于不同的Flutter引擎。

使用多个 Flutter 引擎的优点是，每个实例都是独立的，并维护其自己的内部导航堆栈、UI和应用程序状态。这简化了整个应用程序代码的状态保持责任，并提高了模块化能力。

![](https://qcloudimg.tencent-cloud.cn/raw/912d986a5ff57606422455a273a033f3.png)

在 Android 和 iOS 上添加多个 Flutter 引擎，主要基于一个 FlutterEngineGroup 类(Android API、iOS API)来构造并管理多个 FlutterEngine（Flutter 引擎）。

在我们的项目中，我们基于一个统一的 FlutterEngineGroup，来管理两个 FlutterEngine（Flutter 引擎），分别用于承载 Chat 和 Calling 模块。

<a target="_blank" href="https://github.com/TencentCloud/tencentchat-add-flutter-to-app/tree/main/Multiple%20Flutter%20Engines"><img src="https://qcloudimg.tencent-cloud.cn/raw/b622951f776a505e83f843de1f62fffc.png" /></a>

### Flutter Module 开发

要将 Flutter 嵌入到现有应用程序中，请首先创建一个 Flutter 模块。

在您项目的根目录外层，运行

```
cd some/path/
flutter create --template module tencent_chat_module
```

这会在 some/path/tencent_chat_module/ 创建一个 Flutter 模块项目。 在该目录中，您可以运行与在任何其他 Flutter 项目中相同的 Flutter 命令，例如 `flutter run --debug` 或 `flutter build ios`。 您还可以使用 Flutter 和 Dart 插件在 Android Studio, IntelliJ 或 VS Code 中运行该模块。 该项目在嵌入到现有应用程序之前包含模块的单视图示例版本，这对于测试代码的仅 Flutter 部分很有用。

`tencent_chat_module` 模块目录结构类似于普通的 Flutter 应用程序：

```
tencent_chat_module/
├── .ios/
│   ├── Runner.xcworkspace
│   └── Flutter/podhelper.rb
├── lib/
│   └── main.dart
├── test/
└── pubspec.yaml
```

现在，我们可以在 `lib/` 中，编写代码了。

#### 梳理 Flutter lib 目录

>?以下代码结构，仅供参考，您可根据需要灵活组织，以引入腾讯云 IM Flutter。

在 `lib/` 我们创建三个目录，`call`, `chat`, `common`。分别用于放置通话引擎，IM引擎，及通用model类。

```
tencent_chat_module/
├── lib/
│   └── call/
│   └── chat/
│   └── common/
```

#### 通用 model 类模块

新建 `common/common_model.dart` 文件，如下所示，新建两个class，用于定义Flutter与原生应用通信规范。

```dart
class ChatInfo {
  String? sdkappid;
  String? userSig;
  String? userID;

  ChatInfo.fromJSON(Map<String, dynamic> json) {
    sdkappid = json["sdkappid"].toString();
    userSig = json["userSig"].toString();
    userID = json["userID"].toString();
  }

  Map<String, String> toMap(){
    final Map<String, String> map = {};
    if(sdkappid != null){
      map["sdkappid"] = sdkappid!;
    }
    if(userSig != null){
      map["userSig"] = userSig!;
    }
    if(userID != null){
      map["userID"] = userID!;
    }
    return map;
  }
}

class CallInfo{
  String? userID;
  String? groupID;

  CallInfo();

  CallInfo.fromJSON(Map<String, dynamic> json) {
    groupID = json["groupID"].toString();
    userID = json["userID"].toString();
  }

  Map<String, String> toMap(){
    final Map<String, String> map = {};
    if(userID != null){
      map["userID"] = userID!;
    }
    if(groupID != null){
      map["groupID"] = groupID!;
    }
    return map;
  }
}
```

#### Chat 模块

**首先编写 IM 引擎。本模块所有代码及文件，均在 `lib/chat` 目录下。**

1. 新建全局状态管理 Model，名为 `model.dart`。
>?该 Model 用于挂载初始化并管理腾讯云 IM Flutter 模块，离线推送能力，全局状态管理，维护与 Native 间通信。是整个 Chat 模块的核心。
>
详细代码可查看 Demo 源码。重点关注三个部分：
    - `Future<dynamic> _handleMessage(MethodCall call)`：动态监听 Native 透传来的事件，包括登录信息及点击推送事件。
    - `Future<void> handleClickNotification(Map<String, dynamic> msg)`：点击通知处理事件，来自Native透传，从 Map 中取出数据，跳转至对应的子模块，如某个具体会话。
    - `Future<void> initChat()`：初始化腾讯云IM/登录腾讯云 IM/并完成离线推送的初始化及Token上报。该方法使用线程锁机制，保证同时只能执行一个，并在初始化成功后，不重复执行。
> ?请根据 [离线推送接入指引](https://cloud.tencent.com/document/product/269/74605)，完成厂商离线推送功能接入，才可正常上报推送 Token，使用推送功能。
2. 新建 `chat_main.dart` 文件，用于 Chat 模块主入口。
   - 该页面也是 Flutter Chat 模块的首页。
   - 在 Demo 中，该页面在未登录前为加载状态，登录后展示会话列表。
   - 此外，还需要在这里，完成 `didChangeAppLifecycleState` 监听与前后台切换事件上报，详情请查看 [离线推送插件文档步骤5](https://cloud.tencent.com/document/product/269/74605#.E6.AD.A5.E9.AA.A45.EF.BC.9A.E5.89.8D.E5.90.8E.E5.8F.B0.E5.88.87.E6.8D.A2.E7.9B.91.E5.90.AC.3Ca-id.3D.22step_5.22.3E.3C.2Fa.3E)。
   - 详细代码可查看 Demo 源码。
3. 新建 `push.dart` 文件，用于单例管理 [离线推送插件](https://cloud.tencent.com/document/product/269/74605) 能力。用于获取并上报Token/获取推送权限等操作。详细代码可查看 Demo 源码。
4. 新建 `conversation.dart` 文件，用于承载 TUIKit 的会话模块组件 `TIMUIKitConversation`。详细代码可查看 Demo 源码。
5. 新建 `chat.dart` 文件，用于承载 TUIKit 的历史消息列表和发送消息模块组件 `TIMUIKitChat`。
   该页面还有跳转至 Profile 及 Group Profile 页面的能力。
   详细代码可查看 Demo 源码。
6. 新建 `user_profile.dart` 文件，用于承载 TUIKit 的用户信息及关系链管理模块组件 `TIMUIKitProfile`。详细代码可查看 Demo 源码。
7. 新建 `group_profile.dart` 文件，用于承载 TUIKit 的群信息及群管理模块组件 `TIMUIKitGroupProfile`。详细代码可查看Demo源码。
此时，Chat 模块已开发完成。最终结构如下：

```
tencent_chat_module/
├── lib/
│   └── call/
│       └── chat.dart
│       └── model.dart
│       └── chat_main.dart
│       └── push.dart
│       └── conversation.dart
│       └── user_profile.dart
│       └── group_profile.dart
│   └── chat/
│   └── common/
```

#### Call 模块

该模块用于承载音视频通话能力，该能力由 [音视频通话插件](https://cloud.tencent.com/document/product/269/72485) 提供。

该模块的核心是，监听收到新的通话邀请时，通过调用Native方法，自动弹出通话页面；并接受 Chat 模块经由Native转发来的通话请求，主动发起通话。

**首先编写 IM 引擎。本模块所有代码及文件，均在 `lib/call` 目录下。**

1. 新建全局状态管理 Model，名为 `model.dart`。
   该 Model 用于挂载初始化并管理 [音视频通话插件](https://cloud.tencent.com/document/product/269/72485)，全局状态管理，维护与Native间通信。
   是整个Call模块的核心。
   详细代码可查看Demo源码。重点关注两个部分：
    - `_onRtcListener = TUICallingListener(...)`：定义了通话事件的监听器，通过 Method Channel 通知 Native 层，动态控制 Call 模块所属的 ViewController(iOS)/Activity(Android) 的前端展示与否。
    - `Future<dynamic> _handleMessage(MethodCall call)`：动态监听 Native 透传来的主动发起通话请求，来自 Call 模块的调用，主动发起通话。
2. 新建 `call_main.dart` 文件，用于 Call 模块主入口。该组件用于注入 [音视频通话插件所需绑定的navigatorKey](https://cloud.tencent.com/document/product/269/72485#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.95.E5.85.A5-navigatorkey)。详细代码可查看 Demo 源码。

#### 配置各个 Flutter 引擎的入口

开发完上述三个模块后，现在可完成最终对外暴露的 main 方法，作为 Flutter 引擎的入口。

1. 默认入口。打开 `lib/main.dart` 文件，将 `main()` 方法改成一个空 MaterialApp 即可。该方法作为 Flutter Module 的默认入口，在Flutter多引擎，使用 FlutterEngineGroup 管理的背景下，如果没有子 Flutter Engine 不设置任何 entry point，这个方法就不会被用到。例如，在我们的场景中，这个默认 `main()` 方法就没有被用上。

```dart
void main() {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(MaterialApp(
    title: 'Flutter Demo',
    theme: ThemeData(
      primarySwatch: Colors.blue,
    ),
    home: Container(),
  ));
}
```

2. 配置 Chat 模块的入口。使用 `@pragma('vm:entry-point')` 注解，将该方法标记为一个 `entry-point` 入口。方法名 `chatMain` 即该入口的名称，在 Native 中，也使用该名称，创建对应 Flutter 引擎。使用全局 `ChangeNotifierProvider` 状态管理，维护 `ChatInfoModel` 数据及业务逻辑。

```dart
@pragma('vm:entry-point')
void chatMain() {
  // This call ensures the Flutter binding has been set up before creating the
  // MethodChannel-based model.
  WidgetsFlutterBinding.ensureInitialized();

  final model = ChatInfoModel();

  runApp(
    ChangeNotifierProvider.value(
      value: model,
      child: const ChatAPP(),
    ),
  );
}
```

3. 配置 Call 模块的入口。同理，该入口命名为 `callMain`。使用全局 `ChangeNotifierProvider` 状态管理，维护 `CallInfoModel` 数据及业务逻辑。

```dart
@pragma('vm:entry-point')
void callMain() {
  // This call ensures the Flutter binding has been set up before creating the
  // MethodChannel-based model.
  WidgetsFlutterBinding.ensureInitialized();

  final model = CallInfoModel();

  runApp(
    ChangeNotifierProvider.value(
      value: model,
      child: const CallAPP(),
    ),
  );
}
```

至此，Flutter Module 部分，Dart 代码编写完成。接下来，开始编写 Native 代码。

### iOS Native 开发

本文以 Swift 语言为例。

>?以下代码结构，仅供参考，您可根据需要灵活组织。

进入您的 iOS 项目目录。如果您现有的应用程序，假设叫做 `MyApp`， 还没有 Podfile，请按照 [CocoaPods 入门指南](https://guides.cocoapods.org/using/using-cocoapods.html) 将 `Podfile` 添加到项目中。

#### 引入 Flutter Module

请参考 [此部分](#ios)，将 Flutter module 引入您的原生应用程序中。建议采用方式一。

#### 在 iOS 项目中，管理 Flutter 引擎

![](https://qcloudimg.tencent-cloud.cn/raw/e906c61c593195ca2310d08c1ac4a1f4.png)

**创建一个 `FlutterEngineGroup` （Flutter 引擎组），统一管理多个引擎实例。**

在 `AppDelegate.swift` 文件中，添加如下代码：

```swift
@UIApplicationMain
class AppDelegate: FlutterAppDelegate {
  lazy var flutterEngines = FlutterEngineGroup(name: "chat.flutter.tencent", project: nil)
  ...
}
```

**创建一个用于管理Flutter引擎的单例对象。**

这个 Swift 单例对象，用于集中管理 Flutter 实例，并方便在项目中各处，直接调用。

Demo 代码的逻辑是，使用新的路由，承载 Chat 的 ViewController；Call 的 ViewController，通过 present 和 dismiss 动态弹窗维护。

新建 `FlutterUtils.swift` 文件，编写代码。本部分详细代码，可查看 Demo 源码。

重点关注：

- `private override init()`：初始化各 Flutter 引擎实例，注册 Method Channel，监听事件。
- `func reportChatInfo()`：将用户登录信息和 SDKAPPID 透传至 Flutter Module，使 Flutter 层得以初始化并登录腾讯云IM。
- `func launchCallFunc()`：用于拉起 Call 的 Flutter 页面，可被 Call 模块收到通话邀请触发，也可被 Chat 模块主动发起通话触发。
- `func triggerNotification(msg: String)`：将 iOS Native 层收到的离线推送消息点击事件，及其包含的 ext 信息，以 JSON String形式，透传至 Flutter 层绑定的监听处理事件。用于处理离线推送点击跳转，例如至对应会话。

**监听及转发离线推送点击事件**

离线推送的初始化/Token上报/点击事件对应的会话跳转处理，已在 Flutter Chat 模块中进行，因此，Native 区域，仅需透传点击通知事件的 ext 即可。

之所以这么做，是因为点击通知事件已在 Native 被拦截消费，Flutter 层无法直接拿到，必须经由 Native 转发。

在 `AppDelegate.swift` 文件中，新增如下代码。具体代码，可以参考 Demo 源码。

![](https://qcloudimg.tencent-cloud.cn/raw/9c816ae4745e5a8d2b9b1d64167e1fc5.png)

此时，iOS Native 层编写完成。

### Android Native 开发

本文以 Kotlin 语言为例。

>?以下代码结构，仅供参考，您可根据需要灵活组织。

#### 引入 Flutter Module

请参考 [此部分](#android)，将 Flutter module 引入您的原生应用程序中。建议采用方式二。

#### 在 Android 项目中，管理Flutter引擎

**创建一个用于管理Flutter引擎的单例对象。**

这个 Kotlin 单例对象，用于集中管理 Flutter 实例，并方便在项目中各处，直接调用。

新建 `FlutterUtils.kt` 文件，并定义 `FlutterUtils` 静态类。

```kotlin
@SuppressLint("StaticFieldLeak")
object FlutterUtils {}
```

**创建 `FlutterEngineGroup` （Flutter 引擎组），统一管理多个引擎实例。**

在 `FlutterUtils.kt` 文件中，定义一个 `FlutterEngineGroup`，及配套各个 Flutter Engine 实例和 Method Channel，并在初始化时，将其初始化。

```kotlin
lateinit var context : Context
lateinit var flutterEngines: FlutterEngineGroup
private lateinit var chatFlutterEngine:FlutterEngine
private lateinit var callFlutterEngine:FlutterEngine

lateinit var chatMethodChannel: MethodChannel
lateinit var callMethodChannel: MethodChannel

// 初始化
flutterEngines = FlutterEngineGroup(context)
...
```

**继续完成该用于管理Flutter引擎的单例对象。**

Demo 代码的逻辑是，使用新的路由，承载 Cha t和 Call 的 Activity。

Chat 的 Activity，由用户主动进入及退出，Call 的 Activity，由监听器或主动外呼，自动导航进及返回出。

重点关注：

- `fun init()`：初始化各 Flutter 引擎实例，注册 Method Channel，监听事件。
- `fun reportChatInfo()`：将用户登录信息和 SDKAPPID 透传至 Flutter Module，使 Flutter 层得以初始化并登录腾讯云IM。
- `fun launchCallFunc()`：用于拉起 Call 的 Flutter 页面，可被 Call 模块收到通话邀请触发，也可被 Chat 模块主动发起通话触发。
- `fun triggerNotification(msg: String)`：将 iOS Native 层收到的离线推送消息点击事件，及其包含的ext信息，以 JSON String形式，透传至 Flutter 层绑定的监听处理事件。用于处理离线推送点击跳转，例如至对应会话。

本单例 object 的详细代码，可以参考 Demo 源码。

**在 总入口 `MyApplication` 中，初始化上述对象**

在 `MyApplication.kt` 文件中，将全局context传入单例对象，并执行初始化。

```kotlin
class MyApplication : MultiDexApplication() {

    override fun onCreate() {
        super.onCreate()
        FlutterUtils.context = this // new
        FlutterUtils.init()         // new
    }
}
```

**监听及转发离线推送点击事件**

离线推送的初始化/Token上报/点击事件对应的会话跳转处理，已在 Flutter Chat 模块中进行，因此，Native 区域，仅需透传点击通知事件的ext即可。

之所以这么做，是因为点击通知事件已在 Native 被拦截消费，Flutter 层无法直接拿到，必须经由 Native 转发。

>? 由于不同厂商的离线推送接入步骤不一致，本文以 OPPO 为例，全部厂商接入方案，可查看 [本文档](https://cloud.tencent.com/document/product/269/75428).

在腾讯云 IM 控制台中，新增 OPPO 的推送证书，`点击后续动作` 选择 `打开应用内指定页面`，`应用内页面` 以 `Activity` 方式，配置一个用于处理离线推送信息的页面，建议为应用首页。如，我们的 Demo 配置为：`com.tencent.chat.android.MainActivity`.

![](https://qcloudimg.tencent-cloud.cn/raw/c0f8737ce6fa484479ffc9a1bec6c9c0.png)

在上方控制台配置的用于离线推送的 Activity 文件中，新增如下代码。

该代码的作用是，当厂商拉起相应 Activity 时，从 Bundle 中取出 HashMap 形式 ext 信息，触发单例对象中的方法，将这个信息，手动转发至 Flutter 中。具体代码，可以参考  Demo 源码。

![](https://qcloudimg.tencent-cloud.cn/raw/2ec45c1a8b3bd952bcb86a8095f91515.png)

此时，Android Native 层编写完成。

[](id:single)

## 方案二：Flutter 单引擎方案

本方案，将 Chat 模块和 Call 模块，写在同一个 Flutter 引擎实例中。

![](https://qcloudimg.tencent-cloud.cn/raw/c6c52a028f5b86c88babe3074805b295.png)

这两个模块只能同时出现同时隐藏，仅需维护一个 Flutter 引擎即可。

<a target="_blank" href="https://github.com/TencentCloud/tencentchat-add-flutter-to-app/tree/main/Single%20Flutter%20Engines"><img src="https://qcloudimg.tencent-cloud.cn/raw/b622951f776a505e83f843de1f62fffc.png" /></a>

### Flutter Module 开发

要将 Flutter 嵌入到现有应用程序中，请首先创建一个 Flutter 模块。

在您项目的根目录外层，运行

```
cd some/path/
flutter create --template module tencent_chat_module
```

这会在 some/path/tencent_chat_module/ 创建一个 Flutter 模块项目。 在该目录中，您可以运行与在任何其他 Flutter 项目中相同的 Flutter 命令，例如 `flutter run --debug` 或 `flutter build ios`。 您还可以使用 Flutter 和 Dart 插件在 Android Studio, IntelliJ 或 VS Code 中运行该模块。 该项目在嵌入到现有应用程序之前包含模块的单视图示例版本，这对于测试代码的仅 Flutter 部分很有用。

`tencent_chat_module` 模块目录结构类似于普通的 Flutter 应用程序：

```
tencent_chat_module/
├── .ios/
│   ├── Runner.xcworkspace
│   └── Flutter/podhelper.rb
├── lib/
│   └── main.dart
├── test/
└── pubspec.yaml
```

现在，我们可以在 `lib/` 中，编写代码了。

#### main.dart

修改 `main.dart` 文件，引入 [TUIKit](https://cloud.tencent.com/document/product/269/70747), [离线推送插件](https://cloud.tencent.com/document/product/269/74605) 及 [音视频通话插件](https://cloud.tencent.com/document/product/269/72485)。

全局状态，我们的 IM SDK 及 Method Channel 与 Native 通信状态，管理于 `ChatInfoModel` 中。

接收到 Native 传来的用户信息及 SDKAPPID 后，调用 `_coreInstance.init()` 及 `_coreInstance.login()` 初始化并登录腾讯云IM。并初始化音视频推送插件及离线推送插件，完成推送 Token 上报。

> ?请根据 [离线推送接入指引](https://cloud.tencent.com/document/product/269/74605)，完成厂商离线推送功能接入，才可正常上报推送 Token，使用推送功能。

- 对于音视频通话插件，需要关注：监听收到新的通话邀请时，通过调用 Native 方法，让 Native 检测用户当前是否在本 Flutter 模块页面，如果不在，需要强制将前端页面调整至本模块，以展示来电页面。
- 对于离线推送插件，需要关注：点击通知处理事件，来自 Native 透传，从 Map 中取出数据，跳转至对应的子模块，如某个具体会话。

完成首页的制作，在未登录时展示加载动画；登录成功后，展示会话列表页面。

此外，还需要在这里，完成 `didChangeAppLifecycleState` 监听与前后台切换事件上报，详情请查看 [离线推送插件文档步骤5](https://cloud.tencent.com/document/product/269/74605#.E6.AD.A5.E9.AA.A45.EF.BC.9A.E5.89.8D.E5.90.8E.E5.8F.B0.E5.88.87.E6.8D.A2.E7.9B.91.E5.90.AC.3Ca-id.3D.22step_5.22.3E.3C.2Fa.3E)。

详细代码可查看 Demo 源码。

#### 其他 TUIKit 模块引入

1. 新建 `push.dart` 文件，用于单例管理 [离线推送插件](https://cloud.tencent.com/document/product/269/74605) 能力。用于获取并上报Token/获取推送权限等操作。详细代码可查看 Demo 源码。
2. 新建 `conversation.dart` 文件，用于承载 TUIKit 的会话模块组件 `TIMUIKitConversation`。详细代码可查看 Demo 源码。
3. 新建 `chat.dart` 文件，用于承载 TUIKit 的历史消息列表和发送消息模块组件 `TIMUIKitChat`。该页面还有跳转至 Profile 及 Group Profile 页面的能力。详细代码可查看Demo源码。
4. 新建 `user_profile.dart` 文件，用于承载 TUIKit 的用户信息及关系链管理模块组件 `TIMUIKitProfile`。详细代码可查看 Demo 源码。
5. 新建 `group_profile.dart` 文件，用于承载 TUIKit 的群信息及群管理模块组件 `TIMUIKitGroupProfile`。详细代码可查看 Demo 源码。

至此，统一的 Flutter Module 开发完成。

### iOS Native 开发

本文以 Swift 语言为例。

>?以下代码结构，仅供参考，您可根据需要灵活组织。

进入您的 iOS 项目目录。

如果您现有的应用程序，假设叫做 `MyApp`， 还没有 Podfile，请按照 [CocoaPods入门指南](https://guides.cocoapods.org/using/using-cocoapods.html) 将 `Podfile` 添加到项目中。

#### 引入 Flutter Module

请参考 [此部分](#ios)，将 Flutter module 引入您的原生应用程序中。建议采用方式一。

#### 在 iOS 项目中，管理 Flutter 引擎

**创建一个 FlutterEngine。**

创建 FlutterEngine 的适当位置特定于您的主应用程序入口。作为一个例子，我们演示了如何在 `AppDelegate` 中的app启动时创建一个 FlutterEngine，并公开为一个属性。

```swift
import UIKit
import Flutter
import FlutterPluginRegistrant

@UIApplicationMain
class AppDelegate: FlutterAppDelegate { // More on the FlutterAppDelegate.
  lazy var flutterEngine = FlutterEngine(name: "tencent cloud chat")

  override func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Runs the default Dart entrypoint with a default Flutter route.
    flutterEngine.run();
    GeneratedPluginRegistrant.register(with: self.flutterEngine);
    return super.application(application, didFinishLaunchingWithOptions: launchOptions);
  }
}
```

**创建一个用于管理 Flutter 引擎的单例对象。**

这个 Swift 单例对象，用于集中管理 Flutter Method Channel，并提供一系列与 Flutter Module 通信的方法，方便在项目中各处，直接调用。

这些方法包括：

- `private override init()`：初始化 Method Channel，并为其绑定事件监听方法。
- `func reportChatInfo()`：将用户登录信息和 SDKAPPID 透传至 Flutter Module，使 Flutter 层得以初始化并登录腾讯云IM。
- `func launchChatFunc()`：拉起或导航至 Flutter Module 所在 ViewController。
- `func triggerNotification(msg: String)`：将 iOS Native 层收到的离线推送消息点击事件，及其包含的ext信息，以 JSON String形式，透传至 Flutter 层绑定的监听处理事件。用于处理离线推送点击跳转，例如至对应会话。

详细代码可查看 Demo 源码。

**监听及转发离线推送点击事件**

离线推送的初始化/Token上报/点击事件对应的会话跳转处理，已在 Flutter Chat 模块中进行，因此，Native 区域，仅需透传点击通知事件的ext即可。

之所以这么做，是因为点击通知事件已在 Native 被拦截消费，Flutter 层无法直接拿到，必须经由 Native 转发。

在 `AppDelegate.swift` 文件中，新增如下代码。具体代码，可以参考 Demo 源码。

![](https://qcloudimg.tencent-cloud.cn/raw/0ea48d21696a1e696ab98091983168f9.png)

此时，iOS Native 层编写完成。

### Android Native 开发

本文以 Kotlin 语言为例。

>?以下代码结构，仅供参考，您可根据需要灵活组织。

#### 引入 Flutter Module

请参考 [此部分](#android)，将 Flutter module 引入您的原生应用程序中。建议采用方式二。

#### 在 Android 项目中，管理 Flutter 引擎

**创建一个用于管理 Flutter 引擎的单例对象。**

这个 Kotlin 单例对象，用于集中管理 Flutter Method Channel，并提供一系列与 Flutter Module 通信的方法，方便在项目中各处，直接调用。

新建 `FlutterUtils.kt` 文件，并定义 `FlutterUtils` 静态类。

```kotlin
@SuppressLint("StaticFieldLeak")
object FlutterUtils {}
```

**创建一个 `FlutterEngine` （Flutter 引擎）。**

在 `FlutterUtils.kt` 文件中，定义一个 `FlutterEngine`，并在初始化时，将其初始化。

```kotlin
lateinit var context : Context
private lateinit var flutterEngine:FlutterEngine

// 初始化
flutterEngine = FlutterEngine(context)
```

**继续完成该用于管理 Flutter 引擎的单例对象。**

Demo 代码的逻辑是，使用新的路由，承载 Chat 和 Call 的 Activity。

Chat 的 Activity，由用户主动进入及退出；Call 的 Activity，由监听器或主动外呼，自动导航进及返回出。

重点关注：

- `fun init()`：初始化 Method Channel，并为其绑定事件监听方法。
- `fun reportChatInfo()`：将用户登录信息和 SDKAPPID 透传至 Flutter Module，使 Flutter 层得以初始化并登录腾讯云IM。
- `fun launchChatFunc()`：拉起或导航至 Flutter Module 所在 ViewController。
- `fun triggerNotification(msg: String)`：将 iOS Native 层收到的离线推送消息点击事件，及其包含的ext信息，以 JSON String形式，透传至 Flutter 层绑定的监听处理事件。用于处理离线推送点击跳转，例如至对应会话。

本单例 object 的详细代码，可以参考Demo源码。

**在 总入口 `MyApplication` 中，初始化上述对象**

在 `MyApplication.kt` 文件中，将全局context传入单例对象，并执行初始化。

```kotlin
class MyApplication : MultiDexApplication() {

    override fun onCreate() {
        super.onCreate()
        FlutterUtils.context = this // new
        FlutterUtils.init()         // new
    }
}
```

**监听及转发离线推送点击事件**

离线推送的初始化/Token上报/点击事件对应的会话跳转处理，已在 Flutter Chat 模块中进行，因此，Native 区域，仅需透传点击通知事件的 ext 即可。

之所以这么做，是因为点击通知事件已在 Native 被拦截消费，Flutter 层无法直接拿到，必须经由 Native 转发。

>? 由于不同厂商的离线推送接入步骤不一致，本文以 OPPO 为例，全部厂商接入方案，可查看 [本文档](https://cloud.tencent.com/document/product/269/75428)。

在腾讯云 IM 控制台中，新增 OPPO 的推送证书，`点击后续动作` 选择 `打开应用内指定页面`，`应用内页面` 以 `Activity` 方式，配置一个用于处理离线推送信息的页面，建议为应用首页。如，我们的 Demo 配置为：`com.tencent.chat.android.MainActivity`。

![](https://qcloudimg.tencent-cloud.cn/raw/c0f8737ce6fa484479ffc9a1bec6c9c0.png)

在上方控制台配置的用于离线推送的 Activity 文件中，新增如下代码。

该代码的作用是，当厂商拉起相应 Activity 时，从 Bundle 中取出 HashMap 形式 ext 信息，触发单例对象中的方法，将这个信息，手动转发至 Flutter 中。具体代码，可以参考  Demo 源码。

![](https://qcloudimg.tencent-cloud.cn/raw/2ec45c1a8b3bd952bcb86a8095f91515.png)

此时，Android Native 层编写完成。

[](id:native)

## 附加方案：在 Native 层，初始化并登录腾讯云IM

有的时候，对于 Chat 和 Call 模块能力，您希望对于高频的简单应用场景，能深入嵌入您现有的业务逻辑中。

例如对于游戏场景，在对局内，希望能直接发起会话。

而您的完整功能 Chat 模块，使用 Flutter 实现，仅是您 APP 中一个重要性较低的子模块，因此不希望一上来就启动一个完整的 Flutter Module。

这个时候，您可以在 Native 层调用腾讯云 IM  Native SDK 的初始化及登录方法，此后，便可在您需要的高频简单场景，直接使用腾讯云 IM Native SDK，构建 In-App Chat 能力。

>?当然，在此种情况下，您也可以选择提前先在 Flutter 初始化并登录腾讯云IM，此时，您将不再需要在 Native 层再次初始化并登录。两端仅需初始化并登录一次，即可在双端都能使用。
>由于 Flutter SDK 已自带 Native SDK，您不需要在 Native 层，再次引入，即可直接使用。

### Native 初始化并登录

以 iOS Swift 代码为例，演示如何在 Native 层，初始化并登录。

```swift
import ImSDK_Plus


func initTencentChat(){
        if(isLoginSuccess == true){
            return
        }
        let data = V2TIMManager.sharedInstance().initSDK( 您的SDKAPPID , config: nil);
        if (data == true){
            V2TIMManager.sharedInstance().login(
                chatInfo.userID,
                userSig: chatInfo.userSig,
                succ: {
                    self.isLoginSuccess = true
                    self.reportChatInfo()
                },
                fail: onLoginFailed()
            )
        }
}
```

此后，在 Native 层面，便可直接使用Native SDK，搭建您的业务功能模块。详情可查阅 [iOS 快速入门](https://cloud.tencent.com/document/product/269/68228) 或 [Android 快速入门](https://cloud.tencent.com/document/product/269/36838)。

### 初始化 Flutter TUIKit

如果您已在 Native 层完成初始化并登录，您不需要再次在 Flutter 层再次执行，但需要调用 TUIKit 的 `_coreInstance.setDataFromNative()`，将当前用户信息传入。

```dart
final CoreServicesImpl _coreInstance = TIMUIKitCore.getInstance();
_coreInstance.setDataFromNative(userId: chatInfo?.userID ?? "");
```

**更详细代码，请查阅我们的 Demo 源码。**

<a target="_blank" href="https://github.com/TencentCloud/tencentchat-add-flutter-to-app/tree/main/Initialize%20from%20Native"><img src="https://qcloudimg.tencent-cloud.cn/raw/b622951f776a505e83f843de1f62fffc.png" /></a>


### 可选操作：开通内容审核功能
在消息发送、资料修改场景中，很有可能会扩散不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。


## 联系我们

至此，腾讯云 IM Flutter - Native 混合开发方式已全部介绍完成。

您可以基于本文档给出的方案，快速在您现有的原生开发 Android/iOS APP 中，使用 Flutter SDK，使用同一套 Flutter 代码，快速植入 Chat 和 Call 模块能力。

如果您还有任何疑问，欢迎随时联系我们。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)

## Reference

1. [Integrate a Flutter module into your Android project](https://docs.flutter.dev/development/add-to-app/android/project-setup).
2. [Integrate a Flutter module into your iOS project](https://docs.flutter.dev/development/add-to-app/ios/project-setup).
3. [Adding a Flutter screen to an iOS app](https://docs.flutter.dev/development/add-to-app/ios/add-flutter-screen?tab=no-engine-vc-swift-tab).
4. [Multiple Flutter screens or views](https://docs.flutter.dev/development/add-to-app/multiple-flutters).
