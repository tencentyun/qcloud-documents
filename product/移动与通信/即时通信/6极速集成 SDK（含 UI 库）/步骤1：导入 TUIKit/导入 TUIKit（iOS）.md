
## 开发环境要求

- Xcode 10 及以上
- iOS 8.0 及以上


## 集成说明


### CocoaPods 集成（推荐）

TUIKit 支持 CocoaPods 方式和手动集成两种方式。我们推荐使用 CocoaPods 方式集成，以便随时更新至最新版本。

1. 在 Podfile 中增加以下内容。
```
pod 'TXIMSDK_TUIKit_iOS'
```
2. 执行以下命令，更新本地库版本。
```bash
pod update
```


### 手动集成
我们**不推荐**使用手动集成。

1. 在 Framework Search Path 中加上 ImSDK 的文件路径，手动地将 TUIKit 和 ImSDK 目录添加到您的工程。
2. 手动将 TUIKit 使用的第三方库添加到您的工程：
 - [MMLayout](https://github.com/annidy/MMLayout)
 - [SDWebImage](https://github.com/SDWebImage/SDWebImage)
 - [ReactiveObjC](https://github.com/ReactiveCocoa/ReactiveObjC.git)
 - [Toast](https://github.com/scalessec/Toast)
 - [ISVImageScrollView](https://github.com/yuriiik/ISVImageScrollView)

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
