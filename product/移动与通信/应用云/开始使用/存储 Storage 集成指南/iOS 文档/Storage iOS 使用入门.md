
## 准备工作

在开始使用移动开发平台（MobileLine） Storage之前，您需要：

1. 一个启用了移动开发平台（MobileLine）的应用。
2. 您集成了 TACCore。

## 将移动开发平台（MobileLine） Storage 代码库添加到您的 Xcode 项目中

> 无论您使用哪种代码集成方式，都请**配置程序需要脚本**。如果您选择手工集成，则需要先从：[下载地址](http://ios-release-1253960454.cossh.myqcloud.com/tac.zip),下载 移动开发平台（MobileLine）所需要的 SDK 集合文件。并仔细阅读文件中的 Readme.md 文档。


### 1. 在您的项目中集成移动开发平台（MobileLine） SDK。

并在您的 Podfile 文件中添加移动开发平台（MobileLine）的私有源：

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

>** 注意:**
>一定要添加 [CocoaPods](https://github.com/CocoaPods/Specs) 的原始源，否则会造成部分仓库找不到的问题。

### 2. 添加 TACStorage 到您的 Podfile，您可以按照以下方法在 Podfile 中纳入一个 Pod。

~~~
pod 'TACStorage"
~~~

### 3. 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目。

~~~
$ pod install
$ open your-project.xcworkspace
~~~

### 4. 在 UIApplicationDelegate 子类中导入 TACStorage 模块。

Objective-C 代码示例：
~~~
#import <TACStorage/TACStorage.h>
~~~

Swift 代码示例：
~~~
import TACStorage
~~~


### 5. 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置。

一般情况下您使用默认配置就可以了，用以下代码使用默认配置启动 Crash 服务。如果您在引入其它模块的时候，调用了该方法，请不要重复调用。

Objective-C 代码示例：
~~~
    [TACApplication configurate];
~~~

Swift 代码示例：
~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了 Objective-C 的语法特性 Category 和一些 Runtime 的技巧，保障了只有在您引入了 TACStorage 模块的时候，才能从 TACApplicaitonOptiosn 里面看到其对应的配置属性，如果你没有引入 TACStorage 模块这些属性就不存在，请不要在没有引入 TACStorage 模块的时候使用这些配置，这将会导致您编译不通过：

Objective-C 代码示例：
~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.storageOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~
Swift 代码示例：
~~~
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.storageOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~

### 6. 配置 TACStorage 的使用权限。

TACStorage 后台为腾讯云 COS 服务，在使用 COS 服务的时候需要对请求进行权限校验，来确保对应的请求是否有权限访问对应的资源。因而您需要在您的代码中实现 `QCloudCredentailFenceQueueDelegate` 协议来提供相关的权限信息。

~~~
@interface TACStorageDemoViewController () <QCloudCredentailFenceQueueDelegate>
@end

@implementation  TACStorageDemoViewController
- (void) fenceQueue:(QCloudCredentailFenceQueue *)queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock
{
    QCloudCredential* crendential = [[QCloudCredential alloc] init];

    // 在调试阶段您可以通过直接设置secretID和secretKey来测试服务，但是强烈不建议在线上环境使用该方式！！！
#ifdef ! DEBUG
    QCloudCredential* crendential = [[QCloudCredential alloc] init];
    crendential.secretID = <#secretID#>;
    crendential.secretKey = <#secretKey#>;
    QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:crendential];
    continueBlock(creator, nil);
#else

    //您需要配置自己的服务器，来获取CAM临时密钥。并通过临时密钥来创建权限Creator。具体可以参考：[快速搭建移动应用传输服务](https://cloud.tencent.com/document/product/436/9068)
    void(^NetworkCall)(id response, NSError* error) = ^(id response, NSError* error) {
        if (error) {
            continueBlock(nil, error);
        } else {
            QCloudCredential* crendential = [[QCloudCredential alloc] init];
            crendential.secretID = @"AKIDPiqmW3qcgXVSKN8jngPzRhvxzYyDL5qP";
            crendential.secretKey = @"EH8oHoLgpmJmBQUM1Uoywjmv7EFzd5OJ";
            crendential.experationDate = nil;
            crendential.token = ;
            QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:crendential];
            continueBlock(creator, nil);
        }

    };
    <#do network with callback:NetworkCall #>
#endif
}
@end
~~~
