## 通讯管理器初始化
IM SDK 一切操作都是由通讯管理器 `TIMManager` 开始，SDK 操作第一步需要获取 `TIMManager` 单例。

**原型：**
```
@interface TIMManager : NSObject
/**
 *  获取管理器实例
 *
 *  @return 管理器实例
 */
+(TIMManager*)sharedInstance;
@end
```

**示例：**
```
TIMManager * manager = [TIMManager sharedInstance];
```
在使用 SDK 进一步操作之前，需要初始化 SDK。

**原型:**
```
@interface TIMManager : NSObject

/**
 *  初始化 SDK
 *
 *  @param config      配置信息，全局有效
 *
 *  @return 0 成功
 */
- (int)initSdk:(TIMSdkConfig*)globalConfig;

/**
 *  初始化当前 manager，在 initSdk:后调用，login:前调用
 *
 *  @param config    配置信息，对当前 TIMManager 有效
 *
 *  @return 0 成功
 */
- (int)setUserConfig:(TIMUserConfig*)config;
 
@end

//全局配置信息
@interface TIMSdkConfig : NSObject

//用户标识接入 SDK 的应用 ID，必填
@property(nonatomic,assign) int sdkAppId;

//禁止在控制台打印 log
@property(nonatomic,assign) BOOL disableLogPrint;

//本地写 log 文件的等级，默认 DEBUG 等级
@property(nonatomic,assign) TIMLogLevel logLevel;

//log 文件路径，不设置时为默认路径，可以通过 TIMManager -> getLogPath 获取 log 路径
@property(nonatomic,strong) NSString * logPath;

//回调给 logFunc 函数的 log 等级，默认 DEBUG 等级
@property(nonatomic,assign) TIMLogLevel logFuncLevel;

//log 监听函数
@property(nonatomic,copy) TIMLogFunc logFunc;

//消息数据库路径，不设置时为默认路径
@property(nonatomic,strong) NSString * dbPath;

//网络监听器，监听网络连接成功失败的状态
@property(nonatomic,strong) id<TIMConnListener> connListener;

@end

//用户配置信息
@interface TIMUserConfig : NSObject

//禁用本地存储
@property(nonatomic,assign) BOOL disableStorage;

//是否开启多终端同步未读提醒，这个选项主要影响多终端登录时的未读消息提醒逻辑。YES：只有当一个终端调用 setReadMessage() 将消息标记为已读，另一个终端再登录时才不会收到未读提醒；NO：消息一旦被一个终端接收，另一个终端都不会再次提醒。同理，卸载 App 再安装也无法再次收到这些未读消息。
@property(nonatomic,assign) BOOL disableAutoReport;

//是否开启被阅回执。YES：接收者查看消息（setReadMessage）后，消息的发送者会收到 TIMMessageReceiptListener 的回调提醒；NO: 不开启被阅回执，默认不开启。
@property(nonatomic,assign) BOOL enableReadReceipt;

//设置默认拉取的群组资料，如果想要拉取自定义字段，要通过即时通信 IM 控制台 > 功能配置 > 群维度自定义字段配置对应的 "自定义字段" 和用户操作权限，控制台配置之后5分钟后才会生效。
@property(nonatomic,strong) TIMGroupInfoOption * groupInfoOpt;

//设置默认拉取的群成员资料，如果想要拉取自定义字段，要通过即时通信 IM 控制台 > 功能配置 > 群成员维度自定义字段配置对应的 "自定义字段" 和用户操作权限，控制台配置之后5分钟后才会生效。
@property(nonatomic,strong) TIMGroupMemberInfoOption * groupMemberInfoOpt;

//关系链参数
@property(nonatomic,strong) TIMFriendProfileOption * friendProfileOpt;

//用户登录状态监听器,用于监听用户被踢，断网重连失败，UserSig 过期的通知
@property(nonatomic,weak) id<TIMUserStatusListener> userStatusListener;

//会话刷新监听器，用于监听会话的刷新
@property(nonatomic,weak) id<TIMRefreshListener> refreshListener;

//消息已读回执监听器，用于监听消息已读回执，enableReadReceipt 字段需要设置为 YES
@property(nonatomic,weak) id<TIMMessageReceiptListener> messageReceiptListener;

//消息修改监听器，用于监听消息状态的变化
@property(nonatomic,weak) id<TIMMessageUpdateListener> messageUpdateListener;

//消息撤回监听器，用于监听会话中的消息撤回通知
@property(nonatomic,weak) id<TIMMessageRevokeListener> messageRevokeListener;

//文件上传进度监听器，发送语音，图片，视频，文件消息的时候需要先上传对应文件到服务器，这里可以监听上传进度
@property(nonatomic,weak) id<TIMUploadProgressListener> uploadProgressListener;

//群组事件通知监听器
@property(nonatomic,weak) id<TIMGroupEventListener> groupEventListener;

//关系链数据本地缓存监听器
@property(nonatomic,weak) id<TIMFriendshipListener> friendshipListener;

@end
```

