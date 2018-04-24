通常我们的服务都是按照默认配置自动启动的，您不需要关心配置的细节。但您也可以通过修改服务配置，定制 Analytics 服务。

## 如何修改服务配置

### 在 `AppDelegate` 中添加代码

您可能也有需求在程序运行时，去改变一些特定的参数来改变程序的行为。为了支持您的这种需求，我们增加了修改程序配置的接口，您可以仿照如下形式来修改移动开发平台（MobileLine）的配置。

Objective-C 代码示例：
~~~
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
// 自定义配置
// options.analyticsOptions.xxx = xxx;
[TACApplication configurateWithOptions:options];
~~~

Swift 代码示例：
~~~
let options = TACApplicationOptions.default()
// 自定义配置
// options?.analyticsOptions.xxx = xxx
TACApplication.configurate(with: options)
~~~

## 定制 Analytics 服务

我们提供了一些高级配置项，您可以通过这些配置项定制化您的 Analytics 服务。

### 获取 Options

通过方法 `analyticsOptions` 可以从 `TACApplicationOptions` 获取 Analytics 的配置 Options：

Objective-C 代码示例：
```
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
options.analyticsOptions;
```

Swift 代码示例：
```
let options = TACApplicationOptions.default()
options?.analyticsOptions
```

### 设置数据上报策略

Analytics 有多种上报策略，您可以根据需要选择：

Objective-C 代码示例：
```
options.analyticsOptions.strategy = TACAnalyticsStrategyInstant;
```

Swift 代码示例：
```
options?.analyticsOptions.strategy = TACAnalyticsStrategy.instant
```
每种上报策略的说明如下：

| 编号	| 策略名称	|  说明 | 
| :---: | :----: | :---- |
| 1	| TACAnalyticsStrategyInstant	| 实时发送，APP 每产生一条消息都会发送到服务器。| 
| 2	| TACAnalyticsStrategyOnlyWifi	| 只在 WIFI 状态下发送，非 WIFI 情况缓存到本地。| 
| 3	| TACAnalyticsStrategyBatch	| 批量发送，默认当消息数量达到 30 条时发送一次。| 
| 4	| TACAnalyticsStrategyLaunch	| 只在启动时发送，本次产生的所有数据在下次启动时发送。| 
| 5	| TACAnalyticsStrategyDeveloper	| 开发者模式，开发者在代码中主动调用发送行为.| 
| 6	| TACAnalyticsStrategyPeriod	| 间隔一段时间发送，每隔一段时间一次性发送到服务器。默认24小时| 
| 7| TACAnalyticsStrategyOnlyWifiWithoutCache	| 仅在WIFI网络下发送, 发送失败以及非WIFI网络情况下不缓存数据 | 
| 8	| TACAnalyticsStrategyBatchPeriodWithoutCache	| 不缓存数据，批量上报+间隔上报组合。适用于上报特别频繁的场景。| 

如果您使用 `BATCH` 上报策略，那么您可以通过 `minBatchReportCount` 方法设置最小批量发送消息个数，默认是 30 条：

Objective-C 代码示例：
```
options.analyticsOptions.minBatchReportCount = 30;
```

Swift 代码示例：
```
options?.analyticsOptions.minBatchReportCount = 30
```

如果您使用 `PERIOD` 上报策略，那么您可以通过 `sendPeriodMillis` 方法设置发送时间间隔，默认为 3 小时：

Objective-C 代码示例：
```
options.analyticsOptions.sendPeriodMillis = 10000;
```

Swift 代码示例：
```
options?.analyticsOptions.sendPeriodMillis = 10000
```

如果您希望在 WIFI 下立即发送，而在其他网络情况下使用您设置好的策略，可以开启智能发送策略：

Objective-C 代码示例：
```
options.analyticsOptions.strategy = TACAnalyticsStrategyOnlyWifi;
```

Swift 代码示例：
```
options?.analyticsOptions.strategy = TACAnalyticsStrategy.onlyWifi
```

### 设置会话超时时长

设置会话超时时长，默认 30 秒，时长内回到应用的用户视为同一次会话。

Objective-C 代码示例：
```
options.analyticsOptions.sessionTimeoutMillis = 30000;
```

Swift 代码示例：
```
options?.analyticsOptions.sendPeriodMillis = 30000
```

### 关闭自动统计页面访问

默认情况下我们会自动统计您的页面访问历史，您不需要关心。如果您想要完全手动统计所有的页面访问，您可以关闭这个选项。

Objective-C 代码示例：
```
options.analyticsOptions.autoTrackPageEvents = NO;
```

Swift 代码示例：
```
options?.analyticsOptions.autoTrackPageEvents = false
```
