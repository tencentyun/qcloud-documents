## 集成 SDK

### 前置条件[](id:qztj)
- **环境要求**
  - `iOS` >= 7.0
  - `Xcode` >= 10.0
- **组件依赖**
  - `openssl`
  - `Tars`
  - `MQQTcc`
  - `MQQComponents`
  - `TMFSSL`
  - `TMFShark`
  - `TMFProfile`

### 集成方式
TMFPush 的集成方式有以下 2 种，可选择其一进行集成：
- CocoaPods 集成 SDK（离线 Pod）
- 手动集成 SDK

#### CocoaPods 集成 SDK（离线 Pod）
1. 在您项目中的 `Podfile` 文件里添加如下内容：
  ```objective-c
  target 'YourTarget' do

    # 依赖组件
    pod 'openssl',          :path => './Frameworks/openssl'
    pod 'MQQTcc',           :path => './Frameworks/MQQTcc'
    pod 'TMFSSL',           :path => './Frameworks/TMFSSL'
    pod 'Tars',             :path => './Frameworks/Tars'
    pod 'MQQComponents',    :path => './Frameworks/MQQComponents'
    pod 'TMFShark',         :path => './Frameworks/TMFShark'
    pod 'TMFProfile',     	:path => './Frameworks/TMFProfile'
    
    # TMFPush
    pod 'TMFPush',    :path => './Frameworks/TMFPush'
      
  end
```
  其中：
  - `YourTarget` 为您的项目需要引入 `TMFPush` 的 target 的名字。
  - `:path =>` 指向的路径，为当前组件的 `.podspec` 文件所在目录与 `Podfile` 文件的**相对路径**。 例如，上面示例中的 `'./Frameworks/TMFPush'` 为 `TMFPush.podspec` 文件所在目录的相对路径。
2. Terminal `cd` 到 Podfile 文件所在目录，并执行 `pod install` 进行组件安装。
```shell
  $ pod install
```

#### 手动集成 SDK
1. **添加 SDK**
  把 `TMFPush` 组件的目录添加到您项目的 Xcode Project 中的合适位置，并选择合适的 target。
  您可以把组件的目录从 Finder 直接拖动到 Xcode Project 中，以进行快捷添加。
