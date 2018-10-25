在 iOS 中开始使用 应用云 Storage

## 准备工作

在开始使用应用云 Storage之前，您需要：

1. 一个启用了 应用云 的应用
2. 您集成了TACCore

## 将应用云 Storage 代码库添加到您的Xcode项目中


##### （1）在您的项目中集成 应用云 SDK

并在您的 Podfile 文件中添加 应用云 的私有源

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> 注意一定要添加 https://github.com/CocoaPods/Specs 的原始源，否则会造成部分仓库找不到的问题

##### （2) 添加 TACStorage 到您的 Podfile。您可以按照以下方法在 Podfile 中纳入一个 Pod：

~~~
pod 'TACStorage"
~~~

##### (3) 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目。

~~~
$ pod install
$ open your-project.xcworkspace
~~~

##### (4)在 UIApplicationDelegate 子类中导入 TACStorage 模块：

~~~objective-c
#import <TACStorage/TACStorage.h>
~~~

~~~swift
import TACStorage
~~~


##### (5) 配置 TACApplication 共享实例，通常是在 `application:didFinishLaunchingWithOptions:` 方法中配置

一般情况下您使用默认配置就可以了，用一下代码使用默认配置启动Crash服务。如果您在引入其它模块的时候，调用了该方法。请不要重复调用。

~~~objective-c
    [TACApplication configurate];
~~~

~~~
	TACApplication.configurate();
~~~

如果您需要进行自定义的配置，则可以使用以下方法，我们使用了Objective-C的语法特性Category和一些Runtime的技巧保障了，只有在您引入了 TACStorage模块的时候，才能从TACApplicaitonOptiosn里面看到其对应的配置属性，如果你没有引入TACStorage模块这些属性就不存在，请不要在没有引入TACStorage模块的时候使用这些配置，这将会导致您编译不通过：

~~~objective-c
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	//     options.storageOptions.[Key] = [Value];
    //
    [TACApplication configurateWithOptions:options];
~~~

~~~swift
	let options = TACApplicationOptions.default()
	// 自定义配置
	// options?.storageOptions.[Key] = [Value];
	TACApplication.configurate(with: options);
~~~

##### （6） 配置 TACStorage 的使用权限

TACStorage 后台为腾讯云COS服务，在使用COS服务的时候需要对请求进行权限校验，来确保对应的请求是否有权限访问对应的资源。因而您需要在您的代码中实现 `QCloudCredentailFenceQueueDelegate` 协议来提供相关的权限信息。

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
