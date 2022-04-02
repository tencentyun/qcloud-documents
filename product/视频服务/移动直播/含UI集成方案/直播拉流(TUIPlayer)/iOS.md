## TUIPlayer简介
`TUIPlayer` 组件是一套开源的、完整的视频解决方案，它基于腾讯云 `MLVB SDK` 和` IM SDK`，可以实现直播拉流，直播连麦等功能，通过 `TUIPlayer` 组件您可以轻松实现直播视频拉流，而无需自己实现复杂的UI与逻辑功能
<table>
<tr>
   <th>观看直播</th>
   <th>发起连麦</th>
 </tr>
<tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/9cbd0d20c12b86a87436fc72e0b4950d.jpg"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/4125d61586106e87a414d738848ad0c6.jpg"/></td>
</tr>
</table>

[](id:model)
## 二. 组件集成
[](id:model.step1)
### 步骤一：下载并导入 TUIPlayer 组件
点击进入 [Github](https://github.com/LiteAV-TUIKit/TUIPlayer) ，选择克隆/下载代码。在您的工程 `Podfile` 文件同一级目录下创建 `TUIPlayer` 文件夹， 然后将 [**iOS**](https://github.com/tencentyun/TUIPlayer/tree/main/iOS) 目录下的 `Source`、`Resources` 文件夹 和 `TUIPlayer.podspec` 文件拷贝到您在自己工程创建的`TUIPlayer`目录下。，并完成如下导入动作：

**通过 cocoapods 导入组件**，具体步骤如下：

1. 在您的 `Podfile` 文件中添加以下依赖。之后执行 `pod install` 命令，完成导入。

```
# :path => "指向TUIPlayer.podspec所在目录的相对路径"
pod 'TUIPlayer', :path => "TUIPlayer/"
```


[](id:model.step2)
### 步骤二：配置权限


使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。

```
<key>NSCameraUsageDescription</key>
<string>TUIPlayerApp需要访问你的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>TUIPlayerApp需要访问你的麦克风权限，开启后录制的视频才会有声音</string>
```
![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)


[](id:model.step3)
### 步骤三：初始化 SDK 并登录 TUI 组件库
```Swift
// 设置Licence
TXLiveBase.setLicenceURL(LICENSEURL, key: LICENSEURLKEY)
```

#### 3.1 初始化SDK参数说明
进入**云直播管理控制台** > **[License 管理](https://console.cloud.tencent.com/live/license)**，单击**创建应用并绑定License**，创建应用所需要的鉴权 License。
![](https://qcloudimg.tencent-cloud.cn/raw/886dbc5cf9cea301a69a7c06c80390d4.png)
创建成功后即可获得 ` License Key `和 `License URL`
- **LICENSEURL**：**TRTC 应用LICENSEURL**，
- **LICENSEURLKEY**：**TRTC 应用LICENSEURLKEY**


```Swift
// 组件登陆
TUILogin.initWithSdkAppID(SDKAPPID)
TUILogin.login(userId, userSig: userSig) {
    print("login success")
} fail: { code, message in
    print("login failed, code:\(code), error: \(message ?? "nil")")
}
```

#### 3.2 登录组件参数说明
- **SDKAppID**：**TRTC 应用ID**，如果您未开通腾讯云 TRTC 服务，可以点击 [这里](https://console.cloud.tencent.com/trtc/app)，进入腾讯云实时音视频控制台，创建一个新的的TRTC应用后，点击应用信息，SDKAppID信息如下图所示；
 <img src="https://liteav.sdk.qcloud.com/app/doc/app_manager_sdk_secretkey.png" width="700">
    
- **Secretkey**：**TRTC 应用密钥**，和SDKAppId对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey信息如上图所示；

- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。

- **userSig**：根据SDKAppId、userId，Secretkey等信息计算得到的安全保护签名，您可以点击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的userSig，也可以参照我们的[TUIPusher示例工程](https://github.com/LiteAV-TUIKit/TUIPlayer/iOS/Example/Debug/GenerateTestUserSig.swift#L84)自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

[](id:model.step4)
### 步骤四：初始化组件并使用相关功能

#### 4.1. 创建 `TUIPlayerView`

```Swift
let mTUIPlayerView = TUIPlayerView(frame: view.bounds);
view.addSubview(mTUIPlayerView);
```

#### 4.2. 开始拉流
按照相关政策要求，您需要在  [云直播管理控制台](https://console.cloud.tencent.com/live/domainmanage) 中添加自有的**已备案域名**，这样才能使用腾讯云直播的播放功能，请参见 [域名管理](https://cloud.tencent.com/document/product/267/20381) 和 [CNAME 配置](https://cloud.tencent.com/document/product/267/30560) 进行配置。
拉流URL可以参照我们的[TUIPusher示例工程](https://github.com/LiteAV-TUIKit/TUIPlayer/iOS/Example/Debug/URLUtils.swift#L42)自行实现，更多信息请点击[这里](https://cloud.tencent.com/document/product/454/7915)

```Swift
// 开始拉流
mTUIPlayerView.startPlay("")
```

#### 4.3. 停止拉流

```
mTUIPlayerView.stopPlay();
```

[](id:model.step5)
### 步骤五：在TUIPlayer中集成其他TUIKit组件（可选）
我们在自己的[小直播](https://github.com/tencentyun/XiaoZhiBo)工程中使用了该TUIPlayer组件并集成了其他 `TUIKit` 组件，您可以以此为参考自行实现。

## 三. 常见问题

>? 更多帮助信息，详见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)，欢迎加入 QQ 群：592465424，进行技术交流和反馈~
