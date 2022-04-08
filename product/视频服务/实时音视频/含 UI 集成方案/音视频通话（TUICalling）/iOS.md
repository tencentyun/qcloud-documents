## 组件介绍

TUICalling 是一个开源的音视频 UI 组件，通过在项目中集成 TUICalling 组件，您只需要编写几行代码就可以为您的 App 添加“一对一音视频通话”，“多人音视频通话”等场景，并且支持离线唤起能力。TUICalling 同时支持 Android、Web、小程序、Flutter、UniApp 等平台，基本功能如下图所示：

<table class="tablestyle">
<tbody><tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/c792c6fa94e4c4dd3151003b0f28eab7.png" width="250"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/a75f7d5f2911f2e21d3e4b3b9dfc4db5.png" width="500"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/3bb1a748b590518e2be09326cc30dc0b.png" width="250"></td>
</tr>
</tbody></table>

## 组件集成

### 步骤一：导入 TUICalling 组件

**通过 cocoapods 导入组件**，具体步骤如下：
1. 在您的工程 `Podfile` 文件同一级目录下创建 `TUICalling` 文件夹。
2. 单击进入 [**Github/TUICalling**](https://github.com/tencentyun/TUICalling) ，选择克隆/下载代码，然后将 [**TUICalling/iOS/**](https://github.com/tencentyun/TUICalling/tree/main/iOS) 目录下的 `Source`、`Resources` 文件夹 和 `TUICalling.podspec` 文件拷贝到您在 `步骤1` 创建的 TUICalling 文件夹下。
3. 在您的 Podfile 文件中添加以下依赖，之后执行 `pod install` 命令，完成导入。
```
# :path => "指向TUICalling.podspec的相对路径"
pod 'TUICalling', :path => "TUICalling/TUICalling.podspec", :subspecs => ["TRTC"]
```

>!  `Source`、`Resources` 文件夹 和`TUICalling.podspec`文件必需在同一目录下。

### 步骤二：配置权限

使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。

```
<key>NSCameraUsageDescription</key>
<string>CallingApp需要访问您的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>CallingApp需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
```
![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)

### 步骤三：创建并初始化组件

<dx-tabs>
:::  Objective-C
```
// 1.组件登录
[TUILogin initWithSdkAppID:@"您的SDKAppID"];
[TUILogin login:@"您的UserID" userSig:@"您的UserSig" succ:^{
    NSLog(@"login success");
} fail:^(int code, NSString *msg) {
    NSLog(@"login failed, code: %d, error: %@", code, msg);
}];

// 2.初始化TUICalling实例
[TUICalling shareInstance];
```
:::
::: Swift
```
// 1.组件登录
TUILogin.initWithSdkAppID("您的SDKAppID")
TUILogin.login("您的UserID", userSig: "您的UserSig") {
    print("login success")
} fail: { code, message in
    print("login failed, code: \(code), error: \(message ?? "nil")")
}

// 2.初始化TUICalling实例
TUICalling.shareInstance()
```
:::
</dx-tabs>

**参数说明**：
- **SDKAppID**：**TRTC 应用ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3d6ebfa2a1e4ae5d3af3ecd564fb1463.png)
- **SecretKey**：**TRTC 应用密钥**，和 SDKAppID 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **UserID**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **UserSig**：根据 SDKAppId、UserID，SecretKey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [TUICalling示例工程](https://github.com/tencentyun/TUICalling/blob/main/iOS/Example/Debug/GenerateTestUserSig.swift#L39) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

### 步骤四：实现音视频通话

- 实现1对1视频通话 [TUICalling#call](https://cloud.tencent.com/document/product/647/47748#call)
<dx-codeblock>
:::  Objective-C Objectivec
// 发起1对1视频通话，假设userId为：1111
[[TUICalling shareInstance] call:@[@"1111"] type:TUICallingTypeVideo];
:::
::: Swift Swift
// 发起1对1视频通话，假设userId为：1111
TUICalling.shareInstance().call(userIDs: ["1111"], type: .video)
:::
</dx-codeblock>
- 实现多人视频通话 [TUICalling#call](https://cloud.tencent.com/document/product/647/47748#call)
<dx-codeblock>
:::  Objective-C Objectivec
// 发起多人视频通话，假设userId分别为：1111、2222、3333；
[[TUICalling shareInstance] call:@[@"1111", @"2222", @"3333"] type:TUICallingTypeVideo];
:::
::: Swift Swift
// 发起多人视频通话，假设userId分别为：1111、2222、3333；
TUICalling.shareInstance().call(userIDs: ["1111", "2222", "3333"], type: .video)
:::
</dx-codeblock>

>? 当接收方完成步骤三后，即登录成功后，再收到通话请求后，TUICalling组件会自动启动相应的接听界面。

### 步骤五：离线推送（可选）
完成以上四个步骤，就可以实现视频通话的拨打和接通，但如果您的业务场景需要在 `App 的进程被杀死后`或者 `App 退到后台后`，还可以正常接收到音视频通话请求，就需要为 TUICalling 组件增加离线推送功能，详情见 [**离线推送（iOS）**](https://cloud.tencent.com/document/product/269/44517)。

### 步骤六：状态监听（可选）

如果您的业务需要 [监听通话的状态](https://cloud.tencent.com/document/product/647/47748#setCallingListener)，例如通话开始、结束等，可以监听以下事件：
<dx-codeblock>
:::  Objective-C Objectivec
[[TUICalling shareInstance] setCallingListener:self];

- (BOOL)shouldShowOnCallView {
    return YES;
}

- (void)callStart:(nonnull NSArray<NSString *> *)userIDs type:(TUICallingType)type role:(TUICallingRole)role viewController:(UIViewController * _Nullable)viewController {

}

- (void)callEnd:(nonnull NSArray<NSString *> *)userIDs type:(TUICallingType)type role:(TUICallingRole)role totalTime:(float)totalTime {

}

- (void)onCallEvent:(TUICallingEvent)event type:(TUICallingType)type role:(TUICallingRole)role message:(nonnull NSString *)message {

}
:::
::: Swift Swift
TUICalling.shareInstance().setCallingListener(listener: self)

public func shouldShowOnCallView() -> Bool {
    return true
}
    
public func callStart(userIDs: [String], type: TUICallingType, role: TUICallingRole, viewController: UIViewController?) {

}
    
public func callEnd(userIDs: [String], type: TUICallingType, role: TUICallingRole, totalTime: Float) {

}
    
public func onCallEvent(event: TUICallingEvent, type: TUICallingType, role: TUICallingRole, message: String) {

}
:::
</dx-codeblock>

### 步骤七：悬浮窗功能（可选）

如果您的业务需要开启 [悬浮窗功能](https://cloud.tencent.com/document/product/647/47748#enableFloatWindow)，您可以在 TUICalling 组件初始化时调用`TUICalling.shareInstance().enableFloatWindow(enable: true)`开启该功能。

>? 目前组件仅支持应用内悬浮窗（最小化退到上一层界面）。

## 常见问题

### TUICalling 组件支持自定义铃声吗？

支持，调用 [TUICalling#setCallingBell](https://cloud.tencent.com/document/product/647/47748#setCallingBell) 即可。

### CocoaPods如何安装？

在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```

### TUICalling 是否支持后台运行？

支持，如需要进入后台仍然运行相关功能，可选中当前工程项目，在 **Capabilities** 下的设置  **Background Modes** 打开为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture** ，如下图所示：
![](https://main.qcloudimg.com/raw/d960dfec88388936abce2d4cb77ac766.jpg)

>? 更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
