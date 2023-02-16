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
  - `TMFInstruction`
  - `SSZipArchive`

### 集成方式
TMFWebOffline 的集成方式有以下 2 种，可选择其一进行集成：
- [CocoaPods 集成 SDK（离线 Pod）](#CocoaPods-sdk)
- [手动集成 SDK](#sdjc)

#### CocoaPods 集成 SDK（离线 Pod）[](id:CocoaPods-sdk)
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
    pod 'TMFInstruction',   :path => './Frameworks/TMFInstruction'
    pod 'SSZipArchive',     :path => './Frameworks/SSZipArchive'
    pod 'TMFQWebView',      :path => './Frameworks/TMFQWebView'
    # TMFWebOffline
    pod 'TMFWebOffline',    :path => './Frameworks/TMFWebOffline'
    end
```
其中：
  - `YourTarget` 为您的项目需要引入 `TMFWebOffline` 的 target 的名字。
  - `:path =>` 指向的路径，为当前组件的 `.podspec` 文件所在目录与 `Podfile` 文件的**相对路径**。 例如，上面示例中的 `'./Frameworks/TMFWebOffline'` 为 `TMFWebOffline.podspec` 文件所在目录的相对路径。
2. Terminal `cd` 到 Podfile 文件所在目录，并执行 `pod install` 进行组件安装。
```shell
  $ pod install
```

#### 手动集成 SDK[](id:sdjc)
1. **添加SDK**
  将`TMFWebOffline` 组件的目录添加到您项目的 Xcode Project 中的合适位置，并选择合适的 target。
  您可以把组件的目录从 Finder 直接拖动到 Xcode Project 中，以进行快捷添加。
2. **添加依赖的 SDK**
  把 `TMFWebOffline` 依赖的所有组件添加到项目中，依赖的组件列表，请参见前置条件中的 [组件依赖](#qztj)。
3. **添加依赖的系统库**
  把  `TMFWebOffline` 依赖的系统库添加到项目中，在 Xcode 中打开 project 设置页，选中相关的 target，单击**General**，在“Linked Frameworks and Libraries”中进行添加。
4. **系统库依赖**
	- `Foundation.framework`
	- `UIKit.framework`
	- `CoreGraphics.framework`
	- `Security.framework`
	- `libbz2.1.0.tdb`
	- `libz.tdb`
5. **Project 设置**
  添加 `TMFWebOffline` 后，需要进行相关的 Project 设置。
  在 Xcode 中打开 Project 设置页，选中相关的 target，进行以下设置：
选择 **Build Settings** > **Linking** > **Other Linker Flags**，增加：`-ObjC`。


## 使用 SDK

### 调试[](id:ts)

#### 配置说明
1. 在 `AppDelegate` 的 `-application:didFinishLaunchingWithOptions:` 中注册离线包调试日志输出回调，可以在终端控制台中查看到离线包的调试日志，方便定位问题。
```objective-c
  // 日志输出回调定义：
  void loggerWebOffline(TMFWebOfflineLoggerLevel level, const char* log) {
  #ifdef DEBUG
      if (level <= TMFWebOfflineLoggerLevelInfo) {
          NSLog(@"%s", log);
      }
  #endif
  }
  
  // 离线包下载进度监听回调
  void downloadProgressHandler(NSString *Bid, NSProgress *progress){
  #ifdef DEBUG
      NSLog(@"[TMFWebOffline Prog] download Bid:%@, progerss:%.2lf",Bid,progress.completedUnitCount *1.0 / progress.totalUnitCount);
  #endif   
  }
  
  // 配置日志输出
  - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  #ifdef DEBUG
      [TMFWebOfflineService registerLogger:loggerWebOffline];
  #endif
    return YES;
  }
```
>!日志打印建议仅在 DEBUG 环境中进行，发布版本不要输出离线包的相关日志。
>
2. Xcode 控制台中添加 Filter：TMFWebOffline
![](https://qcloudimg.tencent-cloud.cn/raw/6c7f97be4eed3f09d2e30a6fe37343af.png)
3. App 中调用离线包的相关接口，在控制台中观察的相关日志输出。

#### 日志级别说明

**日志分为 `Debug`、`Info`、`Warn`、`Error` 四个级别**
```objective-c
/**
 @brief 日志级别
 */
typedef NS_ENUM(NSInteger, TMFWebOfflineLoggerLevel) {
    TMFWebOfflineLoggerLevelDebug = 0,         ///< 调试帮助日志
    TMFWebOfflineLoggerLevelInfo = 1,          ///< 运行过程关键日志
    TMFWebOfflineLoggerLevelWarn = 2,          ///< 存在潜在问题日志
    TMFWebOfflineLoggerLevelError = 3,         ///< 严重错误导致系统退出日志
};
```
可根据日志级别在 loggerWebOffline 中灵活控制日志输出。例如，想输出 `Debug` 和 `Info` 的日志，可参考下面的设置：
```objective-c
#ifdef DEBUG
    if (level <= TMFWebOfflineLoggerLevelInfo) {
        NSLog(@"%s", log);
    }
#endif
```

**日志标签/关键字说明**
- 离线包预加载到生效的整体过程日志：（关键字：TMFWebOffline、TMFWebOfflineApp、download）
![](https://qcloudimg.tencent-cloud.cn/raw/8a09e0ff6a56a6ed587943ee4bcc9e80.png)
- webView 加载离线包过程日志：（关键字：TMFWebOffline、WebOfflineHandler、apply）
![](https://qcloudimg.tencent-cloud.cn/raw/efde9795b60a6be4e4004a3a8682160c.png)
- 终端预置离线包加载日志：（关键字：TMFWebOffline、preset、activate）
![](https://qcloudimg.tencent-cloud.cn/raw/d632dcb47ac3c0614250a697c3136c98.png)
>?终端预置离线包文件夹必须命名为 webappCachein，压缩包名字为 webappCachein.zip，详情请参见 [预置离线包说明](#yzlxb)。


### 运营统计[](id:yytj)
在 `AppDelegate` 的 `-application:didFinishLaunchingWithOptions:` 中注册离线包运营统计输出回调，业务可以根据实际选择运营统计平台进行上报，例如 `TMFAnalytics` 或者小马分析 SDK（`MTA`）。
```objective-c
// 离线包运营统计上报事件定义:
void reporterWebOffline(NSString *event, NSDictionary *kvs) { 
#ifdef DEBUG
    NSLog(@"event: %@ -> %@", event, kvs);
#endif
    [MTA trackCustomKeyValueEvent:event props:kvs];
}

// 配置运营统计回调:
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [TMFWebOfflineService registerReporter:reporterWebOffline];
  return YES;
}
```

[](id:yzlxb)
### 预置离线包说明

#### 目录结构
```makefile
webappCachein
  |-- BID
    |-- config.json
    |-- BID.zip
