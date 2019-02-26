### 上报策略基础介绍
设置数据上报策略，可以有效节省流量，使用以下 3 种方式调整 App 的数据上报策略：
1.App 启动时指定上报策略（默认为 MTA_STRATEGY_APP_LAUNCH）  

```
@property MTAStatReportStrategy reportStrategy
```
腾讯移动分析目前支持的上报策略包括 6 种：

|编号            |策略名称        |说明    |
|:-------------:|:-------------:|-----|
|1 | MTA_STRATEGY_INSTANT| 实时发送，App 每产生一条消息都会发送到服务器。|
|2 | MTA_STRATEGY_ONLY_WIFI|只在 WiFi 状态下发送，非 WiFi 情况缓存到本地。|
|3 | MTA_STRATEGY_BATCH|批量发送，默认当消息数量达到 30 条时发送一次。 |
|4|MTA_STRATEGY_APP_LAUNCH |只在启动时发送，本次产生的所有数据在下次启动时发送。 |
|5 |MTA_STRATEGY_DEVELOPER |开发者模式，只在 App 调用 void commitEvents(Context) 时发送，否则缓存消息到本地。 |
|6|MTA_STRATEGY_PERIOD |间隔一段时间发送，每隔一段时间一次性发送到服务器。|

SDK 默认为 MTA_STRATEGY_APP_LAUNCH + wifi 下实时上报，对于响应要求比较高的应用，比如竞技类游戏可关闭 WiFi 实时上报，并选择 MTA_STRATEGY_APP_LAUNCH或MTA_STRATEGY_PERIOD 上报策略。
2.考虑到 WiFi 上报数据的代价比较小，为了更及时获得用户数据，SDK 默认在 WiFi 网络下实时发送数据，可以调用下面的接口禁用此功能（在 WiFi 条件下仍使用原定策略）。

```
@property BOOL smartReporting
```
3.通过在 Web 界面配置，开发者可以在线更新上报策略，替换 App 内原有的策略，App 下次启动时会自动生效并存储该策略。

上面 3 种方式的优先级依次递增。例如，WiFi 下转为实时发送会优先于第 1 种方式中选定的任何策略执行，在 Web 界面上配置的策略会覆盖 App 本地已经生效的策略。

### 数据上报相关的设置
1.设置最大缓存未发送消息个数（默认 1024）。
```
@property uint32_t maxStoreEventCount
```

缓存消息的数量超过阈值时，最早的消息会被丢弃。
2.（仅在发送策略为 MTA_STRATEGY_BATCH 时有效）设置最大批量发送消息个数（默认 30）。

```
@property uint32_t minBatchReportCount
```
3.（仅在发送策略为 PERIOD 时有效）设置间隔时间（默认为 24*60，即 1 天）。

```
@property uint32_t sendPeriodMinutes
```