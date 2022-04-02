## TUIPusher简介
`TUIPusher` 组件是一套开源的、完整的视频解决方案，它基于腾讯云 `MLVB SDK` 和` IM SDK`，可以实现直播推流，直播PK，直播连麦等功能，通过 `TUIPusher` 组件您可以轻松实现直播视频推流，而无需自己实现复杂的UI与逻辑功能

## 效果展示
<table>
<tr>
   <th>开始直播</th>
   <th>直播PK</th>
 </tr>
<tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/3e424e1eac5f1ca02d42a19e01502e5c.jpg" width="450"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/e8fcb12be7c08bd57030e78a5c53428b.jpg" width="450"/></td>
</tr>
</table>


[](id:model)
## 二. 组件集成
[](id:model.step1)
### 步骤一：下载并导入 TUIPusher 组件
点击进入 [Github](https://github.com/LiteAV-TUIKit/TUIPusher) ，选择克隆/下载代码。在您的工程 `Podfile` 文件同一级目录下创建 `TUIPusher` 文件夹， 然后将 [**iOS**](https://github.com/LiteAV-TUIKit/TUIPusher/tree/main/iOS) 目录下的 `Source`、`Resources` 文件夹 和 `TUIPusher.podspec` 文件拷贝到您在自己工程创建的`TUIPusher`目录下。并完成如下导入动作：

**通过 cocoapods 导入组件**，具体步骤如下：

1. 在您的 `Podfile` 文件中添加以下依赖。之后执行 `pod install` 命令，完成导入。

```
# :path => "指向TUIPusher.podspec所在目录的相对路径"
pod 'TUIPusher', :path => "TUIPusher/"
```

[](id:model.step2)
### 步骤二：配置权限


使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。

```
<key>NSCameraUsageDescription</key>
<string>TUIPusherApp需要访问你的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>TUIPusherApp需要访问你的麦克风权限，开启后录制的视频才会有声音</string>
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

#### 4.1. 创建 `TUIPusherView`

```
let mTUIPusherView = TUIPusherView(frame: view.bounds);
view.addSubview(mTUIPusherView)
```

#### 4.2. 为 `TUIPusherView` 设置事件回调`TUIPusherViewDelegate`

```
 mTUIPusherView.setDelegate(self)
```

#### 4.3 开始推流
按照相关政策要求，您需要在  [云直播管理控制台](https://console.cloud.tencent.com/live/domainmanage) 中添加自有的**已备案域名**，这样才能使用腾讯云直播的播放功能，请参见 [域名管理](https://cloud.tencent.com/document/product/267/20381) 和 [CNAME 配置](https://cloud.tencent.com/document/product/267/30560) 进行配置。
推流URL可以参照我们的[TUIPusher示例工程](https://github.com/LiteAV-TUIKit/TUIPlayer/iOS/Example/Debug/URLUtils.swift#L27)自行实现，更多信息请点击[这里](https://cloud.tencent.com/document/product/454/7915)

```
mTUIPusherView.start(String url);
```

### 4.4. 停止推流
```
mTUIPusherView.stop();
```

### 4.5. 发起PK请求(可选)
```
mTUIPusherView.sendPKRequest(userID: "xxxx");
```

### 4.6. 取消PK请求(可选)
```
mTUIPusherView.cancelPKRequest();
```

### 4.7. 退出PK(可选)
```
mTUIPusherView.stopPK();
```

[](id:model.step5)
### 步骤五：实现PK功能（可选）
1. 发起方：调用` mTUIPusherView.sendPKRequest()`后会向接收方发起Pk请求，请求超时会收到`onPKTimeout`回调
2. 接收方：接收方设置的 `mTUIPusherView.setDelegate`回调中，`TUIPusherViewDelegate`回调回通知接收方收到PK请求，可在此回调中处理PK请求
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

[](id:model.step6)
### 步骤六：实现连麦功能（可选）

1. 发起方：连麦功能发起方为 `TUIPlayer` 用户，需要您自行跑通[TUIPlayer](https://github.com/LiteAV-TUIKit/TUIPlayer)工程
2. 接收方：接收方设置的 `mTUIPusherView.setDelegate`回调中，`TUIPusherViewDelegate`回调回通知接收方收到PK请求，可在此回调中处理PK请求
```
//接收方收到连麦请求回调
func onReceiveJoinAnchorRequest(_ pusherView: TUIPusherView, userId: String, responseCallback completion: @escaping Response) {
    let alert = UIAlertController(title: "收到连麦邀请，是否接受？", message: "", preferredStyle: .alert)
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


[](id:model.step7)
### 步骤七：在TUIPusher中集成其他TUIKit组件（可选）
我们在自己的[小直播](https://github.com/tencentyun/XiaoZhiBo)工程中使用了该TUIPusher组件并集成了其他 `TUIKit` 组件，您可以以此为参考自行实现。

## 三. 常见问题

>? 更多帮助信息，详见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)，欢迎加入 QQ 群：592465424，进行技术交流和反馈~