```
<table>
<tr>
<th>目录</th>
<th>名称</th>
<th>描述</th>
</tr>
<tr>
<td>根目录</td>
<td>webappCachein</td>
<td>预置离线包根目录，用于存放本地离线包资源，名字不能修改</td>
</tr>
<tr>
<td>二级目录</td>
<td>BID </td>
<td>以离线包 BID 命名，跟管理平台上配置的离线包业务 ID 一致</td>
</tr>
<tr>
<td rowspan="2">三级目录</td>
<td>config.json</td>
<td>从管理平台下载的 zip 包解压后，拷贝到三级目录的位置</td>
</tr>
<tr>
<td>BID.zip</td>
<td>从管理平台下载的 zip 包，拷贝到三级目录的位置</td>
</tr>
</table>

![](https://qcloudimg.tencent-cloud.cn/raw/eb63d06b7640cc3725207d4d080fd055.png)

#### 管理平台下载离线包并制作预置离线包
1. 登录 **[移动金融开发平台](https://console.cloud.tencent.com/tmf)** > **离线包** > **离线包管理中**，选择需要预置的离线包以及版本，在右侧操作栏，单击**详情**，单击**基础包链接**，下载需要预置的离线包。
![](https://qcloudimg.tencent-cloud.cn/raw/020053b445f8e31661730c696431fc7b.png)
2. [](id:step2)并从压缩包中解压中 `config.json` 文件存放到离线包目录结构中的三级目录下。
```shell
   $ cd Downloads/                       # 进入下载目录，假设基础包文件为bsdiff_180.zip bid是bid1
   $ mkdir bid1                            # 创建BID目录
   $ mv bsdiff_181.zip bid1/                # 将离线包文件移动到BID目录下
   $ cd bid1/                                                                                # 进入BID目录下
   $ mkdir tmp_bid                            # 创建临时解压目录
   $ unzip bsdiff_181.zip -d tmp_bid/        # 将离线包zip文件解压至临时目录
   $ mv tmp_bid/config.json ./                # 提取config.json至BID目录下
   $ mv bsdiff_181.zip bid1.zip               # bid1.zip重命名为bsdiff_181.zip
   $ rm -r tmp_bid/                          # 移除临时解压目录tmp_bid
   $ ls                                # 当前目录包含两个文件[config.json, bid1.zip]
