
## 开发环境要求

- Xcode 10 及以上
- iOS 8.0 及以上


## 集成说明


### CocoaPods 集成（推荐）

TUIKit 支持 CocoaPods 方式和手动集成两种方式。我们推荐使用 CocoaPods 方式集成，以便随时更新至最新版本。

<ol><li>在 Podfile 中增加以下内容。

```ruby

// TUIKit 使用到了第三方静态库，这个设置需要屏蔽
#use_frameworks!

// TXIMSDK_TUIKit_live_iOS 使用了 *.xcassets 资源文件，需要加上这条语句防止与项目中资源文件冲突。
install! 'cocoapods', :disable_input_output_paths => true  

// 集成聊天，关系链，群组功能，默认依赖 TXLiteAVSDK_TRTC 音视频库
 pod 'TXIMSDK_TUIKit_iOS'  
	 
// 集成聊天，关系链，群组功能，默认依赖 TXLiteAVSDK_Professional 音视频库
// pod 'TXIMSDK_TUIKit_iOS_Professional' 

// 集成群直播，直播广场，默认依赖 TXLiteAVSDK_TRTC 音视频库
pod 'TXIMSDK_TUIKit_live_iOS'	

// 集成群直播，直播广场，默认依赖 TXLiteAVSDK_Professional 音视频库
// pod 'TXIMSDK_TUIKit_live_iOS_Professional' 

```

腾讯云的 [音视频库](https://cloud.tencent.com/document/product/647/32689) 不能同时集成，会有符号冲突，如果您使用了非 [TRTC](https://cloud.tencent.com/document/product/647/32689#TRTC) 版本的音视频库，建议先去掉，然后 pod 集成 `TXIMSDK_TUIKit_iOS_Professional` 版本，该版本依赖的 [LiteAV_Professional](https://cloud.tencent.com/document/product/647/32689#.E4.B8.93.E4.B8.9A.E7.89.88.EF.BC.88professional.EF.BC.89) 音视频库包含了音视频的所有基础能力。

<li> 执行以下命令，安装 TUIKit。<br>

```bash
pod install
```
 如果无法安装 SDK 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。<br>
 
```bash
 pod repo update
```
</ol></li>

### 手动集成（不推荐）

1. 在 Framework Search Path 中加上 ImSDK 的文件路径，手动地将 TUIKit 和 ImSDK 目录添加到您的工程。
2. 手动将 TUIKit 使用的第三方库添加到您的工程：
 - [MMLayout - Tag : 0.2.0](https://github.com/annidy/MMLayout)
 - [SDWebImage - Tag : 5.9.0](https://github.com/SDWebImage/SDWebImage/tree/5.9.0)
 - [ReactiveObjC - Tag  : 3.1.1](https://github.com/ReactiveCocoa/ReactiveObjC.git)
 - [Toast - Tag  : 4.0.0](https://github.com/scalessec/Toast)
 - [TXLiteAVSDK_TRTC](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/SDK)

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

### 1 ** target has transitive dependencies that include statically linked binaries

如果在pod过程中出现该错误，是因为`TUIKit`使用到了第三方静态库，需要在podfile中注释掉 `use_frameworks!`。

如果在某种情况下，需要使用`use_frameworks!`，则请使用`cocoapods 1.9.0`及以上版本进行 `pod install`，并修改为：

```
use_frameworks! :linkage => :static
```

如果您使用的是 `swift`，请将头文件引用改成@import模块名形式引用。