## 新消息通知
在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调 `TIMMessageListener`，在用户登录状态下，会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。

**原型：**

```
/**
 *  新消息接收回调
 */
@protocol TIMMessageListener <NSObject>
@optional
/**
 *  新消息回调通知
 *
 *  @param msgs 新消息列表，TIMMessage 类型数组
 */
- (void)onNewMessage:(NSArray*) msgs;
@end
 
@interface TIMManager : NSObject
 
/**
 *  添加消息回调（重复添加无效）
 *
 *  @param listener 回调
 *
 *  @return 成功
 */
- (int)addMessageListener:(id<TIMMessageListener>)listener;
 
@end
```

回调消息内容通过参数 `TIMMessage` 传递，通过 `TIMMessage` 可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等。以下示例中设置消息回调通知，并且在有新消息时直接打印消息。详细可参阅 [消息解析](https://cloud.tencent.com/doc/product/269/9150#.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90) 部分。

**示例：**

```
@interface TIMMessageListenerImpl : NSObject
- (void)onNewMessage:(TIMMessage*) msg;
@end
@implementation TIMMessageListenerImpl
- (void)onNewMessage:(NSArray*) msgs {
    NSLog(@"NewMessages: %@", msgs);
}
@end
TIMMessageListenerImpl * impl = [[TIMMessageListenerImpl alloc] init];
[[TIMManager sharedInstance] addMessageListener:impl];
```

## 网络事件通知
可选设置，如果要用户感知是否已经连接服务器，需要设置此回调，用于通知调用者跟通讯后台链接的连接和断开事件。另外，如果断开网络，等网络恢复后会自动重连，自动拉取消息通知用户，用户无需关心网络状态，仅作通知之用。

> **注意：**
> 这里的网络事件不表示用户本地网络状态，仅指明 SDK 是否与即时通信 IM 云 Server 连接状态。只要用户处于登录状态，**IM SDK 内部会进行断网重连，用户无需关心。**

**原型：**

```
/**
 *  连接通知回调
 */
@protocol TIMConnListener <NSObject>
@optional
/**
 *  网络连接成功
 */
- (void)onConnSucc;
/**
 *  网络连接失败
 *
 *  @param code 错误码
 *  @param err  错误描述
 */
- (void)onConnFailed:(int)code err:(NSString*)err;
/**
 *  网络连接断开（断线只是通知用户，不需要重新登录，重连以后会自动上线）
 *
 *  @param code 错误码
 *  @param err  错误描述
 */
- (void)onDisconnect:(int)code err:(NSString*)err;
/**
 *  连接中
 */
- (void)onConnecting;
@end
@interface TIMSdkConfig : NSObject
/**
 *  网络监听器
 */
@property(nonatomic,retain) id<TIMConnListener> connListener;
@end
```

以下示例监听网络事件，并输出日志。
**示例：**

```
@interface TIMConnListenerImpl : NSObject
- (void)onConnSucc;
- (void)onConnFailed:(int)code err:(NSString*)err;
- (void)onDisconnect:(int)code err:(NSString*)err;
@end
@implementation TIMConnListenerImpl
 
- (void)onConnSucc {
    NSLog(@"Connect Succ");
} 
- (void)onConnFailed:(int)code err:(NSString*)err {
  // code 错误码：具体参见错误码表
    NSLog(@"Connect Failed: code=%d, err=%@", code, err);
} 
- (void)onDisconnect:(int)code err:(NSString*)err {
  // code 错误码：具体参见错误码表
    NSLog(@"Disconnect: code=%d, err=%@", code, err);
} 
@end
TIMConnListenerImpl * connListenerImpl = [[TIMConnListenerImpl alloc] init];
TIMSdkConfig * cfg = [[TIMSdkConfig alloc] init];
cfg.connListener = connListenerImpl;
[[TIMManager sharedInstance] initSdk:cfg];
```

## 日志事件
IM SDK 内部会打印日志，如果调用方有自己统一的日志收集方式，可以设置日志回调事件，SDK 会通过回调将日志返给调用方。回调通过两种形式，一种**使用闭包进行回调**，另一种**使用 `protocol` 接口回调**。
设置回调后 IM SDK 内部仍然会打印日志，如果需要禁用内部打印，可以设置控制台不打印日志，或者设置日志级别。

**原型：**

```
@interface TIMSdkConfig : NSObject
/**
 *  log监听函数
 */
@property(nonatomic,copy) TIMLogFunc logFunc;
@end
```
 
以下示例中通过闭包回调打印日志到控制台。
**示例：**

```
TIMSdkConfig * cfg = [[TIMSdkConfig alloc] init];
cfg.logFunc = ^(NSString* content) {
		NSLog(@"%@", content);
}];
```

## 用户状态变更

用户状态变更的时候，SDK 会有相应的通知。通过设置 `TIMUserConfig` 中的 `userStatusListener` 属性可以设置用户状态变更通知监听器来对相应的通知进行监听。目前用户状态变更有三种通知，具体可参见 [用户被踢下线通知](#.E7.94.A8.E6.88.B7.E8.A2.AB.E8.B8.A2.E4.B8.8B.E7.BA.BF.E9.80.9A.E7.9F.A5) 和 [用户票据过期通知](#.E7.94.A8.E6.88.B7.E7.A5.A8.E6.8D.AE.E8.BF.87.E6.9C.9F.E9.80.9A.E7.9F.A5)。这种情况下需要重新登录帐号后才能正常使用消息、群组和好友功能。

**原型：**
```
/**
 *  用户在线状态通知
 */
@protocol TIMUserStatusListener <NSObject>
@optional
/**
 *  踢下线通知
 */
- (void)onForceOffline;
/**
 *  断线重连失败
 */
- (void)onReConnFailed:(int)code err:(NSString*)err;
/**
 *  用户登录的 userSig 过期（用户需要重新获取 userSig 后登录）
 */
- (void)onUserSigExpired;
@end
@interface TIMUserConfig : NSObject
/**
 *  用户登录状态监听器
 */
@property(nonatomic,retain) id<TIMUserStatusListener> userStatusListener;
@end
```
 
以下示例中当用户被踢下线时，收到回调后打印日志。**示例：**
 
```
@interface TIMUserStatusListenerImpl : NSObject{
}
- (void)onForceOffline;
- (void)onUserSigExpired;
@end
@implementation TIMUserStatusListenerImpl 
- (void)onForceOffline {
    NSLog(@"force offline");
}
- (void)onUserSigExpired {
    NSLog(@"userSig expired");
}
@end
TIMUserStatusListenerImpl * impl = [[TIMUserStatusListenerImpl alloc] init];
TIMUserConfig * cfg = [[TIMUserConfig alloc] init];
cfg.userStatusListener = impl;
```

### 用户被踢下线通知
用户如果在其他终端调用 login 登录，会被踢下线，这时会收到用户被踢下线的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onForceOffline` 中进行相应的处理，出现这种情况常规的做法是提示用户进行操作（退出，或者再次调用 login 把对方踢下线）。

> **注意：**
> 用户如果在离线状态下被踢，下次调用 login 登录将会失败，可以给用户一个非常强的提醒（登录错误码 `ERR_IMSDK_KICKED_BY_OTHERS：6208`），开发者也可以选择忽略这次错误，再次登录即可。

**用户在线情况下的互踢：**如下图所示，用户在设备 1 调用 login 登录，保持在线状态下，该用户又在设备 2 调用 login 登录，这时用户会在设备 1 上强制下线，收到 `onForceOffline` 回调。用户在设备 1 上收到回调后，提示用户，可继续调用 `login` 上线，强制设备 2 下线。

![](https://main.qcloudimg.com/raw/aed1b1ab63d16431d0ef34cc16023387.png)

**用户离线状态互踢：**如下图所示，用户在设备 1 调用 login 登录，没有进行 `logout` 情况下进程退出（此时可接收 iOS 远程推送消息）。该用户在设备 2 调用 login 登录，此时由于设备 1 用户不在线，无法感知此事件，为了显式提醒用户，避免无感知的互踢，用户在设备 1 重新调用 login 登录时，会返回 `ERR_IMSDK_KICKED_BY_OTHERS：6208` 错误码，表明之前被踢，是否需要把对方踢下线。如果需要，则再次调用 `login` 强制上线，设备 2 的登录的实例将会收到 `onForceOffline` 回调。

![](https://main.qcloudimg.com/raw/552d6b22b3528a1d76935a4551cfb372.png)

### 用户票据过期通知
在用户登录（参见 [登录](https://cloud.tencent.com/doc/product/269/9149#1.-.E7.99.BB.E5.BD.951)）的时候，需要提供一个用户票据，而这个用户票据在生成的时候是有一个有效使用期限的。在正常使用过程中，如果超过了用户票据的使用期限时，SDK 与服务器的交互会因为票据验证失败而操作失败，这个时候 SDK 会给出用户票据过期的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onUserSigExpired` 中进行相应的处理，出现这种情况，如果仍需要继续与服务器进行交互，则需要更换票据后重新登录。

## 设置日志级别
IM SDK 内部日志级别可通过配置 `TIMSdkConfig` 进行修改，控制 IM SDK 的日志输出。可以通过设置日志级别为 `TIM_LOG_NONE` 来关闭 IM SDK 的日志输出，提升性能，建议在开发期间打开日志，方便排查问题。

**原型：**

```
@interface TIMSdkConfig : NSObject
/**
 *  本地写 log 文件的等级，默认 DEBUG 等级
 */
@property(nonatomic,assign) TIMLogLevel logLevel;
@end
```

## 控制台不打印日志或修改日志路径
默认 IM SDK 日志会打印到控制台，如果调试期间干扰太多，可选择关闭控制台日志（此时文件日志仍然会打印，可设置日志级别禁用），另外也可以修改默认的存储路径，方便管理。如果不修改日志路径，仅修改级别，可使用 `getLogPath` 获取默认路径传入 `initLogSettings`。日志默认路径在 App 目录下：`Library/Caches/imsdk_YYYYMMDD.log`。

**原型：**

```
@interface TIMSdkConfig : NSObject
/**
 *  log 文件路径，不设置时为默认路径
 */
@property(nonatomic,retain) NSString * logPath;
/**
 *  禁止在控制台打印 log
 */
@property(nonatomic,assign) BOOL disableLogPrint;
@end
```


