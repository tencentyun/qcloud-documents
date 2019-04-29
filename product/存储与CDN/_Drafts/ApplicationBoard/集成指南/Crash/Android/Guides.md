# 应用云 Crash 服务 Android 接入指南

## 启动 Crash 服务

要想使用 Crash 服务，您需要先启动 Crash 服务，我们建议您放在 Application 的 onCreate 方法中执行该操作。具体代码如下：

```
// 首先获取 TACCrashService 实例
TACCrashService crashService = TACCrashService.getInstance();

// 调用 start 接口启动 Crash 服务，context 这里最好是使用 application context。
crashService.start(context);
```

服务启动之后，会在应用程序崩溃后自动收集信息上报，您不需要再另外配置。


## 添加自定义日志

要为导致崩溃的事件提供更多背景信息，您可以将自定义 Crash 日志添加到您的应用。Crash 会将日志与您的崩溃数据相关联，并在控制台中显示这些日志。

```
crashService.log(TACCrashLogLevel.DEBUG, "payment", "user clicked secret buttom");
```

## 添加自定义键

自定义键可以帮助您获取导致崩溃的应用的特定状态。您可以将任意键/值对与您的崩溃报告相关联，然后在控制台中查看这些键/值对。

```
String key = "userName";
String value = "xiaoming";
crashService.putUserData(context, key, value)
```

## 设置用户 ID

要诊断某个问题，了解哪些用户遇到了特定的崩溃通常很有帮助。Crash 提供了一种在崩溃报告中以匿名方式标识用户的方法。

要将用户 ID 添加到报告中，请以 ID 编号、令牌或哈希值的形式为每个用户分配一个唯一标识符：

```
String userId = "#123456"
crashService.setUserId(context, userId);
```

## MultiDex注意事项

如果使用了MultiDex，建议通过Gradle的“multiDexKeepFile”配置等方式把Bugly的类放到主Dex，另外建议在Application类的"attachBaseContext"方法中主动加载非主dex：

```
public class MyApplication extends SomeOtherApplication {
  @Override
  protected void attachBaseContext(Context base) {
     super.attachBaseContext(context);
     Multidex.install(this);
  }
}
```
