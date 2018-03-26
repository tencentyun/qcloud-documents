## 准备工作

在开始使用移动开发平台（MobileLine） Authorization 之前，您需要：

1. 一个启用了移动开发平台（MobileLine）的应用。
2. 您集成了 [TACCore](https://cloud.tencent.com/document/product/666/14306)。

## 将移动开发平台（MobileLine） Authorization 代码库添加到您的 Xcode 项目中

> 无论您使用哪种代码集成方式，都请**配置程序需要脚本**。如果您选择手工集成，则需要先从：[下载地址](http://ios-release-1253960454.cossh.myqcloud.com/tac.zip),下载 移动开发平台（MobileLine）所需要的 SDK 集合文件。并仔细阅读文件中的 Readme.md 文档。



### 1. 在您的项目中集成移动开发平台（MobileLine） SDK，并在您的 Podfile 文件中添加移动开发平台（MobileLine）的私有源。
 
~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

>**注意：**
>一定要添加 [CocoaPods](https://github.com/CocoaPods/Specs) 的原始源，否则会造成部分仓库找不到的问题。

### 2. 添加 TACAuthorization 到您的 Podfile，您可以按照以下方法在 Podfile 中纳入一个 Pod。

~~~
pod 'TACAuthorization'
~~~

权限模块将提供以下第三方集成方式：

* QQ
* WeChat

如果您要使用权限模块的第三方登录功能，则必须集成需要第三方授权的模块。

#### 使用 QQ 第三方登录
 
~~~
pod 'TACAuthorizationQQ'
~~~

该模块依赖 TACSocialQQ 模块，将会自动引入 TACSocialQQ 模块，请查看 TACSocialQQ 的配置手册，并对 TACSocialQQ 进行配置。

#### 使用 WeChat 第三方登录
 
~~~
pod 'TACAuthorizationWechat'
~~~

该模块依赖 TACSocialWechat 模块，将会自动引入 TACSocialWechat 模块，请查看 TACSocialWechat 的配置手册，并对 TACSocialWechat 进行配置。


### 3. 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目。

~~~
$ pod install
$ open your-project.xcworkspace
~~~

### 4. 在 UIApplicationDelegate 子类中导入 TACAuthorization 模块。

Objective-C 示例代码：
~~~
#import <TACAuthorization/TACAuthorization.h>
~~~
Swift 示例代码：
~~~
import TACAuthorization
~~~

如果您使用了第三方登录则需要引入对应模块的头文件才可以使用对应的第三方登录平台的功能。


#### 使用 QQ 第三方登陆

~~~
#import <TACAuthorizationQQ/TACAuthorizationQQ.h>
pod 'TACAuthorizationQQ'
~~~

>**注意：**
`TACAuthorizationQQ`依赖基础模块`TACSocialQQ`,将会自动引入 `TACSocialQQ` 模块，该模块分装了对于 TencentOpenAPI。如果您需要使用 TencentOpenAPI 也可以直接通过 `TACSocialQQ` 来调用，具体的可以参考 `TACSocialQQ` 的编程指南。

#### 使用 WeChat 第三方登陆

~~~
#import <TACAuthorizationWechat/TACAuthorizationWechat.h>
~~~

  >**注意：**
 `TACAuthorizationWechat` 依赖基础模块 `TACSocialWechat`，将会自动引入 `TACSocialWechat` 模块，该模块分装了对于 TencentOpenAPI。如果您需要使用 `libWeChatSDK` 也可以直接通过 `TACSocialWechat` 来调用，具体的可以参考  `TACSocialWechat` 的编程指南。


#### 5. 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置。

一般情况下您使用默认配置就可以了，用一下代码使用默认配置启动 Crash 服务。如果您在引入其它模块的时候，调用了该方法，请不要重复调用。

Objective-C 示例代码：
~~~
    [TACApplication configurate];
~~~
Swift 示例代码：
~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了 Objective-C 的语法特性 Category 和一些 Runtime 的技巧保障了，只有在您引入了 TACAuthorization 模块的时候，才能从 TACApplicaitonOptiosn 里面看到其对应的配置属性，如果你没有引入 TACAuthorization 模块这些属性就不存在，请不要在没有引入 TACAuthorization 模块的时候使用这些配置，这将会导致您编译不通过：

Objective-C 示例代码：
~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.authoriztionOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~

Swift 示例代码：
~~~
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.authoriztionOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~

使用同样的方式您也可以配置第三方登录模块的功能。

## 配置 Authorization 中的配置脚本 (主要为第三方登录模块的配置脚本)

>**注意：**
>如果您已经集成了 TACSicoalQQ 和 TACSocialWehcat 则不需要重复该步骤

 为了配合其他 SDK 的使用，需要 Info.plist 里面注册回调 scheme 和 query scheme。为了方便您快速集成，和减少集成过程中的挫折。我们使用了自动化的技术来执行上报的操作。请确保根据：TACCore集成指南 中的脚本配置章节正确配置了运行脚本，尤其是构建之前运行脚本。

Authorization 没有脚本功能。主要的脚本功能在支付插件中。脚本会自动的帮助您完成以下功能：


1. 根据读取您的 tac_services_configurations_qq 中的 appId 信息按照 `qqwallet[appId]` 的规则增加回调的 scheme。
2. 在 LSApplicationQueriesSchemes 中添加 weixin。