![](https://qcloudimg.tencent-cloud.cn/raw/96be3f02bc0228e10b76cbc55366ed65.png)
![](https://qcloudimg.tencent-cloud.cn/raw/200b58fa1028c492d07104f9ce001a6c.png)
2. **添加依赖的 SDK**
  把 `TMFPush` 依赖的所有组件添加到您的项目中。
  依赖的组件列表见 [前置条件 - 组件依赖](#qztj)。
3. **添加依赖的系统库**
  把 `TMFPush` 依赖的系统库添加到您的项目中。
  在 Xcode 中打开您的 project 设置页，选中相关的 target，单击**General**，在“Linked Frameworks and Libraries”中进行添加。
4. **系统库依赖**
  - `Foundation.framework`
  - `UIKit.framework`
  - `UserNotifications.framework`
  - `libc++.tbd`
  - `libsqlite3.0.tbd`
  - `libz.tbd`
5. **Project 设置**
  添加 `TMFPush` 之后，需要进行相关的 Project 设置。
  在 Xcode 中打开您的 Project 设置页，选中相关的 target，进行以下设置：
  - 选择 **Build Settings** > **Linking** > **Other Linker Flags**，增加：`-ObjC`
  - 单击 **Capabilities**，打开“Push Notifications“和”Background Modes”配置推送。
![](https://qcloudimg.tencent-cloud.cn/raw/dba1c1bf2422ae3c457a568fee438464.png)
![](https://qcloudimg.tencent-cloud.cn/raw/cc4aeab0414cf00fc0bb4acc54f3a06f.png)

## 使用 SDK

### 调试
1. 打开 `Debug` 模式，可以在终端控制台中查看到推送的 Debug 日志，方便定位问题。
```objective-c
[[TMFPush defaultManager] setLogEnabled:YES];
```
2. 观察日志
在控制台中查看 tag:  `TMFPush` 的相关日志。

### 启动推送服务
**接口定义**
```objective-c
- (void)startPushWithDelegate:(nullable id<TMFPushDelegate>)delegate;
```

**参数说明**

| 参数             | 类型                                   | 描述                     | 必选 |
| ---------------- | -------------------------------------- | ------------------------ | ---- |
| delegate             | TMFPushDelegate                              | 实现 `TMFPushDelegate` 协议的回调对象，一般是 `AppDelegate`                  | NO    |

**调用示例**
```objective-c
[[TMFPush defaultManager] startPushWithDelegate:self];
```

### 终止推送服务
终止推送服务以后，将无法通过推送服务向设备推送消息，如果再次需要接收服务的消息推送，则必须需要再次调用 `startPushWithDelegate:` 方法重启推送服务。
**接口定义**
```
- (void)stopPushNotification;
```

**调用示例**
```
[[TMFPush defaultManager] stopPushNotification];
```

### 自定义通知栏消息行为

#### 创建消息支持的行为[创建消息支持的行为](id:cjxx)
在通知消息中创建一个可以点击的事件行为。
**接口定义**
```objective-c
+ (nullable id)actionWithIdentifier:(nonnull NSString *)identifier title:(nonnull NSString *)title options:(TMFNotificationActionOptions)options;
```

**参数说明**

| 参数       | 类型                         | 描述           | 必选 |
| ---------- | ---------------------------- | -------------- | ---- |
| identifier | NSString                     | 行为唯一标识         | NO    |
| title      | NSString                     | 行为名称       | YES    |
| options    | TMFNotificationActionOptions | 行为支持的选项 | YES    |

其中，TMFNotificationActionOptions 的定义如下：
```objective-c
/**
 @brief 点击行为对象的属性配置
 
 - TMFNotificationActionOptionNone: 无
 - TMFNotificationActionOptionAuthenticationRequired: 执行前需要解锁验证
 - TMFNotificationActionOptionDestructive: 显示高亮（红色）
 - TMFNotificationActionOptionForeground: 拉起应用到前台
 */
typedef NS_OPTIONS(NSUInteger, TMFNotificationActionOptions) {
    TMFNotificationActionOptionNone = (0),
    TMFNotificationActionOptionAuthenticationRequired = (1 << 0),
    TMFNotificationActionOptionDestructive = (1 << 1),
    TMFNotificationActionOptionForeground = (1 << 2)
};
```

**返回值**

| 类型                  | 描述                                   |
| --------------------- | -------------------------------------- |
| TMFNotificationAction | 在通知消息中创建一个可以点击的事件行为 |

**调用示例**
```objective-c
TMFNotificationAction *action1 = [TMFNotificationAction actionWithIdentifier:@"tmfaction001" title:@"tmfAction1" options:TMFNotificationActionOptionNone];
```
>?通知栏带有点击事件的特性，只有在 iOS8.0 + 以上支持，iOS 7.x or earlier 的版本，此方法返回空。
>

#### 创建分类对象[](id:cjfldx)
创建分类对象，用以管理通知栏的 Action 对象。
**接口定义**
```objective-c
+ (nullable id)categoryWithIdentifier:(nonnull NSString *)identifier actions:(nullable NSArray<TMFNotificationAction *> *)actions intentIdentifiers:(nullable NSArray<NSString *> *)intentIdentifiers options:(TMFNotificationCategoryOptions)options;
```

**参数说明**

| 参数       | 类型                         | 描述           | 必选 |
| ---------- | ---------------------------- | -------------- | ---- |
| identifier | NSString                     | 分类对象的标识  | YES   |
| actions | SArray<TMFNotificationAction *> | 当前分类拥有的行为对象组 | NO   |
| intentIdentifiers | NSArray<NSString *> | 用以表明可以通过 Siri 识别的标识 | NO   |
| options | TMFNotificationCategoryOptions | 分类的特性 | YES|

其中，TMFNotificationCategoryOptions 的定义如下：
```objective-c
/**
 @brief 分类对象的属性配置
 
 - TMFNotificationCategoryOptionNone: 无
 - TMFNotificationCategoryOptionCustomDismissAction: 发送消失事件给UNUserNotificationCenter(iOS 10 or later)对象
 - TMFNotificationCategoryOptionAllowInCarPlay: 允许CarPlay展示此类型的消息
 */
typedef NS_OPTIONS(NSUInteger, TMFNotificationCategoryOptions) {
    TMFNotificationCategoryOptionNone = (0),
    TMFNotificationCategoryOptionCustomDismissAction = (1 << 0),
    TMFNotificationCategoryOptionAllowInCarPlay = (1 << 1)
};
```

TMFNotificationAction 的定义见 [创建消息支持的行为](#cjxx)。
**返回值**

| 类型                    | 描述                                 |
| ----------------------- | ------------------------------------ |
| TMFNotificationCategory | 创建用以管理通知栏 Action 的分类对象 |

>?通知栏带有点击事件的特性，只有在 iOS8+ 以上支持，iOS 8 or earlier 的版本，此方法返回空。
>
**调用示例**
```Objective-C
TMFNotificationCategory *category = [TMFNotificationCategory categoryWithIdentifier:@"tmfCategory" actions:@[action1, action2] intentIdentifiers:@[] options:TMFNotificationCategoryOptionNone];
```

#### 创建配置类
管理推送消息通知栏的样式和特性。
**接口定义**
```objective-c
+ (nullable instancetype)configureNotificationWithCategories:(nullable NSSet<TMFNotificationCategory *> *)categories types:(TMFUserNotificationTypes)types;
```

**参数说明**

| 参数       | 类型                         | 描述           | 必选 |
| ---------- | ---------------------------- | -------------- | ---- |
| categories | NSSet<TMFNotificationCategory *> | 通知栏中支持的分类集合 | NO    |
| types | TMFUserNotificationTypes | 注册通知的样式 | YES|

其中，TMFUserNotificationTypes 的定义如下：
```objective-c
/**
 @brief 注册通知支持的类型
 
 - TMFUserNotificationTypeNone: 无
 - TMFUserNotificationTypeBadge: 支持应用角标
 - TMFUserNotificationTypeSound: 支持铃声
 - TMFUserNotificationTypeAlert: 支持弹框
 - TMFUserNotificationTypeCarPlay: 支持CarPlay,iOS 10.0+
 - TMFUserNotificationTypeCriticalAlert: 支持紧急提醒播放声音, iOS 12.0+
 - TMFUserNotificationTypeProvidesAppNotificationSettings: 让系统在应用内通知设置中显示按钮, iOS 12.0+
 - TMFUserNotificationTypeProvisional: 能够将非中断通知临时发布到 Notification Center, iOS 12.0+
 - TMFUserNotificationTypeNewsstandContentAvailability: 支持 Newsstand, iOS 3.0–8.0
 */
typedef NS_OPTIONS(NSUInteger, TMFUserNotificationTypes) {
    TMFUserNotificationTypeNone = (0),
    TMFUserNotificationTypeBadge = (1 << 0),
    TMFUserNotificationTypeSound = (1 << 1),
    TMFUserNotificationTypeAlert = (1 << 2),
    TMFUserNotificationTypeCarPlay = (1 << 3),
    TMFUserNotificationTypeCriticalAlert = (1 << 4),
    TMFUserNotificationTypeProvidesAppNotificationSettings = (1 << 5),
    TMFUserNotificationTypeProvisional = (1 << 6),
    TMFUserNotificationTypeNewsstandContentAvailability = (1 << 3)
};
```

TMFNotificationCategory 的定义见 [创建分类对象](#cjfldx)
**调用示例**
```objective-c
TMFNotificationConfigure *configure = [TMFNotificationConfigure configureNotificationWithCategories:[NSSet setWithObject:category] types:TMFUserNotificationTypeAlert|TMFUserNotificationTypeBadge|TMFUserNotificationTypeSound];
```

### 管理设备 Token

查询当前应用从 APNs 获取的 Token 字符串。
**接口定义**
```objective-c
@property (copy, nonatomic, nullable, readonly) NSString *deviceTokenString;
```
**调用示例**
```objective-c
NSString *token = [[TMFPushTokenManager defaultTokenManager] deviceTokenString];
```

#### 查询注册结果
SDK 的启动方法自动注册设备从 APNs 获取的 Token 到TMF推送服务器，注册结果会在 `TMFPushDelegate` 的回调方法返回。
**接口定义**
```objective-c
- (void)tmfPushDidRegisterDeviceToken:(NSString *)deviceToken error:(NSError *)error;
```
**参数说明**

| 参数        | 类型     | 描述                       | 必选 |
| ----------- | -------- | -------------------------- | ---- |
| deviceToken | NSString | 回调从 APNs 获取到的 Token | YES    |
| error       | NSError  | 注册通知的样式             | NO|

>?此回调方法在注册成功之后调用，当前的 Token 已经注册过之后，SDK 将缓存注册信息，此方法将不会再调用。
>
**调用示例**
```objective-c
- (void)tmfPushDidRegisterDeviceToken:(NSString *)deviceToken error:(NSError *)error {
    NSLog(@"[TMFPush] did register deviceToken: %@, error: %@", deviceToken, error);
}
```

### 收到推送的回调
SDK 收到推送结果会在 `TMFPushDelegate` 的回调方法返回。
**接口定义**
```objective-c
- (void)tmfPushDidReceiveRemoteNotification:(id)notification withCompletionHandler:(nullable void (^)(UIBackgroundFetchResult))completionHandler;
```
**参数说明**

| 参数         | 类型         | 描述         | 必选 |
| ------------ | ------------ | ------------ | ---- |
| notification | NSDictionary | 当前推送消息 | YES    |

- notification：当前推送消息。
- completionHandler：处理结果。

**completionHandler 回调**

| 参数   | 类型                    | 描述                         | 必选 |
| ------ | ----------------------- | ---------------------------- | ---- |
| result | UIBackgroundFetchResult | 收到通知后，告知后台操作结束 | YES    |

其中，UIBackgroundFetchResult 的系统定义如下：

```objective-c
typedef NS_ENUM(NSUInteger, UIBackgroundFetchResult) {
    UIBackgroundFetchResultNewData,
    UIBackgroundFetchResultNoData,
    UIBackgroundFetchResultFailed
} NS_ENUM_AVAILABLE_IOS(7_0);
```

操作类型定义如下：

- UIBackgroundFetchResultNewData 成功拉取到数据。
- UIBackgroundFetchResultNoData 没有新数据。
- UIBackgroundFetchResultFailed 拉取数据失败或者超时。

**调用示例**
```objective-c
- (void)tmfPushDidReceiveRemoteNotification:(nonnull id)notification withCompletionHandler:(nullable void (^)(UIBackgroundFetchResult))completionHandler {
    NSLog(@"[TMFPush] did receive remote notification: %@", notification);
    if ([notification isKindOfClass:[NSDictionary class]]) {
        // NSDictionary
        NSDictionary *data = notification;
        for (NSString *key in data) {
            id value = data[key];
            NSLog(@"[TMFPush] key: %@, value: %@", key, value);
        }
        
        completionHandler(UIBackgroundFetchResultNewData);
    }
}
```

### 收到推送的回调（iOS 10）
SDK 收到推送结果会在 `TMFPushDelegate` （以下）的回调方法返回。
**接口定义**
```objective-c
- (void)tmfPushUserNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(nullable UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler API_AVAILABLE(ios(10.0));
```

**参数说明**

| 参数         | 类型                     | 描述                                                 | 必选 |
| ------------ | ------------------------ | ---------------------------------------------------- | ---- |
| center       | UNUserNotificationCenter | [UNUserNotificationCenter currentNotificationCenter] | YES    |
| notification | UNNotification           | 当前推送消息                                         | NO|

**completionHandler 回调**

| 参数    | 类型                              | 描述                         | 必选 |
| ------- | --------------------------------- | ---------------------------- | ---- |
| options | UNNotificationPresentationOptions | 收到通知后，告知后台处理结束 | YES    |

其中，UNNotificationPresentationOptions 的系统定义如下：

```objective-c
typedef NS_OPTIONS(NSUInteger, UNNotificationPresentationOptions) {
    UNNotificationPresentationOptionBadge   = (1 << 0),
    UNNotificationPresentationOptionSound   = (1 << 1),
    UNNotificationPresentationOptionAlert   = (1 << 2),
} __IOS_AVAILABLE(10.0) __TVOS_AVAILABLE(10.0) __WATCHOS_AVAILABLE(3.0) __OSX_AVAILABLE(10.14);
```

提醒类型如下：
- UNNotificationPresentationOptionBadge 角标提醒。
- UNNotificationPresentationOptionSound 声音提醒。
- UNNotificationPresentationOptionAlert 弹窗提醒。

可以通过或操作同时设置多种类型。
**调用示例**
```objective-c
- (void)tmfPushUserNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(nullable UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler API_AVAILABLE(ios(10.0)) {
    NSLog(@"[TMFPush] did receive remote notification(iOS10+): %@", notification);
    UNNotification *unNotification = notification;
    UNNotificationContent *content = unNotification.request.content;
    NSLog(@"[TMFPush] title: %@, body: %@", content.title, content.body);
    NSLog(@"[TMFPush] userInfo: %@", content.userInfo);
    
    completionHandler(UNNotificationPresentationOptionBadge
                     |UNNotificationPresentationOptionSound);
}
```

### 收到推送点击的回调（iOS 10）
SDK 收到推送提示点击结果会在 `TMFPushDelegate` （以下）的回调方法返回。
**接口定义**
```objective-c
- (void)tmfPushUserNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(nullable UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler API_AVAILABLE(ios(10.0));
```

**参数说明**

| 参数     | 类型                     | 描述                                                 | 必选 |
| -------- | ------------------------ | ---------------------------------------------------- | ---- |
| center   | UNUserNotificationCenter | [UNUserNotificationCenter currentNotificationCenter] | YES    |
| response | UNNotificationResponse   | 用户对通知消息的响应对象                             | NO    |

**completionHandler 回调**

| 参数 | 类型 | 描述 | 必选 |
| ---- | ---- | ---- | ---- |
| void | -    | -    | YES    |

推送弹窗点击处理结束时，需要调用 `completionHandler()` 结束当前行为。
**调用示例**
```objective-c
- (void)tmfPushUserNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(nullable UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler API_AVAILABLE(ios(10.0)) {
    
    NSDictionary *userInfo = response.notification.request.content.userInfo;
    NSLog(@"[TMFPush] did handle action for remote notification, userInfo: %@", userInfo);
    
    completionHandler();
}
```

### 查询设备通知权限
查询设备通知权限是否被用户允许。 
**接口定义**
```objective-c
- (void)deviceNotificationIsAllowed:(nonnull void (^)(BOOL isAllowed))handler;
```

**completionHandler 回调**

| 参数      | 类型 | 描述                     | 必选 |
| --------- | ---- | ------------------------ | ---- |
| isAllowed | BOOL | 设备是否具备推送通知权限 | YES    |

**调用示例**
```objective-c
[[TMFPush defaultManager] deviceNotificationIsAllowed:^(BOOL isAllowed) {
		<#code#>
}];
```

### 查询 SDK 版本
查询当前 SDK 的版本。
**接口定义**
```objective-c
- (nonnull NSString *)sdkVersion;
```
**调用示例**
```objective-c
[[TMFPush defaultManager] sdkVersion];
```

## 证书生成

### P12证书导出
1. `钥匙串`中同时选择**`推送证书`**和**`密钥文件`**，然后导出两项。
![](https://qcloudimg.tencent-cloud.cn/raw/2367d97759cf6d92ecc8f59cca1a3b98.png)
2. 选择证书存放目录。
![](https://qcloudimg.tencent-cloud.cn/raw/3d1f38719c453555fe98bab407ceacbc.png)
3. 输入证书的密码(例:123)
![](https://qcloudimg.tencent-cloud.cn/raw/29b441ef05fbba82686aac9d8ae4c9bc.png)


### Pem证书生成
1. 打开「终端」`cd`至 p12 证书所在目录。
2. 输入脚本导出 pem 文件。
```shell
openssl pkcs12 -in 证书.p12 -out 证书.pem -clcerts -nodes
```
3. 输入证书密码（p12导出时设置的密码，上文中的123）。
![](https://qcloudimg.tencent-cloud.cn/raw/184b98d49365de641135606d1713fd15.png)
4. 导出成功提示。
![](https://qcloudimg.tencent-cloud.cn/raw/59fc45749f13be7f94342cbb57b43e73.png)

## TMF iOS 消息推送（TMFDataPush）用户手册

### 集成 SDK

#### 前置条件（TMFDataPush）
* **环境要求**
  * `iOS` >= 8.0
  * `Xcode` >= 10.0

- **组件依赖**
  - `TMFInstruction`
  - `TMFShark`
  - `Tars`
  - `openssl`
  - `MQQTcc`
  - `MQQComponents`
  - `TMFSSL`

### 集成方式
`MQQCodeDetector` 的集成方式有以下 2 种，可选择其一进行集成：
- CocoaPods 集成 SDK（离线 Pod）
- 手动集成 SDK

#### CocoaPods 集成 SDK（离线 Pod）
- 在您项目中的 Podfile 文件里添加如下内容：
```objective-c
  target 'YourTarget' do
   
    # 依赖组件
    pod 'TMFInstruction',       :path => './Frameworks/TMFInstruction'
    pod 'TMFShark',             :path => './Frameworks/TMFShark'
    pod 'Tars',                 :path => './Frameworks/Tars'
    pod 'openssl',              :path => './Frameworks/openssl'
    pod 'MQQTcc',               :path => './Frameworks/MQQTcc'
    pod 'MQQComponents',        :path => './Frameworks/MQQComponents'
    pod 'TMFSSL',               :path => './Frameworks/TMFSSL'
    
    # TMFDataPush
    pod 'TMFDataPush',          :path => './Frameworks/TMFDataPush
      
  end
```
  其中：
  - `YourTarget` 为您的项目需要引入 TMFDataPush` 的 target 的名字。
  - `:path => ` 指向的路径，为当前组件的 `.podspec` 文件所在目录与 `Podfile` 文件的**相对路径**。
    例如，上面示例中的 `'./Frameworks/TMFDataPush'` 为 `TMFDataPush.podspec` 文件所在目录的相对路径。
- Terminal `cd` 到 Podfile 文件所在目录，并执行 `pod install` 进行组件安装。
```shell
  $ pod install
```

#### 手动集成 SDK
1. 把 `TMFDataPush` 组件的目录添加到您项目的 Xcode Project 中的合适位置，并选择合适的 target。
  您可以把组件的目录从 Finder 直接拖动到 Xcode Project 中，以进行快捷添加。
>?手动集成 SDK 不要引入 `LICENSE` 与 `podspec` 等无关文件到项目中。
>
![](https://qcloudimg.tencent-cloud.cn/raw/97428556b09874f394dc2cfe918e823a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/d02ff61513f285f39b760e61eb214398.png)
2. 把 `TMFDataPush` 依赖的所有组件添加到您的项目中。
  依赖的组件列表见 [前置条件 - 组件依赖](#qztj)。
3. 添加 `TMFDataPush` 依赖的系统库。
  在 Xcode 中打开您的 project 设置页，选中相关的 target，单击**General**，在“Linked Frameworks and Libraries”中进行添加。
  **系统库依赖**
  - `Foundation.framework`
  - `UIKit.framework`
  - `Security.framework`
  - `CoreTelephony.framework`
  - `SystemConfiguration.framework`
  - `CoreFoundation.framework`
  - `libsqlite3.0.tdb`
  - `libc++.tdb`
  - `libc.tbd`
  - `libz.1.2.5.tbd`
  ![](https://qcloudimg.tencent-cloud.cn/raw/4d284fe74eeb6ad0d288e54e11385666.png)
  
4. **Project 设置**
添加 `TMFDataPush` 之后，需要进行相关的 Project 设置。
在 Xcode 中打开您的 Project 设置页，选中相关的 target，进行以下设置：
  - 选择 **Build Settings** > **Linking** > **Other Linker Flags**，增加：
    - `-ObjC`
  - 选择 **Build Settings** > **Apple Clang** - **Custom Compiler Flags** > **Other C Flags** ，增加：
    - `-fshort-wchar`
    - `-D__FIXWCHART__`
  - 选择 **Build Settings** > **Apple Clang - Custom Compiler Flags** > **Other C++ Flags**，增加：
    - `-fshort-wchar`
    - `-D__FIXWCHART__`

## 使用 SDK

### 初始化[](id:csh)
使用组件前，需要完成的基本初始化操作。

#### 前置条件
若要通过组件初始化，必须先完成 SDK 集成，详情请参见 [前置条件](#qztj) 。

#### 引入头文件
```objective-c
#import 'TMFDataPush.h'
```

#### 初始化
```objective-c
+ (instancetype)defaultManager;
```

#### 初始化示例
```objective-c
TMFDataPush *dataPushManager = [TMFDataPush defaultManager];
```

### 数据透传
通过数据透传监听，可以将云端下发的数据透传给客户端业务。

#### 前置条件
若要通过组件进行数据透传，必须先完成初始化，详情请参见 [初始化](#csh) 。

#### 透传监听
```objective-c
- (void)observerDataPushWithHandler:(TMFDataPushHandler)handler;
```
**参数**
<table>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
<th>必选</th>
</tr>
<tr>
<td>handler</td>
<td>`TMFDataPushHandler`(block)</td>
<td>监听到云数据下发后的回调处理，详见 <a href="#TMFDataPushHandler">TMFDataPushHandler 回调</a></td>
<td>Y</td>
</tr>
</table>

- **TMFDataPushHandler 回调**[](id:TMFDataPushHandler)
```objective-c
typedef void (^TMFDataPushHandler)(TMFDataPushInfo *info);
```
<table>
<tr>
<th>类型</th>
<th>描述</th>
</tr>
<tr>
<td>`info *`</td>
<td>透传的数据模型，详见 <a href="#TMFDataPushInfo">TMFDataPushHandler 回调</a></td>
</tr>
</table>
  
- **TMFDataPushInfo 数据模型**[](id:TMFDataPushInfo)
```objective-c
@interface TMFDataPushInfo : NSObject

- (instancetype)init NS_UNAVAILABLE;

@property (nonatomic, copy, readonly) NSString *stringValue; ///< 云数据下发的字符串

@end
```
<table>
<tr>
<th>属性</th>
<th>类型</th>
<th>描述</th>
<th>权限</th>
</tr>
<tr>
<td>stringValue</td>
<td>`NSString *` </td>
<td>透传的字符串数据</td>
<td>readonly</td>
</tr>
</table>

#### 数据透传示例
下面是注册数据透传监听的示例：
```objective-c
[[TMFDataPush defaultManager] observerDataPushWithHandler:^(TMFDataPushInfo * _Nonnull info) {
      NSLog(@"[TMFDataPush] did observer data push, value: %@", info.stringValue);
}];
```

