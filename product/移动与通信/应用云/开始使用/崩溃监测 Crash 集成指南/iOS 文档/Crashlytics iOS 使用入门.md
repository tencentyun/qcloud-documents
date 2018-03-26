
## 准备工作

在开始使用移动开发平台（MobileLine） Crashlytics 之前，您需要：

* 一个启用了移动开发平台（MobileLine）的应用。
* 您集成了 [TACCore](https://cloud.tencent.com/document/product/666/14306)。

## 配置 Crashlytics 中的脚本
<<<<<<< HEAD
为了配合其它SDK的使用，需要在Info.plist里面注册一些额外的信息。为了方便您快速集成，和减少集成过程中的挫折。我们使用了自动化的技术来执行上报的操作。请确保根据：[TACCore集成指南](https://cloud.tencent.com/document/product/666/14306) 中的脚本配置章节正确配置了运行脚本，尤其是构建之前运行脚本。
=======
为了配合其它SDK的使用，需要在Info.plist里面注册一些额外的信息。为了方便您快速集成，和减少集成过程中的挫折。我们使用了自动化的技术来执行上报的操作。请确保根据：[TACCore集成指南](https://cloud.tencent.com/document/product/666/14299) 中的脚本配置章节正确配置了运行脚本，尤其是构建之前运行脚本。
>>>>>>> TAC iOS连接修改


## 将移动开发平台（MobileLine） Crashlytics 代码库添加到 Xcode 项目中

> 无论您使用哪种代码集成方式，都请**配置程序需要脚本**。如果您选择手工集成，则需要先从：[下载地址](http://ios-release-1253960454.cossh.myqcloud.com/tac.zip),下载 移动开发平台（MobileLine）所需要的 SDK 集合文件。并仔细阅读文件中的 Readme.md 文档。


### 1. 在您的项目中集成移动开发平台（MobileLine） SDK：
 
并在您的 Podfile 文件中添加移动开发平台（MobileLine）的私有源：

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> **注意：**
   一定要添加 [CocoaPods](https://github.com/CocoaPods/Specs) 的原始源，否则会造成部分仓库找不到的问题。
 
### 2. 添加 TACCrash 到您的 Podfile，您可以按照以下方法在 Podfile 中纳入一个 Pod：
 
~~~
pod 'TACCrash'
~~~

### 3. 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目：
 
~~~
$ pod install
$ open your-project.xcworkspace
~~~

### 4. 在 UIApplicationDelegate 子类中导入 TACCrash 模块：
 
Objective-C 代码示例：
~~~
#import <TACCrash/TACCrash.h>
~~~
Swift 代码示例：
~~~
import TACCrash
~~~


### 5. 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置：
 
一般情况下您使用默认配置就可以了，用一下代码使用默认配置启动 Crash 服务。如果您在引入其它模块的时候，调用了该方法，请不要重复调用。
Objective-C 代码示例：
~~~
    [TACApplication configurate];
~~~
Swift 代码示例：
~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了 Objective-C 的语法特性 Category 和一些 Runtime 的技巧保障了，只有在您引入了 TACCrash 模块的时候，才能从 TACApplicaitonOptiosn 里面看到其对应的配置属性，如果你没有引入 TACCrash 模块这些属性就不存在，请不要在没有引入 TACCrash 模块的时候使用这些配置，这将会导致您编译不通过：

Objective-C 代码示例：
~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.crashOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~

Swift 代码示例：
~~~
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.crashOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~


## 配置 Crashlytics 上报符号表脚本

Crashlytics 需要在您编译成功上上传符号表以方便解析。我们使用了自动化的技术来执行上报的操作。请确保根据：[TACCore 集成指南]() 中的脚本配置章节正确配置了运行脚本，尤其是构建之后运行脚本。
