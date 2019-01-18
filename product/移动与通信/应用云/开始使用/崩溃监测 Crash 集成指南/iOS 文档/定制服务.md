我们提供了一些高级配置项，您可以通过这些配置项定制您的 Crash 服务。
>**注意：**
>您需要在启动服务前完成配置。

## 获取 Options

Objective-C 代码示例：
```
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
TACCrashOptions* crashOptions = options.crashOptions;
```
Swift 代码示例：
```
let options = TACApplicationOptions.default()
let crashOptions = options?.crashOptions
```
## 过滤崩溃数据

如果不希望崩溃数据中包含某个第三方库的数据（例如搜狗输入法，SogouInputIPhone.dylib）的话，您可通过设置过滤关键字的形式将其去掉。

Objective-C 代码示例：
```
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
TACCrashOptions* crashOptions = options.crashOptions;
NSArray* excludeModuleFilters = @[@"SogouInputIPhone.dylib"];
crashOptions.excludeModuleFilters = excludeModuleFilters;
```
Swift 代码示例：
```
let options = TACApplicationOptions.default()
let crashOptions = options?.crashOptions
let excludeModuleFilters = ["SogouInputIPhone.dylib"]
crashOptions?.excludeModuleFilter = excludeModuleFilters      
```

## 设置 Crash 委托回调
您可以通过设置 delegate 来提供更多的信息以辅助定位分析问题：

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


## 关闭 Crash 上报

如果您引入了多个崩溃检测服务，可能不希望启动该模块，请在程序中设置为 NO（默认为 YES）。

Objective-C 代码示例：
```
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
TACCrashOptions* crashOptions = options.crashOptions;
crashOptions.enable = NO;
```
Swift 代码示例：
```
let options = TACApplicationOptions.default()
let crashOptions = options?.crashOptions
crashOptions?.enable = false
```
## 开启或者关闭卡顿监控

卡顿监控可以监控应用内的卡顿情况，并进行上报。如果希望开启或者关闭的话，可以直接设置对应的属性实现：

Objective-C 代码示例：
```
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
TACCrashOptions* crashOptions = options.crashOptions;
//设置为 YES 开启卡顿监控
crashOptions.blockMonitorEnable = YES;
```
Swift 代码示例：
```
let options = TACApplicationOptions.default()
let crashOptions = options?.crashOptions
//设置为 YES 开启卡顿监控
crashOptions?.blockMonitorEnable = true
```
## 更多设置

更多设置信息可以直接参考 TACCrashOptions.h 头文件中的注释。
