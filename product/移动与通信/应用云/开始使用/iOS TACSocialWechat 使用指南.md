TACSocialWechat 封装了 [libWeChatSDK](https://open.weixin.qq.com/) 微信开放平台的 SDK，您可以通过引入 TACSocialWechat 来引入微信开放平台能力。同时，TACSocialWechat 提供了更方便的该 SDK 集成方式，请不要重复引入 libWeChatSDK 。

## 准备工作

在开始使用应用云 TACSocialWechat 之前，您需要：

1. 一个启用了应用云的应用。
2. 您集成了 TACCore。

## 将应用云 TACSocialWechat 代码库添加到 Xcode 项目中


### 1. 在您的项目中集成应用云 SDK，并在 Podfile 文件中添加应用云的私有源：
~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> **注意：**
>一定要添加 [CocoaPods](https://github.com/CocoaPods/Specs) 的原始源，否则会造成部分仓库找不到的问题。

### 2. 添加 TACSocialWechat 到您的 Podfile，您可以按照以下方法在 Podfile 中纳入一个 Pod：
 ~~~
pod 'TACSocialWechat'
~~~

### 3. 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目：
~~~
$ pod install
$ open your-project.xcworkspace
~~~

### 4. 在 UIApplicationDelegate 子类中导入 TACSocialWechat 模块：
Objective-C 代码示例：
~~~
#import <TACSocialWechat/TACSocialWechat.h>
~~~

Swift 代码示例：
~~~
import TACSocialWechat
~~~

### 5. 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置：
 
#### 先行配置--引入配置文件

我们使用腾讯云 iOS SDK 统一配置机制,只要您加入 TACSocialWechat 的配置文件，我们会自动化初始化相关的配置和参数。
 
>**注意：**
>所有的配置文件（plist）文件都以 `tac_services_configurations`开始，以扩展名 plist 结束。 我们会加载所有符合正则表达式 `tac_services_configurations*.plist` 的文件，并解析合并。解析顺序为 ASCII 排序，也就是说 ASCII 排序较后的配置文件的参数将会优先生效。

您需要在您的工程中创建以 `tac_services_configurations` 为前缀的 plist 文件，例如：

~~~
tac_services_configurations_wechat.plist
~~~

文件的内容为需要配置的参数信息，请注意 WechatOptions 的配置路径`（:services:social:qq）: `例如配置文件：

~~~
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>services</key>
	<dict>
		<key>social</key>
		<dict>
			<key>wechat</key>
			<dict>
				<key>appID</key>
				<string>wx256642f480c15e3e</string>
			</dict>
		</dict>
	</dict>
</dict>
</plist>

~~~

目前支持的配置为：

| 参数 Key | 参数含义                |
|:--------|:------------------------|:-----|
| appID   | 微信开放平台中程序 appID |

>**注意：** 
>目前不支持通过配置文件将 appKey 直接配置，因为这是个危险的操作。

#### 程序配置

一般情况下您使用默认配置就可以了，用以下代码使用默认配置启动 Crash 服务。如果您在引入其它模块的时候，调用了该方法，请不要重复调用。

Objective-C 代码示例：
~~~
    [TACApplication configurate];
~~~

Swift 代码示例：
~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了 Objective-C 的语法特性 Category 和一些 Runtime 的技巧保障了，只有在您引入了 TACSocialWechat 模块的时候，才能从 TACApplicaitonOptiosn 里面看到其对应的配置属性，如果你没有引入 TACSocialWechat 模块这些属性就不存在，请不要在没有引入 TACSocialWechat 模块的时候使用这些配置，这将会导致您编译不通过：

>**注意：** 
>如果您希望使用我们提供的在终端获取微信用户信息的能力，您需要在这里配置您的 appKey。请注意这是个危险的操作，我们仍然建议您在自己的后台去获取微信用户的信息。

Objective-C 代码示例：
~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.wechatOptions.[Key] = [Value];
    //
		options.wechatOptions.appKey = @"您的appKey";
    [TACApplication configurateWithOptions:options];
~~~

Swift 代码示例：
~~~
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.wechatOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~

#### 配置 TACSocialWechat 中的配置脚本 (主要为第三方登陆模块的配置脚本)

1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 点击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 WechatSetupScripts。
> **注意**
> 请确保 `New Run Script Phase` 脚本在 `Build Phases` 中排序为第二。

4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框。

#### 需要黏贴的代码
~~~
THIRD_FRAMEWORK_PATH=[]
${THIRD_FRAMEWORK_PATH}/Scripts/run
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同：
 
* 如果您使用 Cocoapods 来集成的则为 `${PODS_ROOT}/TACSocialWechat/Scripts/run`。
* 如果您使用手工集成的方式则为 `${SRCROOT}/TACSocialWechat/Scripts/run`。
 

### 6. 使用 libWeChatSDK 的功能：
 
我们已经为您自动化配置好了 libWeChatSDK 的其他功能，包括 HandleOpenURL 等函数的响应，和在 Info.plist 文件中注册相关的回调和 Scheme 等操作，您不需要重复执行该操作。如果您要使用 libWeChatSDK 的功能，您可以引入头文件：

~~~
#import <TACSocialWechat/WXApi.h>
~~~

我们其进行了初始化处理，并配置好了其初始化需要的相关程序功能，请先配置其响应的 delegate：

~~~
[[TACSocialWechatService shareService].delegateProxy addDelegate:delegate];
~~~

其中 delegate 为 TencentOAuth 对象的 delegate，这里我们对原始的 delegate 进行了转发。你可以注册多个 delegate，请在不使用的时候移除：

~~~
[[TACSocialWechatService shareService].delegateProxy removeDelegate:delegate];
~~~
