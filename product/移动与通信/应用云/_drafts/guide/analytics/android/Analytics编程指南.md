
## 启动服务实例

Analytics 服务在使用前必须先启动，我们建议你放在 Application 的 onCreate 方法中执行该操作。

您可以调用 start(Context) 方法将启动 Analytics 服务：

```
TACAnalyticsService.getInstance().start(this);
```

## 上报页面访问

Analytics 默认会统计所有的页面访问，你不需要另外配置，如果需要手动上报页面访问，可以调用：

```
// 页面访问开始
TACAnalyticsService.getInstance().trackPageAppear(context, pageName);

// 页面访问结束
TACAnalyticsService.getInstance().trackPageDisappear(context, pageName);
```

## 上报自定义事件

自定义事件分为两种，单次事件和持续事件。普通事件是指单次事件，而持续事件除了事件本身的属性外，包含了事件的开始和结束时间。

上报单次事件，可以调用：

```
TACAnalyticsService.getInstance().trackEvent(context, TACAnalyticsEvent);

```

上报持续事件，可以调用：

```
// 事件开始
TACAnalyticsService.getInstance().trackEventDurationBegin(context, TACAnalyticsEvent);

// 事件结束
TACAnalyticsService.getInstance().trackEventDurationEnd(context, TACAnalyticsEvent);

// 指定时间时长
TACAnalyticsService.getInstance().trackEventDuration(context, TACAnalyticsEvent, duration);
```

## 会话统计

会话统计用于统计启动次数，由 SDK 本身维护，通常开发者无需额外设置或调用接口。

以下3种情况下，会视为用户打开一次新的会话：

1. 应用第一次启动，或者应用进程在后台被杀掉之后启动

2. 应用退到后台或锁屏超过一定时间之后再次回到前台，默认是 30 秒，你也可以根据业务需要修改。

3. 调用 SDK 提供的startNewSession()函数

```
void TACAnalyticsService.getInstance().exchangeNewSession(Context context)
```

## 定制 Analytics 服务

我们提供了一些高级配置项，您可以通过这些配置项定制化您的 Analytics 服务。
> **注意:**
> 您需要在启动服务前完成配置。

### 获取 Options

```
final TACApplicationOptions tacApplicationOptions = TACApplication.options();
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");
```

### 设置会话超时时长

设置会话超时时长，默认 30 秒，时长内回到应用的用户视为同一次会话。

```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

// 单位是ms
tacAnalyticsOptions.sessionTimeoutMillis(50000);
```

### 设置渠道

通常我们建议您在 AndroidManifest 中设置 `com.tencent.tac.channel` 元数据的方式配置渠道，但您也可以在代码中手动设置。

```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.setChannel("channel");
```

### 多进程支持

设置是否开启多进程的支持，默认**开启**。对于多进程并发，需要开启本配置，否则可能会出现数据库读写异常。

```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.multiProcess(true);
```

### 自动统计页面访问

默认情况下我们会自动统计您的页面访问历史，您不需要关心。如果您关闭了这个选项，您必须完全手动统计所有的页面访问。

```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.setAutoTrackPageViewEnabled(false);
```

### 数据上报策略

Analytics 有多种上报策略，您可以根据需要选择：

```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

// 上报策略设置为立即发送
tacAnalyticsOptions.strategy(TACAnalyticsStrategy.INSTANT);
```

每种上报策略的说明如下：

| 编号	| 策略名称	|  说明 | 
| :---: | :----: | :---- |
| 1	| INSTANT	| 实时发送，APP 每产生一条消息都会发送到服务器。| 
| 2	| ONLY_WIFI	| 只在 WIFI 状态下发送，非 WIFI 情况缓存到本地。| 
| 3	| BATCH	| 批量发送，默认当消息数量达到 30 条时发送一次。| 
| 4	| APP_LAUNCH	| 只在启动时发送，本次产生的所有数据在下次启动时发送。| 
| 5	| DEVELOPER	| 开发者模式，只在手动调用 `sendEvents(Context)` 时发送，否则缓存消息到本地。| 
| 6	| PERIOD	| 间隔一段时间发送，每隔一段时间一次性发送到服务器。| 

如果您使用 `BATCH` 上报策略，那么您可以通过 `minBatchReportCount` 方法设置最小批量发送消息个数，默认是 30 条：
 
```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

// 设置为当消息数量达到 50 条时发送一次
tacAnalyticsOptions.minBatchReportCount(50);
```

如果您使用 `PERIOD` 上报策略，那么您可以通过 `sendPeriodMillis` 方法设置发送时间间隔，默认为 3 小时：

```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

// 设置为发送时间间隔为 1 小时，单位是 ms
tacAnalyticsOptions.sendPeriodMillis(60 * 60 * 1000);
```

如果您希望在 WIFI 下立即发送，而在其他网络情况下使用您设置好的策略，可以开启智能发送策略：

```
final TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.setWifiInstantSendEnabled(true);
```
