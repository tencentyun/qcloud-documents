## 开发环境要求

- Xcode 10 及以上
- iOS 8.0 及以上
>?更多实操教学视频请参见：[极速集成 TUIKit（iOS）](https://cloud.tencent.com/edu/learning/course-3130-56699)。

## CocoaPods 集成

`TUIKit` 从 5.7.1435 版本开始支持模块化集成，您可以选择集成整个 `TUIKit` 组件（包含会话、聊天、关系链、群组、搜索等功能），也可以选择集成单独的功能模块（比如聊天功能）。

### 集成 TUIKit 组件

<ol><li>在 Podfile 中增加以下内容。

```objectivec
// TXIMSDK_TUIKit_live_iOS  使用了 *.xcassets 资源文件，需要加上这条语句防止与您项目中资源文件冲突。
install! 'cocoapods', :disable_input_output_paths => true  

// TUICalling 和 TXIMSDK_TUIKit_live_iOS 组件使用到了静态库，需要屏蔽下如下设置
#use_frameworks!

// 集成会话、聊天，关系链，群组、搜索等功能
pod 'TXIMSDK_TUIKit_iOS'  
 
// 集成音视频通话功能，默认依赖 TXLiteAVSDK_TRTC 音视频库
pod 'TUICalling'

// 集成音视频通话功能，默认依赖 TXLiteAVSDK_Professional 音视频库
// pod 'TUICalling/Professional'
 
// 集成群直播功能，默认依赖 TXLiteAVSDK_TRTC 音视频库
pod 'TXIMSDK_TUIKit_live_iOS'    

// 集成群直播功能，默认依赖 TXLiteAVSDK_Professional 音视频库
// pod 'TXIMSDK_TUIKit_live_iOS/Professional' 

```
>! 1、腾讯云的 [音视频库](https://cloud.tencent.com/document/product/647/32689) 不能同时集成，会有符号冲突，如果您使用了非 [TRTC](https://cloud.tencent.com/document/product/647/32689#TRTC) 版本的音视频库，建议 pod 集成 `TUICalling/Professional` 和 `TXIMSDK_TUIKit_live_iOS/Professional` 版本，该版本依赖的 [LiteAV_Professional](https://cloud.tencent.com/document/product/647/32689#.E4.B8.93.E4.B8.9A.E7.89.88.EF.BC.88professional.EF.BC.89) 音视频库包含了音视频的所有基础能力。
>2、如果您不需要音视频通话或群直播功能，可以选择在 Podfile 文件里屏蔽  `TUICalling` 或则 `TXIMSDK_TUIKit_live_iOS` 的 pod 依赖，也可以通过 [TUIBaseChatViewController.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/UI/Chat/TUIBaseChatViewController.h) 里的 `isEnableVideoCall`、`isEnableAudioCall`、`isEnableLive` 参数屏蔽对应功能。
>3、如果您不需要搜索功能，可以通过 [TUIConversationListController.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIConversation/UI/TUIConversationListController.h) 里的 `isEnableSearch` 参数屏蔽对应功能。

<li> 执行以下命令，安装 TUIKit。<br>

```bash
pod install
```
 如果无法安装 TUIKit 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。<br>
 
```bash
 pod repo update
```
</ol></li>

###  集成单独的功能模块
<ol><li>在 Podfile 中增加以下内容。
```objectivec
// 集成聊天功能模块
pod 'TUIChat'
// 集成会话功能模块
pod 'TUIConversation'
// 集成关系链功能模块
pod 'TUIContact'
// 集成群组功能模块
pod 'TUIGroup'
// 集成搜索功能模块
pod 'TUISearch'
// 集成音视频通话模块
pod 'TUICalling'
// TUICalling 使用到了第三方静态库，这个设置需要屏蔽
#use_frameworks!   
```

>! 
>1、功能模块之间是互相独立的，您可以根据业务需求选择需要集成的功能模块。
>2、在使用功能模块之前，您需要主动调用 [TUILogin.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUICore/TUILogin.h) 的 `initWithSdkAppID` 和 `login` 接口初始化和登录 `IMSDK`，详情请参考 [TUIKit.m](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIKit/TUIKit.m) 代码实现。

<li> 执行以下命令，安装 UI 组件。<br>

```bash
pod install
```
 如果无法安装 UI 组件最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。<br>
 
```bash
 pod repo update
```
</ol></li>


## 引用 TUIKit

<ol><li>在 AppDelegate.m 文件中引入 TUIKit，并初始化。

```objectivec
#import "TUIKit.h"

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [[TUIKit sharedInstance] setupWithAppId:sdkAppid]; // SDKAppID 可以在 即时通信 IM 控制台中获取
}
```
</li>
<li>保存并编译。<br>
  编译成功表示集成完成。如果编译失败，请检查错误原因或重新按照本文集成。
</li></ol>

## 常见问题

### 1. target has transitive dependencies that include statically linked binaries

如果在 pod 过程中出现该错误，是因为`TUIKit`使用到了第三方静态库，需要在 podfile 中注释掉 `use_frameworks!`。

如果在某种情况下，需要使用`use_frameworks!`，则请使用`cocoapods 1.9.0`及以上版本进行 `pod install`，并修改为：

```
use_frameworks! :linkage => :static
```

如果您使用的是 `swift`，请将头文件引用改成 @import 模块名形式引用。
