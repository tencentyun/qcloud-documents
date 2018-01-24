TACSocialQQ 封装了 [TencentOpenAPI](wiki.connect.qq.com/ios_sdk环境搭建) QQ 互联的 SDK，您可以通过引入 TACSocialQQ 来引入 QQ 互联能力。同时，TACSocialQQ 提供了更方便的改 SDK 集成方式，请不要重复引入 TencentOpenAPI 。

## 准备工作

在开始使用应用云 TACSocialQQ 之前，您需要：

1. 一个启用了应用云的应用。
2. 您集成了 TACCore。

## 将应用云 TACSocialQQ 代码库添加到您的 Xcode 项目中


### 1.在您的项目中集成应用云 SDK，并在您的 Podfile 文件中添加应用云的私有源：
 
~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> **注意：**
一定要添加 https://github.com/CocoaPods/Specs 的原始源，否则会造成部分仓库找不到的问题。

### 2.添加 TACSocialQQ 到您的 Podfile，您可以按照以下方法在 Podfile 中纳入一个 Pod：
 
~~~
pod 'TACSocialQQ"
~~~

### 3.安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目：
 
~~~
$ pod install
$ open your-project.xcworkspace
~~~

### 4.在 UIApplicationDelegate 子类中导入 TACSocialQQ 模块：
Objective-C 代码示例：
~~~
import <TACSocialQQ/TACSocialQQ.h>
~~~
Swift 代码示例：
~~~
import TACSocialQQ
~~~


### 5.配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置：
 

#### 先行配置--引入配置文件

我们使用腾讯云 iOS SDK 统一配置机制。只要您加入 TACSocialQQ 的配置文件，我们会自动化初始化相关的配置和参数。

>**注意：**
> 所有的配置文件（plist）文件都以 `tac_services_configurations` 开始，以扩展名 plist 结束。 我们会加载所有符合正则表达式 `tac_services_configurations*.plist` 的文件，并解析合并。解析顺序为 ASCII 排序，也就是说ASCII排序较后的配置文件的参数将会优先生效。

您需要在您的工程中创建以 `tac_services_configurations` 为前缀的 plist 文件，例如：

~~~
tac_services_configurations_qq.plist
~~~

文件的内容为需要配置的参数信息，请注意 QQOptions 的配置路径（:services:social:qq）: 例如配置文件：
 
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
				<string>请填充您的 AppID</string>
				<key>appKey</key>
				<string>请填充您的 APPKey</string>
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

| 参数Key     | 参数含义                             | 
|:------------|:-------------------------------------|:-----|
| appID       | QQ 互联中程序的 appID                  |      
| appKey      | QQ 互联中程序的 appKey                 |      
| permissions | 进行 QQ 授权的时候，需要申请的权限列表 |      



#### 程序配置

一般情况下您使用默认配置就可以了，用以下代码使用默认配置启动 Crash 服务。如果您在引入其它模块的时候，调用了该方法，请不要重复调用。

~~~objective-c
    [TACApplication configurate];
~~~

~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了 Objective-C 的语法特性 Category 和一些 Runtime 的技巧保障了，只有在您引入了 TACSocialQQ 模块的时候，才能从 TACApplicaitonOptiosn 里面看到其对应的配置属性，如果你没有引入 TACSocialQQ 模块这些属性就不存在，请不要在没有引入 TACSocialQQ 模块的时候使用这些配置，这将会导致您编译不通过：

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

#### 配置 TACSocialQQ 中的配置脚本 (主要为第三方登陆模块的配置脚本)


1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 点击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 QQSetupScripts。
> **注意：**
请确保该脚本在 `Build Phases` 中排序为第二。
4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:。

#### 需要黏贴的代码

~~~
THIRD_FRAMEWORK_PATH=[]
${THIRD_FRAMEWORK_PATH}/Scripts/run
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同：
 
* 如果您使用 Cocoapods 来集成的则为 `${PODS_ROOT}/TACSocialQQ/Scripts/run`。
* 如果您使用 手工集成 的方式则为 `${SRCROOT}/TACSocialQQ/Scripts/run`。


#### 6.使用 TencentOpenApi 的功能。

我们已经为您自动化配置好了 TencentOpenApi 的其他功能，包括 HandleOpenURL 等函数的响应，和在 Info.plist 文件中注册相关的回调和 Scheme 等操作，您不需要重复执行该操作。如果您要使用 TencentOpenApi 的功能，您可以引入头文件：

~~~
#import <TACSocialQQ/TencentOpenAPI/TencentOAuth.h>
~~~

我们其进行了初始化处理，并生成了一个 TencentOAuth  的对象，存储在 TACSociallQQService 中如果您要手动使用其相关的功能，请先配置其响应的 delegate：

~~~
[[TACSocialQQService defaultService].tencentOAuthDelegate addDelegate:delegate]
~~~

其中 delegate 为 TencentOAuth 对象的 delegate，这里我们对原始的 delegate 进行了转发。你可以注册多个 delegate，请在不使用的时候移除：

~~~
[[TACSocialQQService defaultService].tencentOAuthDelegate removeDelegate:delegate]
~~~
