### 功能介绍

使用这些函数可以动态调整 App 和 SDK 的相关设置。

### Android App 接口设置

1.会话时长（默认 30000ms，30000ms 回到应用的用户视为同一次会话）
```
void StatConfig.setSessionTimoutMillis(int sessionTimoutMillis)
```
2.消息失败重发次数（默认 3）
```
void StatConfig.setMaxSendRetryCount(int maxSendRetryCount)
```
3.用户自定义时间类型事件的最大并行数量（默认 1024）
```
void StatConfig.setMaxParallelTimmingEvents(int max)
```

4.设置安装渠道
```
void StatConfig.setInstallChannel(String installChannel)
```
5.设置 App Key
```
void StatConfig.setAppKey(Context ctx, String appkey)
```
6.设置统计功能开关（默认为 true）
```
void StatConfig.setEnableStatService(boolean enableStatService)
```
如果为 false，则关闭统计功能，不会缓存或上报任何信息。
7.设置 session 内产生的消息数量（默认为 0，即无限制）
```
void StatConfig.setMaxSessionStatReportCount(int maxSessionStatReportCount)
```
若为 0，则不限制；若大于 0，每个 session 内产生的消息数量不会超过此值；若超过了，新产生的消息将会被丢弃。

8.设置每天/每个进程时间产生的会话数量（默认为 20）
为防止开发者调用 MTA 不合理导致上报大量的会话数量（session），SDK 默认每天/每个进程时间内最多产生的会话数量，当达到此值时，SDK 不再产生并上报新的会话。当进程重启或跨天时，会被清 0。
```
void StatConfig.setMaxDaySessionNumbers (int maxDaySessionNumbers)
```
9.设置单个事件最大长度（默认为 4k，单位：bytes）
为防止上报事件长度过大导致用户流量增加，SDK 默认不上报超过 4k 的单个事件；对于错误异常堆栈事件，异常堆栈长度不超过 100（可以超过 4k）。
```
void StatConfig.setMaxReportEventLength (int maxReportEventLength)
```
10.支持多进程（默认为 false）
同一个 App 多个进程同时使用 MTA，请参考注意事项中的“多进程支持”。
```
void StatConfig.setEnableConcurrentProcess(boolean enableConcurrentProcess)
```

### iOS App 接口设置

1.使用 MTAConfig 单例对象属性设置可以动态调整 App 和 SDK 的相关设置，调用形式为：

```
[[MTAConfig getInstance] setPropertyName:value];
```
2.会话时长（默认 30s，离开应用 30 秒之后再回来，视为一次新的会话）

```
@property uint32_t sessionTimeoutSecs
```
3.消息失败重发次数（默认 3）

```
@property uint32_t maxSendRetryCount
```
4.用户自定义时间类型事件的最大并行数量（默认 1024）

```
@property uint32_t maxParallelTimingEvents
```
5.设置安装渠道(默认为 appstore)

```
@property (nonatomic, retain) NSString* channel
```
6.设置App Key

```
@property (nonatomic, retain) NSString* appkey
```
7.设置统计功能开关（默认为 true）

```
@property BOOL statEnable
```
如果为 false，则关闭统计功能，不会缓存或上报任何信息，设置 session 内发送消息限制（默认为 0，即无限制）。
```
@property int32_t maxSessionStatReportCount
```
若为 0，则不限制 session 内发送消息的个数；若大于 0，每个 session 内发送的消息不会超过此值；若超过了，新产生的消息将会被丢弃。
