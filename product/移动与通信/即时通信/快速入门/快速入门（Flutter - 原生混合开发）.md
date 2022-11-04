[](id:toc)
通过阅读本文，你可以了解在您现有的 Android / iOS 原生开发项目中，集成腾讯云IM Flutter 的方法。

有的时候，使用Flutter重写您现有的应用程序是不现实的。如果您想在现有APP中，使用腾讯云IM的能力，推荐采用混合开发方案，即将Flutter模块，嵌入您的原生开发APP项目中。

**可在很大程度上，降低您的工作量，快速在双端原生APP中，植入IM通信能力。**

![](https://qcloudimg.tencent-cloud.cn/raw/c28c621153e684bdb64cf8ae3f92ea4c.png)

## 环境要求

| 环境  | 版本 |
|---------|---------|
| Flutter | SDK 最低要求 Flutter 2.2.0版本，TUIKit 集成组件库最低要求 Flutter 2.10.0 版本。|
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 前置知识点

在开始前，您首先需要了解腾讯云IM Flutter的SDK构成及使用方式。

主要包括两个SDK：[无UI版本](https://cloud.tencent.com/document/product/269/68823#.E7.AC.AC.E4.BA.94.E9.83.A8.E5.88.86.EF.BC.9A.E8.87.AA.E5.AE.9E.E7.8E.B0-ui-.E9.9B.86.E6.88.90)及[含UI组件库](https://cloud.tencent.com/document/product/269/70747)。本文将以 [含UI组件库（TUIKit）](https://cloud.tencent.com/document/product/269/70747) 为例，介绍混合开发方案。

**关于腾讯云IM Flutter详细用法，可从我们的 [快速入门文档](https://cloud.tencent.com/document/product/269/68823) 看起。**

## 混合开发选型

我们推荐您使用Flutter Module方式进行混合开发集成。在Native原生项目中，构建Flutter引擎，来承载Flutter中的IM及Calling模块。

对于Flutter引擎的创建管理，目前两种方式：单Flutter引擎及多Flutter引擎。

| 引擎模式 | 介绍 | 优点 | 缺点 |
|---------|---------|---------|---------|
| [Flutter单引擎](#single) | Chat模块和Calling模块在同一个Flutter引擎中承载。 | 方便，所有Flutter代码统一维护。 | 由于Calling插件，在有电话呼入时，需要自动展示来电页面。如果在同一个引擎中，需要强制跳转至Flutter所在页面，体验较差。 |
| [Flutter多引擎](#multiple) | Chat模块和Calling模块分别承载于不同的Flutter引擎中，使用Flutter引擎组来统一管理这两个引擎。 | Calling插件独立存在于一个Flutter引擎中，独立页面控制，来电时，直接将该页面弹窗即可，不影响用户当前所在页面，体验较好。 | 通话模块无法最小化成浮窗形式。 |

[](id:multiple)

## 方案一：IM 和 Calling 分别独立 Flutter 引擎 【推荐】

使用多个Flutter引擎的优点是，每个实例都是独立的，并维护其自己的内部导航堆栈、UI和应用程序状态。这简化了整个应用程序代码的状态保持责任，并提高了模块化能力。

![](https://qcloudimg.tencent-cloud.cn/raw/912d986a5ff57606422455a273a033f3.png)

在Android和iOS上添加多个Flutter引擎，主要基于一个FlutterEngineGroup类(Android API、iOS API)来构造并管理多个FlutterEngine（Flutter引擎）。

在我们的项目中，我们基于一个统一的FlutterEngineGroup，来管理两个FlutterEngine（Flutter引擎），分别用于承载 Chat 和 Calling 模块。

[![](https://qcloudimg.tencent-cloud.cn/raw/b622951f776a505e83f843de1f62fffc.png)](https://dscache.tencent-cloud.cn/upload/uploader/tencentcloudchat_flutter_add_to_app-1667532740459.zip)

### Flutter Module 开发

要将Flutter嵌入到现有应用程序中，请首先创建一个Flutter模块。

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

#### 梳理Flutter lib 目录

>? 
>
> 以下代码结构，仅供参考，您可根据需要灵活组织，以引入腾讯云IM Flutter。

在 `lib/` 我们创建三个目录，`call`, `chat`, `common`。分别用于放置通话引擎，IM引擎，及通用model类。

```
tencent_chat_module/
├── lib/
│   └── call/
│   └── chat/
│   └── common/
```

#### 通用model类模块

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

**首先编写IM引擎。本模块所有代码及文件，均在 `lib/chat` 目录下。**

1. 新建全局状态管理Model，名为 `model.dart`。
该Model用于挂载初始化并管理腾讯云IM Flutter模块，离线推送能力，全局状态管理，维护与Native间通信。
是整个Chat模块的核心。
详细代码可查看Demo源码。重点关注三个部分：
    - Future<dynamic> _handleMessage(MethodCall call): 动态监听 Native 透传来的事件，包括登录信息及点击推送事件。
    - Future<void> handleClickNotification(Map<String, dynamic> msg): 点击通知处理事件，来自Native透传，从 Map 中取出数据，跳转至对应的子模块，如某个具体会话。
    - Future<void> initChat(): 初始化腾讯云IM/登录腾讯云IM/并完成离线推送的初始化及Token上报。该方法使用线程锁机制，保证同时只能执行一个，并在初始化成功后，不重复执行。

> ?
> 
> 请根据 [离线推送接入指引](https://cloud.tencent.com/document/product/269/74605)，完成厂商离线推送功能接入，才可正常上报推送Token，使用推送功能。

2. 新建 `chat_main.dart` 文件，用于Chat模块主入口。
该页面也是Flutter Chat模块的首页。
在Demo中，该页面在未登录前为加载状态，登录后展示会话列表。
详细代码可查看Demo源码。

3. 新建 `push.dart` 文件，用于单例管理 [离线推送插件](https://cloud.tencent.com/document/product/269/74605) 能力。用于获取并上报Token/获取推送权限等操作。详细代码可查看Demo源码。

4. 新建 `conversation.dart` 文件，用于承载TUIKit的会话模块组件 `TIMUIKitConversation`。详细代码可查看Demo源码。

5. 新建 `chat.dart` 文件，用于承载TUIKit的历史消息列表和发送消息模块组件 `TIMUIKitChat`。
该页面还有跳转至 Profile 及 Group Profile 页面的能力。
详细代码可查看Demo源码。

6. 新建 `user_profile.dart` 文件，用于承载TUIKit的用户信息及关系链管理模块组件 `TIMUIKitProfile`。详细代码可查看Demo源码。

7. 新建 `group_profile.dart` 文件，用于承载TUIKit的群信息及群管理模块组件 `TIMUIKitGroupProfile`。详细代码可查看Demo源码。

此时，Chat模块已开发完成。最终结构如下：

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

**首先编写IM引擎。本模块所有代码及文件，均在 `lib/call` 目录下。**

1. 新建全局状态管理Model，名为 `model.dart`。
该Model用于挂载初始化并管理 [音视频通话插件](https://cloud.tencent.com/document/product/269/72485)，全局状态管理，维护与Native间通信。
是整个Call模块的核心。
详细代码可查看Demo源码。重点关注两个部分：
    - _onRtcListener = TUICallingListener(...): 定义了通话事件的监听器，通过 Method Channel 通知Native层，动态控制 Call 模块所属的 ViewController(iOS)/Activity(Android) 的前端展示与否。
    - Future<dynamic> _handleMessage(MethodCall call): 动态监听 Native 透传来的主动发起通话请求，来自 Call 模块的调用，主动发起通话。

2. 2. 新建 `call_main.dart` 文件，用于Call模块主入口。
该组件用于注入[音视频通话插件所需绑定的navigatorKey](https://cloud.tencent.com/document/product/269/72485#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.95.E5.85.A5-navigatorkey)。
详细代码可查看Demo源码。


#### 配置各个Flutter引擎的入口

开发完上述三个模块后，现在可完成最终对外暴露的main方法，作为Flutter引擎的入口。

1. 默认入口

打开 `lib/main.dart` 文件，将 `main()` 方法改成一个空 MaterialApp 即可。

该方法作为 Flutter Module 的默认入口，在Flutter多引擎，使用FlutterEngineGroup管理的背景下，如果没有子Flutter Engine不设置任何entry point，这个方法就不会被用到。

例如，在我们的场景中，这个默认 `main()` 方法就没有被用上。

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

2. 配置 Chat 模块的入口

使用 `@pragma('vm:entry-point')` 注解，将该方法标记为一个 `entry-point` 入口。方法名 `chatMain` 即该入口的名称，在Native中，也使用该名称，创建对应Flutter引擎。

使用全局 `ChangeNotifierProvider` 状态管理，维护 `ChatInfoModel` 数据及业务逻辑。

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

3. 配置 Call 模块的入口

同理，该入口命名为 `callMain`。

使用全局 `ChangeNotifierProvider` 状态管理，维护 `CallInfoModel` 数据及业务逻辑。

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

至此，Flutter Module部分，Dart代码编写完成。

接下来，开始编写 Native 代码。

### iOS Native 开发

本文以 Swift 语言为例。

>? 
>
> 以下代码结构，仅供参考，您可根据需要灵活组织，在iOS Native层面，引入上一步所构建的Flutter Module。

进入您的iOS项目目录。

如果您现有的应用程序，假设叫做 `MyApp`， 还没有Podfile，请按照[CocoaPods入门指南](https://guides.cocoapods.org/using/using-cocoapods.html)将 `Podfile` 添加到项目中。

#### 引入 Flutter Module

1. 将以下代码添加到Podfile中:

```
// 上一步构建的Flutter Module的路径
flutter_chat_application_path = '../tencent_chat_module'

load File.join(flutter_chat_application_path, '.ios', 'Flutter', 'podhelper.rb')
```

2. 对于每个需要嵌入Flutter的[Podfile target](https://guides.cocoapods.org/syntax/podfile.html#target)，调用 `install_all_flutter_pods(flutter_chat_application_path)`.

```
target 'MyApp' do
  install_all_flutter_pods(flutter_chat_application_path)
end
```

3. 在Podfile的 `post_install` 块中，调用 `flutter_post_install(installer)`，并完成 [腾讯云IM TUIKit](https://cloud.tencent.com/document/product/269/70747) 所需的权限声明，包括麦克风权限/相机权限/相册权限。

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

4. 执行 `pod install`。
> ?
> 
> - 在 `tencent_chat_module/pubspec.yaml` 中更改Flutter插件依赖时，请在Flutter Module目录中运行 `flutter pub get` 以刷新 `podhelper.rb` 脚本读取的插件列表。然后，从您iOS应用程序的根目录，再次执行 `pod install`。
> - 对于 Apple Silicon 芯片 arm64 架构的 Mac电脑，可能需要执行 `arch -x86_64 pod install --repo-update`。

`podhelper.rb` 脚本将您的插件 / `Flutter.framework` / `App.framework` 植入您的项目中。

#### 在 iOS 项目中，管理Flutter引擎

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

Demo代码的逻辑是，使用新的路由，承载Chat的ViewController；Call的ViewController，通过present和dismiss动态弹窗维护。

新建 `FlutterUtils.swift` 文件，编写代码。本部分详细代码，可查看Demo源码。

重点关注：
- private override init(): 初始化各 Flutter 引擎实例，注册Method Channel，监听事件。
- func reportChatInfo(): 将用户登录信息和SDKAPPID透传至Flutter Module，使Flutter层得以初始化并登录腾讯云IM。
- func launchCallFunc(): 用于拉起Call的Flutter页面，可被Call模块收到通话邀请触发，也可被Chat模块主动发起通话触发。
- func triggerNotification(msg: String): 将 iOS Native 层收到的离线推送消息点击事件，及其包含的ext信息，以 JSON String形式，透传至 Flutter 层绑定的监听处理事件。用于处理离线推送点击跳转，例如至对应会话。

**监听及转发离线推送点击事件**

离线推送的初始化/Token上报/点击事件对应的会话跳转处理，已在Flutter Chat模块中进行，因此，Native区域，仅需透传点击通知事件的ext即可。

之所以这么做，是因为点击通知事件已在Native被拦截消费，Flutter层无法直接拿到，必须经由Native转发。

在 `AppDelegate.swift` 文件中，新增如下代码。具体代码，可以参考Demo源码。

![](https://qcloudimg.tencent-cloud.cn/raw/9c816ae4745e5a8d2b9b1d64167e1fc5.png)

此时，iOS Native层编写完成。

### Android Native 开发

// TODO


[](id:single)

## 方案二：IM 和 Calling 承载于一个Flutter引擎中

本方案，将Chat模块和Call模块，写在同一个Flutter引擎实例中。

这两个模块只能同时出现同时隐藏，仅需维护一个 Flutter引擎 即可。

[![](https://qcloudimg.tencent-cloud.cn/raw/b622951f776a505e83f843de1f62fffc.png)](https://dscache.tencent-cloud.cn/upload/uploader/tencentcloudchat_flutter_add_to_app-1667532740459.zip)

### Flutter Module 开发

要将Flutter嵌入到现有应用程序中，请首先创建一个Flutter模块。

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

修改 `main.dart` 文件，引入[TUIKit](https://cloud.tencent.com/document/product/269/70747), [离线推送插件](https://cloud.tencent.com/document/product/269/74605)及[音视频通话插件](https://cloud.tencent.com/document/product/269/72485)。

全局状态，我们的IM SDK及Method Channel与Native通信状态，管理于 `ChatInfoModel` 中。

接收到Native传来的用户信息及SDKAPPID后，调用 `_coreInstance.init()` 及 `_coreInstance.login() ` 初始化并登录腾讯云IM。并初始化音视频推送插件及离线推送插件，完成推送Token上报。

> ?
> 
> 请根据 [离线推送接入指引](https://cloud.tencent.com/document/product/269/74605)，完成厂商离线推送功能接入，才可正常上报推送Token，使用推送功能。

对于音视频通话插件，需要关注：
- 监听收到新的通话邀请时，通过调用Native方法，让Native检测用户当前是否在本Flutter模块页面，如果不在，需要强制将前端页面调整至本模块，以展示来电页面。

对于离线推送插件，需要关注：
- 点击通知处理事件，来自Native透传，从 Map 中取出数据，跳转至对应的子模块，如某个具体会话。

完成首页的制作，在未登录时展示加载动画；登录成功后，展示会话列表页面。

详细代码可查看Demo源码。

#### 其他TUIKit模块引入

1. 新建 `push.dart` 文件，用于单例管理 [离线推送插件](https://cloud.tencent.com/document/product/269/74605) 能力。用于获取并上报Token/获取推送权限等操作。详细代码可查看Demo源码。

2. 新建 `conversation.dart` 文件，用于承载TUIKit的会话模块组件 `TIMUIKitConversation`。详细代码可查看Demo源码。

3. 新建 `chat.dart` 文件，用于承载TUIKit的历史消息列表和发送消息模块组件 `TIMUIKitChat`。
该页面还有跳转至 Profile 及 Group Profile 页面的能力。
详细代码可查看Demo源码。

4. 新建 `user_profile.dart` 文件，用于承载TUIKit的用户信息及关系链管理模块组件 `TIMUIKitProfile`。详细代码可查看Demo源码。

5. 新建 `group_profile.dart` 文件，用于承载TUIKit的群信息及群管理模块组件 `TIMUIKitGroupProfile`。详细代码可查看Demo源码。

至此，统一的Flutter Module开发完成。

### iOS Native 开发

本文以 Swift 语言为例。

>? 
>
> 以下代码结构，仅供参考，您可根据需要灵活组织，在iOS Native层面，引入上一步所构建的Flutter Module。

进入您的iOS项目目录。

如果您现有的应用程序，假设叫做 `MyApp`， 还没有Podfile，请按照[CocoaPods入门指南](https://guides.cocoapods.org/using/using-cocoapods.html)将 `Podfile` 添加到项目中。

#### 引入 Flutter Module

1. 将以下代码添加到Podfile中:

```
// 上一步构建的Flutter Module的路径
flutter_chat_application_path = '../tencent_chat_module'

load File.join(flutter_chat_application_path, '.ios', 'Flutter', 'podhelper.rb')
```

2. 对于每个需要嵌入Flutter的[Podfile target](https://guides.cocoapods.org/syntax/podfile.html#target)，调用 `install_all_flutter_pods(flutter_chat_application_path)`.

```
target 'MyApp' do
  install_all_flutter_pods(flutter_chat_application_path)
end
```

3. 在Podfile的 `post_install` 块中，调用 `flutter_post_install(installer)`，并完成 [腾讯云IM TUIKit](https://cloud.tencent.com/document/product/269/70747) 所需的权限声明，包括麦克风权限/相机权限/相册权限。

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

4. 执行 `pod install`。
> ?
> 
> - 在 `tencent_chat_module/pubspec.yaml` 中更改Flutter插件依赖时，请在Flutter Module目录中运行 `flutter pub get` 以刷新 `podhelper.rb` 脚本读取的插件列表。然后，从您iOS应用程序的根目录，再次执行 `pod install`。
> - 对于 Apple Silicon 芯片 arm64 架构的 Mac电脑，可能需要执行 `arch -x86_64 pod install --repo-update`。

`podhelper.rb` 脚本将您的插件 / `Flutter.framework` / `App.framework` 植入您的项目中。

#### 在 iOS 项目中，管理Flutter引擎

**创建一个FlutterEngine。**

创建FlutterEngine的适当位置特定于您的主应用程序入口。作为一个例子，我们演示了如何在 `AppDelegate` 中的app启动时创建一个FlutterEngine，并公开为一个属性。

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

**创建一个用于管理Flutter引擎的单例对象。**

这个 Swift 单例对象，用于集中管理 Flutter Method Channel，并提供一系列与 Flutter Module 通信的方法，方便在项目中各处，直接调用。

这些方法包括：
- private override init(): 初始化 Method Channel，并为其绑定事件监听方法。
- func reportChatInfo(): 将用户登录信息和SDKAPPID透传至Flutter Module，使Flutter层得以初始化并登录腾讯云IM。
- func launchChatFunc(): 拉起或导航至 Flutter Module 所在 ViewController。
- func triggerNotification(msg: String): 将 iOS Native 层收到的离线推送消息点击事件，及其包含的ext信息，以 JSON String形式，透传至 Flutter 层绑定的监听处理事件。用于处理离线推送点击跳转，例如至对应会话。

详细代码可查看Demo源码。

**监听及转发离线推送点击事件**

离线推送的初始化/Token上报/点击事件对应的会话跳转处理，已在Flutter Chat模块中进行，因此，Native区域，仅需透传点击通知事件的ext即可。

之所以这么做，是因为点击通知事件已在Native被拦截消费，Flutter层无法直接拿到，必须经由Native转发。

在 `AppDelegate.swift` 文件中，新增如下代码。具体代码，可以参考Demo源码。

![](https://qcloudimg.tencent-cloud.cn/raw/0ea48d21696a1e696ab98091983168f9.png)

此时，iOS Native层编写完成。

### Android Native 开发

// TODO

## 附加方案：在 Native 层，初始化并登录腾讯云IM

有的时候，对于Chat和Call模块能力，您希望对于高频的简单应用场景，能深入嵌入您现有的业务逻辑中。

例如对于游戏场景，在对局内，希望能直接发起会话。

而您的完整功能Chat模块，使用Flutter实现，仅是您APP中一个重要性较低的子模块，因此不希望一上来就启动一个完整的Flutter Module。

这个时候，您可以在Native层调用腾讯云IM  Native SDK的初始化及登录方法，此后，便可在您需要的高频简单场景，直接使用腾讯云IM Native SDK，构建 In-App Chat 能力。

以 iOS Swift 代码为例，演示如何在 Native 层，初始化并登录。

```swift
func initTencentChat(){
        if(isLoginSuccess == true){
            return
        }
        let data = V2TIMManager.sharedInstance().initSDK(1400187352, config: nil);
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

此后，在 Native 层面，便可直接使用Native SDK，搭建您的业务功能模块。详情可查阅 [iOS 快速入门]() 或 [Android 快速入门](https://cloud.tencent.com/document/product/269/36838)。

**更详细代码，请查阅我们的Demo 源码。**

[![](https://qcloudimg.tencent-cloud.cn/raw/b622951f776a505e83f843de1f62fffc.png)](https://dscache.tencent-cloud.cn/upload/uploader/tencentcloudchat_flutter_add_to_app-1667532740459.zip)


-----



至此，腾讯云IM Flutter - Native 混合开发方式已全部介绍完成。

您可以基于本文档给出的方案，快速在您现有的原生开发 Android/iOS APP 中，使用 Flutter SDK，使用同一套Flutter代码，快速植入 Chat 和 Call 模块能力。

如果您还有任何疑问，欢迎随时[联系我们](#contact)。


-----


## 引用与参考资料

1. [Integrate a Flutter module into your Android project](https://docs.flutter.dev/development/add-to-app/android/project-setup).
2. [Integrate a Flutter module into your iOS project](https://docs.flutter.dev/development/add-to-app/ios/project-setup).
3. [Adding a Flutter screen to an iOS app](https://docs.flutter.dev/development/add-to-app/ios/add-flutter-screen?tab=no-engine-vc-swift-tab).
4. [Multiple Flutter screens or views](https://docs.flutter.dev/development/add-to-app/multiple-flutters).

[](id:contact)

## 联系我们
如果您在接入使用过程中有任何疑问，请加入 QQ 群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/eacb194c77a76b5361b2ae983ae63260.png)

