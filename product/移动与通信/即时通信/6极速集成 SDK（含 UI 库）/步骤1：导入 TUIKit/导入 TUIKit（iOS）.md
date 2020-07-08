
## 开发环境要求

- Xcode 10 及以上
- iOS 8.0 及以上


## 集成说明


### CocoaPods 集成（推荐）

TUIKit 支持 CocoaPods 方式和手动集成两种方式。我们推荐使用 CocoaPods 方式集成，以便随时更新至最新版本。

1. 在 Podfile 中增加以下内容。
```
#use_frameworks!   // TUIKit 使用到了第三方静态库，这个设置需要屏蔽
use_modular_headers!
pod 'TXIMSDK_TUIKit_iOS'
```
2. 执行以下命令，安装 TUIKit。
```bash
pod install
```
 如果无法安装 SDK 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。
```bash
 pod repo update
```


### 手动集成（不推荐）

1. 在 Framework Search Path 中加上 ImSDK 的文件路径，手动地将 TUIKit 和 ImSDK 目录添加到您的工程。
2. 手动将 TUIKit 使用的第三方库添加到您的工程：
 - [MMLayout - Tag : 0.2.0](https://github.com/annidy/MMLayout)
 - [SDWebImage - Tag : 5.5.2](https://github.com/SDWebImage/SDWebImage)
 - [ReactiveObjC - Tag  : 3.1.1](https://github.com/ReactiveCocoa/ReactiveObjC.git)
 - [Toast - Tag  : 4.0.0](https://github.com/scalessec/Toast)
 - [ISVImageScrollView - Tag : 0.1.2](https://github.com/yuriiik/ISVImageScrollView)
 - [AFNetworking - Tag : 4.0.1](https://github.com/AFNetworking/AFNetworking)
 - [SnapKit - Tag : 4.2.0](https://github.com/SnapKit/SnapKit)
 - [Toast-Swift - Tag :5.0.1](https://github.com/scalessec/Toast-Swift)
 - [RxSwift - Tag :5.1.1](https://github.com/ReactiveX/RxSwift)
 - [RxCocoa - Tag :5.1.1](https://github.com/ReactiveX/RxSwift/tree/master/RxCocoa)
 - [NVActivityIndicatorView - Tag :4.8.0](https://github.com/ninjaprox/NVActivityIndicatorView)
 - [Material - Tag :3.1.8](https://github.com/CosmicMind/Material)
 - [Alamofire - Tag :4.9.1](https://github.com/Alamofire/Alamofire)
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
