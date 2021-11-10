## 说明

本文档中账号功能、标签功能及用户属性功能适用于 **SDK 1.2.9.0或更高版本**，**1.2.7.2**及之前版本请参见 [接口文档](https://cloud.tencent.com/document/product/548/36668)。

## 启动腾讯移动推送服务

以下为设备注册相关接口方法，若需了解调用时机及调用原理，可查看 [设备注册流程](https://cloud.tencent.com/document/product/548/36662#.E8.AE.BE.E5.A4.87.E6.B3.A8.E5.86.8C.E6.B5.81.E7.A8.8B)。

#### 接口说明

通过使用在腾讯移动推送官网注册的应用信息，启动腾讯移动推送服务。
（此接口为 SDK 1.2.7.2版本新增，1.2.7.1及之前版本请参考 SDK 包内 XGPush.h 文件`startXGWithAppID` 接口）。

```objective-c
/// @note TPNS SDK1.2.7.2+
- (void)startXGWithAccessID:(uint32_t)accessID accessKey:(nonnull NSString *)accessKey delegate:(nullable id<XGPushDelegate>)delegate；
```

#### 参数说明

- accessID：通过前台申请的 AccessID。
- accessKey：通过前台申请的 AccessKey。
- Delegate：回调对象。 

>! 接口所需参数必须要正确填写，否则腾讯移动推送服务将不能正确为应用推送消息。
>

#### 示例代码

```Objective-C
 [[XGPush defaultManager] startXGWithAccessID:<your AccessID> accessKey:<your AccessKey> delegate:self];
```

## 终止腾讯移动推送服务

以下为设备注册相关接口方法，若需了解调用时机及调用原理，可查看 [设备反注册流程](https://cloud.tencent.com/document/product/548/36662#.E8.AE.BE.E5.A4.87.E5.8F.8D.E6.B3.A8.E5.86.8C.E6.B5.81.E7.A8.8B)。

#### 接口说明

终止腾讯移动推送服务后，将无法通过腾讯移动推送服务向设备推送消息，如再次需要接收腾讯移动推送服务的消息推送，则必须再次调用 `startXGWithAccessID:accessKey:delegate:` 方法重启腾讯移动推送服务。

```objective-c
- (void)stopXGNotification;
```

#### 示例代码

```Objective-C
[[XGPush defaultManager] stopXGNotification];
```



## TPNS Token 及注册结果

### 查询 TPNS Token

#### 接口说明

查询当前应用从腾讯移动推送服务器生成的 Token 字符串。

```objective-c
@property (copy, nonatomic, nullable, readonly) NSString *xgTokenString;
```

#### 示例代码

```objective-c
NSString *token = [[XGPushTokenManager defaultTokenManager] xgTokenString];
```

### 注册结果回调

#### 接口说明

SDK 启动之后，通过此方法回调来返回注册结果及 Token。

```objective-c
- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken xgToken:(nullable NSString *)xgToken error:(nullable NSError *)error
```

#### 返回参数说明

- deviceToken：APNs 生成的 Device Token。
- xgToken：TPNS 生成的 Token，推送消息时需要使用此值。TPNS 维护此值与 APNs 的 Device Token 的映射关系。
- error：错误信息，若 error 为 nil，则注册推送服务成功。

### 注册失败回调

#### 接口说明

SDK 1.2.7.2 新增，当注册推送服务失败会走此回调。

```objective-c
/// @note TPNS SDK1.2.7.2+
- (void)xgPushDidFailToRegisterDeviceTokenWithError:(nullable NSError *)error
```

### 通知授权弹窗的回调

#### 接口说明

SDK 1.3.1.0 新增，通知弹窗授权的结果会走此回调。

```objective-c
- (void)xgPushDidRequestNotificationPermission:(bool)isEnable error:(nullable NSError *)error;

```

#### 返回参数说明

- isEnable：是否同意授权。
- error：错误信息，若 error 为 nil，则获取弹窗结果成功。

## 账号功能

以下为账号相关接口方法，若需了解调用时机及调用原理，可查看 [账号相关流程](https://cloud.tencent.com/document/product/548/36662#.E8.B4.A6.E5.8F.B7.E7.9B.B8.E5.85.B3.E6.B5.81.E7.A8.8B)。

### 添加账号

#### 接口说明

若原来没有该类型账号，则添加；若原来有，则覆盖。（TPNS SDK1.2.9.0+ 新增）

```Objective-C
- (void)upsertAccountsByDict:(nonnull NSDictionary<NSNumber *, NSString *> *)accountsDict;

```

>? 此接口应该在 xgPushDidRegisteredDeviceToken:error: 返回正确之后被调用。
>

#### 参数说明 

accountsDict：账号字典。

> ?
> - 账号类型和账号名称一起作为联合主键。
> - 需要使用字典类型，key 为账号类型，value 为账号，示例：@{@(accountType):@"account"}。
> - Objective-C的写法 : @{@(0):@"account0",@(1):@"account1"}；Swift的写法：[NSNumber(0):@"account0",NSNumber(1):@"account1"]。
> - 更多 accountType 请参照 SDK Demo 包内的 XGPushTokenAccountType 枚举或 [账号类型取值表](https://cloud.tencent.com/document/product/548/56434)。
> 

#### 示例代码

```Objective-C
XGPushTokenAccountType accountType = XGPushTokenAccountTypeUNKNOWN;
NSString *account = @"account";
[[XGPushTokenManager defaultTokenManager] upsertAccountsByDict:@{ @(accountType):account }];
```

### 添加手机号

#### 接口说明

添加或更新用户手机号，等于调用`upsertAccountsByDict:@{@(1002):@"具体手机号"}`。

```objective-c
/// @note TPNS SDK1.3.2.0+
- (void)upsertPhoneNumber:(nonnull NSString *)phoneNumber;
```

#### 参数说明

- phoneNumber：E.164标准，格式为+[国家或地区码][手机号],例如+8613711112222。SDK内部加密传输。

#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] upsertPhoneNumber:@"+8613712345678"];;

```

> ! 1.此接口应该在xgPushDidRegisteredDeviceToken:error:返回正确之后被调用
> 2.如需要删除手机号，调用`delAccountsByKeys:[[NSSet alloc] initWithObjects:@(1002), nil]`

### 删除账号

#### 接口说明

接口说明：删除指定账号类型下的所有账号。（TPNS SDK1.2.9.0+ 新增）

```Objective-C
- (void)delAccountsByKeys:(nonnull NSSet<NSNumber *> *)accountsKeys;

```

> ?此接口应该在 xgPushDidRegisteredDeviceToken:error: 返回正确之后被调用。

#### 参数说明 

- accountsKeys：账号类型组成的集合。

> ?
>
> - 使用集合且 key 是固定要求。
> - 更多 accountType 请参照 SDK 包内 XGPush.h 文件中的 XGPushTokenAccountType 枚举。

#### 示例代码

```Objective-C
XGPushTokenAccountType accountType = XGPushTokenAccountTypeUNKNOWN;

NSSet *accountsKeys = [[NSSet alloc] initWithObjects:@(accountType), nil];

[[XGPushTokenManager defaultTokenManager] delAccountsByKeys:accountsKeys];

```

### 清除账号

#### 接口说明

清除所有设置的账号。

```Objective-C
- (void)clearAccounts;

```

>? 此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。
>

#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] clearAccounts];

```

## 标签功能

以下为标签相关接口方法，若需了解调用时机及调用原理，可查看 [标签相关流程](https://cloud.tencent.com/document/product/548/36662#.E6.A0.87.E7.AD.BE.E7.9B.B8.E5.85.B3.E6.B5.81.E7.A8.8B)。

### 绑定/解绑标签

#### 接口说明

开发者可以针对不同的用户绑定标签，然后对该标签进行推送。

```Objective-C
- (void)appendTags:(nonnull NSArray<NSString *> *)tags
- (void)delTags:(nonnull NSArray<NSString *> *)tags

```

>?
> - 此接口为追加方式。
> - 此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。
> - 单个应用最多可以有10000个自定义 tag， 每个设备 Token 最多可绑定100个自定义 tag，如需提高该限制，请联系 [在线客服](https://cloud.tencent.com/act/event/Online_service)，每个自定义 tag 可绑定的设备 Token 数量无限制。
> 

#### 参数说明

tags：标签数组。

>? 标签操作 tags 为标签字符串数组（标签字符串不允许有空格或者是 tab 字符）。
>

#### 示例代码

```Objective-C
//绑定标签：
[[XGPushTokenManager defaultTokenManager] appendTags:@[ tagStr ]];

//解绑标签
[[XGPushTokenManager defaultTokenManager] delTags:@[ tagStr ]];

```



### 更新标签

#### 接口说明

清空已有标签，然后批量添加标签。

```Objective-C
- (void)clearAndAppendTags:(nonnull NSArray<NSString *> *)tags

```

>?
> - 此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。
> - 此接口会将当前 Token 对应的旧有的标签全部替换为当前的标签。
> 

#### 参数说明 

tags：标签数组。

>? 标签操作 tags 为标签字符串数组（标签字符串不允许有空格或者是 tab 字符）。
>



#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] clearAndAppendTags:@[ tagStr ]];

```

### 清除全部标签

#### 接口说明

清除所有设置的标签。

```Objective-C
- (void)clearTags

```

>? 此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。
>

#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] clearTags];

```

### 查询标签

#### 接口说明

SDK 1.3.1.0 新增，查询设备绑定的标签。

```Objective-C
- (void)queryTags:(NSUInteger)offset limit:(NSUInteger)limit;

```

> ?此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。

#### 参数说明 

- offset：此次查询的偏移大小。
- offset：limit 此次查询的分页大小, 最大200。

#### 示例代码

```Objective-C
 [[XGPushTokenManager defaultTokenManager] queryTags:0 limit:100];

```

### 查询标签的回调

#### 接口说明

SDK 1.3.1.0 新增，查询标签的结果会走此回调。

```objective-c
- (void)xgPushDidQueryTags:(nullable NSArray<NSString *> *)tags totalCount:(NSUInteger)totalCount error:(nullable NSError *)error;

```

#### 返回参数说明

- tags：查询条件返回的标签。
- totalCount：设备绑定的总标签数量。
- error：错误信息，若 error 为 nil，则查询成功。

## 用户属性功能

以下为用户属性相关接口方法，若需了解调用时机及调用原理，可查看 [用户属性相关流程](https://cloud.tencent.com/document/product/548/36662#.E7.94.A8.E6.88.B7.E5.B1.9E.E6.80.A7.E7.9B.B8.E5.85.B3.E6.B5.81.E7.A8.8B)。

### 新增用户属性

#### 接口说明

添加或更新用户属性（key-value 结构，若原来没有该 key 的用户属性 value，则新增；若原来有该 key 的用户属性 value，则更新该 value）。

```Objective-C
- (void)upsertAttributes:(nonnull NSDictionary<NSString *,NSString *> *)attributes

```

> ?此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。

#### 参数说明 

attributes：用户属性字符串字典，字符串不允许有空格或者是 tab 字符。

> ? 
>
> - 需要先在管理台配置用户属性的键，才能操作成功。
> - key，value 长度都限制50个字符以内。
> - 需要使用字典且 key 是固定要求。
> - Objective-C 的写法 : @{@"gender": @"Female", @"age": @"29"}；
> - Swift 的写法：["gender":"Female", "age": "29"]

#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] upsertAttributes:attributes];

```

### 删除用户属性

#### 接口说明

删除用户已有的属性。

```Objective-C
- (void)delAttributes:(nonnull NSSet<NSString *> *)attributeKeys

```

>? 此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。
>

#### 参数说明 

attributeKeys：用户属性 key 组成的集合，字符串不允许有空格或者是 tab 字符。

>? 使用集合且key是固定要求。
>

#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] delAttributes:attributeKeys];

```

### 清空已有用户属性

#### 接口说明

清空已有用户属性。

```Objective-C
- (void)clearAttributes;

```

> ?此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。

#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] clearAttributes];

```

### 更新用户属性

#### 接口说明

清空已有用户属性，然后批量添加用户属性。



```Objective-C
- (void)clearAndAppendAttributes:(nonnull NSDictionary<NSString *,NSString *> *)attributes

```

> ?此接口应在 xgPushDidRegisteredDeviceToken:error: 返回正确后被调用。

#### 示例代码

```Objective-C
[[XGPushTokenManager defaultTokenManager] clearAndAppendAttributes:attributes];

```

## 角标功能

### 同步角标

#### 接口说明

当应用本地角标值更改后，需调用此接口将角标值同步到 TPNS 服务器，下次推送时以此值为基准，此功能在管理台位置（【新建推送】>【高级设置】>【角标数字】）。

```objective-c
- (void)setBadge:(NSInteger)badgeNumber;

```

#### 参数说明

badgeNumber：应用的角标数。

> ! 当本地应用角标设置后需调用此接口同步角标值到 TPNS 服务器，并在下次推送时生效，此接口必须在 TPNS 注册成功后调用（xgPushDidRegisteredDeviceToken）。

#### 示例代码

```Objective-C
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    /// 每次启动 App 应用角标清零（本地应用角标设置需要在主线程执行）
    if ([XGPush defaultManager].xgApplicationBadgeNumber > 0) {
        [XGPush defaultManager].xgApplicationBadgeNumber = 0;
    }
    return YES;
}

- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken xgToken:(nullable NSString *)xgToken error:(nullable NSError *)error {
    /// 在注册完成后同步角标数到TPNS
    if (!error) {
        [[XGPush defaultManager] setBadge:0];
    }
}

```

##  应用内消息展示
### 轮询时间设置

#### 接口说明

此接口可以设置应用内消息的轮询时间，最小为10s，默认为258s。

```objective-c
/// 设置消息轮询时间间隔，最小值为10s，此方法需要在单例初始化之前调用
- (void)setMessageTimerInterval:(NSTimeInterval)interval;
```
#### 参数说明
NSTimeInterval：NSTimeInterval类型，应用内消息轮询时间间隔。

### 自定义事件处理

#### XGInAppMessageActionDelegate 代理说明

用户通过代理方法 `onClickWithCustomAction`获取自定义事件参数来处理相关业务。

```objective-c
/// 按钮事件响应代理
@property (weak, nonatomic, nullable) id<XGInAppMessageActionDelegate> actionDelegate;
```


## 查询设备通知权限

#### 接口说明

查询设备通知权限是否被用户允许。 

```objective-c
- (void)deviceNotificationIsAllowed:(nonnull void (^)(BOOL isAllowed))handler;

```

#### 参数说明

handler：查询结果的返回方法。

#### 示例代码

```objective-c
[[XGPush defaultManager] deviceNotificationIsAllowed:^(BOOL isAllowed) {
        <#code#>
    }];

```

## 查询 SDK 版本

#### 接口说明

查询当前 SDK 的版本。

```objective-c
- (nonnull NSString *)sdkVersion;

```

#### 示例代码

```objective-c
[[XGPush defaultManager] sdkVersion];

```

## 日志上报接口

#### 接口说明

开发者如果发现推送相关功能异常，可以调用该接口，触发本地 push 日志的上报，通过联系 [在线客服](https://cloud.tencent.com/act/event/Online_service) 反馈问题时，请将文件地址提供给我们，便于排查问题。

```
/// @note TPNS SDK1.2.4.1+
- (void)uploadLogCompletionHandler:(nullable void(^)(BOOL result,  NSString * _Nullable errorMessage))handler;

```

#### 参数说明

- @brief：上报日志信息 （SDK1.2.4.1+）。
- @param handler：上报回调。

#### 示例代码

```
[[XGPush defaultManager] uploadLogCompletionHandler:nil];

```

## TPNS 日志托管

#### 接口说明

可以在此方法获取 TPNS 的 log 日志。此方法和 XGPush > enableDebug 无关。

#### 参数说明

logInfo：日志信息。

#### 示例代码

```
- (void)xgPushLog:(nullable NSString *)logInfo;

```

## 自定义通知栏消息行为

### 创建消息支持的行为

#### 接口说明

在通知消息中创建一个可以点击的事件行为。

```objective-c
+ (nullable id)actionWithIdentifier:(nonnull NSString *)identifier title:(nonnull NSString *)title options:(XGNotificationActionOptions)options;

```

#### 参数说明

- identifier：行为唯一标识。 
- title：行为名称。 
- options：行为支持的选项。

#### 示例代码

```objective-c
XGNotificationAction *action1 = [XGNotificationAction actionWithIdentifier:@"xgaction001" title:@"xgAction1" options:XGNotificationActionOptionNone];

```

> ! 通知栏带有点击事件的特性，只有在 iOS8.0+ 以上支持，iOS 7.x or earlier 的版本，此方法返回空。

### 创建分类对象

#### 接口说明

创建分类对象，用以管理通知栏的 Action 对象。

```objective-c
+ (nullable id)categoryWithIdentifier:(nonnull NSString *)identifier actions:(nullable NSArray<id> *)actions intentIdentifiers:(nullable NSArray<NSString *> *)intentIdentifiers options:(XGNotificationCategoryOptions)options

```

#### 参数说明

- identifier：分类对象的标识。
- actions：当前分类拥有的行为对象组。
- intentIdentifiers：用以表明可以通过 Siri 识别的标识。
- options：分类的特性。

> ! 通知栏带有点击事件的特性，只有在 iOS8+ 以上支持，iOS 8 or earlier的版本，此方法返回空。

#### 示例代码

```Objective-C
XGNotificationCategory *category = [XGNotificationCategory categoryWithIdentifier:@"xgCategory" actions:@[action1, action2] intentIdentifiers:@[] options:XGNotificationCategoryOptionNone];
```

### 创建配置类

#### 接口说明

管理推送消息通知栏的样式和特性。

```objective-c
+ (nullable instancetype)configureNotificationWithCategories:(nullable NSSet<id> *)categories types:(XGUserNotificationTypes)types;
```

#### 参数说明

- categories：通知栏中支持的分类集合。 
- types：注册通知的样式。

#### 示例代码

```objective-c
XGNotificationConfigure *configure = [XGNotificationConfigure configureNotificationWithCategories:[NSSet setWithObject:category] types:XGUserNotificationTypeAlert|XGUserNotificationTypeBadge|XGUserNotificationTypeSound];
```

## 本地推送

本地推送相关功能请参见 [苹果开发者文档](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SchedulingandHandlingLocalNotifications.html#//apple_ref/doc/uid/TP40008194-CH5-SW1)。
