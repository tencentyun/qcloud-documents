### Xcode13 iOS9 编译报 UserNotifications.framework 无法加载或 archive 包无法启动，该如何处理？
错误信息：
```xml
Dyld Error Message:
Dyld Message: Library not loaded: /System/Library/Frameworks/UserNotifications.framework/UserNotifications
```

解决：`Target > Build Phases > Link Binary With Libraries `将 `UserNotifications.framework` 设置成 `Optional` 或者使用低版本打包。

### iOS 的开发环境 token，被当做生产环境 token 是什么原因？该如何处理？

在 Xcode 开发环境下安装 App，并使用 TPNS 推送开发环境的消息时，出现以下两种错误提示：
- 在 TPNS 控制台推送排查工具查询，出现提示"Token注册环境为：product，推送环境为：dev两者不匹配"。
![](https://qcloudimg.tencent-cloud.cn/raw/9aa45dc28e5fc654cb8bf8c835674490.png)
- Xcode 调试 TPNS SDK 错误日志提示 embedded.mobileprovision 缺失。
```xml
Missing Provisioning Profile - iOS Apps must contain a provisioning profile  named embedded.mobileprovision.
缺少配置文件-iOS应用程序必须包含名为embedded.mobileprovision的配置文件。
```

错误原因：App 包缺少配置文件 embedded.mobileprovision，导致 token 环境未知。
出现此问题时，可按以下步骤解决：
1. 在 Xcode 顶部菜单栏，单击**File**>**Project Settings**。
![](https://main.qcloudimg.com/raw/c470889681e34e87cc7f661ffb677e7d.png)
2. 将**Build System**设置为**Legacy Build System**，单击**Done**。
![](https://main.qcloudimg.com/raw/812b625ddfe5c2e7c40c0ad52cae9aec.png)
3. 重新打包, 卸载 App 重新安装。
4. 注册成功后，对 token 进行推送测试。

### iOS 打包生产环境无法收到推送？
1. 生产环境的测试满足条件：App 是 ad-hoc 打包/App Store 版本（发布证书 Production），上传了发布证书并验证通过。
2. 请检查 Xcode 工程中配置的 bundle id，是否与设置的 Provision Profile 文件匹配，且对应 App 的 Provision Profile 文件是否已配置消息推送能力。
3. 检查 embedded.mobileprovision 文件中的 aps-environment 字段对应的环境是否正确。

### Xcode12 模拟器集成通知扩展插件编译报错 building for iOS Simulator, but linking in object file built for iOS，该如何处理？

需要找到扩展插件 target，选择**Build Settings**>**Excluded Architectures**，添加 arm64 指令集，如下图所示：
![](https://main.qcloudimg.com/raw/1b62d4bc884c1870c70209b99200d6a6.png)

### TPNS 控制台上传 push 证书失败如何解决？

将推送证书 p12 文件转换成 pem 文件，并按以下步骤排查：

1. 打开终端，进入到 p12 文件目录。
2. 执行以下命令生成证书（apns-dev-cert 为示例推送证书名称，需改成您证书的名称）。
<dx-codeblock>
:::  plaintext
openssl pkcs12 -clcerts -nokeys -out apns-dev-cert.pem -in apns-dev-cert.p12
:::
</dx-codeblock>
3. 输入 p12 文件密码。
4. 执行以下命令，将 pem 格式证书转成文本：
<dx-codeblock>
:::  plaintext
openssl x509 -in apns-dev-cert.pem -inform pem -noout -text
:::
</dx-codeblock>
5. 查看证书环境及对应 Bundle id 看是否与应用匹配，如下图所示：
![](https://main.qcloudimg.com/raw/ba0e35a8bbd0e77022f26ad1dcca83ca.png)

### 在 App 冷启动时点击通知， 为什么没有触发点击通知事件的回调？

1. 请检查 TPNS SDK 的版本，如果是 V1.2.5.3 及之前的版本，建议更新至 V1.2.5.4 及之后的 SDK 版本。
2. 请检查 TPNS SDK 的初始化方法调用时机，目前需要在 App 启动方法中的主线程中尽快调用，保证 TPNS SDK 第一时间被设置为通知中心的代理。

### 推送内容为空时，在 iOS 10系统版本及以下的设备无法弹出通知？

在调用 Rest API 推送时 `content` 字段不能设置空，否则将导致在 **iOS 10系统及以下**的设备上无法弹出通知。


### TPNS 支持 p8 证书吗？

p8 证书存在安全隐患。虽然 p8 比 p12 有更长的有效期，但是同时也有更大的推送权限和范围。若泄露，可能会造成更加严重的影响。TPNS 推荐您使用 p12 来分别管理您的应用的推送服务。



### 推送消息无法收到？
消息推送是一个涉及到很多关联模块协作的任务，每一个环节出现异常都可能会导致消息收不到，建议使用 [工具箱](https://console.cloud.tencent.com/tpns/user-tools) 进行排查。以下是最为常见的问题：

**客户端排查**
- 检查设备通知设置
请检查**通知**>**应用名**，查看您的应用是否打开了推送消息权限。
- 检查设备网络设置
设备网络问题，可能导致客户端在注册 APNs 时获取接收消息的标识（Token）失败，这会导致无法使用移动推送 TPNS 服务给指定设备推送消息。

即使是客户端正确获取 Token，且已经将 Token 注册到移动推送 TPNS 后台，当使用移动推送 TPNS 服务器推送下发消息成功时，如果是设备未联网的状态，客户端将无法收到消息。若设备在短时内恢复网络连接，可能还会收到消息（APNs 会持有一段时间，然后再次下发消息）。

SDK 接入问题，在接入 SDK 之后，请确保能够获取到接收消息的标识（Device Token），具体请参见 [iOS SDK 集成指南](https://cloud.tencent.com/document/product/548/36663)。


**服务器排查**
- APNs 服务器问题
由于移动推送 TPNS 服务针对 iOS 设备下发消息是通过 APNs 服务下发，若 APNs 出现故障，将直接导致移动推送 TPNS 服务器请求 APNs 给设备下发消息失败。
- 移动推送 TPNS 服务器问题
移动推送 TPNS 服务端使用了多个功能模块之间的协作方式完成消息的下发，若其中任何一个模块有问题，也会导致消息推送出现问题。


**推送证书排查**
移动推送 TPNS 服务器在向 APNs 请求消息下发的时候，需要使用两个必需的参数：消息推送证书和设备标识（Device Token），在进行消息推送的时候，请确保消息推送证书是有效的。关于消息推送证书的设置请参见 [iOS 推送证书获取指引](https://cloud.tencent.com/document/product/548/36664)。




### 终端出现未找到应用程序的 “aps-environment” 的授权字符串错误？
请检查 Xcode 工程中配置的 bundle id 是否和设置的 Provision Profile 文件匹配，且对应 App 的 Provision Profile 文件是否已配置了消息推送能力。



### 客户端如何播放自定义推送消息音频？

首先，终端开发侧，需将音频文件放到 bundle 目录下：
- 若使用移动推送 TPNS 管理台创建推送时，在**高级设置**中填写音频文件名称（不需要音频文件的全路径）。
- 若使用 REST API 调用时，将 sound 参数设为音频文件名即可（不需要音频文件的全路径）。


### iOS 是否支持离线保存？ 
不支持，移动推送 TPNS 服务器下发消息请求到 APNs，若 APNs 发现设备不在线，APNs 会持有一段时间，具体时长 APNs 并未给出明确的说明。



### 为何 iOS 没有抵达数据？
- iOS 9.x 之前的版本，操作系统未提供 API 接口来监听消息抵达终端，故而无法统计。  
- iOS 10.0+ 的版本，操作系统提供了 Service Extension 接口，可供客户端调用，从而可以监听消息的到达。详情请参见 [通知服务扩展的使用说明](https://cloud.tencent.com/document/product/548/36667)。


### 使用移动推送 TPNS 服务端 SDK ，如何创建静默推送？
请给参数 content-available 赋值1，同时不使用 alert、badge、sound。



### iOS 开发环境下，注册偶现不返回 DeviceToken 或提示 APNs 请求 token 失败？
此问题现象是由于 APNs 服务不稳定导致的，可尝试通过以下方式解决：
1. 给手机插入 SIM 卡后使用4G网络测试。
2. 卸载重装、重启 App、关机重启后测试。
3. 打生产环境的包测试。
4. 更换其它 iOS 系统的手机测试。


### iOS 如何在测试设备有限的情况下扩大测试规模？
1. 企业级证书签名
申请企业级签名证书和企业级推送证书，发布方式如下：
使用企业级签名证书构建并发布 App，体验者可以通过企业内部开放的渠道下载安装 App。
2. AppStore 发布证书签名
使用当前 AppStore 的发布签名证书，发布方式如下：
TestFlight 发布预览版，先将 ipa 包上传到 [App Store Connect](https://appstoreconnect.apple.com)，然后通过 TestFlight 创建一个灰度版本，并在 TestFlight 上设置指定版本的体验人员名单(Apple ID)，最后体验者可以通过苹果官方**TestFlight**App 下载安装。


### iOS 如何只更改角标而不弹出信息？
可使用 API 在创建推送时使用通知栏消息类型，且标题内容设为空，同时只设置 badge_type 即可，详情可参考 [API 文档说明](https://cloud.tencent.com/document/product/548/39064#.E5.8F.AF.E9.80.89.E5.8F.82.E6.95.B0)。
示例如下：
<dx-codeblock>
:::  json
{
    "platform": "ios",
    "audience_type": "token",
    "environment":"dev",
    "token_list": [
    "05a8ea6924590dd3a94480fa1c9fc8448b4e"],
    "message_type":"notify",
    "message":{
    "ios":{
        "aps": {
            "badge_type":-2
        }
    }
 }
}
:::
</dx-codeblock>



### App 出现 Crash: you can't call -sendResponse: twice nor after encoding it 报错，该如何处理？
如果您的 App 集成了 TPNS iOS SDK（1.2.7.2 - 1.2.5.4），且使用到 TPNS 的**撤回**功能，同时 App 侧实现了如下系统回调：
```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo  fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler
```
则可能会遇到此问题。您可以使用**覆盖**功能来实现已发送消息的处理。


###  Xcode 调试提示“Error Domain=NSCocoaErrorDomain Code=1001 "APNS 请求 token 失败，如何处理？
**问题描述**：
Xcode 调试提示“Error Domain=NSCocoaErrorDomain Code=1001 "APNS请求token失败-->请依次按以下方法解决：优先使用4G网络并重启手机，若多次重启仍然不行，建议更换手机测试!" UserInfo={NSLocalizedDescription=APNS请求token失败-->请依次按以下方法解决：优先使用4G网络并重启手机，若多次重启仍然不行，建议更换手机测试!“，按照提示操作后问题还是存在。

**排查思路**：
1. 建议使用 TPNS SDK 的相关方法，避免与其他注册远程通知的方法同时运行。
2. 建议修改 Xcode 编译的系统，改用 Legacy Build System 去编译，看是否存在类似静态库重复导入引起的类重复定义的问题，具体操作如下：
	1. 在 Xcode 顶部菜单栏，单击**File**>**Project Settings**。
	![](https://main.qcloudimg.com/raw/bec61fe573cfe656b426f2e76a6e7310.png)
	2. 将**Build System**设置为**Legacy Build System**，单击**Done**。
	![](https://main.qcloudimg.com/raw/e3ac972a5e6c6c7f8ebdab886c7f2342.png)
	3. 重新编译。如果有编译错误针对修改。







