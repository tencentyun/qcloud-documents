在 iOS 中开始使用 应用云 Messaging

## 准备工作

在开始使用应用云 Messaging 之前，您需要：

1. 一个启用了 应用云 的应用
2. 您集成了TACCore

## 将应用云 Messaging 代码库添加到您的Xcode项目中


##### （1）在您的项目中集成 应用云 SDK

并在您的 Podfile 文件中添加 应用云 的私有源

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> 注意一定要添加 https://github.com/CocoaPods/Specs 的原始源，否则会造成部分仓库找不到的问题

##### （2) 添加 TACMessaging 到您的 Podfile。您可以按照以下方法在 Podfile 中纳入一个 Pod：

~~~
pod 'TACMessaging"
~~~

##### (3) 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目。

~~~
$ pod install
$ open your-project.xcworkspace
~~~

##### (4)在 UIApplicationDelegate 子类中导入 TACMessaging 模块：

~~~objective-c
#import <TACMessaging/TACMessaging.h>
~~~

~~~swift
import TACMessaging
~~~


##### (5) 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置

一般情况下您使用默认配置就可以了，用一下代码使用默认配置启动Crash服务。如果您在引入其它模块的时候，调用了该方法。请不要重复调用。

~~~objective-c
    [TACApplication configurate];
~~~

~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了Objective-C的语法特性Category和一些Runtime的技巧保障了，只有在您引入了 TACMessaging模块的时候，才能从TACApplicaitonOptiosn里面看到其对应的配置属性，如果你没有引入TACMessaging模块这些属性就不存在，请不要在没有引入TACMessaging模块的时候使用这些配置，这将会导致您编译不通过：

~~~objective-c
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.messagingOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~

~~~swift
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.messagingOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~
