[](id:配置推送)
## 配置离线推送
如想要接收 APNs 离线消息通知，需要在腾讯云管理平台提交 Push 证书，在客户端每次登录时，获取并通过 API 接口上报 Token。APNs 推送功能只用于通知用户，如果 App 在前台，以 `onNewMessage` 回调获取新消息为准，`didReceiveRemoteNotification` 获取到的消息可以忽略。详细推送原理请参见 [Apple Push Notification Service](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)。

### 申请 APNs 证书
申请 APNs 证书的具体操作步骤请参见 [Apple 推送证书申请](https://cloud.tencent.com/document/product/269/3898)。

### 上传证书到控制台
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
2. 单击目标应用卡片，进入应用的基础配置页面。
3. 单击【iOS平台推送设置】右侧的【添加证书】。
4. 选择证书类型，上传 iOS 证书（p.12），设置证书密码，单击【确认】。
>!
>- 上传证书名最好使用全英文（尤其不能使用括号等特殊字符）。
>- 上传证书需要设置密码，无密码收不到推送。
>- 发布 App Store 的证书需要设置为生产环境，否则无法收到推送。
>- 上传的 p12 证书必须是自己申请的真实有效的证书。
>
5. 待推送证书信息生成后，记录证书的 ID。

### 客户端实现 APNs 推送

客户端要实现接收 APNs 推送，需要实现以下几个步骤，更详细的操作步骤可参考 [即时通信 iOS IM SDK 离线推送视频](https://cloud.tencent.com/edu/learning/learn-1059-1112)。

#### 向苹果后台请求 DeviceToken

```
- (void)registNotification
{
    if ([[[UIDevice currentDevice] systemVersion] floatValue] >= 8.0)
    {
        [[UIApplication sharedApplication] registerUserNotificationSettings:[UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeSound | UIUserNotificationTypeAlert | UIUserNotificationTypeBadge) categories:nil]];
        [[UIApplication sharedApplication] registerForRemoteNotifications];
    }
    else
    {
        [[UIApplication sharedApplication] registerForRemoteNotificationTypes: (UIUserNotificationTypeBadge | UIUserNotificationTypeSound | UIUserNotificationTypeAlert)];
    }
}
/**
 *  在 AppDelegate 的回调中会返回 deviceToken，需要在登录后上报给腾讯云后台
/**
-(void)application:(UIApplication *)app didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken
{
    //记录下 Apple 返回的 deviceToken
    _deviceToken = deviceToken;
}
```

#### 登录 IM SDK 后上传 Token 到腾讯云

>!busiID 需要与控制台分配的证书 ID 保持一致。

```
  __weak typeof(self) ws = self;
 //这里如果使用了 TUIKit，请在 TUKit 登录回调里面设置 Token，如果没有使用，请在 TIMManager 的 login 回调里面设置 Token。
 [[TUIKit sharedInstance] loginKit:identifier userSig:userSig succ:^{
    TIMTokenParam *param = [[TIMTokenParam alloc] init];
/* 用户自己到苹果注册开发者证书，在开发者帐号中下载并生成证书(p12 文件)，将生成的 p12 文件传到腾讯证书管理控制台，控制台会自动生成一个证书 ID，将证书 ID 传入一下 busiID 参数中。*/
#if kAppStoreVersion
// App Store 版本
#if DEBUG
    param.busiId = 2383;
#else
    param.busiId = 2382;
#endif
#else
    //企业证书 ID
    param.busiId = 2516;
#endif    
    [param setToken:ws.deviceToken];    
    [[TIMManager sharedInstance] setToken:param succ:^{       
        NSLog(@"-----> 上传 token 成功 ");
    } fail:^(int code, NSString *msg) {
        NSLog(@"-----> 上传 token 失败 ");
    }];
 } fail:^(int code, NSString *msg) {
        NSLog(@"登录失败！");
    }];
  }
```

#### App 进入后台时上报切后台事件

```
- (void)applicationDidEnterBackground:(UIApplication *)application
{
    __block UIBackgroundTaskIdentifier bgTaskID;
    bgTaskID = [application beginBackgroundTaskWithExpirationHandler:^ {
        //不管有没有完成，结束 background_task 任务
        [application endBackgroundTask: bgTaskID];
        bgTaskID = UIBackgroundTaskInvalid;
    }];
     //获取未读计数
    int unReadCount = 0;
    NSArray *convs = [[TIMManager sharedInstance] getConversationList];
    for (TIMConversation *conv in convs) {
        if([conv getType] == TIM_SYSTEM){
            continue;
        }
        unReadCount += [conv getUnReadMessageNum];
    }
    [UIApplication sharedApplication].applicationIconBadgeNumber = unReadCount;
    
    //doBackground
    TIMBackgroundParam  *param = [[TIMBackgroundParam alloc] init];
    [param setC2cUnread:unReadCount];
    [[TIMManager sharedInstance] doBackground:param succ:^() {
        NSLog(@"doBackgroud Succ");
    } fail:^(int code, NSString * err) {
        NSLog(@"Fail: %d->%@", code, err);
    }];
}
```

#### App 进入前台时上报切前台事件

```
- (void)applicationDidBecomeActive:(UIApplication *)application {
    [[TIMManager sharedInstance] doForeground:^() {
        NSLog(@"doForegroud Succ");
    } fail:^(int code, NSString * err) {
        NSLog(@"Fail: %d->%@", code, err);
    }];
}
```

## 推送格式 
推送格式示例如下图所示。
<img src="//main.qcloudimg.com/raw/d23be65b4c481beb71db993045b4fec9.png" width=480 />


### 通用推送规则
对于单聊消息，APNs 推送规则如下，其中昵称是发送方用户昵称，如果未设置昵称，则只显示内容。

```
昵称:内容
```

对于群聊消息，APNs 推送规则如下，其中名称为群名片或者发送者昵称，优先级为`群名片`>`群名`。

```
名称(群名):内容
```

### 不同类型消息推送规则
APNs 推送内容部分由消息体中各个 `Elem` 内容组成，不同 `Elem` 的离线消息展示效果如下表所示。

| 参数 | 说明 |
| --- | --- |
| 文本 Elem | 直接显示内容 |
| 语音 Elem | 显示`[语音]` |
| 文件 Elem | 显示`[文件]` |
| 图片 Elem | 显示`[图片]` |
| 自定义 Elem | 显示 `desc` 字段内容，若自定义消息 `desc` 为空，则该消息不进行离线推送 |


### 多 App 互通

如果将多个 App 中的 `SDKAppID` 设置为相同值，则可以实现多 App 互通。不同 App 需要使用不同的推送证书，您需要为每一个 App [申请 APNs 证书](https://cloud.tencent.com/document/product/269/3898) 并完成 [离线推送配置](#配置推送)。


## 推送提示音
### 设置自定义推送提示音

IM SDK 提供了设置用户声音的接口，可按需自定义设置单聊消息提示音和群组消息提示音，也可在用户级别设置是否接收推送。

```
/**
 *  APNs 配置
 */
@interface TIMAPNSConfig : NSObject
/**
 *  是否开启推送：0-不进行设置 1-开启推送 2-关闭推送
 */
@property(nonatomic,assign) uint32_t openPush;
/**
 *  C2C 消息声音,不设置传入 nil
 */
@property(nonatomic,retain) NSString * c2cSound;
/**
 *  Group 消息声音,不设置传入 nil
 */
@property(nonatomic,retain) NSString * groupSound;
@end
@interface TIMManager : NSObject
/**
 *  设置 APNS 配置
 *
 *  @param config APNS 配置
 *  @param succ   成功回调
 *  @param fail   失败回调
 *
 *  @return 0 成功
 */
-(int) setAPNS:(TIMAPNSConfig*)config succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明**

| 参数 | 说明 |
| --- | --- |
| config | openPush：是否开启推送。0表示不进行设置，1表示开启推送，2表示关闭推送<br>c2cSound：表示单聊消息提示音，需设置为文件名（含后缀）<br>groupSound：表示群组消息提示音，需设置为文件名（含后缀）|
| succ | 成功回调 |
| fail | 失败回调 |

**操作步骤**
1. 把音频文件集成到工程中。
 <img src="//main.qcloudimg.com/raw/c0aca90f7de2f67d815ddfcf13f9fcfc.png" width=480 />
2. 登录成功后调用 `setToken` 接口设置 token 和 busiID 信息。
3. 调用 `setAPNS` 接口设置音频文件信息。
 >?只需要设置音频文件的**文件名称（含后缀）**即可。
 >
<img src="//main.qcloudimg.com/raw/76005ecd34b9cabf23536d77828f2de7.png" width=480 />

### 获取推送消息提示音

如需获取推送消息提示音，可使用 `getAPNSConfig` 获取，此接口每次都从服务器同步数据，不会进行本地缓存。

```
@interface TIMManager : NSObject
/**
 *  获取 APNS 配置
 *
 *  @param succ 成功回调，返回配置信息
 *  @param fail 失败回调
 *
 *  @return 0 成功
 */
-(int) getAPNSConfig:(TIMAPNSConfigSucc)succ fail:(TIMFail)fail;
@end
```

参数说明如下表所示：

| 参数 | 说明 |
| --- | --- |
| succ | 成功回调，返回 TIMAPNSConfig 结构体 |
| fail | 失败回调 |

## 自定义离线消息属性

如果需要定制每条消息的展示文本、扩展字段、提示音、是否推送属性，可以在消息设置 `TIMOfflinePushInfo`，此条消息在推送时，会替换用户原有的默认属性，实现每条消息定制化推送。例如，填入 `kIOSOfflinePushNoSound` 到 `sound` 属性时接收端强制为静音提示。

```
/**
 填入 sound 字段表示接收时不会播放声音
 */
extern NSString * const kIOSOfflinePushNoSound;
@interface TIMAndroidOfflinePushConfig : NSObject
/**
 *  离线推送时展示标签
 */
@property(nonatomic,retain) NSString * title;
/**
 *  Android 离线 Push 时声音字段信息
 */
@property(nonatomic,retain) NSString * sound;
/**
 *  离线推送时通知形式
 */
@property(nonatomic,assign) TIMAndroidOfflinePushNotifyMode notifyMode;
@end
@interface TIMIOSOfflinePushConfig : NSObject
/**
 *  离线 Push 时声音字段信息
 */
@property(nonatomic,retain) NSString * sound;
/**
 *  忽略 badge 计数
 */
@property(nonatomic,assign) BOOL ignoreBadge;
@end
@interface TIMOfflinePushInfo : NSObject
/**
 *  自定义消息描述信息，做离线 Push 时文本展示
 */
@property(nonatomic,retain) NSString * desc;
/**
 *  离线 Push 时扩展字段信息
 */
@property(nonatomic,retain) NSString * ext;
/**
 *  推送规则标志
 */
@property(nonatomic,assign) TIMOfflinePushFlag pushFlag;
/**
 *  iOS 离线推送配置
 */
@property(nonatomic,retain) TIMIOSOfflinePushConfig * iosConfig;
/**
 *  Android 离线推送配置
 */
@property(nonatomic,retain) TIMAndroidOfflinePushConfig * androidConfig;
@end
```