```
3. 创建 `webappCachein.zip` 文件，可预知多个 BID。
>?
> - 前提我们已经在 Download 中按照 [步骤2](#step2) 创建了两个 BID 文件夹 [bid1, bid2]。
> - 压缩包名字不能改变，必须是`webappCachein`。
> 
```shell
$ mkdir webappCachein					# 创建webappCachein目录
$ mv bid1 webappCachein/				
$ mv bid2 webappCachein/			# 将bid1, bid2移动到webappCachein目录
$ zip -r webappCachein.zip webappCachein/	# 压缩webappCachein.zip
```

#### 预置离线包
将压缩后的 `webappCachein.zip` 添加到 Xcode工程的 Copy Bundle Resources 中。

### 激活离线包服务
激活离线包服务。
**接口定义**
```objective-c
+ (void)activate;
```

**调用说明**
- 在 `-application:didFinishLaunchingWithOptions:` App 函数中调用。
- 建议放置到前面初始化，在网关配置之后，其他代码初始化之前调用。

**调用示例**
```objective-c
[TMFWebOfflineService activate];
```

### 自定义离线包更新配置[](id:zdylxb)
生成离线包更新配置实例。
早期版本离线包任务推拉是依赖数据同步组件来完成的，从公有云版本起，离线包支持直接使用移动网关来实现任务推拉，可以解除任务推拉对数据同步组件的依赖。不过本次协议调整对新版服务有依赖，考虑到私有化客户不同的服务版本，SDK 侧做了兼容，同时保留了两套协议实现，客户在初始化时根据自身服务情况指定协议版本即可。其中使用公有云的初始化协议参数说明如下：
```objective-c
/**
 @brief 离线包推送协议
 */
typedef NS_ENUM(NSInteger, TMFWebOfflinePushPassagePolicy) {
    TMFWebOfflinePushPassagePolicyInstruction   = 0,    // default
    TMFWebOfflinePushPassagePolicyPushGo        = 1,
};
```

**接口定义**
```objective-c
/**
 @brief 离线包更新可选设置项
 */
@interface TMFWebOfflineServiceOptions : NSObject

/**
 @brief 离线包更新可选设置项实例
 */
+ (instancetype)options;

/**
 @brief Mask，默认0
 */
@property (nonatomic, assign) NSInteger mask;

/**
 @brief 更新来源，默认 `TMFWebOfflineServiceOptionsSourceRequest`
 */
@property (nonatomic, assign) TMFWebOfflineServiceOptionsSource source;

/**
 @brief 本地缓存更新策略，默认 `TMFWebOfflineServiceOptionsCachePolicyDownloadAndUpdate`
 */
@property (nonatomic, assign) TMFWebOfflineServiceOptionsCachePolicy cachePolicy;

/**
 @brief 是否忽略更新频率，默认NO
 */
@property (nonatomic, assign) BOOL ignoresFrequency;

