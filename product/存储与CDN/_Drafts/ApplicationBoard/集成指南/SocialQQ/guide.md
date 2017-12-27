在 iOS 中开始使用 应用云 TACSocialQQ

 >  TACSocialQQ 封装了 [TencentOpenAPI](wiki.connect.qq.com/ios_sdk环境搭建) -- QQ互联 的SDK，您可以通过引入TACSocialQQ来引入 QQ 互联能力。同时，TACSocialQQ提供了更方便的改SDK集成方式。请不要重复引入 TencentOpenAPI 。

## 准备工作

在开始使用应用云 TACSocialQQ 之前，您需要：

1. 一个启用了 应用云 的应用
2. 您集成了TACCore

## 将应用云 TACSocialQQ 代码库添加到您的Xcode项目中


##### （1）在您的项目中集成 应用云 SDK

并在您的 Podfile 文件中添加 应用云 的私有源

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> 注意一定要添加 https://github.com/CocoaPods/Specs 的原始源，否则会造成部分仓库找不到的问题

##### （2) 添加 TACSocialQQ 到您的 Podfile。您可以按照以下方法在 Podfile 中纳入一个 Pod：

~~~
pod 'TACSocialQQ"
~~~

##### (3) 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目。

~~~
$ pod install
$ open your-project.xcworkspace
~~~

##### (4)在 UIApplicationDelegate 子类中导入 TACSocialQQ 模块：

~~~objective-c
#import <TACSocialQQ/TACSocialQQ.h>
~~~

~~~swift
import TACSocialQQ
~~~


##### (5) 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置


###### 先行配置--引入配置文件

我们使用腾讯云 iOS SDK 统一配置机制。只要您加入 TACSocialQQ 的配置文件，我们会自动化初始化相关的配置和参数。

> 所有的配置文件（plist）文件都以 `tac_services_configurations`开始，以扩展名plist结束。 我们会加载所有符合正则表达式 `tac_services_configurations*.plist` 的文件，并解析合并。解析顺序为ASCII排序，也就是说ASCII排序较后的配置文件的参数将会优先生效。

您需要在您的工程中创建以 `tac_services_configurations` 为前缀的 plist文件，例如：

~~~
tac_services_configurations_qq.plist
~~~

文件的内容为需要配置的参数信息，请注意 QQOptions 的配置路径（:services:social:qq）: 例如配置文件

~~~
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>services</key>
	<dict>
		<key>social</key>
		<dict>
			<key>qq</key>
			<dict>
				<key>appID</key>
				<string>请填充您的AppID</string>
				<key>appKey</key>
				<string>请填充您的APPKey</string>
				<key>permissions</key>
				<array>
					<string>get_user_info</string>
					<string>get_simple_userinfo</string>
					<string>add_t</string>
				</array>
			</dict>
		</dict>
	</dict>
</dict>
</plist>

~~~

目前支持的配置为：

| 参数Key     | 参数含义                             | 附注 |
|:------------|:-------------------------------------|:-----|
| appID       | QQ互联中程序的AppID                  |      |
| appKey      | QQ互联中程序的AppKey                 |      |
| permissions | 进行qq授权的时候，需要申请的权限列表 |      |



###### 程序配置

一般情况下您使用默认配置就可以了，用一下代码使用默认配置启动Crash服务。如果您在引入其它模块的时候，调用了该方法。请不要重复调用。

~~~objective-c
    [TACApplication configurate];
~~~

~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了Objective-C的语法特性Category和一些Runtime的技巧保障了，只有在您引入了 TACSocialQQ模块的时候，才能从TACApplicaitonOptiosn里面看到其对应的配置属性，如果你没有引入TACSocialQQ模块这些属性就不存在，请不要在没有引入TACSocialQQ模块的时候使用这些配置，这将会导致您编译不通过：

~~~objective-c
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.qqOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~

~~~swift
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.qqOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~

###### 配置 TACSocialQQ 中的配置脚本 (主要为第三方登陆模块的配置脚本)


1. 在导航栏中打开您的工程
2. 打开Tab `Build Phases`
3. 点击 `Add a new build phase` , 并选择 `New Run Script Phase`. **请确保该脚本在 `Build Phases` 中排序为第二!!!!**。您可以将改脚本命名QQSetupScripts.
4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:

####### 需要黏贴的代码

~~~
THIRD_FRAMEWORK_PATH=[]
${THIRD_FRAMEWORK_PATH}/Scripts/run
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同：

1. 如果您使用Cocoapods来集成的则为 `${PODS_ROOT}/TACSocialQQ/Scripts/run`
2. 如果您使用 手工集成 的方式则为 `${SRCROOT}/TACSocialQQ/Scripts/run`


#### （6） 使用 TencentOpenApi 的功能

 > 我们已经为您自动化配置好了 TencentOpenApi 的其他功能，包括HandleOpenURL等函数的响应，和在Info.plist文件中注册相关的回调和Scheme等操作，您不需要重复执行该操作

如果您要使用 TencentOpenApi 的功能，您可以引入头文件：

~~~
#import <TACSocialQQ/TencentOpenAPI/TencentOAuth.h>
~~~

我们其进行了初始化处理，并生成了一个 TencentOAuth  的对象，存储在 TACSociallQQService 中如果您要手动使用其相关的功能。请先配置 其响应的delegate

~~~
[[TACSocialQQService defaultService].tencentOAuthDelegate addDelegate:delegate]
~~~

其中delegate为TencentOAuth对象的delegate，这里我们对原始的delegate进行了转发。你可以注册多个delegate。请在不使用的时候移除：

~~~
[[TACSocialQQService defaultService].tencentOAuthDelegate removeDelegate:delegate]
~~~
