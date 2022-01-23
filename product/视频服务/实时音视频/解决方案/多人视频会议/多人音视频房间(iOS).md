## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验多人视频会话的效果，包括屏幕分享、美颜、低延时视频通话等 TRTC 在多人音视频场景下的相关能力。
<table>
     <tr>
         <th>进入房间</th>  
         <th>屏幕分享</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/tuiroom_demo.gif" width="300px" height="640px"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/screencapture.gif" width="300px" height="640px"/></td>
</tr>
</table>

## 方案优势
- 集成了超低延时音视频通话、屏幕共享、美颜等能力，覆盖多人音视频房间常见功能。
- 根据需求二次开发，可以快速实现自定义 UI 界面和布局，助力业务快速上线。
- 封装了 TRTC 和 IM 基础 SDK，实现基础的逻辑控制，并提供接口方便调用。

## 接入指引
如需快速接入多人音视频房间功能，您可以直接基于我们提供的 App 进行修改适配，也可以使用的 App 内的 Module 模块实现自定义 UI 界面。

[](id:ui_step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助 > [快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 输入应用名称，例如 `TestTUIRoom` ，单击 **创建**。
3. 单击 **已下载，下一步**，跳过此步骤。

![](https://qcloudimg.tencent-cloud.cn/raw/639111e18b2244c6f4ff8cc6d2711acd.png)
>!本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。

[](id:ui_step2)
### 步骤2：下载 App 源码
单击进入 [TUIRoom](https://github.com/tencentyun/TUIRoom)，Clone 或者下载源码。

[](id:ui_step3)
### 步骤3：配置 App 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Example/Debug/GenerateTestUserSig.swift` 文件。
3. 设置 `GenerateTestUserSig.swift` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为0，请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</ul>
<img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/sdkappid_secretkey_ios.png" width="650" height="295"/>
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。

>?
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui_step4)
### 步骤4：运行工程
使用 Xcode（11.0及以上的版本）打开源码工程 `Example/DemoApp.xcworkspace`，单击 **运行** 即可开始调试本 App。

[](id:ui_step5)
### 步骤5：修改工程源代码
源码中的 `Source` 中包 UI 文件夹，此文件夹均为 UI 相关代码，如下表格列出了各个文件夹所对应的 UI 界面，以便于您进行二次调整：

| 文件夹 | 功能描述 |
|:-------:|:--------|
| TUIRoomEnter | TUIRoom入口相关实现代码，TUIRoomEntranceViewController类为 Pods 对外暴露的公共类。 |
| TUIRoomMain | TUIRoom主界面相关 UI 实现代码，此类为 Pods 私有类。 |
| TUIRoomMemberList | 成员列表界面相关 UI 实现代码，此类为 Pods 私有类。 |
| TUIRoomSet | 设置界面相关 UI 实现代码，此类为 Pods 私有类。 |

## 体验应用
>! 体验应用至少需要两台设备。
### 入口界面
请选择 **创建房间** 或 **加入房间**，如图示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/fbb6286ef73d5c8a079703efed44586b.png" width=300px>

### 创建房间页面
A 用户创建，房间号会默认生成，单击 **创建房间** 可以进入主页面。
<img src="https://qcloudimg.tencent-cloud.cn/raw/031fc9dd8b36bf3e52a0a6d319186e66.png" width=300px>

### 加入房间页面
B 用户输入 A 用户的房间号，单击 **加入房间** 可以进入主页面。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7b81436bb76f59a72a6e90c7708788dc.png" width=300px>


### 主页面（A 用户）
<img src="https://qcloudimg.tencent-cloud.cn/raw/4b0c5e954cd7f988fffe553cdbac1495.png" width=300px>


### 麦上列表
麦上列表可以展示当前房间内的成员，对方打开摄像头和麦克风后可以看到对方的画面，听到对方的声音。

### 顶部控制栏
实现了耳麦切换，前后摄像头切换，房间信息，退出的功能。

### 底部工具栏
实现了控制自己的麦克风/摄像头，美颜，成员列表，设置等功能。

### 美颜
可在直播中针对画面进行美颜和特效展示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/e8360ac236737d92ad0d8154663ce5b0.png" width=300px>


### 设置窗口
可对音视频相关参数进行设置，支持开启**屏幕共享**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/664f7c624476bc5dcb3975ce0a9049cc.png" width=300px>


### 退出房间
- **主持人**：解散房间，即所有人退出房间。
- **非主持人**：自己离开房间。

## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TUIRoom) 中的 `Source` 文件夹包含 UI 和 Presenter，Presenter 文件夹中包含可重用的开源组件 TUIRoomCore，您可以在 `TUIRoomCore.h` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![#600px](https://qcloudimg.tencent-cloud.cn/raw/26d50df38b49c1aa36446ce909aa9ce4.png)

[](id:ui_step1)
### 步骤1：集成 SDK
多人音视频视频组件 TUIRoom 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

- **方法一：通过 cocoapods 仓库依赖**
```
 pod 'TXIMSDK_iOS'
 pod 'TXLiteAVSDK_TRTC'
```
>? 两个 SDK 产品的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
- **方法二：通过本地依赖**
如果您的开发环境访问 cocoapods 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。
<table>
<thead><tr><th>SDK</th><th>下载页面</th><th>集成指引</th></tr></thead>
<tbody><tr>
<td>TRTC SDK</td>
<td><a href="https://cloud.tencent.com/document/product/647/32689">DOWNLOAD</a></td>
<td><a href="https://cloud.tencent.com/document/product/647/32173">集成文档</a></td>
</tr>
<tr>
<td>IM SDK</td>
<td><a href="https://cloud.tencent.com/document/product/269/36887">DOWNLOAD</a></td>
<td><a href="https://cloud.tencent.com/document/product/269/32675">集成文档</a></td>
</tr>
</tbody></table>

[](id:model_step2)
### 步骤2：配置权限
在 `info.plist` 文件中需要添加 `Privacy > Camera Usage Description` 和 `Privacy > Microphone Usage Description` 申请摄像头和麦克风权限。

[](id:model_step3)
### 步骤3：导入 TUIRoom 组件
您可通过 **cocoapods 导入组件**，具体步骤如下：
1. 将工程目录下的 `Source`、`Resources`、`TCBeautyKit`、`TXAppBasic` 文件夹、`TUIRoom.podspec` 文件拷贝到您的工程目录下。
2. 在您的 `Podfile` 文件中添加以下依赖。之后执行 `pod install` 命令，完成导入。
```swift
# 本地依赖库
def local
  pod 'TXAppBasic', :path => "../../TXAppBasic/"
  pod 'TCBeautyKit', :path => "../../TCBeautyKit/"
  pod 'TXLiteAVSDK_TRTC',:path => "../../../SDK/"
end

def pod_local(type)
  loadLocalPod('TUIRoom', type)
end

def loadLocalPod(name, type)
    pod "#{name}/#{type}", :path => "../"
end

target 'DemoApp' do
  local
  pod_local('TRTC')
end
```

[](id:model_step4)
### 步骤4：创建并登录组件
1.  调用 TUICore 中的 TUILogin 进行登录，请参考如下示例：
```swift
TUILogin.initWithSdkAppID(Int32(SDKAPPID))
let userID = ProfileManager.shared().curUserID()
let userSig = GenerateTestUserSig.genTestUserSig(userID)
TUILogin.login(userID, userSig: userSig, succ: {
    debugPrint("login success") 
}, fail: { (code, errorDes) in
   debugPrint("login failed, code:\(code), error: \(errorDes ?? "nil")")
})
``` 
2. 登录成功后，可以调用 TUIRoomCore 创建房间。
```swift
let roomId = 123
TUIRoomCore.shareInstance().createRoom("\(roomId)",speechMode: .freeSpeech,callback: { [weak self] code, message in
    if code == 0 {
       debugPrint("create room success") 
    } else {
    }
})
``` 
4. 创建成功，进入主页面。
```swift
let vc = TUIRoomMainViewController(roomId: roomId, isVideoOn: openCameraSwitch.isOn, isAudioOn: openMicSwitch.isOn)
TUIRoomCore.shareInstance().setDelegate(vc)
navigationController?.pushViewController(vc, animated: true)
```
![#600px](https://qcloudimg.tencent-cloud.cn/raw/e286295b14f04efb4f52be0da991ab56.png)

[](id:model_step5)
### 步骤5：成员进入房间
1. 成员调用 TUICore 中的 TUILogin 进行登录，请参考如下示例：
```swift
TUILogin.initWithSdkAppID(Int32(SDKAPPID))
let userID = ProfileManager.shared().curUserID()
let userSig = GenerateTestUserSig.genTestUserSig(userID)
TUILogin.login(userID, userSig: userSig, succ: {
    debugPrint("login success") 
}, fail: { (code, errorDes) in
   debugPrint("login failed, code:\(code), error: \(errorDes ?? "nil")")
})
``` 
2. 登录成功后，可以调用 TUIRoomCrre 进入房间。
```swift
let roomId = 123
TUIRoomCore.shareInstance().enterRoom("\(roomId)", callback: { [weak self] code, message in
    if code == 0 {
	    debugPrint("enter room success") 
	} else {
	}
})
``` 
4. 进入成功后，再进入主页面。
```swift
let vc = TUIRoomMainViewController(roomId: roomId, isVideoOn: openCameraSwitch.isOn, isAudioOn: openMicSwitch.isOn)
TUIRoomCore.shareInstance().setDelegate(vc)
navigationController?.pushViewController(vc, animated: true)
```
![#600px](https://qcloudimg.tencent-cloud.cn/raw/bc320a6fbd044ddad021aed0a488c298.png)

[](id:model_step6)
### 步骤6：屏幕分享
1. 调用 TUIRoomCore 的 `startScreenCapture` 实现分享。
2. 房间中其他成员会收到 `onRemoteUserScreenVideoAvailable` 的事件通知。

```swift
// 按钮点击实现屏幕分享
if #available(iOS 12.0, *) {
    // 屏幕分享
    let params = TRTCVideoEncParam()
    params.videoResolution = TRTCVideoResolution._1280_720
    params.resMode = TRTCVideoResolutionMode.portrait
    params.videoFps = 10
    params.enableAdjustRes = false
    params.videoBitrate = 1500
    TUIRoomCore.shareInstance().startScreenCapture(params)
    TUIRoomBroadcastExtensionLauncher.launch()
} else {
    view.window?.makeToast(.versionLowToastText)
}    
```

[](id:step)
### 步骤7：离开房间
- **主持人**调用 destoryRoom 接口解散房间，解散 IM 群聊，退出 TRTC 房间，成员端会收到 onDestroyRoom 回调消息，通知群解散，退出 TRTC 房间。
- **成员**调用 leaveRoom 接口解散房间，退出 IM 群聊，退出 TRTC 房间，其他成员端会收到 onRemoteUserLeave 回调，通知有成员离开房间。

```swift
if isHomeowner {
    TUIRoomCore.shareInstance().destroyRoom { [weak self] _, _ in
        guard let self = self else { return }
        self.navigationController?.popViewController(animated: true)
    }
} else {
    TUIRoomCore.shareInstance().leaveRoom { [weak self] _, _ in
        guard let self = self else { return }
        self.navigationController?.popViewController(animated: true)
    }
 }
```
