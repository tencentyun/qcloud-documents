## 组件介绍
`TUIPlayer` 组件是一套开源的、完整的视频直播互动播放组件，它基于腾讯云 [直播 Live SDK](https://cloud.tencent.com/document/product/454/19074) 和 [即时通信 IM SDK](https://cloud.tencent.com/document/product/269/1498) ，实现直播播放，直播连麦等功能，同时支持弹幕、点赞、美颜等外挂插件，通过 `TUIPlayer` 组件您可以轻松实现直播视频拉流，快速搭建诸如秀场直播、电商直播等场景化解决方案。

<img src="https://qcloudimg.tencent-cloud.cn/raw/56974460aea1eff23adb1ab6410c910d.png" width="900"/>

[](id:model)
## 组件集成
[](id:model.step1)
### 步骤一：下载并导入 TUIPlayer 组件
单击进入 [Github](https://github.com/tencentyun/XiaoZhiBo) ，选择克隆/下载代码。将 [iOS 目录](https://github.com/tencentyun/XiaoZhiBo/tree/main/iOS) 下的 `TUIPlayer` 、`TUIGift` 和 `TUIBarrage` 文件夹拷贝到您在自己工程创建的 `Podfile` 文件同一级目录下，并导入组件。

**通过 cocoapods 导入组件**：
在您的 `Podfile` 文件中添加以下依赖。之后执行 `pod install` 命令，完成导入。
```
# :path => "指向TUIPlayer.podspec所在目录的相对路径"
pod 'TUIPlayer', :path => "TUIPlayer/"

# :path => "指向TUIBarrage.podspec所在目录的相对路径"
pod 'TUIBarrage', :path => "TUIBarrage/"

# :path => "指向TUIGift.podspec所在目录的相对路径"
pod 'TUIGift', :path => "TUIGift/"
```

[](id:model.step2)
### 步骤二：配置权限
使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。

```
<key>NSCameraUsageDescription</key>
<string>TUIPlayerApp需要访问您的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>TUIPlayerApp需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
```

![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)

### 步骤三：初始化&创建组件

```Swift
// 1. 创建TUIPlayer组件
let mTUIPlayerView = TUIPlayerView(frame: view.bounds);
view.addSubview(mTUIPlayerView);

// 2. 为 TUIPlayerView 设置事件回调 TUIPlayerViewDelegate
mTUIPlayerView.setDelegate(self)
```

### 步骤四：开始&停止播放
- **开始播放**
```
mTUIPlayerView.startPlay(url: "xxxx")
```
腾讯云直播支持两种播放协议：WebRTC 协议（即快直播，更低延时，更强抗性）、RTMP 协议、此处参数 URL 的生成，您可以参考 [示例工程](https://github.com/tencentyun/XiaoZhiBo/blob/main/iOS/APP/Scene/ShowLive/model/URLUtils.swift#L40) 中封装好的 Utils 方法，更多参数信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
- **停止播放**
```
mTUIPlayerView.stopPlay();
```

[](id:model.step5)
### 步骤五：实现连麦功能（可选）
1. **开通云直播服务**：
	如果您未开通腾讯云直播相关服务，请先按照如下步骤开通相关服务并完成SDK鉴权：
	-  [开通云直播服务](https://console.cloud.tencent.com/live/livestat) 
	-  [创建应用并绑定 License](https://console.cloud.tencent.com/live/license) ，并记录下 `LICENSEURL`、`LICENSEURLKEY` 等关键信息。
	- 按照如下方式，完成 SDK 推流鉴权：
```java
V2TXLivePremier.setLicence(LICENSEURL, key: LICENSEURLKEY)
```
2. **开通连麦服务**
因为连麦时需要更低的延时需求，需要在腾讯云直播控制台控制台开通对应的连麦应用服务，如果您未开通，请登录**云直播管理控制台**选择 **[应用管理](https://console.cloud.tencent.com/live/micro/appmanage)**，单击 **新建连麦应用** 输入应用名称（例如 `TUIPlayer` ），然后在该应用的对应操作栏中，选择**应用信息**进入应用管理页，查看并记录应用的 **SDKAppID** 和 **SECRETKEY（密钥）** 。
![img](https://qcloudimg.tencent-cloud.cn/raw/cb2b2381b92994404dfece3cdaf77608.png)
3. **组件登录**
因为连麦服务，需要观众与主播相互通信，所以需要进行单独登录，登录流程如下：
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
4. **开始&停止连麦**
在 `TUIPlayer` 组件内部已经封装好了连麦功能，完成上述步骤后，即可单击**连麦**按钮发起&停止连麦，如您需要修改连麦 icon 或显示位置，详情请参见 [连麦按钮](https://github.com/tencentyun/XiaoZhiBo/blob/main/iOS/TUIPlayer/Source/UI/TUIPlayerContainerView.m#L95) 文件。

## 交流&反馈

更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
