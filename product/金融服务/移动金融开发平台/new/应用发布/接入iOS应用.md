## SDK集成[](id:sdkjc)
* [前置条件](#qztj)
* [集成方式](#jcfs)
  * [CocoaPods 集成 SDK](#cocoapods-sdk)
  * [手动集成 SDK](#sdjc-sdk)

### 前置条件[](id:qztj)
- **环境要求**
  - `iOS` >= 8.0
  - `Xcode` >= 10.0
- **组件依赖**
  - `Tars`
  - `TMFInstruction`
  - `TMFShark`
  - `TMFSSL`
  - `MQQComponents`
  - `MQQTcc`
  - `openssl`
  - `TMFXlog`

### 集成方式[](id:jcfs)
`TMFDistribution` 的集成方式有以下 2 种，可选择其一进行集成：
- CocoaPods 集成 SDK（离线 Pod）
- 手动集成 SDK

### CocoaPods 集成 SDK[](id:cocoapods-sdk)
- 在您项目中的 `Podfile` 文件里添加如下内容：
```objective-c
target 'YourTarget' do

# 依赖组件
pod 'Tars',                 :path => './Frameworks/Tars'
pod 'TMFInstruction',       :path => './Frameworks/TMFInstruction'
pod 'TMFShark',             :path => './Frameworks/TMFShark'
pod 'openssl',              :path => './Frameworks/openssl'
pod 'MQQTcc',               :path => './Frameworks/MQQTcc'
pod 'MQQComponents',        :path => './Frameworks/MQQComponents'
pod 'TMFSSL',               :path => './Frameworks/TMFSSL'
pod 'TMFXlog',    					:path => './Frameworks/TMFXlog'

# TMFDistribution
pod 'TMFDistribution',      :path => './Frameworks/TMFDistribution'

end
```
其中：
  - `YourTarget` 为您的项目需要引入 `TMFDistribution` 的 target 的名字。
  - `:path => ` 指向的路径，为当前组件的 `.podspec` 文件所在目录与 `Podfile` 文件的**相对路径**。
    例如，上面示例中的 `'./Frameworks/TMFDistribution'` 为 `TMFDistribution.podspec` 文件所在目录的相对路径。
- Terminal `cd` 到 Podfile 文件所在目录，并执行 `pod install` 进行组件安装。
```shell
$ pod install
```

### 手动集成 SDK[](id:sdjc-sdk)
1. 把 `TMFDistribution` 组件的目录添加到您项目的 Xcode Project 中的合适位置，并选择合适的 target。
  您可以把组件的目录从 Finder 直接拖动到 Xcode Project 中，以进行快捷添加。
>?手动集成 SDK 不要引入 `LICENSE` 与 `podspec` 等无关文件到项目中。
>
![](https://qcloudimg.tencent-cloud.cn/raw/1bb1d31989203e10087b19046f8eceea.png)
![](https://qcloudimg.tencent-cloud.cn/raw/5c6ec14e41ba269a67bb12f84e5e3a48.png)
2. 把 `TMFDistribution` 依赖的所有组件添加到项目中，依赖的组件列表，请参见前置条件中的 [组件依赖](#qztj)。
3. 添加 `TMFDistribution` 依赖的系统库。
  在 Xcode 中打开 project 设置页，选中相关的 target，单击 **General**，在“Linked Frameworks and Libraries”中进行添加。
  **系统库依赖**
  - `Foundation.framework`
  - `UIKit.framework`
  - `Security.framework`
  - `CoreTelephony.framework`
  - `SystemConfiguration.framework`
  - `CoreFoundation.framework`
  - `libsqlite3.tdb`
  - `libc++.tdb`
  - `libc.tbd`
  - `libz.1.2.5.tbd`
![](https://qcloudimg.tencent-cloud.cn/raw/d00f839fd033cc8c2ce0c25d33a67b2b.png)
4. **Project 设置**
  添加 `TMFDistribution` 之后，需要进行相关的 Project 设置。
  在 Xcode 中打开 Project 设置页，选中相关的 target，进行以下设置：
  - 选择 **Build Settings** > **Linking** > **Other Linker Flags**，增加：
    - `-ObjC`
  - 选择 **Build Settings** > **Apple Clang - Custom Compiler Flags** > **Other C Flags**，增加：
    - `-fshort-wchar`
    - `-D__FIXWCHART__`
  - 选择 **Build Settings** > **Apple Clang - Custom Compiler Flags** > **Other C++ Flags**，增加：
    - `-fshort-wchar`
    - `-D__FIXWCHART__`



## SDK使用
### 初始化[](id:csh)
使用组件前，需要完成的基本初始化操作。

#### 前置条件
- 若要通过组件初始化，必须先完成 SDK 集成，详情请参见 [集成 SDK](#sdkjc)。
- 请确保启动后在云指令组件 `TMFInstruction` 初始化之前初始化本组件。

#### 引入头文件
```objective-c
#import "TMFDistribution.h"
```

#### 初始化
早期版本应用发布任务推拉是依赖数据同步组件来完成的，从公有云版本起，应用发布支持直接使用移动网关来实现任务推拉，可以解除任务推拉对数据同步组件的依赖。不过本次协议调整对新版服务有依赖，考虑到私有化客户不同的服务版本，SDK侧做了兼容，同时保留了两套协议实现，客户在初始化时根据自身服务情况指定协议版本即可。
```objective-c
+ (instancetype)sharedManager;
- (void)initialize;
```
```objective-c
/**
 @brief 应用发布推送协议
 */
typedef NS_ENUM(NSInteger, TMFDistributionPushPassagePolicy) {
    TMFDistributionPushPassagePolicyConch   = 0,    // default 旧协议
    TMFDistributionPushPassagePolicyShark   = 1,
};
```
```objective-c
/**
 *  @brief  使新协议传入回调
 *
 *  @note 初始化时SDK未拉取更新单，需要App调用自动/手动检查更新
 */
- (void)initWithDistributionHandler:(TMFDistributionHandler)handler
             TMFDistributionPushMsg:(TMFDistributionPushPassagePolicy)pushMsg;
```

#### 初始化示例
```objective-c
// AppDelegate.m

[[TMFDistributionManager sharedManager] initialize];
// 新协议
[[TMFDistributionManager sharedManager] initWithDistributionHandler:nil TMFDistributionPushMsg:TMFDistributionPushPassagePolicyShark];
```



### 发布监听
对发布更新监听，弹出更新推送弹窗。
主动拉取支持两种方式：
- 自动检查更新：该方式会检查弹窗频率限制，更新结果通过初始化传入的TMFDistributionHandler回调给开发者。
- 手动检查更新：该方式不会检查弹窗评率限制，检查更新结果会通过独立设置的TMFDistributionSharkCallBack回调给开发者。使用场景是应用内的**检查更新**菜单，由用户触发。

#### 前置条件
若要执行发布监听，必须先完成组件初始化，详情请参见 [初始化](#csh)。

#### 监听设置
通过实现监听接口，通过接口回调，监听应用发布更新。

**接口定义**
```objective-c
- (void)setDidReceiveDistributionHandler:(TMFDistributionHandler)handler;
```

其中，`TMFDistributionHandler` 的定义如下：
```objective-c
typedef void (^TMFDistributionHandler)(
    TMFDistributionInfo * _Nullable info, 
    TMFDistributionCompletionBlock completionHandler
);
```
其中，`TMFDistributionCompletionBlock` 的定义如下：
```objective-c
typedef void (^TMFDistributionCompletionBlock)(
    BOOL updated
);
```
- 参数
<table>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
<th>必选</th>
</tr>
<tr>
<td>handler</td>
<td>`TMFDistributionHandler`(block)</td>
<td>监听回调，详见 <a href="#handler">handler 回调</a></td>
<td>YES</td>
</tr>
<table>
- handler 回调[](id:handler)
<table>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
<th>必选</th>
</tr>
<tr>
<td>info</td>
<td>`TMFDistributionInfo *`</td>
<td>更新数据对象，用于储存当次更新的数据信息，详见  <a href="#sjdx">数据对象</a>。</td>
<td>NO</td>
</tr>
<tr>
<td>completionHandler</td>
<td>`TMFDistributionCompletionBlock`(block) </td>
<td>业务操作回调，通知组件是否同意发起更新，详见  <a href="#completionHandler">completionHandler 回调</a>。</td>
<td>YES</td>
</tr>
<table>
- completionHandler 回调[](id:completionHandler)
<table>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
<th>必选</th>
</tr>
<tr>
<td>updated</td>
<td>`BOOL`</td>
<td>自定义 Handler 的完成回调，在自定义 Handler 中调用，通知组件是否同意发起更新</td>
<td>YES</td>
</tr>
<table>

#### 数据对象[](id:sjdx)
数据对象支持复制，序列化。
```objective-c
@interface TMFDistributionInfo : NSObject <NSCoding, NSCopying>
@property (nonatomic, assign) BOOL updatesForcibly;         ///< 是否强制更新
@property (nonatomic, assign) NSInteger noticeTimeInterval; ///< 更新提示周期
@property (nonatomic, retain) NSURL *appStoreURL;           ///< 更新的 App Store 链接
@property (nonatomic, copy) NSString *buildNumberString;    ///< 更新 Build 号
@property (nonatomic, copy, nullable) NSString *distributionTitle;   ///< 更新标题
@property (nonatomic, copy, nullable) NSString *featureDescription;  ///< 更新的功能描述

@end
```
- **属性说明**
<table>
<tr>
<th>属性</th>
<th>类型</th>
<th>描述</th>
<th>权限</th>
</tr>
<tr>
<td>updatesForcibly</td>
<td>`BOOL`</td>
<td>是否强制更新</td>
<td>readwrite </td>
</tr>
<tr>
<td>noticeTimeInterval</td>
<td>`NSInteger`</td>
<td>更新提示周期</td>
<td>readwrite </td>
</tr>
<tr>
<td>appStoreURL</td>
<td>`NSURL *`</td>
<td>更新的 app store 链接</td>
<td>readwrite </td>
</tr>
<tr>
<td>buildNumberString</td>
<td>`NSString *`</td>
<td>更新版本号</td>
<td>readwrite </td>
</tr>
<tr>
<td>distributionTitle</td>
<td>`NSString *`</td>
<td>更新标题</td>
<td>readwrite </td>
</tr>
<tr>
<td>featureDescription</td>
<td>`NSString *`</td>
<td>更新的功能描述</td>
<td>readwrite </td>
</tr>
<table>

#### 监听示例
下面是开启并自定义发布处理的示例：
```objc
// 注册自定义 Handler
[[TMFDistributionManager sharedManager] setDidReceiveDistributionHandler:^(TMFDistributionInfo * _Nullable info,
                                                                 TMFDistributionCompletionBlock  _Nonnull completionHandler) {
    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:info.distributionTitle
                                          message:info.featureDescription
                                          preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction *cancelAction = [UIAlertAction actionWithTitle:@"取消" style:UIAlertActionStyleCancel
                                   handler:^(UIAlertAction * _Nonnull action) {
                                       completionHandler(NO);
                                   }];
    UIAlertAction *updateAction = [UIAlertAction actionWithTitle:@"更新" style:UIAlertActionStyleDefault
                                   handler:^(UIAlertAction * _Nonnull action) {
                                       if ([[UIApplication sharedApplication] canOpenURL:info.appStoreURL]) {
                                           [[UIApplication sharedApplication] openURL:info.appStoreURL];
                                       }
                                       completionHandler(YES);
                                   }];
    [alertController addAction:updateAction];
    if (!info.updatesForcibly) {
        [alertController addAction:cancelAction];
    }

    // 弹出弹窗
    UIViewController *rootController = [UIApplication sharedApplication].keyWindow.rootViewController;
    [rootController presentViewController:alertController animated:YES completion:nil];
}];
```
新协议下的自动检查更新：
```objc
// 注册自动拉取弹窗处理 并且使用SDK默认弹窗
    [[TMFDistributionManager sharedManager] autoCheckForUpdatesDistributionHandler:nil];
```
新协议下的主动检查更新：
```objc
// 注册自动拉取弹窗处理 并且使用自定义弹窗
[[TMFDistributionManager sharedManager] drivingCheckForUpdatesDistributionHandler:^(TMFDistributionInfo * _Nullable distributionInfo, NSError * _Nullable error, TMFDistributionCompletionBlock  _Nullable completionHandler) {
            
            
            if (error) {
                UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"TMFDistribution"
                                                                                         message:[NSString stringWithFormat:@"没有获取到更新单失败\n error = %@",error]
                                                                                  preferredStyle:UIAlertControllerStyleAlert];
                [alertController addAction:[UIAlertAction actionWithTitle:@"OK" style:UIAlertActionStyleDefault handler:nil]];
                [self presentViewController:alertController animated:YES completion:nil];
                return;
            }
            
            UIAlertController *alertController = [UIAlertController alertControllerWithTitle:distributionInfo.distributionTitle
                                                                                     message:distributionInfo.featureDescription
                                                                              preferredStyle:UIAlertControllerStyleAlert];
            UIAlertAction *cancelAction = [UIAlertAction actionWithTitle:@"取消" style:UIAlertActionStyleCancel
                                                                 handler:^(UIAlertAction * _Nonnull action) {

            }];
            UIAlertAction *updateAction = [UIAlertAction actionWithTitle:@"更新" style:UIAlertActionStyleDefault
                                                                 handler:^(UIAlertAction * _Nonnull action) {
                                                                     [self _jumpAppStoreWithURL:distributionInfo.appStoreURL];
                                                                 }];
            [alertController addAction:updateAction];
            if (!distributionInfo.updatesForcibly) {
                [alertController addAction:cancelAction];
            }
            
            // 弹出弹窗
            [[UIApplication sharedApplication].keyWindow.rootViewController presentViewController:alertController animated:YES completion:nil];
            
        }];
```
下面是默认和自定义的监听到发布更新后的弹窗，其中左侧为强制更新，右侧为非强制更新。
![](https://qcloudimg.tencent-cloud.cn/raw/a6cbd4cee916d60530d2fc1dd61b0104.png)

### 数据查询
组件提供数据查询属性，可供业务查询最近一次更新信息。

#### 前提条件
若要查询更新数据，必须先完成组件初始化，详情请参见 [初始化](#csh)。

#### 相关接口
```objective-c
@property (nonatomic, readonly, nullable) TMFDistributionInfo *distributionInfo;
```

#### 使用示例
下面是获取上一次更新数据并弹窗展示的示例：
```objective-c
TMFDistributionInfo *distributionInfo = [TMFDistributionManager sharedManager].distributionInfo;
NSMutableString *message = [NSMutableString string];
[message appendFormat:@"【更新 Build 号】 %@\n", distributionInfo.buildNumberString];
[message appendFormat:@"【App Store 链接】 %@\n", distributionInfo.appStoreURL.absoluteString];
[message appendFormat:@"【更新标题】 %@\n", distributionInfo.distributionTitle];
[message appendFormat:@"【更新描述】 %@\n", distributionInfo.featureDescription];
[message appendFormat:@"【更新提示周期】 %ld秒\n", (long)distributionInfo.noticeTimeInterval];
[message appendFormat:@"【是否强制更新】 %@\n", distributionInfo.updatesForcibly ? @"是" : @"否"];

UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"TMFDistribution" 
                                      message:message 
                                      preferredStyle:UIAlertControllerStyleAlert];
[alertController addAction:[UIAlertAction actionWithTitle:@"OK" 
                            style:UIAlertActionStyleDefault 
                            handler:nil]];
[self presentViewController:alertController animated:YES completion:nil];
```

### 日志
组件提供日志接口，可供业务黑盒调试。

#### 前提条件
若要配置日志，必须先完成组件初始化，详情请参见 [初始化](#csh)。

#### 相关接口
```objective-c
@property (class, nonatomic, assign) TMFDistributionLogLevel logLevels;
```

#### 日志等级
```objective-c
typedef NS_OPTIONS(NSUInteger, TMFDistributionLogLevel) {
    TMFDistributionLogLevelNone  = 0,        ///< 无日志
    TMFDistributionLogLevelInfo  = 1 << 0,   ///< 普通日志
    TMFDistributionLogLevelWarn  = 1 << 1,   ///< 警告日志
    TMFDistributionLogLevelError = 1 << 2,   ///< 错误日志
    
    TMFDistributionLogLevelAll   = 0xFF,     ///< 全部日志
};
```
#### 日志示例
下面是在 `AppDelegate.m` 中配置组件日志的示例：
```objective-c
// AppDelegate.m

#if DEBUG
[TMFDistribution setLogLevels:TMFDistributionLogLevelAll];
#elif
[TMFDistribution setLogLevels:TMFDistributionLogLevelNone];
#endif
```
下面是只输出警告+错误的日志配置示例：
```objective-c
[TMFDistribution setLogLevels:(TMFDistributionLogLevelWarn | TMFDistributionLogLevelError)];
```
