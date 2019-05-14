## 通讯管理器初始化

ImSDK 一切操作都是由通讯管理器 `TIMManager` 开始，SDK 操作第一步需要获取 `TIMManager` 单例。

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

## 新消息通知

在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调 `TIMMessageListener`，在用户登录状态下，会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。回调消息内容通过参数 `TIMMessage` 传递，通过 `TIMMessage` 可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等等，可参阅 [消息解析](/doc/product/269/1569#.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90)。

**原型：**
```
@protocol TIMMessageListener
@optional
/**
 *  新消息通知
 *
 *  @param msgs 新消息列表，TIMMessage 类型数组
 */
- (void)onNewMessage:(NSArray*) msgs;
@end
@interface TIMManager : NSObject
-(int) setMessageListener: (id)listener;
@end
```

以下示例中设置消息回调通知，并且在有新消息时直接打印消息。**示例：**

```
@interface TIMMessageListenerImpl : NSObject
- (void)onNewMessage:(TIMMessage*) msg;
@end
@implementation TIMMessageListenerImpl
@synthesize onMessage;
- (void)onNewMessage:(NSArray*) msgs {
    NSLog(@"NewMessages: %@", msgs);
}
@end 
TIMMessageListenerImpl * impl = [[TIMMessageListenerImpl alloc] init];
[[TIMManager sharedInstance] setMessageListener:impl];
```

## 网络事件通知

可选设置，如果要用户感知是否已经连接服务器，需要设置此回调，用于通知调用者跟通讯后台链接的连接和断开事件。另外，如果断开网络，等网络恢复后会自动重连，自动拉取消息通知用户，用户无需关心网络状态，仅作通知之用。

> **注意：**
> 这里的网络事件不表示用户本地网络状态，仅指明 SDK 是否与 IM 云 Server 连接状态。只要用户处于登录状态，**ImSDK 内部会进行断网重连，用户无需关心。**

**原型：**

```
/**
 *  连接通知回调
 */
@protocol TIMConnListener@optional
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
 *  网络连接断开
 *
 *  @param code 错误码
 *  @param err  错误描述
 */
- (void)onDisconnect:(int)code err:(NSString*)err;
@end 
@interface TIMManager : NSObject 
-(int) setConnListener: (id)listener; 
@end
```

以下示例监听网络事件，并输出日志。**示例：**

```
@interface TIMConnListenerImpl : NSObject{
}
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
[[TIMManager sharedInstance] setConnListener:connListenerImpl];
[[TIMManager sharedInstance] initSdk];
```

## 日志事件

SDK 内部会进行打印日志，如果调用方有自己统一的日志收集方式，可以设置日志回调事件，SDK 会把日志通过回调返给调用方，但 ImSDK 仍然内部仍然会打印，如果需要禁掉，可以通过设置控制台不打印日志，或者设置日志级别。回调通过两种形式，一种**使用闭包进行回调**，另一种**使用 `protocol` 接口回调**。

**原型：**

```
@interface TIMManager : NSObject
/**
 *  设置日志函数
 *
 *  @param cb 日志函数，SDK 打印日志会通过此函数返给调用方，内部不进行打印
 */
-(void) setLogFunc:(TIMLogFunc)cb;
/**
 *  设置日志监听
 *
 *  @param cb 日志监听，SDK 打印日志会通过此接口返给调用方，内部不进行打印
 */
-(void) setLogListener:(id)cb;
@end
```
 
示例中通过闭包回调打印日志到控制台。**示例：**

```
[[TIMManager sharedInstance] setLogFunc:^(NSString* content) {
    NSLog(@"%@", content);
}];
```

## 用户状态变更

用户状态变更的时候，SDK 会有相应的通知。通过 `TIMManager` 中的 `setUserStatusListener` 方法可以设置用户状态变更通知监听器来对相应的通知进行监听。目前用户状态变更有两种通知，具体可参见 [用户被踢下线通知](#.E7.94.A8.E6.88.B7.E8.A2.AB.E8.B8.A2.E4.B8.8B.E7.BA.BF.E9.80.9A.E7.9F.A5) 和 [用户票据过期通知](#.E7.94.A8.E6.88.B7.E7.A5.A8.E6.8D.AE.E8.BF.87.E6.9C.9F.E9.80.9A.E7.9F.A5)。这种情况下需要重新登录帐号后才能正常使用消息、群组和好友功能。

**原型：**

```
/**
 *  用户在线状态通知
 */
@protocol TIMUserStatusListener@optional
/**
 *  踢下线通知
 */
- (void)onForceOffline;
 /**
 *  用户登录的 userSig 过期（用户需要重新获取 userSig 后登录）
 */
- (void)onUserSigExpired;
@end
@interface TIMManager : NSObject
/**
 *  设置用户状态通知回调
 *
 *  @param listener 回调
 *
 *  @return 0 成功
 */
-(int) setUserStatusListener: (id)listener; 
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
[[TIMManager sharedInstance] setUserStatusListener : impl];
```

### 用户被踢下线通知

用户如果在其他终端登录，会被踢下线，这时会收到用户被踢下线的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onForceOffline` 中进行相应的处理，出现这种情况常规的做法是提示用户进行操作（退出，或者再次把对方踢下线）。


> **注意：**
> 用户如果在离线状态下被踢，下次登录将会失败，可以给用户一个非常强的提醒（登录错误码 `ERR_IMSDK_KICKED_BY_OTHERS：6208`），开发者也可以选择忽略这次错误，再次登录即可。

**用户在线情况下的互踢：**如下图所示，用户在设备 1 登录，保持在线状态下，该用户又在设备 2 登录，这时用户会在设备 1 上强制下线，收到 `onForceOffline` 回调。用户在设备 1 上收到回调后，提示用户，可继续调用 `login` 上线，强制设备 2 下线。

![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021645_19906.png)

**用户离线状态互踢：**如下图所示，用户在设备 1 登录，没有进行 `logout` 情况下进程退出（此时可接收 iOS 远程推送消息）。该用户在设备 2 登录，此时由于用户不在线，无法感知此事件，为了显式提醒用户，避免无感知的互踢，用户在设备 1 重新登录时，会返回 `ERR_IMSDK_KICKED_BY_OTHERS：6208` 错误码，表明之前被踢，是否需要把对方踢下线。如果需要，则再次调用 `login` 强制上线，设备 2 的登录的实例将会收到 `onForceOffline` 回调。

![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021702_68733.png)

### 用户票据过期通知

在用户登录（参见 [登录](/doc/product/269/%E7%99%BB%E5%BD%95%EF%BC%88iOS%20SDK%EF%BC%89#1.-.E7.99.BB.E5.BD.95)）的时候，需要提供一个用户票据，而这个用户票据在生成的时候是有一个有效使用期限的。在正常使用过程中，如果超过了用户票据的使用期限时，SDK 与服务器的交互会因为票据验证失败而操作失败，这个时候 SDK 会给出用户票据过期的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onUserSigExpired` 中进行相应的处理，出现这种情况，如果仍需要继续与服务器进行交互，则需要更换票据后重新登录。

## Crash 上报

ImSDK 内部集成了 Bugly 系统（http://bugly.qq.com )，当应用 Crash 后，会自动上报到平台，用户可以根据 Bugly 文档指示上传符号表，显示 Crash 详细信息，如果用户有自己的上报组件，可调用 `disableCrashReport` 接口禁用上报。

**原型：**

```
@interface TIMManager : NSObject
/**
 *  禁用 Crash 上报，由用户自己上报，如果需要，必须在 initSdk 之前调用
 */
-(void) disableCrashReport;
@end
```

**示例：**

```
[[TIMManager sharedInstance] disableCrashReport];
```

## 设置日志级别

ImSDK 内部日志级别可通过 `setLogLevel` 进行修改，控制 ImSDK 的日志输出。可以通过设置日志级别为 `TIM_LOG_NONE` 来关闭 ImSDK 的日志输出，提升性能，建议在开发期间打开日志，方便排查问题。

**原型：**

```
/**
 * 设置日志级别，在 initSDK 之前调用
 *
 *  @param level 日志级别
 */
-(void) setLogLevel:(TIMLogLevel)level;
```

## 控制台不打印日志或修改日志路径

默认 ImSDK 日志会打印到控制台，如果调试期间干扰太多，可选择关闭控制台日志（此时文件日志仍然会打印，可设置日志级别禁用），另外也可以修改默认的存储路径，方便管理。如果不修改日志路径，仅修改级别，可使用 `getLogPath` 获取默认路径传入 `initLogSettings`。日志默认路径在 App 目录下：`Library/Caches/imsdk_YYYYMMDD.log`。

**原型：**

```
/**
 *  初始化日志设置，必须在 initSdk 之前调用，在 initSdk 之后设置无效
 *
 *  @param isEnableLogPrint 是否开启日志打印
 *  @param logPath  日志文件路径
 */
-(void) initLogSettings: (BOOL)isEnableLogPrint logPath:(NSString*) logPath;
/**
 * 获取日志文件路径
 */
-(NSString *) getLogPath;
/**
 * 是否开启 SDK 日志打印
 */
-(BOOL) getIsLogPrintEnabled;
```

## 禁用存储

默认情况 ImSDK 会进行消息的存储，如无需存储，可选择关闭存储来提升处理性能。

**原型:**

```
@interface TIMManager : NSObject
/**
 * 禁用存储，在不需要消息存储的场景可以禁用存储，提升效率
 */
-(void) disableStorage;
@end
```

**示例：**

```
[[TIMManager sharedInstance] disableStorage];
[[TIMManager sharedInstance] initSdk];
```

## 通讯管理器初始化

在使用 SDK 进一步操作之前，需要初始 SDK。

**原型:**

```
@interface TIMManager : NSObject
-(int) initSdk;
@end
```

**示例：**

```
[[TIMManager sharedInstance] initSdk];
```
