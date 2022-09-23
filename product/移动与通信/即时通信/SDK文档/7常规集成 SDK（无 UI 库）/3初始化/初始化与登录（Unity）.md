## 初始化

即时通信 IM Unity SDK 需要初始化并登录后才能使用。集成 SDK 后，首先需要进行初始化，在 Unity 中代码如下：

```c#
public static void Init() {
        SdkConfig sdkConfig = new SdkConfig();

        sdkConfig.sdk_config_config_file_path = Application.persistentDataPath + "/TIM-Config";

        sdkConfig.sdk_config_log_file_path = Application.persistentDataPath + "/TIM-Log";

        if (sdkappid == "")
        {
            return;
        }

        TIMResult res = TencentIMSDK.Init(long.Parse(sdkappid), sdkConfig);
}
```

### SDKAppID

SDKAppID 即应用 ID，它是腾讯云 IM 服务用于区分客户帐号的唯一标识。每一个独立的 App 都建议申请一个新的 SDKAppID，不同 SDKAppID 之间的消息天然隔离，不能互通。
您可以在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 查看所有的 SDKAppID，单击**添加新应用**即可创建新的 SDKAppID。

### sdkConfig

配置即时通信 IM 运行时的日志、数据的存储路径。

### sdk_config_config_file_path

即时通信 IM 本地数据存储路径。
>!该路径需要应用有可读写权限。

### sdk_config_log_file_path

即时通信 IM 日常存储路径。
>!该路径需要应用有可读写权限。

### TIMResult

调用 SDK 同步返回的结果，当 res 为 TIMResult.TIM_SUCC = 0 时接口调用成功。

### 其他

在 SDK 初始化成功后，请立即添加需要用到的事件监听，以免消息遗漏。

## 登录

```c#
public static void Login() {
        if (userid == "" || user_sig == "")
        {
            return;
        }
        // 业务可以替换自己的 sdkappid
        TIMResult res = TencentIMSDK.Login(userid, user_sig, (int code, string desc, string json_param, string user_data)=>{
          
        });
}
```

## UserID

登录用户唯一 ID， 建议只包含大小写英文字母（a-z、A-Z）、数字（0-9）、下划线（_）和连词符（-），长度最大不超过32字节。

## UserSig

IM SDK 登录票据，由您的业务服务器进行计算以保证安全，计算方法请参考 [UserSig 后台 API](https://cloud.tencent.com/document/product/269/32688)。

### 登录时机

- App 启动后首次使用 IM SDK 的能力时。
- IM SDK 抛出 `UserSigExpiredCallback` 回调，即登录票据已过期时，需要使用新的 UserSig 进行登录。
- IM SDK 抛出 `KickedOfflineCallback` 回调，即当前用户被踢下线时，可以通过 UI 提示用户“您已经在其他端登录了当前帐号，是否重新登录？” 如果用户选择“是”，就可以进行重新登录。

### 无需重新登录

- 用户的网络断开并重新连接后，不需要调用 login 函数，SDK 会自动上线。
- 当一个登录过程在进行时，不需要进行重复登录。

### 多端登录

同样类型的两台手机不能同时登录一个帐号，例如两台苹果手机不能同时登录一个帐号。但是一台 Android 手机和一台苹果手机会被认为是两端，可以同时登录。多端登录相关配置请参考 [登录设置](https://cloud.tencent.com/document/product/269/38656#.E7.99.BB.E5.BD.95.E8.AE.BE.E7.BD.AE)。

### 登出

登出操作相对简单，使用 Logout 函数即可。

```c#
public static void Logout() {
        TIMResult res = TencentIMSDK.Logout((int code, string desc, string json_param, string user_data)=>{
        
        });
}
```



### 其他

调用 IM SDK Login 成功登录后，将会开始计算 DAU，请根据业务场景合理使用 IM SDK Login 操作，避免出现 DAU 过高的情况。
