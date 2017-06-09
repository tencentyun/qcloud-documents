## 1. 概述 

### 1.1 推送原理

如想要接收APNs离线消息通知，需要在腾讯云管理平台提交Push证书，在客户端每次登录时，获取并通过API接口上报Token。详细推送原理可参阅：[Apple Push Notification Service](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)。

APNs推送功能只用于通知用户，如果APP在前台，以 onNewMessage 回调获取新消息为准，didReceiveRemoteNotification 获取到的消息由于不可控，可以忽略。

### 1.2 证书申请流程

APNs 证书申请流程可参考文档：[Apple推送证书申请](/doc/product/269/Apple推送证书申请)。

### 1.3 上传证书到控制台

完成APNs 证书申请以后，需要把生成的p12证书上传到控制台：

<img src="http://mc.qcloudimg.com/static/img/d34bd0d7d3fe35a9171d396230df0fc6/image.png" width=480 />

上传时有几个注意点：

1. 上传证书名最好使用全英文（尤其不能使用括号等特殊字符）
2. 上传证书生效时间为10分钟左右
3. 上传证书需要设置密码，无密码收不到推送
4. 注意生产环境的选择，发布AppStore的证书需要设置为生产环境，否则无法收到推送
5. 上传的p12证书必须是自己申请的真实有效的证书

### 1.4 客户端实现APNs推送

客户端要实现接收APNs推送，需要实现4个部分：***向苹果后台请求DeviceToken***、***登录SDK后上传Token到腾讯云***、***APP进入后台时上报切后台事件***、***APP进入前台时上报切前台事件***。

向苹果后台请求DeviceToken请参考如下代码：

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
 *  在AppDelegate的回调中会返回DeviceToken，需要在登录后上报给腾讯云后台
/**
-(void)application:(UIApplication *)app didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken
{
    [[IMAPlatform sharedInstance] configOnAppRegistAPNSWithDeviceToken:deviceToken];
}

```

上传Token到腾讯云请参考如下代码，填写参数时***busiId需要和控制台分配的证书ID保持一致***：

```

- (void)configOnAppRegistAPNSWithDeviceToken:(NSData *)deviceToken
{
    DebugLog(@"didRegisterForRemoteNotificationsWithDeviceToken:%ld", (unsigned long)deviceToken.length);
    NSString *token = [NSString stringWithFormat:@"%@", deviceToken];
    [[TIMManager sharedInstance] log:TIM_LOG_INFO tag:@"SetToken" msg:[NSString stringWithFormat:@"My Token is :%@", token]];
    TIMTokenParam *param = [[TIMTokenParam alloc] init];

/* 用户自己到苹果注册开发者证书，在开发者账号中下载并生成证书(p12文件)，将生成的p12文件传到腾讯证书管理控制台，控制台会自动生成一个证书id，将证书id传入一下busiId参数中。*/
#if kAppStoreVersion

// AppStore版本
#if DEBUG
    param.busiId = 2383;
#else
    param.busiId = 2382;
#endif
    
#else
    //企业证书id
    param.busiId = 2516;
#endif
    
    [param setToken:deviceToken];
    
//    [[TIMManager sharedInstance] setToken:param];
    [[TIMManager sharedInstance] setToken:param succ:^{
       
        NSLog(@"-----> 上传token成功 ");
    } fail:^(int code, NSString *msg) {
        NSLog(@"-----> 上传token失败 ");
    }];
}

```

上报切后台事件请参考如下代码：

```

- (void)applicationDidEnterBackground:(UIApplication *)application
{
    __block UIBackgroundTaskIdentifier bgTaskID;
    bgTaskID = [application beginBackgroundTaskWithExpirationHandler:^ {
        
        //不管有没有完成，结束background_task任务
        [application endBackgroundTask: bgTaskID];
        bgTaskID = UIBackgroundTaskInvalid;
    }];
    
    [[IMAPlatform sharedInstance] configOnAppEnterBackground];
}

- (void)configOnAppEnterBackground
{
    NSUInteger unReadCount = [[IMAPlatform sharedInstance].conversationMgr unReadMessageCount];
    [UIApplication sharedApplication].applicationIconBadgeNumber = unReadCount;
    
    TIMBackgroundParam  *param = [[TIMBackgroundParam alloc] init];
    [param setC2cUnread:(int)unReadCount];
    
    [[TIMManager sharedInstance] doBackground:param succ:^() {
        DebugLog(@"doBackgroud Succ");
    } fail:^(int code, NSString * err) {
        DebugLog(@"Fail: %d->%@", code, err);
    }];
}

```

上报切前台事件请参考如下代码：

```

- (void)applicationDidBecomeActive:(UIApplication *)application
{
   [[TIMManager sharedInstance] doForeground:^() {
	       DebugLog(@"doForegroud Succ");
	 } fail:^(int code, NSString * err) {
	       DebugLog(@"Fail: %d->%@", code, err);
	 }];
}

