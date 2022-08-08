本文将介绍如何用最短的时间完成 TUICallKit 组件的接入，跟随本文档，您将在一个小时的时间内完成如下几个关键步骤，并最终得到一个包含完备 UI 界面的视频通话功能。

## 环境准备
- iOS 9.0 (API level 16) 及更高。

[](id:step1)
## 步骤一：开通服务
TUICallKit 是基于腾讯云 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 和 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 两项付费 PaaS 服务构建出的音视频通信组件。您可以按照如下步骤开通相关的服务并体验 7 天的免费试用服务：

1. 登录到 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击**创建新应用**，在弹出的对话框中输入您的应用名称，并单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/1105c3c339be4f71d72800fe2839b113.png)
2. 单击刚刚创建出的应用，进入**基本配置**页面，并在页面的右下角找到**开通腾讯实时音视频服务**功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。
![](https://qcloudimg.tencent-cloud.cn/raw/667633f7addfd0c589bb086b1fc17d30.png)
3. 在同一页面找到 **SDKAppID** 和**密钥**并记录下来，它们会在后续的[步骤四：登录 TUI 组件](#step4)中被用到。
![](https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png)


[](id:step2)
## 步骤二：下载并导入组件
**通过 cocoapods 导入组件**，具体步骤如下：
1. 在您的工程 `Podfile` 文件同一级目录下创建 `TUICallKit` 文件夹。
2. 单击进入 [**Github/TUICalling**](https://github.com/tencentyun/TUICalling) ，选择克隆/下载代码，然后将 [**TUICalling/iOS/**](https://github.com/tencentyun/TUICalling/tree/main/iOS) 目录下的 `TUICallKit`、`Resources` 文件夹 和 `TUICallKit.podspec` 文件拷贝到您在 `步骤1` 创建的 TUICallKit 文件夹下。
3. 在您的 Podfile 文件中添加以下依赖，之后执行 `pod install` 命令，完成导入。
```
# :path => "指向TUICalling.podspec的相对路径"
pod 'TUICallKit', :path => "TUICallKit/TUICallKit.podspec", :subspecs => ["TRTC"]
```

>!  `TUICallKit`、`Resources` 文件夹 和`TUICallKit.podspec`文件必需在同一目录下。

[](id:step3)
## 步骤三：完成工程配置
使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。

```
<key>NSCameraUsageDescription</key>
<string>CallingApp需要访问您的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>CallingApp需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
```
![](https://qcloudimg.tencent-cloud.cn/raw/7f91f3f8defa5a0650f08b8acf960219.png)


## 步骤四：登录 TUI 组件
在您的项目中添加如下代码，它的作用是通过调用 TUICore 中的相关接口完成 TUI 组件的登录。这个步骤异常关键，因为只有在登录成功后才能正常使用 TUICallKit 的各项功能，故请您耐心检查相关参数是否配置正确：
<dx-codeblock>
:::  Objective-C
```
// 组件登录
[TUILogin login:Int32(sdkAppId) userId:user userSig:userSig succ:^{
        NSLog(@"login success");
} fail:^(int code, NSString *msg) {
        NSLog(@"login failed, code: %d, error: %@", code, msg);
}];
```
:::
::: Swift
```
// 组件登录
TUILogin.login(sdkAppId, userId: user, userSig: userSig) {
        print("login success")
} fail: { (code, err) in
        print("login failed, code: \(code), error: \(message ?? "nil")")
}
```
:::
</dx-codeblock>

**参数说明**：
这里详细介绍一下 login 函数中所需要用到的几个关键参数：
- sdkAppId：在步骤一中的最后一步中您已经获取到，这里不再赘述。
- userId：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。
- userSig：使用步骤三中获取的 SecretKey 对 SDKAppID、UserID 等信息进行加密，就可以得到 UserSig，它是一个鉴权用的票据，用于腾讯云识别当前用户是否能够使用 TRTC 的服务。您可以通过控制台中的 [**辅助工具**](https://console.cloud.tencent.com/im/tool-usersig) 生成一个临时可用的 UserSig。
- 更多信息请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。
​
> ! 这个步骤也是目前我们收到的反馈最多的步骤，常遇到的问题有如下几个：
> 1. sdkAppId 设置错误，国内站的 SDKAppID 一般是以140开头的10位整数；
> 2. userSig 被错配成了加密密钥（Secretkey），userSig 是用 SecretKey 把 sdkAppId、userId 以及过期时间等信息加密得来的，而不是直接把 Secretkey 配置成 userSig。
> 3. userId 被设置成“1”、“123”、“111”等简单字符串，由于 **TRTC 不支持同一个 UserID 多端登录**，所以在多人协作开发时，形如 “1”、“123”、“111” 这样的 userId 很容易被您的同事占用，导致登录失败，因此我们建议您在调试的时候设置一些辨识度高的 userId。
​
>! Github 中的示例代码使用了 genTestUserSig 函数在本地计算 userSig 是为了更快地让您跑通当前的接入流程，但该方案会将您的 SecretKey 暴露在 App 的代码当中，这并不利于您后续升级和保护您的 SecretKey，所以我们强烈建议您将 userSig 的计算逻辑放在服务端进行，并由 App 在每次使用 TUICallKit 组件时向您的服务器请求实时计算出的 userSig。



[](id:step5)
## 步骤五：拨打通话
### 1对1视频通话
通过调用 TUICallKit 的 call 函数并指定通话类型和被叫方的 userid，就可以发起语音或者视频通话。
- <dx-codeblock>
:::  Objective-C
```
// 发起1对1视频通话(假设 userid 为 mike)
[[TUICallKit createInstance] call: @"mike" callMediaType: TUICallMediaTypeVideo];
```
```
:::
::: Swift
```
// 发起1对1视频通话(假设 userid 为 mike)
TUICallKit.createInstance().call(userId: "mike", callType: .video)
```
:::
</dx-codeblock>

### 群内视频通话
通过调用 TUICallKit 的 groupCall 函数并指定通话类型和被叫方的 userid，就可以发起群内的视频或语音通话。
-  <dx-codeblock>
:::  Objective-C
```
[[TUICallKit createInstance] groupCall:@"12345678" userIdList:@[@"denny", @"mike", @"tommy"] callMediaType:TUICallMediaTypeVideo];
```
```
:::
::: Swift
```
TUICallKit.createInstance().groupCall("12345678", userIdList: ["denny", "mike", "tommy"], callMediaType: .video)
```
:::
</dx-codeblock>

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| groupId | String | 群组 Id，示例：`@"12345678"` |
| userIdList | Array | 目标用户的userId 列表，示例：`@[@"denny", @"mike", @"tommy"]` |
| callMediaType | TUICallMediaType | 通话的媒体类型，示例：`TUICallMediaTypeVideo` |

>? 
>1. 群组的创建详见：[ IM 群组管理](https://cloud.tencent.com/document/product/269/75394#.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84) ，或者您也可以直接使用 [IM TUIKit](https://cloud.tencent.com/document/product/269/37059)，一站式集成聊天、通话等场景。
>2. TUICallKit 目前还不支持发起非群组的多人视频通话，如果您有此类需求，欢迎反馈： [TUICalling 需求收集表]()。

[](id:step6)
## 步骤六：接听通话
在步骤四完成后，收到来电请求后，TUICallKit 组件会自动启动相应的接听界面。

[](id:step7)
## 步骤七：更多特性
### 一. 设置昵称&头像
如果您需要自定义昵称或头像，可以使用如下接口进行更新：
-  <dx-codeblock>
:::  Objective-C
```
[[TUICallKit createInstance] setSelfInfo:@"昵称" avatar:@"头像url" succ:^{
        NSLog(@"login success");
} fail:^(int code, NSString *errMsg) {
        NSLog(@"login failed, code: %d, error: %@", code, errMsg);
}];
```
```
:::
::: Swift
```
TUICallKit.createInstance().setSelfInfo(nickname: "昵称", avatar: "头像url") {
        print("login success")
} fail: {(code, desc) in
        print("login failed, code: \(code), error: \(desc ?? "nil")")
}
```
:::
</dx-codeblock>
> ! 这里有个常见问题：因为用户隐私限制，非好友之间的通话，被叫的昵称和头像更新可能会有延迟，一次通话成功后就会顺利更新，请知悉~

### 二. 离线唤醒
完成以上步骤，就可以实现音视频通话的拨打和接通，但如果您的业务场景需要在 `App 的进程被杀死后`或者`APP 退到后台后`，还可以正常接收到音视频通话请求，就需要增加离线唤醒功能，详情见 [**离线唤醒（iOS）**](https://tcloud-doc.isd.com/document/product/647/78741?!preview)。

### 三. 悬浮窗功能
如果您的业务需要开启悬浮窗功能，您可以在 TUICallKit 组件初始化时调用以下接口开启该功能：
-  <dx-codeblock>
:::  Objective-C
```
[[TUICallKit createInstance] enableFloatWindow:true];
```
```
:::
::: Swift
```
TUICallKit.createInstance().enableFloatWindow(enable: true))
```
:::
</dx-codeblock>

### 四. 通话状态监听
如果您的业务需要 **监听通话的状态**，例如通话开始、结束，以及通话过程中的网络质量等等，可以监听以下事件：
<dx-codeblock>
:::  Objective-C Objectivec
[[TUICallEngine createInstance] addObserver:self];

- (void)onCallBegin:(nonnull TUIRoomId *)roomId callMediaType:(TUICallMediaType)callMediaType callRole:(TUICallRole)callRole {
    
}

- (void)onCallEnd:(nonnull TUIRoomId *)roomId callMediaType:(TUICallMediaType)callMediaType callRole:(TUICallRole)callRole totalTime:(float)totalTime {
   
}

- (void)onUserNetworkQualityChanged:(nonnull NSArray<TUINetworkQualityInfo *> *)networkQualityList {
    
}
:::
::: Swift
TUICallEngine.createInstance().add(self)

public func onCallBegin(roomId: TUIRoomId, callMediaType: TUICallMediaType, callRole: TUICallRole) {
        
}
public func onCallEnd(roomId: TUIRoomId, callMediaType: TUICallMediaType, callRole: TUICallRole, totalTime: Float) {
        
}
public func onUserNetworkQualityChanged(networkQualityList: [TUINetworkQualityInfo]) {
        
}
:::
</dx-codeblock>

### 五. 自定义铃音
如果您需要自定义来电铃音，可以通过如下接口进行设置：
<dx-codeblock>
:::  Objective-C Objectivec
[[TUICallKit createInstance] setCallingBell:filePath];
:::
::: Swift
TUICallKit.createInstance().setCallingBell(filePath: filePath)
:::
</dx-codeblock>