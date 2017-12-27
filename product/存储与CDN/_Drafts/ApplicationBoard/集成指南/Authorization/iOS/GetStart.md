在 iOS 中开始使用 应用云 Authorization

> 按照本指南在您的 iOS 应用中设置 应用云 Authorization。


## 准备工作

在开始使用应用云 Authorization 之前，您需要：

1. 一个启用了 应用云 的应用
2. 您集成了TACCore

## 将应用云 Authorization 代码库添加到您的Xcode项目中


##### （1）在您的项目中集成 应用云 SDK

并在您的 Podfile 文件中添加 应用云 的私有源

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> 注意一定要添加 https://github.com/CocoaPods/Specs 的原始源，否则会造成部分仓库找不到的问题

##### （2) 添加 TACAuthorization 到您的 Podfile。您可以按照以下方法在 Podfile 中纳入一个 Pod：

~~~
pod 'TACAuthorization'
~~~

权限模块将提供以下第三方集成方式：

1. QQ
2. WeChat

如果您要使用权限模块的第三方登陆功能，则必须集成需要第三方授权的模块：

###### 使用QQ第三方登陆

~~~
pod 'TACAuthorizationQQ'
~~~

该模块依赖 TACSocialQQ 模块，将会自动引入 TACSocialQQ 模块，请查看 TACSocialQQ 的配置手册，并对 TACSocialQQ 进行配置。

###### 使用WeChat第三方登陆

~~~
pod 'TACAuthorizationWechat'
~~~

该模块依赖 TACSocialWechat 模块，将会自动引入 TACSocialWechat 模块，请查看 TACSocialWechat 的配置手册，并对 TACSocialWechat 进行配置。


##### (3) 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目。

~~~
$ pod install
$ open your-project.xcworkspace
~~~

##### (4)在 UIApplicationDelegate 子类中导入 TACAuthorization 模块：

~~~objective-c
#import <TACAuthorization/TACAuthorization.h>
~~~

~~~swift
import TACAuthorization
~~~

如果您使用了第三方登陆则需要引入对应模块的头文件才可以使用对应的第三方登录平台的功能：


###### 使用QQ第三方登陆

~~~
#import <TACAuthorizationQQ/TACAuthorizationQQ.h>
pod 'TACAuthorizationQQ'
~~~

>  `TACAuthorizationQQ`依赖基础模块`TACSocialQQ`。将会自动引入 `TACSocialQQ` 模块。该模块分装了对于TencentOpenAPI。如果您需要使用TencentOpenAPI也可以直接通过 `TACSocialQQ` 来调用。具体的可以参考  `TACSocialQQ` 的编程指南。

###### 使用WeChat第三方登陆

~~~
#import <TACAuthorizationWechat/TACAuthorizationWechat.h>
~~~

>  `TACAuthorizationWechat`依赖基础模块`TACSocialWechat`。将会自动引入 `TACSocialWechat` 模块。该模块分装了对于TencentOpenAPI。如果您需要使用 `libWeChatSDK` 也可以直接通过 `TACSocialWechat` 来调用。具体的可以参考  `TACSocialWechat` 的编程指南。


##### (5) 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置

一般情况下您使用默认配置就可以了，用一下代码使用默认配置启动Crash服务。如果您在引入其它模块的时候，调用了该方法。请不要重复调用。

~~~objective-c
    [TACApplication configurate];
~~~

~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了Objective-C的语法特性Category和一些Runtime的技巧保障了，只有在您引入了 TACAuthorization模块的时候，才能从TACApplicaitonOptiosn里面看到其对应的配置属性，如果你没有引入TACAuthorization模块这些属性就不存在，请不要在没有引入TACAuthorization模块的时候使用这些配置，这将会导致您编译不通过：

~~~objective-c
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.authoriztionOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~

~~~swift
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.authoriztionOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~

使用同样的方式您也可以配置第三方登陆模块的功能

## 配置 Authorization 中的配置脚本 (主要为第三方登陆模块的配置脚本)

> 您添加了多个第三方权限模块，则需要重复本操作多次。

1. 在导航栏中打开您的工程
2. 打开Tab `Build Phases`
3. 点击 `Add a new build phase` , 并选择 `New Run Script Phase`. **请确保该脚本在 `Build Phases` 中排序为第二!!!!**。您可以将改脚本命名为您引入的第三方登陆模块的名称，比如QQSetupScripts、WechatSetupScripts....
4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:

### 需要黏贴的代码

~~~
THIRD_FRAMEWORK_PATH=[]
${THIRD_FRAMEWORK_PATH}/Scripts/run
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同

1. 如果您使用Cocoapods来集成的则为 `${PODS_ROOT}/[第三方登录模块名称]/Scripts/run`
  1. 如果您使用了QQ则为 `${PODS_ROOT}/TACSocialQQ/Scripts/run`
  2. 如果您使用了WeChat则为  `${PODS_ROOT}/TACSocialWechat/Scripts/run`
2. 如果您使用 手工集成 的方式则为 `${SRCROOT}/[第三方登录模块相对于工程根目录的路径]/Scripts/run`