```

具体操作请参考视频：[云通信IM-iOS ImSDK离线推送](https://qcloud.com/course/detail/80)。

## 2. 推送格式 

<img src="//mccdn.qcloud.com/static/img/719853e769ad57dfaad2077e5815dd68/image.png" width=480 />

### 2.1 通用推送规则

对于单聊消息，APNs推送规则为：

```
昵称:内容
```

其中昵称是发送方用户昵称，如果未设置昵称，则只显示内容。

对于群聊消息，APNs 推送规则为：

```
名称(群名):内容
```

其中名称为群名片或者发送者昵称，优先级为 群名片 > 群名。

### 2.2 不同类型消息推送规则

APNs 推送内容部分为消息体中各个Elem内容组合：

- 文本Elem：直接显示内容
- 语音Elem：显示 [语音]
- 文件Elem：显示 [文件]
- 图片Elem：显示 [图片]
- 自定义Elem：显示desc字段内容

例如：
一条消息中包含 文本Elem和图片Elem，文本内容为Test，最终显示的内容为： Test[图片]
另外一条消息中内容为空，则不进行下发，例如如果消息中只有自定义Elem，并且desc为空，则不进行下发；

这里不用关心是否托管账号还是独立账号，只要设置了昵称或者群名推送消息就会带上。 

## 3. 多APP支持

对于需要多APP互通的场景，可在多个APP中写同一个sdkappid，可实现消息互通，由于多个APP推送证书不同，所以需要在控制台上提交多个证书，每个证书在IM通讯云上生成一个编号，可参考 [3.1 Token 上报](/doc/product/269/离线推送（iOS%20SDK）#3.1-token-.E4.B8.8A.E6.8A.A5) 设置证书，并提供当前证书的编号。


## 4. 推送声音

### 4.1 设置自己的推送声音

不同用户可能想使用不通的推送声音，sdk提供了设置用户声音的接口，可实现单聊声音、群组声音、音视频（暂不支持）声音的设置，也可在用户级别设置是否接收推送。

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
 *  C2C消息声音,不设置传入nil
 */
@property(nonatomic,retain) NSString * c2cSound;

/**
 *  Group消息声音,不设置传入nil
 */
@property(nonatomic,retain) NSString * groupSound;

/**
 *  Video声音,不设置传入nil
 */
@property(nonatomic,retain) NSString * videoSound;

@end

@interface TIMManager : NSObject

/**
 *  设置APNS配置
 *
 *  @param config APNS配置
 *  @param succ   成功回调
 *  @param fail   失败回调
 *
 *  @return 0 成功
 */
-(int) setAPNS:(TIMAPNSConfig*)config succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```


**参数说明：**

参数 | 说明
---|---
config|设置配置
| openPush ： 是否开启推送 0-不进行设置 1-开启推送 2-关闭推送
| c2cSound ： 单聊声音，文件名
| groupSound ： 群组声音，文件名
| videoSound ： 音视频邀请声音，文件名
succ|成功回调
fail|失败回调

### 4.2 获取自己的推送声音

界面展示如果需要获取推送声音，可使用 getAPNSConfig 获取，此接口每次都从服务器同步数据，不会进行本地缓存。

```
@interface TIMManager : NSObject

/**
 *  获取APNS配置
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

参数 | 说明
---|---
succ|成功回调，返回 TIMAPNSConfig 结构体
fail|失败回调

### 4.3 每条离线推送属性

如果需要定制每条消息的展示文本、扩展字段、提示音、是否推送属性，可以在消息设置TIMOfflinePushInfo，此条消息在推送时，会替换用户原有的默认属性。可实现每条消息定制化推送。**填入kIOSOfflinePushNoSound到sound属性时接收端强制为静音提示**

```
/**
 填入sound字段表示接收时不会播放声音
 */
extern NSString * const kIOSOfflinePushNoSound;

@interface TIMAndroidOfflinePushConfig : NSObject
/**
 *  离线推送时展示标签
 */
@property(nonatomic,retain) NSString * title;
/**
 *  Android离线Push时声音字段信息
 */
@property(nonatomic,retain) NSString * sound;
/**
 *  离线推送时通知形式
 */
@property(nonatomic,assign) TIMAndroidOfflinePushNotifyMode notifyMode;

@end

@interface TIMIOSOfflinePushConfig : NSObject
/**
 *  离线Push时声音字段信息
 */
@property(nonatomic,retain) NSString * sound;
/**
 *  忽略badge计数
 */
@property(nonatomic,assign) BOOL ignoreBadge;
@end

@interface TIMOfflinePushInfo : NSObject
/**
 *  自定义消息描述信息，做离线Push时文本展示
 */
@property(nonatomic,retain) NSString * desc;
/**
 *  离线Push时扩展字段信息
 */
@property(nonatomic,retain) NSString * ext;
/**
 *  推送规则标志
 */
@property(nonatomic,assign) TIMOfflinePushFlag pushFlag;
/**
 *  iOS离线推送配置
 */
@property(nonatomic,retain) TIMIOSOfflinePushConfig * iosConfig;
/**
 *  Android离线推送配置
 */
@property(nonatomic,retain) TIMAndroidOfflinePushConfig * androidConfig;
@end

```

