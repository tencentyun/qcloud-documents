

## 服务启动与停止

当您集成了 Crashlytics 服务之后，系统将会在程序启动的时候自动启动服务。

如果您不希望在启动的时候默认启动 Crashlytics 服务，您可以在配置中设置关掉 (例如在 AppDelegate 中加入如下代码)：

Objective-C 代码示例：
~~~
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
options.crashOptions.enable = NO;
~~~

Swift 代码示例：
~~~
let options = TACApplicationOptions.default()
options?.crashOptions.enable = false
~~~
## 设置 Crashlytics 委托

> 您可以通过设置 delegate 来提供更多的信息以辅助定位分析问题

Objective-C 代码示例：
~~~
[TACCrashService shareService].delegate = <#the instance of TACCrashServiceDelegate#>
~~~
Swift 代码示例：
~~~
TACCrashService.share().delegate = <#the instance of TACCrashServiceDelegate#>
~~~

其中协议 TACCrashServiceDelegate 实现拥有以下接口：

~~~
@optional
/**
 当放生异常的时候，需要附带上的环境信息。您可以通过该接口提供更多的信息以辅助您定位问题。

 @param service 当前的Crash服务实例
 @param exception 异常信息
 */
- (NSString*) crashService:(TACCrashService*)service  attachmentForException:(NSException*)exception;
~~~

## 手动上报异常

~~~
/**
 上报异常信息

 @param exception 异常
 */
- (void) reportException:(NSException*)exception;

~~~

## 定制崩溃服务

### 开启卡顿监控

卡顿监控用于监控主线程卡顿问题，默认关闭。

Objective-C 代码示例：
~~~

/**
 *  卡顿监控开关，默认关闭
 */
 options.crashOptions.blockMonitorEnable = YES;
~~~

Swift 代码示例：
~~~

/**
 *  卡顿监控开关，默认关闭
 */
 options?.crashOptions.blockMonitorEnable = true
~~~
## 用户策略行为

### 设置标签
自定义标签，用于标明 App 的某个“场景”。在发生 Crash 时会显示该 Crash 所在的“场景”，以最后设置的标签为准，标签 id 需大于 0 。例：当用户进入界面 A 时，打上 9527 的标签：

Objective-C 代码示例：
```
[TACCrashService shareService].userSenceTag =999;
```

Swift 代码示例：
```
TACCrashService.share().userSenceTag = 999
```
打标签之前，需要在 Bugly 产品页配置中添加标签，取得标签 ID 后在代码中上报。

### 设置自定义Map参数

自定义 Map 参数可以保存发生 Crash 时的一些自定义的环境信息。在发生 Crash 时会随着异常信息一起上报并在页面展示。

Objective-C 代码示例：
```
[[TACCrashService shareService] setUserValue:@"value" forKey:@"key"];
```

Swift 代码示例：
```
TACCrashService.share().setUserValue("value", forKey: "key")
```

最多可以有 9 对自定义的 key-value（超过则添加失败）；
key 限长 50 字节，value 限长 200 字节，过长截断；
key 必须匹配正则：[a-zA-Z[0-9]]+。


## 其他功能

其他功能请参考 TACCrashService.h 中的定义。
