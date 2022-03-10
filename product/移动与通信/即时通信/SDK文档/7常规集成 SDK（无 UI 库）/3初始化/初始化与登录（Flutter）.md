## 初始化与登录
类 [V2TIMManager](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager-class.html) 是 IM SDK 主核心类也是 IM SDK 的入口类，负责 IM SDK 的初始化、登录、消息收发，建群退群等功能。调用 [initSDK](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/initSDK.html) 接口即可完成初始化：

```
import 'package:tencent_im_sdk_plugin/enum/V2TimSDKListener.dart';
import 'package:tencent_im_sdk_plugin/enum/log_level_enum.dart';
import 'package:tencent_im_sdk_plugin/tencent_im_sdk_plugin.dart';


    TencentImSDKPlugin.v2TIMManager.initSDK(
      sdkAppID: 0,   // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
      loglevel: LogLevelEnum.V2TIM_LOG_DEBUG, //日志
      listener: V2TimSDKListener(),
    );
```


初始化接口 initSDK（SDKAppID、loglevel、listener）包含三个必填的参数，分别是 SDKAppID，LogLevelEnum 和事件监听器。

### SDKAppID
SDKAppID 即应用 ID，它是腾讯云 IM 服务用于区分客户帐号的唯一标识。每一个独立的 App 都建议申请一个新的 SDKAppID，不同 SDKAppID 之间的消息天然隔离，不能互通。
您可以在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 查看所有的 SDKAppID，单击 **创建新应用** 即可创建新的 SDKAppID。
![](https://qcloudimg.tencent-cloud.cn/raw/d7f4bacfc440fe50cec41a48030a9928.png)

### loglevel
参数 `loglevel` 用于对日志级别的设置，即 [logLevel](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/enum_log_level_enum/LogLevelEnum.html) 参数，日志级别如下表所示：

| 日志级别 | LOG 输出量 |
|---------|---------|
| V2TIM_LOG_NONE | 不输出任何 log | 
| V2TIM_LOG_DEBUG | 输出 DEBUG，INFO，WARNING，ERROR 级别的 log | 
| V2TIM_LOG_INFO | 输出 INFO，WARNING，ERROR 级别的 log | 
| V2TIM_LOG_WARN | 输出 WARNING，ERROR 级别的 log | 
| V2TIM_LOG_ERROR | 输出 ERROR 级别的 log | 


### 事件监听器
[V2TimSDKListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimSDKListener/V2TimSDKListener-class.html) 提供了网络状态以及用户信息变更的监听：

| 事件回调 | 事件描述 | 推荐操作 |
|---------|---------|---------|
| onConnecting | 正在连接到腾讯云服务器 | 适合在 UI 上展示“正在连接”状态。 |
| onConnectSuccess | 已经成功连接到腾讯云服务器 | - |
| onConnectFailed | 连接腾讯云服务器失败 | 可以提示用户当前网络连接不可用。 |
| onKickedOffline | 当前用户被踢下线 | 此时可以 UI 提示用户“您已经在其他端登录了当前帐号，是否重新登录？” |
| onUserSigExpired | 登录票据已经过期 | 请使用新签发的 UserSig 进行登录。  |
| onSelfInfoUpdated | 当前用户的资料发生了更新 | 可以在 UI 上更新自己的头像和昵称。 |

>!若收到 `onUserSigExpired` 回调，说明您登录用的 UserSig 票据已经过期，请更新后重新登录。如果继续使用过期的 UserSig，会导致 SDK 登录死循环。

## 登录
调用 `v2TIMManager` 的 [login(userID, userSig)](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/login.html) 函数可以进行登录，只有在 SDK 登录成功后，才能使用 IM SDK 的各项能力。

```
    V2TimCallback res = await TencentImSDKPlugin.v2TIMManager.login(
      userID: userID,
      userSig: userSig, 
    );
```

- UserID： 建议只包含大小写英文字母、数字、下划线和连词符集中类型的字符，长度最大不超过32字节。
- UserSig：IM SDK 登录票据，由您的业务服务器进行计算以保证安全，计算方法请参考 [UserSig 后台 API](https://cloud.tencent.com/document/product/269/32688)。
>!调用 IM SDK Login 成功登录后，将会开始计算 DAU，请根据业务场景合理使用 IM SDK Login 操作，避免出现 DAU 过高的情况。

### 登录时机
以下场景需调用登录：
- App 启动后首次使用 IM SDK 的能力时。
- IM SDK 抛出 `onUserSigExpired` 回调时，即登录票据已过期时，需要使用新的 UserSig 进行登录。
- IM SDK 抛出 `onKickOffline` 回调时，即当前用户被踢下线时，可以通过 UI 提示用户“您已经在其他端登录了当前帐号，是否重新登录？” 如果用户选择“是”，就可以进行重新登录。

以下场景无需调用登录：
- 用户的网络断开并重新连接后，不需要调用 login 函数，SDK 会自动上线。
- 当一个登录过程在进行时，不需要进行重复登录。

### 多端登录
同样类型的两台手机不能同时登录一个帐号，例如两台苹果手机不能同时登录一个帐号。但是一台 Android 手机和一台苹果手机会被认为是两端，可以同时登录。多端登录相关配置请参考 [登录设置](https://cloud.tencent.com/document/product/269/38656#.E7.99.BB.E5.BD.95.E8.AE.BE.E7.BD.AE)。

## 登出
登出比较简单，使用 [logout()](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/logout.html) 函数即可。




