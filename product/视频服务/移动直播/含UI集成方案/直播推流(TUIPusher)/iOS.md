## 组件介绍
`TUIPusher` 组件是一套开源的、完整的视频直播互动推流组件，它基于腾讯云 [直播 Live SDK](https://cloud.tencent.com/document/product/454/19074) 和 [即时通信 IM SDK](https://cloud.tencent.com/document/product/269/1498) ，实现直播推流，直播 PK 等功能，同时支持弹幕、点赞、美颜等外挂插件，使用 `TUIPusher` 组件您可以快速搭建诸如秀场直播、电商直播等场景化解决方案。

<img src="https://qcloudimg.tencent-cloud.cn/raw/56974460aea1eff23adb1ab6410c910d.png" width="900"/>

[](id:model)
## 组件集成
[](id:model.step1)
### 步骤一：下载并导入 TUIPusher 组件
1. 单击进入 [Github](https://github.com/tencentyun/XiaoZhiBo)，选择克隆/下载代码。将 [iOS 目录](https://github.com/tencentyun/XiaoZhiBo/tree/main/iOS) 下的 `TUIPusher` 、 `TUIGift` 、 `TUIBeauty` 、`TUIBarrage` 和 `TUIAudioEffect` 文件夹拷贝到您在自己工程创建的 `Podfile` 文件同一级目录下。
2. **通过 cocoapods 导入组件**：
在您的 `Podfile` 文件中添加以下依赖。之后执行 `pod install` 命令，完成导入。
```
# :path => "指向TUIPusher.podspec所在目录的相对路径"
pod 'TUIPusher', :path => "TUIPusher/"

# :path => "指向TUIAudioEffect.podspec所在目录的相对路径"
pod 'TUIAudioEffect', :path => "TUIAudioEffect/"

# :path => "指向TUIBarrage.podspec所在目录的相对路径"
pod 'TUIBarrage', :path => "TUIBarrage/"

# :path => "指向TUIBeauty.podspec所在目录的相对路径"
pod 'TUIBeauty', :path => "TUIBeauty/"

# :path => "指向TUIGift.podspec所在目录的相对路径"
pod 'TUIGift', :path => "TUIGift/"
```

>! 关于 TUIBeauty 的美颜特效依赖库编译失败问题，请前往 [美颜特效-SDK集成指引iOS](https://cloud.tencent.com/document/product/616/65887)，下载并解压 [Demo 包](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/2.4.1vcube/MLVB-API-Example.zip)，将 SDK 目录中的 `libpag.framework`、`XMagic.framework`、`YTCommonXMagic.framework`导入到 TUIBeauty 下的 Frameworks 目录，重新执行命令 "pod install"即可 。

[](id:model.step2)
### 步骤二：配置权限
使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
```
<key>NSCameraUsageDescription</key>
<string>TUIPusherApp需要访问您的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>TUIPusherApp需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
```

![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)

[](id:model.step3)
### 步骤三：初始化&创建组件
如果您未开通腾讯云直播相关服务，请先按照如下步骤开通相关服务：
-  [开通云直播服务](https://console.cloud.tencent.com/live/livestat) ，并在 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 页面中配置推流域名和拉流域名。
-  [创建应用并绑定License](https://console.cloud.tencent.com/live/license) ，并记录下 `LICENSEURL`、`LICENSEURLKEY` 等关键信息。
```Swift
// 1. 初始化直播服务
V2TXLivePremier.setLicence(LICENSEURL, key: LICENSEURLKEY)

// 2. 创建TUIPusher组件
let mTUIPusherView = TUIPusherView(frame: view.bounds);
view.addSubview(mTUIPusherView)

// 3. 为 TUIPusherView 设置事件回调 TUIPusherViewDelegate

mTUIPusherView.setDelegate(self)
```

### 步骤四：有互动直播推流
1.  **服务开通**
因为连麦& PK 时需要更低的延时需求，需要在腾讯云直播控制台控制台开通对应的连麦应用服务，如果您未开通，请登录**云直播管理控制台**选择 **[应用管理](https://console.cloud.tencent.com/live/micro/appmanage)**，单击**新建连麦应用**输入应用名称（例如 `TUIPusher`），然后在该应用的对应操作栏中，选择**应用信息**进入应用管理页，查看并记录应用的 **SDKAppID** 和 **SECRETKEY（密钥）**。
![img](https://qcloudimg.tencent-cloud.cn/raw/cb2b2381b92994404dfece3cdaf77608.png)
>! 因为在连麦/PK 过程中，观众端还是需要正常观看 CDN 流，所以需要进入 **CDN 观看配置**页，开启旁路推流，推荐全局自动旁路。
>![](https://qcloudimg.tencent-cloud.cn/raw/62adb00b3445a0d88fcf92f357109e5c.png)
2.  **组件登录**
因为 PK 服务，需要主播间相互通信，所以需要进行单独登录，登录流程如下：
```Swift
// 组件登录
TUILogin.initWithSdkAppID(SDKAPPID)
TUILogin.login(userId, userSig: userSig) {
    print("login success")
} fail: { code, message in
    print("login failed, code:\(code), error: \(message ?? "nil")")
}
```
	- **登录组件参数说明：**
		- **SDKAppID**：服务开通中记录到的 SDKAppID 信息。
		- **SECRETKEY**：服务开通中记录到的 SECRETKEY（密钥）。
		- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
		- **userSig**：根据 SDKAppId、userId，Secretkey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [示例工程](https://github.com/tencentyun/XiaoZhiBo/blob/main/iOS/APP/Debug/GenerateGlobalConfig.swift#L82) 自行计算，更多信息请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/454/14548)。
3.  **开始推流**
```
mTUIPusherView.start(url: "xxxx");
```
基于 `RTC` 协议的推流 `URL` 的生成，可以参见我们的 [示例工程](https://github.com/tencentyun/XiaoZhiBo/blob/main/iOS/APP/Scene/ShowLive/model/URLUtils.swift#L27) 中封装好的 Utils 方法，基本示例如下，具体参数信息详情请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
4. **停止推流**
```
mTUIPusherView.stop();
```
5. **发起 PK 请求**
调用 `mTUIPusherView.sendPKRequest()` 后会向接收方发起 Pk 请求，请求超时 `TUIPusherViewDelegate` 会收到 `onPKTimeout` 回调。
```
mTUIPusherView.sendPKRequest(userID: "xxxx");
```
6. **接受 PK 请求**
接收方设置的 `mTUIPusherView.setDelegate` 回调中，`TUIPusherViewDelegate` 回调回通知接收方收到 `PK` 请求，可在此回调中处理 `PK` 请求。
```
//接收方收到PK请求回调
func onReceivePKRequest(_ pusherView: TUIPusherView, userId: String, responseCallback completion: @escaping Response) {
    let alert = UIAlertController(title: "收到 PK 邀请，是否接受？", message: "", preferredStyle: .alert)
    let accept = UIAlertAction(title: "接受", style: .default) { _ in
        completion(true)
    }
    let reject = UIAlertAction(title: "拒绝", style: .cancel) { _ in
        completion(false)
    }
    alert.addAction(accept)
    alert.addAction(reject)
    present(alert, animated: true, completion: nil)
}
```

[](id:model.step5)
### 步骤五：无互动直播推流
如果您的应用中无连麦或 `PK` 等互动场景，可以选择标准的 `RMTP` 协议进行推流，具体步骤如下：

- **开始推流**
基于 RTMP 推流 URL 的生成，可以参见我们的 [示例工程](https://github.com/tencentyun/XiaoZhiBo/blob/main/iOS/APP/Scene/ShowLive/model/URLUtils.swift#L27) 中封装好的 Utils 方法，基本规则如下图，具体参数信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
```
mTUIPusherView.start(url: "xxxx");
```
- **停止推流**
```
mTUIPusherView.stop();
```

## 交流&反馈
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