/**
 @brief 是否忽略调用延迟，默认YES
 */
@property (nonatomic, assign) BOOL ignoresDelay;

@end
```

**参数说明**

| 参数             | 类型                                   | 描述                       | 必选 |
| ---------------- | -------------------------------------- | -------------------------- | ---- |
| mask             | NSInteger                              | 已废弃                     | NO    |
| source           | TMFWebOfflineServiceOptionsSource      | 更新来源                   | NO    |
| cachePolicy      | TMFWebOfflineServiceOptionsCachePolicy | 本地缓存更新策略           | NO    |
| ignoresFrequency | BOOL                                   | 是否忽略更新频率，默认 NO  | NO   |
| ignoresDelay     | BOOL                                   | 是否忽略调用延迟，默认 YES | NO   |

其中，TMFWebOfflineServiceOptionsSource 的定义如下：
```objective-c
/**
 @brief 离线包更新来源
 
 @note 枚举值对齐 `TMFWebOffline_Tars_EReqSource`
 */
typedef NS_ENUM(NSInteger, TMFWebOfflineServiceOptionsSource) {
    TMFWebOfflineServiceOptionsSourceRequest = 0,   ///< 主动拉取更新
    TMFWebOfflineServiceOptionsSourcePush = 1,      ///< 通过push进行更新
};
```
TMFWebOfflineServiceOptionsCachePolicy 的定义如下：
```objective-c
/**
 @brief 检查到离线包更新时本地缓存的更新策略
 */
typedef NS_ENUM(NSInteger, TMFWebOfflineServiceOptionsCachePolicy) {
    TMFWebOfflineServiceOptionsCachePolicyDownloadAndUpdate = 0,         ///< 检查到更新后，等下载最新离线包后覆盖本地缓存
    TMFWebOfflineServiceOptionsCachePolicyRemoveAndDownload = 1,         ///< 检查到更新后，先移除本地缓存，然后下载最新离线包后更新
};
```

**返回值**

| 类型                        | 描述                     |
| --------------------------- | ------------------------ |
| TMFWebOfflineServiceOptions | 离线包更新可选设置项实例 |

**调用示例**
```objective-c
TMFWebOfflineServiceOptions *options = [TMFWebOfflineServiceOptions options];
options.ignoresFrequency = YES; 
```

### 单业务 ID 检查更新并预加载离线包

#### 默认配置预加载
根据单个离线包业务 ID 以及默认更新配置，检查更新并预加载离线包，回调更新结果。

**接口定义**
```objective-c
+ (void)checkAndUpdateWithBID:(NSString *)BID completionHandler:(void(^)(BOOL isUpdated, NSError * _Nullable error))completionHandler;
```

**参数说明**

| 参数 | 类型     | 描述          | 必选 |
| ---- | -------- | ------------- | ---- |
| BID  | NSString | 离线包业务 ID | YES    |

**completionHandler 回调**

| 参数      | 类型    | 描述                        | 必选 |
| --------- | ------- | --------------------------- | ---- |
| isUpdated | BOOL    | 更新结果，成功 YES，失败 NO | YES   |
| error     | NSError | 更新失败时的错误信息        | NO   |

**调用示例**
```objective-c
[TMFWebOfflineService checkAndUpdateWithBID:@"BID" completionHandler:^(BOOL isUpdated, NSError * _Nullable error) {
	// callback
}];
```

#### 自定义配置预加载
根据单个离线包业务 ID 以及自定义更新配置，检查更新并预加载离线包，回调更新结果。
**接口定义**
```
+ (void)checkAndUpdateWithBID:(NSString *)BID options:(TMFWebOfflineServiceOptions *)options completionHandler:(void(^)(BOOL isUpdated, NSError * _Nullable error))completionHandler;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| BID  | NSString | 离线包业务 ID | YES    |
| options  | TMFWebOfflineServiceOptions | 可选配置 | YES    |

