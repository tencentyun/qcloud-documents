## 开发环境要求

- Xcode 10 及以上
- iOS 9.0 及以上
>?更多实操教学视频请参见：[极速集成 TUIKit（iOS）](https://cloud.tencent.com/edu/learning/course-3130-56699)。

## CocoaPods 集成

`TUIKit` 从 5.7.1435 版本开始支持模块化集成，您即可以选择 pod 集成整个 UI 组件（比如 pod `TXIMSDK_TUIKit_iOS` ，默认包含会话、聊天、关系链、群组、搜索功能），也可以选择 pod 集成单独的功能模块（比如 pod `TUIChat` ，只包含聊天功能）。

### 集成 TUIKit 组件

<ol><li>在 Podfile 中增加以下内容。

```
# TXIMSDK_TUIKit_live_iOS  使用了 *.xcassets 资源文件，需要加上这条语句防止与您项目中资源文件冲突。
install! 'cocoapods', :disable_input_output_paths => true  

# TUICalling 和 TXIMSDK_TUIKit_live_iOS 组件使用到了静态库，需要屏蔽下如下设置
#use_frameworks!

# 集成 TXIMSDK_TUIKit_iOS ，默认包含了会话、聊天，关系链，群组、搜索功能
pod 'TXIMSDK_TUIKit_iOS'  

# 集成音视频通话功能，默认依赖 TXLiteAVSDK_TRTC 音视频库
pod 'TUICalling'

# 集成音视频通话功能，默认依赖 TXLiteAVSDK_Professional 音视频库（需要屏蔽 TUICalling）
# pod 'TUICalling/Professional'
 
# 集成群直播功能，默认依赖 TXLiteAVSDK_TRTC 音视频库
pod 'TXIMSDK_TUIKit_live_iOS'    

# 集成群直播功能，默认依赖 TXLiteAVSDK_Professional 音视频库（需要屏蔽 TXIMSDK_TUIKit_live_iOS）
# pod 'TXIMSDK_TUIKit_live_iOS/Professional' 

```

如果您不需要 `TXIMSDK_TUIKit_iOS` 包含的所有功能，可以选择屏蔽  `TXIMSDK_TUIKit_iOS`，模块化集成所需功能：
```
install! 'cocoapods', :disable_input_output_paths => true  

# 屏蔽 TXIMSDK_TUIKit_iOS
# pod 'TXIMSDK_TUIKit_iOS'  

# 模块化集成聊天功能（如不需要，可以选择屏蔽（#pod 'TUIChat'），其他功能模块屏蔽方法一样）
pod 'TUIChat'
# 模块化集成会话功能
pod 'TUIConversation'
# 模块化集成关系链功能
pod 'TUIContact'
# 模块化集成群组功能
pod 'TUIGroup'
# 模块化集成搜索功能
pod 'TUISearch'
# 模块化集成音视频通话功能
pod 'TUICalling'
```

>! 
>1. 腾讯云的 [音视频库](https://cloud.tencent.com/document/product/647/32689) 不能同时集成，会有符号冲突，如果您使用了非 [TRTC](https://cloud.tencent.com/document/product/647/32689#TRTC) 版本的音视频库，建议 pod 集成 `TUICalling/Professional` 和 `TXIMSDK_TUIKit_live_iOS/Professional` 版本，该版本依赖的 [LiteAV_Professional](https://cloud.tencent.com/document/product/647/32689#.E4.B8.93.E4.B8.9A.E7.89.88.EF.BC.88professional.EF.BC.89) 音视频库包含了音视频的所有基础能力。
>2. 如果您不需要音视频通话功能，可以在 Podfile 文件里屏蔽  `TUICalling` ，也可以通过 [TUIBaseChatViewController.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/UI/Chat/TUIBaseChatViewController.h) 里的 `isEnableVideoCall`、`isEnableAudioCall` 参数屏蔽。
>3. 如果您不需要群直播功能，可以在 Podfile 文件里屏蔽 `TXIMSDK_TUIKit_live_iOS` ，也可以通过 [TUIBaseChatViewController.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/UI/Chat/TUIBaseChatViewController.h) 里的 `isEnableLive` 参数屏蔽。
>4. 如果您不需要搜索功能，可以在 Podfile 文件里屏蔽  `TXIMSDK_TUIKit_iOS` ，模块化集成所需功能，也可以通过 [TUIConversationListController.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIConversation/UI/TUIConversationListController.h) 里的 `isEnableSearch` 参数屏蔽。

<li> 执行以下命令，安装 TUIKit。<br>

```bash
pod install
```
 如果无法安装 TUIKit 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。<br>
 
```bash
 pod repo update
```
</ol></li>

## 初始化 TUI 组件

如果您选择了 pod 集成 `TXIMSDK_TUIKit_iOS`，可以按照下面方法初始化 TUI 组件：

```objectivec
#import "TUIKit.h"
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [[TUIKit sharedInstance] setupWithAppId:SDKAppID]; // SDKAppID 可以在 即时通信 IM 控制台中获取
}
```

如果您选择了 pod 集成独立的功能模块（比如 pod 集成 `TUIChat`），可以按照下面方法初始化 TUI 组件：

```objectivec
#import "TUILogin.h"
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [TUILogin initWithSdkAppID:SDKAppID]; // SDKAppID 可以在 即时通信 IM 控制台中获取
}
```
## 登录 TUI 组件
如果您选择了 pod 集成 `TXIMSDK_TUIKit_iOS`，可以按照下面方法登录 TUI 组件：
```objectivec
#import "TUIKit.h"
- (void)login:(NSString *)identifier userSig:(NSString *)sig succ:(TSucc)succ fail:(TFail)fail
{
    [[TUIKit sharedInstance] login:identifier userSig:sig succ:^{
        NSLog(@"-----> 登录成功");
    } fail:^(int code, NSString *msg) {
        NSLog(@"-----> 登录失败");
    }];
}
```

如果您选择了 pod 集成独立的功能模块（比如 pod 集成 `TUIChat`），可以按照下面方法登录 TUI 组件：
```objectivec
#import "TUILogin.h"
- (void)login:(NSString *)identifier userSig:(NSString *)sig succ:(TSucc)succ fail:(TFail)fail
{
    [TUILogin login:identifier userSig:sig succ:^{
        NSLog(@"-----> 登录成功");
    } fail:^(int code, NSString *msg) {
        NSLog(@"-----> 登录失败");
    }];
}
```

## 常见问题

### 1. target has transitive dependencies that include statically linked binaries

如果在 pod 过程中出现该错误，是因为`TUIKit`使用到了第三方静态库，需要在 podfile 中注释掉 `use_frameworks!`。

如果在某种情况下，需要使用`use_frameworks!`，则请使用`cocoapods 1.9.0`及以上版本进行 `pod install`，并修改为：

```
use_frameworks! :linkage => :static
```

如果您使用的是 `swift`，请将头文件引用改成 @import 模块名形式引用。
