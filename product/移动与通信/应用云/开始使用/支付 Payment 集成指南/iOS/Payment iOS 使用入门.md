## 准备工作

在开始使用移动开发平台（MobileLine） Payment 之前，您需要：

* 一个启用了移动开发平台（MobileLine）的应用。
* 您集成了 [TACCore](https://cloud.tencent.com/document/product/666/14306)。
* 已经申请好了需要的微信/ QQ 支付对应的商户号、开放平台应用，并在控制台上配置。

## 将移动开发平台（MobileLine） Payment 代码库添加到 Xcode 项目中

>**注意：** 
> 无论您使用哪种代码集成方式，都请配置程序需要脚本。如果您选择手工集成，则需要先从：[下载地址](http://ios-release-1253960454.cossh.myqcloud.com/tac.zip) 下载移动开发平台（MobileLine）所需要的 SDK 集合文件。并仔细阅读文件中的 Readme.md 文档。



### 1. 在您的项目中集成移动开发平台（MobileLine） SDK：

并在您的 Podfile 文件中添加移动开发平台（MobileLine）的私有源：

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> **注意：**
> 一定要添加 [CocoaPods](https://github.com/CocoaPods/Specs) 的原始源，否则会造成部分仓库找不到的问题。

### 2. 添加 TACPayment 到您的 Podfile，您可以按照以下方法在 Podfile 中纳入一个 Pod：

~~~
pod 'TACPayment'
~~~

### 3. 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目：

~~~
$ pod install
$ open your-project.xcworkspace
~~~

### 4. 在 UIApplicationDelegate 子类中导入 TACPayment 模块：

Objective-C 代码示例：
~~~
#import <TACPayment/TACPayment.h>
~~~
Swift 代码示例：
~~~
import TACPayment
~~~


### 5. 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置：

一般情况下您使用默认配置就可以了，用以下代码使用默认配置启动 Payment 服务。如果您在引入其它模块的时候，调用了该方法，请不要重复调用。
Objective-C 代码示例：
~~~
    [TACApplication configurate];
~~~
Swift 代码示例：
~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了 Objective-C 的语法特性 Category 和一些 Runtime 的技巧保障了，只有在您引入了 TACPayment 模块的时候，才能从 TACApplicaitonOptiosn 里面看到其对应的配置属性，如果你没有引入 TACPayment 模块这些属性就不存在，请不要在没有引入 TACPayment 模块的时候使用这些配置，这将会导致您编译不通过：

Objective-C 代码示例：
~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.paymentOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~

Swift 代码示例：
~~~
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.paymentOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~

### 6. 配置 URL Schemes
在 Xcode 中，选择工程设置项，选中 "TARGETS" 一栏，在 "Info" 标签栏的 "URL Types" 添加 "URL Schemes"。    

如果使用微信支付，填入微信跳转回本 App 所使用的 URL Scheme（建议直接使用注册的微信应用 ID）。    

同样的，如果使用QQ钱包支付，也需填入手机 QQ 跳转回本 App 所使用的 URL Scheme（建议使用注册的 QQ 应用 ID，并加上自定义的字母前缀）。    
这里需要注意的是，URL Scheme 的首字母必须是英文字母，建议添加与业务相关的特殊字符，以避免与其他程序冲突。    
