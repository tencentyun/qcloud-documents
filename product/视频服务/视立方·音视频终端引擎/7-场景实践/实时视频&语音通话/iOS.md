## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验实时音视频通话的效果。
<table>
<tr>
   <th>主动呼叫</th>
   <th>被叫接听</th>
 </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/video1.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/video2.gif"/></td>
</tr>
</table>


>! 为方便您快速实现音视频通话功能，我们对 TUICalling 组件进行了改造，通话 UI 在 TUICalling 组件内部实现，您可以无需关注 UI。

[](id:ui)

## 运行并体验 App

[](id:ui.step1)

### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助>[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 输入应用名称，例如 `TestVideoCall` ，单击 **创建**。
3. 单击 **已下载，下一步**，跳过此步骤。

![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)
>!本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。


[](id:ui.step2)
### 步骤2：下载 App 源码
单击进入 [TUICalling](https://github.com/tencentyun/TUICalling)，Clone 或者下载源码。

[](id:ui.step3)
### 步骤3：配置 App 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `iOS/Example/Debug/GenerateTestUserSig.swift` 文件。
3. 设置 `GenerateTestUserSig.swift` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为0，请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</ul>
<img src="https://main.qcloudimg.com/raw/a226f5713e06e014515debd5a701fb63.png">
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui.step4)
### 步骤4：运行 App

Xcode（11.0及以上的版本）打开源码工程 `TUICalling/Example/TUICallingApp.xcworkspace`，单击 **运行** 即可开始调试本 App。



## 体验应用
>! 体验应用至少需要两台设备。

### 用户 A
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
<img src="https://main.qcloudimg.com/raw/a0c73f6904ac152a84cdf4d619171fc4.png" width="320"/>
2. 输入要拨打的 userId，单击搜索，如下图示：
<img src="https://main.qcloudimg.com/raw/61edd11a23197ebce26e91863f9fef63.png" width="320"/>
3. 单击 **呼叫**，选择拨打 **视频通话** （**请确保被叫方保持在应用内，否则可能会拨打失败**）。<br>
<img src="https://main.qcloudimg.com/raw/450e50dd4bb58e2950d6574ab88715e2.png" width="320"/>

### 用户 B
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
<img src="https://main.qcloudimg.com/raw/94fcd741becbcfe4cca97778e180e4ca.png" width="320"/>
2. 进入主页，等待接听来电。



[](id:model)
## 具体接入流程

[源码](https://github.com/tencentyun/TUICalling/tree/main/iOS/Source) 文件夹 `Source` 中包含了我们对外暴露的开源组件 TUICalling，您可以在  `TUICalling.h`  文件中看到该组件提供的接口函数。
![](https://main.qcloudimg.com/raw/18e2e6fd62ade4a8bac560d45f4fbab4.png)


您可以直接使用开源组件 TUICalling 轻松实现音视频通话功能，而无需再自己实现复杂的通话UI界面和逻辑。

[](id:model.step1)
### 步骤1：配置权限

使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
- **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
- **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语。

![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)

[](id:model.step2)
### 步骤2：导入 TUICalling 组件

**通过 cocoapods 导入组件**，具体步骤如下：
1. 将工程目录下的 `Source`、`Resources` 文件夹 和 `TUICalling.podspec` 文件拷贝到您的工程目录下。
2. 在您的 `Podfile` 文件中添加以下依赖。之后执行 `pod install` 命令，完成导入。

```swift\
# :path => "指向TUICalling.podspec所在目录的相对路径"
 pod 'TUICalling', :path => "../", :subspecs => ["TRTC"]
```

>!  `Source`、`Resources` 文件夹 和`TUICalling.podspec`文件必需在同一目录下。

[](id:model.step3)
### 步骤3：初始化并登录组件

1. 调用 `TUICalling.sharedInstance()` 进行组件初始化。
2. 调用 `TUILogin.initWithSdkAppID(SDKAPPID)` 进行登录初始化。
3. 调用 `TUILogin.login(userId, userSig)` 完成组件的登录，其中几个关键参数的填写请参考下表：
<table>
<tr><th>参数名</th><th>作用</th></tr>
<tr>
<td>sdkAppID</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr><tr>
<td>userId</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）。建议结合业务实际账号体系自行设置。 </td>
</tr><tr>
<td>userSig</td>
<td>腾讯云设计的一种安全保护签名，计算方式请参考 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算及使用 UserSig</a>。</td>
</tr></table>

<dx-codeblock>
::: swift
// 组件初始化
TUICalling.sharedInstance();
// 登录
TUILogin.initWithSdkAppID(SDKAPPID)
TUILogin.login(userId, userSig) {
   print("login success")
} fail: { code, errorDes in
   print("login failed, code:\(code), error: \(errorDes ?? "nil")")
}
:::
</dx-codeblock>

[](id:model.step4)

### 步骤4：实现音视频通话

1. 发起方：调用 TUICalling 的 `call();` 方法发起通话的请求, 并传入用户 ID数组（userIDs）和通话类型（type），通话类型参数传入`.audio`（音频通话）或者`.video`（视频通话）。如果用户 ID数组（userIDs）只有1个 userID 时视为单人通话，如果用户 ID 数组（userIDs）有多个 userID 时（>=2）视为多人通话。
2. 接收方：当接收方处于已登录状态时，会自动启动相应的界面。如果希望接收方在不处于登录状态时也能收到通话请求，请参见 [离线接听](#model.offline)。

**主动发起通话**，示例代码如下：
<dx-codeblock>
::: swift
TUICalling.shareInstance().call(userIDs, .video)
:::
</dx-codeblock>



[](id:model.offline)


### 步骤5：实现离线接听

>?如果您的业务定位是在线客服等不需要离线接听功能的场景，那么完成上述 [步骤1](#model.step1) - [步骤4](#model.step5) 的对接即可。但如果您的业务定位是社交场景，建议实现离线接听。

IM SDK 支持离线推送，您需要进行相应的设置才能达到可用标准。

1. 申请 Apple 推送证书，具体操作请参见 [Apple 推送证书申请](https://cloud.tencent.com/document/product/269/3898)。
2. 在后台及客户端配置离线推送，具体操作请参见 [离线推送（iOS）](https://cloud.tencent.com/document/product/269/44517)。
3. 目前在信令发送中已经集成了离线发送的函数，当配置好 App 的离线推送后，消息就可实现离线推送。

[](id:api)

## 组件 API 列表

TUICalling 组件的 API 接口列表如下：

| 接口函数                | 接口功能                                                  |
| --------------------  | ------------------------------------ ---------- |
| call                       | C2C 邀请通话                                           |
| setCallingListener  | 设置监听器                                               |
| setCallingBell        | 设置铃声(建议在30s以内)                            |
| enableMuteMode   | 开启静音模式                                            |
| enableFloatWindow | 开启悬浮窗功能（默认关），如果用户自定义视图（enableCustomViewRoute）则不支持悬浮窗    | 
| enableCustomViewRoute      | 开启自定义视图， 开启后，会在呼叫/被叫开始回调中，接收到CallingView的实例，由开发者自行决定展示方式。注意：必须全屏或者与屏幕等比例展示，否则会有展示异常            |

## 常见问题

### 1、CocoaPods 如何安装？

在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```

### 2、TUICalling 是否支持后台运行？

支持，如需要进入后台仍然运行相关功能，可选中当前工程项目，在 **Capabilities** 下的设置  **Background Modes** 打开为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture** ，如下图所示：
![](https://main.qcloudimg.com/raw/d960dfec88388936abce2d4cb77ac766.jpg)