其中，TMFWebOfflineServiceOptions 的定义和实例化，请参见 [自定义离线包更新配置](#zdylxb)。

**completionHandler 回调**

| 参数      | 类型    | 描述                        | 必选 |
| --------- | ------- | --------------------------- | ---- |
| isUpdated | BOOL    | 更新结果，成功 YES，失败 NO |YES    |
| error     | NSError | 更新失败时的错误信息        | NO   |

**调用示例**
```objective-c
TMFWebOfflineServiceOptions *options = [TMFWebOfflineServiceOptions options];
options.ignoresFrequency = YES; 
[TMFWebOfflineService checkAndUpdateWithBID:@"BID" options:options completionHandler:^(BOOL isUpdated, NSError * _Nullable error) {
	// callback
}];
```

#### 通过 TMFHybrid 创建加载本地 H5 资源的通用 WebView 容器
**接口定义**
```objective-c
- (TMFWebViewController *)createWebViewControllerWithFile:(NSString *)filePath;
```

**参数说明**

| 入参     | 类型     | 描述               | 必选 | 默认值 |
| -------- | -------- | ------------------ | ---- | ------ |
| filePath | NSString | 本地 H5 资源的路径 | YES    | /      |

**调用示例**
```objective-c
NSString *filePath = [[NSBundle mainBundle] pathForResource:@"trans" ofType:@"html"];
UIViewController *webViewController = [[TMFHybridManager shareManager] createWebViewControllerWithFile:filePath];
[self.navigationController pushViewController:webViewController animated:YES];
```

#### 创建加载在线 H5 资源的通用 WebView 容器
**接口定义**
```objective-c
- (TMFWebViewController *)createWebViewControllerWithURL:(NSURL *)url;
```

**参数说明**

| 入参 | 类型  | 描述               | 必选 | 默认值 |
| ---- | ----- | ------------------ | ---- | ------ |
| url  | NSURL | 在线 H5 资源的地址 | YES    | /      |

**调用示例**
```objective-c
NSURL *url = [NSURL URLWithString:@"tmf.qq.com"];
UIViewController *webViewController = [[TMFHybridManager shareManager] createWebViewControllerWithURL:url];
[self.navigationController pushViewController:webViewController animated:YES];
```

#### 创建可以使用离线包的 WebView 容器-URL
**接口定义**
```
- (TMFWebViewController *)createOfflineWebViewControllerWithURL:(NSURL *)url;
```

**参数说明**

| 入参 | 类型  | 描述               | 必选 | 默认值 |
| ---- | ----- | ------------------ | ---- | ------ |
| url  | NSURL | 在线 H5 资源的地址 | YES    | /      |

**调用示例**
```objective-c
NSURL *url = [NSURL URLWithString:@"http://3gimg.qq.com/webapp_scan/TMF/TMF_intro/index.html?_bids=home"]
TMFWebViewController *webViewController = [[TMFHybridManager shareManager] createOfflineWebViewControllerWithURL:urlComp.URL];
[self.navigationController pushViewController:webViewController animated:YES];
```

#### 创建可以使用离线包的 WebView 容器-BID
**接口定义**
```
- (TMFWebViewController *)createOfflineWebViewControllerWithMainBID:(NSString *)bid;
```

**参数说明**

| 入参 | 类型     | 描述      | 必选 | 默认值 |
| ---- | -------- | --------- | ---- | ------ |
| bid  | NSString | 离线包BID | YES    | /      |

**调用示例**
```objective-c
UIViewController *webViewController = [[TMFHybridManager shareManager] createOfflineWebViewControllerWithMainBID:@"home"];
[self.navigationController pushViewController:webViewController animated:YES];
```

#### 创建可以使用离线包的 WebView 容器-多参数
**接口定义**
```objective-c
- (TMFWebViewController *)createOfflineWebViewControllerWithMainBID:(NSString *)mainBid commonBIDs:(NSArray <NSString *> * __nullable)commonBids indexPath:(NSString * __nullable)indexPath param:(NSDictionary<NSString *, NSString *> * __nullable)param fragment:(NSString * __nullable)fragment;
```

**参数说明**

| 入参       | 类型         | 描述                         | 必选 | 默认值 |
| ---------- | ------------ | ---------------------------- | ---- | ------ |
| mainBid    | NSString     | 离线包主包 BID                | YES    | /      |
| commonBids | NSArray      | 离线包公共包 BID              | NO    | /      |
| indexPath  | NSString     | 离线包 H5 资源入口           | NO    | /      |
| param      | NSDictionary | url 需要携带的参数信息       | NO    | /      |
| fragment   | NSString     | url 需要携带的 fragment 信息 | NO    | /      |

**调用示例**
```objective-c
UIViewController *vc2 = [[TMFHybridManager shareManager] createOfflineWebViewControllerWithMainBID:@"home" commonBIDs:@[@"static"] indexPath:@"testAk/index.html" param:nil fragment:nil];
[self.navigationController pushViewController:vc2 animated:YES];
```


### 多业务 ID 检查更新并预加载离线包

#### 默认配置预加载
根据一组离线包业务 ID 以及默认更新配置，检查更新并预加载离线包，回调更新结果。
**接口定义**
```objective-c
+ (void)checkAndUpdateWithBIDs:(NSArray<NSString *> *)BIDs completionHandler:(void(^)(NSArray<NSString *> *updatedBIDs))completionHandler;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| BIDs  | NSArray<NSString *> | 离线包业务 ID 列表 | YES    |

**completionHandler 回调**

| 参数      | 类型    | 描述                      | 必选 |
| --------- | ------- | ------------------------- | ---- |
| updatedBIDs | NSArray<NSString *>  | 可更新的离线包业务 ID 列表 | YES    |

**调用示例**
```objective-c
[TMFWebOfflineService checkAndUpdateWithBIDs:@[@"BID1",@"BID2"] completionHandler:^(NSArray<NSString *> * _Nonnull updatedBIDs) {
  // callback
}];
```

#### 自定义配置预加载
根据一组离线包业务 ID 以及自定义更新配置，检查更新并预加载离线包，回调更新结果。
**接口定义**
```objective-c
+ (void)checkAndUpdateWithBIDs:(NSArray<NSString *> *)BIDs options:(TMFWebOfflineServiceOptions *)options completionHandler:(void(^)(NSArray<NSString *> *updatedBIDs))completionHandler;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| BIDs  | NSArray<NSString *> | 离线包业务 ID 列表 | YES    |
| options  | TMFWebOfflineServiceOptions | 可选配置 | YES    |

其中，TMFWebOfflineServiceOptions 的定义和实例化见 [自定义离线包更新配置](#zdylxb)。

**completionHandler 回调**

| 参数      | 类型    | 描述                      | 必选 |
| --------- | ------- | ------------------------- | ---- |
| updatedBIDs | NSArray<NSString *>  | 可更新的离线包业务 ID 列表 | YES    |

**调用示例**
```Objective-C
TMFWebOfflineServiceOptions *options = [TMFWebOfflineServiceOptions options];
options.ignoresFrequency = YES; 
[TMFWebOfflineService checkAndUpdateWithBIDs:@[@"BID1",@"BID2"] options:options completionHandler:^(NSArray<NSString *> * _Nonnull updatedBIDs) {
  // callback
}];
```

### 全量更新并预加载离线包

#### 默认配置预加载
使用默认配置检查全量可更新的离线包并预加载离线包，回调可更新的业务 ID 列表。
**接口定义**
```objective-c
+ (void)checkAndUpdateAllAvailablePackagesWithCompletionHandler:(void(^)(NSArray<NSString *> *updatedBIDs))completionHandler;
```

**completionHandler 回调**

| 参数      | 类型    | 描述                      | 必选 |
| --------- | ------- | ------------------------- | ---- |
| updatedBIDs | NSArray<NSString *>  | 可更新的离线包业务 ID 列表 | YES    |

**调用示例**
```objective-c
[TMFWebOfflineService checkAndUpdateAllAvailablePackagesWithCompletionHandler:^(NSArray<NSString *> * _Nonnull updatedBIDs) {
  // callback
}];
```

#### 自定义配置预加载
使用自定义配置检查全量可更新的离线包并预加载离线包，回调可更新的业务 ID 列表。
**接口定义**
```objective-c
+ (void)checkAndUpdateAllAvailablePackagesWithOptions:(TMFWebOfflineServiceOptions *)options completionHandler:(void(^)(NSArray<NSString *> *updatedBIDs))completionHandler;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| options  | TMFWebOfflineServiceOptions | 可选配置 | YES    |

其中，TMFWebOfflineServiceOptions 的定义和实例化，请参见 [自定义离线包更新配置](#zdylxb)。

**completionHandler 回调**

| 参数      | 类型    | 描述                      | 必选 |
| --------- | ------- | ------------------------- | ---- |
| updatedBIDs | NSArray<NSString *>  | 可更新的离线包业务 ID 列表 | YES    |

**调用示例**
```objective-c
TMFWebOfflineServiceOptions *options = [TMFWebOfflineServiceOptions options];
options.ignoresFrequency = YES; 
[TMFWebOfflineService checkAndUpdateAllAvailablePackagesWithOptions:options completionHandler:^(NSArray<NSString *> * _Nonnull updatedBIDs) {
  // callback
}];
```

### 生效离线包
生效已经下载更新的离线包。
**接口定义**
```objective-c
+ (void)uncompressPackagesIfNeeded;
```
**调用示例**
```objective-c
[TMFWebOfflineService uncompressPackagesIfNeeded];
```

### 获取本地离线包的版本号
根据离线包业务 ID 获取本地离线包的版本号，未安装的话版本号为0。
**接口定义**
```objective-c
+ (int)localVersionForBID:(NSString *)BID;
```
**参数说明**

| 参数 | 类型     | 描述          | 必选 |
| ---- | -------- | ------------- | ---- |
| BID  | NSString | 离线包业务 ID | YES    |

**返回值**

| 类型 | 描述               |
| ---- | ------------------ |
| int  | 本地离线包的版本号 |

**调用示例**
```objective-c
[TMFWebOfflineService localVersionForBID:@"BID"];
```

### 移除本地离线包

#### 单业务 ID 移除本地离线包

根据离线包业务 ID 移除本地离线包。
**接口定义**
```objective-c
+ (void)removeLocalPackageWithBID:(NSString *)BID;
```

**参数说明**

| 参数 | 类型     | 描述          | 必选 |
| ---- | -------- | ------------- | ---- |
| BID  | NSString | 离线包业务 ID | YES    |

**调用示例**
```objective-c
[TMFWebOfflineService removeLocalPackageWithBID:@"BID"];
```

#### 多业务ID移除本地离线包
根据一组离线包业务 ID 移除本地离线包。
**接口定义**
```objective-c
+ (void)removeLocalPackageWithBIDs:(NSArray<NSString *> *)BIDs;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| BIDs  | NSArray<NSString *> | 离线包业务 ID 列表 | YES    |

**调用示例**
```objective-c
[TMFWebOfflineService removeLocalPackageWithBIDs:@[@"BID1",@"BID2"]];
```

#### 移除全部本地离线包
移除全部本地离线包。
**接口定义**
```objective-c
+ (void)removeAllLocalPackage;
```
**调用示例**
```objective-c
[TMFWebOfflineService removeAllLocalPackage];
```

### 注册调试日志输出回调
注册调试日志输出回调。 
**接口定义**
```objective-c
+ (void)registerLogger:(TMFWebOffline_Logger)logger;
```
**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| logger  | TMFWebOffline_Logger | 离线包日志输出器 | YES  |

其中，TMFWebOffline_Logger 的定义如下：
```objective-c
/**
 @brief 用于输出 SDK 调试 log 的回调
 */
typedef void(*TMFWebOffline_Logger)(TMFWebOfflineLoggerLevel level, const char* log);
```

关于日志等级以及详细的调试配置，请参见 [调试](#ts)。
**调用示例**
```objective-c
[TMFWebOfflineService registerLogger:loggerWebOffline];
```

### 注册运营统计回调
注册运营统计事件的回调。
**接口定义**
```objective-c
+ (void)registerReporter:(TMFWebOffline_Reporter)reporter;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| reporter  | TMFWebOffline_Reporter | 离线包运营统计上报回调 | YES   |

其中，TMFWebOffline_Reporter 的定义如下：
```objective-c
/**
 @brief 用于输出SDK统计事件的回调
 */
typedef void(*TMFWebOffline_Reporter)(NSString *event, NSDictionary *kvs);
```

关于日志等级以及详细的调试配置，请参见 [运营统计](#yytj)。
**调用示例**
```objective-c
[TMFWebOfflineService registerReporter:reporterWebOffline];
```

### 配置 WebView 容器的离线包处理

#### 创建离线包网络请求处理实例
根据 WebView 容器创建离线包网络请求处理实例。
**接口定义**
```objective-c
- (instancetype)initWithWebViewController:(UIViewController<TMFWebOfflineWebViewControllerProtocol> *)webViewController;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| webViewController  | UIViewController<TMFWebOfflineWebViewControllerProtocol> | WebView 容器实例 | YES   |

**调用示例**
```objective-c
// webView容器，实现TMFWebOfflineWebViewControllerProtocol协议
@interface TMFWebOfflineUIWebViewController () <UIWebViewDelegate, TMFWebOfflineWebViewControllerProtocol>
@property (nonatomic, strong) NSURL *URL;
@property (nonatomic, strong) UIWebView *webView;
@end

@implementation TMFWebOfflineUIWebViewController

@synthesize tmf_webOfflineHandler = _tmf_webOfflineHandler;

- (instancetype)initWithURL:(NSURL *)URL {
    self = [super init];
    if (self) {
      self.URL = URL;
      // webView容器实例化的同时，创建离线包网络请求处理实例
      self.tmf_webOfflineHandler = [[TMFWebOfflineHandler alloc] initWithWebViewController:self];
    }
    return self;
}

#pragma mark - TMFWebOfflineWebViewControllerProtocol
- (UIView *)tmf_webView {
    return self.webView;
}
@end
```

#### 处理 WebView 的网络请求
在 WebView 的网络请求的回调中转发离线包的网络处理请求。
**接口定义**
```objective-c
- (void)handleRequest:(NSURLRequest *)request;
```

**参数说明**

| 参数 | 类型     | 描述         | 必选 |
| ---- | -------- | ------------ | ---- |
| request  | NSURLRequest | WebView 的网络请求 | YES   |

**调用示例**
```objective-c
#pragma mark - UIWebViewDelegate
- (BOOL)webView:(UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType
{
    // Forward the request to WebOfflineHandler
    [self.tmf_webOfflineHandler handleRequest:request];
    
    return YES;
}
```

#### 离线包减持 WebView 容器
移除离线包对 WebView 容器的请求持有。
**接口定义**
```objective-c
- (void)clearWebViewController;
```

**调用示例**
```objective-c
- (void)dealloc {
    [self.tmf_webOfflineHandler clearWebViewController];
}
```

### 使用离线包
```objective-c
/// WEB_OFFLINE_TEST_URL_FORMAT => http://pimweb.cs0309.3g.qq.com/testAk/index.html?_bids=%@
NSURL *URL = [NSURL URLWithString:[NSString stringWithFormat:WEB_OFFLINE_TEST_URL_FORMAT, @"bid1+bid2"]];	
/// URL => http://pimweb.cs0309.3g.qq.com/testAk/index.html?_bids=bid1+bid2
TMFWebOfflineUIWebViewController *viewController = [[TMFWebOfflineWKWebViewController alloc] initWithURL:URL];
```
加载的本地 HTML 地址为:`Library/TMF/TMFWebOffline/webappCache2/bid1/pimweb.cs0309.3g.qq.com/testAk/index.html `。
>?`bid1` 和`bid2`中只能有一个主包。
>
### WkWebView 的使用注意事项
使用 TMFWkWebView 代替系统 WkWebview 解决页面 post 不正常的问题。

