## 推送原理
如想要接收 APNs 离线消息通知，需要在腾讯云管理平台提交 Push 证书，在客户端每次登录时，获取并通过 API 接口上报 Token。APNs 推送功能只用于通知用户，如果 App 在前台，以 `onNewMessage` 回调获取新消息为准，`didReceiveRemoteNotification` 获取到的消息由于不可控，可以忽略。详细推送原理可参阅：[Apple Push Notification Service](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)。

### 证书申请流程
APNs 证书申请流程可参考文档：[Apple 推送证书申请](/doc/product/269/Apple推送证书申请)。

### 上传证书到控制台
完成 APNs 证书申请以后，您需要登录腾讯云即时通信 IM [控制台](https://console.cloud.tencent.com/avc) 上传 iOS 证书（p.12）。
在【应用列表】页面，单击目标应用所在列的【应用配置】，进入【基础配置】页面。单击 iOS 推送证书区域的【+添加证书】，选择证书类型，上传 iOS 证书（p.12），设置证书密码，单击【确定】。

>!
>- 添加证书前，需确认应用平台已设置为【iOS】，若不是，可单击应用平台右侧的【编辑】进行修改。
>- 上传证书名最好使用全英文（尤其不能使用括号等特殊字符）。
>- 上传证书生效时间为10分钟左右。
>- 上传证书需要设置密码，无密码收不到推送。
>- 注意生产环境的选择，发布 App Store 的证书需要设置为生产环境，否则无法收到推送。
>- 上传的 p12 证书必须是自己申请的真实有效的证书。

![](https://main.qcloudimg.com/raw/e0d5f6d5f93d3d6c4412c2c9acf2d162.png)

### 客户端实现 APNs 推送

客户端要实现接收 APNs 推送，需要实现4个部分：**向苹果后台请求 DeviceToken**、**登录 IM SDK 后上传 Token 到腾讯云**、**App 进入后台时上报切后台事件**、**App 进入前台时上报切前台事件**。具体操作可参考视频：[即时通信 iOS IM SDK 离线推送集成](https://qcloud.com/course/detail/80)。

**向苹果后台请求 DeviceToken**：

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

**登录 IM SDK 后上传 Token 到腾讯云：**

> **注意：**
> busiId 需要和控制台分配的证书 ID 保持一致。

```
  __weak typeof(self) ws = self;
 //这里如果使用了 TUIKit，请在 TUKit 登录回调里面设置 Token，如果没有使用，请在 TIMManager 的 login 回调里面设置 Token。
 [[TUIKit sharedInstance] loginKit:identifier userSig:userSig succ:^{
    TIMTokenParam *param = [[TIMTokenParam alloc] init];
/* 用户自己到苹果注册开发者证书，在开发者帐号中下载并生成证书(p12 文件)，将生成的 p12 文件传到腾讯证书管理控制台，控制台会自动生成一个证书 ID，将证书 ID 传入一下 busiId 参数中。*/
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

**App 进入后台时上报切后台事件：**

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

**App 进入前台时上报切前台事件：**

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
**推送格式示例：**

<img src="//mccdn.qcloud.com/static/img/719853e769ad57dfaad2077e5815dd68/image.png" width=480 />

### 通用推送规则
对于单聊消息，APNs 推送规则如下，其中昵称是发送方用户昵称，如果未设置昵称，则只显示内容。

```
昵称:内容
```

对于群聊消息，APNs 推送规则如下，其中名称为群名片或者发送者昵称，优先级为『群名片』>『群名』。

```
名称(群名):内容
```

### 不同类型消息推送规则
APNs 推送内容部分为消息体中各个 `Elem` 内容组合。这里不用关心是否托管帐号还是独立帐号，只要设置了昵称或者群名推送消息就会带上。 

> 注：
>- 一条消息中包含文本 `Elem` 和图片 `Elem`，文本内容为 Test，最终显示的内容为：`Test[图片]`。
>- 另外一条消息中内容为空，则不进行下发，例如如果消息中只有自定义 `Elem`，并且 `desc` 为空，则不进行下发。


| 参数 | 说明 |
| --- | --- |
| 文本 Elem | 直接显示内容 |
| 语音 Elem | 显示 [语音] |
| 文件 Elem | 显示 [文件] |
| 图片 Elem | 显示 [图片] |
| 自定义 Elem | 显示 desc 字段内容 |

### 多 App 支持

对于需要多 App 互通的场景，可在多个 App 中写同一个 `SDKAppID`，可实现消息互通，由于多个 App 推送证书不同，所以需要在控制台上提交多个证书，每个证书在即时通信 IM 上生成一个编号，可参考 [客户端流程](https://cloud.tencent.com/document/product/269/9154#.E5.AE.A2.E6.88.B7.E7.AB.AF.E5.AE.9E.E7.8E.B0apns.E6.8E.A8.E9.80.81) 设置证书，并提供当前证书的编号。


## 推送声音
### 设置自己的推送声音

不同用户可能想使用不同的推送声音，IM SDK 提供了设置用户声音的接口，可实现单聊声音、群组声音、音视频（暂不支持）声音的设置，也可在用户级别设置是否接收推送。

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
/**
 *  Video 声音,不设置传入 nil
 */
@property(nonatomic,retain) NSString * videoSound;
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

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| config | openPush：是否开启推送（0：不进行设置 1：开启推送 2：关闭推送）<br>c2cSound：单聊声音，文件名<br>groupSound：群组声音，文件名<br>videoSound：音视频邀请声音，文件名
| succ | 成功回调 |
| fail | 失败回调 |

### 获取自己的推送声音

界面展示如果需要获取推送声音，可使用 `getAPNSConfig` 获取，此接口每次都从服务器同步数据，不会进行本地缓存。

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

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| succ | 成功回调，返回 TIMAPNSConfig 结构体 |
| fail | 失败回调 |

## 每条离线推送属性

如果需要定制每条消息的展示文本、扩展字段、提示音、是否推送属性，可以在消息设置 `TIMOfflinePushInfo`，此条消息在推送时，会替换用户原有的默认属性。可实现每条消息定制化推送。填入 `kIOSOfflinePushNoSound` 到 `sound` 属性时接收端强制为静音提示。

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
