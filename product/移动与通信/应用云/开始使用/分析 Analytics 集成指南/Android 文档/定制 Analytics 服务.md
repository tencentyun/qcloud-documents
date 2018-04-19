通常我们的服务都是按照默认配置自动启动的，您不需要关心配置的细节。但您也可以通过修改服务配置，定制 Analytics 服务。

## 如何修改服务配置

### 在 `Application` 子类中添加代码

如果您自己的应用中已经有了 `Application` 的子类，请重载它的 `attachBaseContext(Context)` 方法，在里面添加配置代码，如果没有，请自创建一个 `Application` 的子类。如：

```
public class MyCustomApp extends Application {
  @Override
  protected void attachBaseContext(Context base) {
		super.attachBaseContext(base);
    	// 实例化一个新的配置
		TACApplicationOptions applicationOptions = TACApplicationOptions.newDefaultOptions(this);

		// 获取 Options
		TACAnalyticsOptions analyticsOptions = applicationOptions.sub("analytics");
		
		// 这里是设置行为统计数据上报的策略为实时上报
		analyticsOptions.strategy(TACAnalyticsStrategy.INSTANT);
		
		// 修改其他配置
		... 

		// 让自定义设置生效
		TACApplication.configureWithOptions(this, applicationOptions);
  }
}
```

>**注意：**
>configureWithOptions 只能被调用一次，如果您有多个服务的配置需要修改，请全部修改好再调用 configureWithOptions，让配置生效。

### 在 `AndroidManifest.xml` 文件中注册

在创建好 `Application` 的子类并添加好代码后，您需要在工程的 `AndroidManifest.xml` 文件中注册该 `Application` 类：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.example.tac">
  <application
    <!-- 这里替换成你自己的 Application 子类 -->
    android:name="com.example.tac.MyCustomApp"
    ...>
  </application>
</manifest>
```

>**注意：**
>如果您的 `Application` 子类已经在 `AndroidManifest.xml` 文件中注册，请不要重复注册。


## 定制 Analytics 服务

我们提供了一些高级配置项，您可以通过这些配置项定制化您的 Analytics 服务。

### 获取 Options

通过服务名 `analytics` 可以从 `TACApplicationOptions` 获取 Analytics 的配置 Options：

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");
```


### 设置数据上报策略

Analytics 有多种上报策略，您可以根据需要选择：

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");
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
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");
// 设置为当消息数量达到 50 条时发送一次
tacAnalyticsOptions.minBatchReportCount(50);
```

如果您使用 `PERIOD` 上报策略，那么您可以通过 `sendPeriodMillis` 方法设置发送时间间隔，默认为 3 小时：

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");
// 设置为发送时间间隔为 1 小时，单位是 ms
tacAnalyticsOptions.sendPeriodMillis(60 * 60 * 1000); 
```

如果您希望在 WIFI 下立即发送，而在其他网络情况下使用您设置好的策略，可以开启智能发送策略：

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.setWifiInstantSendEnabled(true);
```


### 设置会话超时时长

设置会话超时时长，默认 30 秒，时长内回到应用的用户视为同一次会话。

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.sessionTimeoutMillis(50000); // 单位是ms
```

### 设置渠道

通常我们建议您在 AndroidManifest 中设置 `com.tencent.tac.channel` 元数据的方式配置渠道，但您也可以在代码中手动设置。

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.setChannel("your channel");
```

### 关闭自动统计页面访问

默认情况下我们会自动统计您的页面访问历史，您不需要关心。如果您想要完全手动统计所有的页面访问，您可以关闭这个选项。

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.setAutoTrackPageViewEnabled(false);
```

### 多进程支持

设置是否开启多进程的支持，默认开启。对于多进程并发，需要开启本配置，否则可能会出现数据库读写异常。

```
TACApplicationOptions tacApplicationOptions = TACApplication.options();
TACAnalyticsOptions tacAnalyticsOptions = tacApplicationOptions.sub("analytics");

tacAnalyticsOptions.multiProcess(true);
```