## 1. 概述 

### 1.1 推送原理

如想要接收APNs离线消息通知，需要在腾讯云管理平台提交Push证书，在客户端每次登录时，获取并通过API接口上报Token。详细推送原理可参阅：[Apple Push Notification Service](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)。

APNs推送功能只用于通知用户，如果APP在前台，以 onNewMessage 回调获取新消息为准，didReceiveRemoteNotification 获取到的消息由于不可控，可以忽略。

### 1.2 证书申请流程

APNs 证书申请流程可参考文档：[Apple推送证书申请](/doc/product/269/Apple推送证书申请)。

### 1.3 上传证书到控制台

APNs 证书申请完成以后，需要把生成的p12证书上传到控制台，上传后会生成证书id，需要setToken调用时设置。APP开发周期中，证书申请流程如下图：

<img src="https://mc.qcloudimg.com/static/img/7ff07f369fa14f0669631c3e0a0f97c1/imsdk_ios_apns_busiId_big.jpg" width=480 />

另外上传时有几个注意点：

1. 上传证书名最好使用全英文（尤其不能使用括号等特殊字符）
2. 上传证书生效时间为10分钟左右
3. 上传证书需要设置密码，无密码收不到推送
4. 注意生产环境的选择，需要跟证书是否正式的发布证书对应，否则无法收到推送

### 1.4 客户端进行APNs推送

客户端按照如下4个步骤使用APNs推送：

1. 注册离线推送服务（registerForRemoteNotifications）
2. 上传设备Token（[[TIMManager sharedInstance] setToken:]）
3. 设备切后台时上报事件（[[TIMManager sharedInstance] doBackground:succ:fail:]）
4. 设备回到前台时上报事件（[[TIMManager sharedInstance] doForeground]）

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

## 3. 事件上报 

### 3.1 Token 上报

在APP完成初始化时，可通过系统函数 registerForRemoteNotifications（ios 8.0及以上） 或 registerForRemoteNotificationTypes（ios 8.0 以下） 告知系统需要APNs离线推送，随后会在 didRegisterForRemoteNotificationsWithDeviceToken 回调中得到系统的Token，进行上报。另外需要注意，应当在每次登录时都进行上报，API接口调用可在登陆前或登录后设置。
 
**上报函数原型：**

```
/**
 *  SetToken 参数
 */
@interface TIMTokenParam : NSObject
/**
 *  获取的客户端Token信息
 */
@property(nonatomic,retain) NSData* token;
/**
 *  业务ID，传递证书时分配
 */
@property(nonatomic,assign) uint32_t busiId;
@end

// setToken 原型
@interface TIMManager : NSObject
-(int) setToken: (TIMTokenParam *)token;
@end
```
**参数说明：**

参数 | 说明
---|---
token  | 为系统获取到的二进制Token 
busiId  |  网站分配的证书编号，多证书时用于区分不同证书 

**示例：**
 
在app获取Token的回调中上报Token，接口无需在登陆后进行调用，ImSDK会缓存到登录后上报： 

```
- (void)application:(UIApplication *)app didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    NSString *token = [NSString stringWithFormat:@"%@", deviceToken];
    TIMTokenParam * param = [[TIMTokenParam alloc] init];
    
    [param setToken:deviceToken];
    
    [[TIMManager sharedInstance] setToken:param];
}
```

### 3.2 后台/锁屏切换上报 

IM云后台进行APNs离线推送是从系统锁屏或者通过Home键把APP切换到后台开始，需要APP在锁屏事件和切后台事件发生时进行上报，另外为了APNs下发未读计数的准确性，需要切后台同时上报当前消息的未读计数，注意：这里上报未读计数仅是修改服务器未读，客户端桌面未读需要用户调用系统API进行重置：
 
**原型：**

```
@interface TIMManager : NSObject

/**
 *  app 切后台时调用
 *
 *  @param param 上报参数
 *  @param succ  成功时回调
 *  @param fail  失败时回调
 *
 *  @return 0 表示成功
 */
-(int) doBackground: (TIMBackgroundParam*)param succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
param|设置参数，可以设置当前未读计数
succ|成功回调
fail|失败回调

**示例：**

```
TIMBackgroundParam * param = [[TIMBackgroundParam alloc] init];
[param setC2cUnread:0];

[[TIMManager sharedInstance] doBackground:param succ:^() {
	NSLog(@"Succ");
} fail:^(int code, NSString * err) {
	NSLog(@"Fail: %d->%@", code, err);
}];
```

### 3.3 前台切换上报

当用户切换到前台，APP收到通知时，应该上报前台切换消息，以终止APNs的推送，这里建议切到前台时对客户端桌面未读计数清零处理，需要用户调用系统API进行重置：
 
**原型：**

```
-(int) doForeground;
```

**示例： **

```
[[TIMManager sharedInstance] doForeground];
```

## 4. 多APP支持

对于需要多APP互通的场景，可在多个APP中写同一个sdkappid，可实现消息互通，由于多个APP推送证书不同，所以需要在控制台上提交多个证书，每个证书在IM通讯云上生成一个编号，可参考 [3.1 Token 上报](/doc/product/269/离线推送（iOS%20SDK）#3.1-token-.E4.B8.8A.E6.8A.A5) 设置证书，并提供当前证书的编号。


## 5. 推送声音

### 5.1 设置自己的推送声音

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

### 5.2 获取自己的推送声音

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

### 5.3 每条离线推送属性

如果需要定制每条消息的展示文本、扩展字段、提示音、是否推送属性，可以在消息设置TIMOfflinePushInfo，此条消息在推送时，会替换用户原有的默认属性。可实现每条消息定制化推送。

```
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

