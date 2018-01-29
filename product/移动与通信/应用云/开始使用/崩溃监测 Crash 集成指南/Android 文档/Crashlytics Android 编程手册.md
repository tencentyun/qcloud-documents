# 应用云 Crash 服务 Android 接入指南

## 启动 Crash 服务

要想使用 Crash 服务，您需要先启动 Crash 服务，我们建议您放在 Application 的 onCreate 方法中执行该操作，具体代码如下：

```
// 首先获取 TACCrashService 实例
TACCrashService crashService = TACCrashService.getInstance();

// 调用 start 接口启动 Crash 服务，context 这里最好是使用 application context。
crashService.start(context);
```

服务启动之后，会在应用程序崩溃后自动收集信息上报，不需要再另外配置。


## MultiDex 注意事项

如果使用了MultiDex，建议通过 Gradle 的 "multiDexKeepFile" 配置等方式把 Bugly 的类放到主 Dex，另外建议在 Application 类的 "attachBaseContext" 方法中主动加载非主 dex：

```
public class MyApplication extends SomeOtherApplication {
  @Override
  protected void attachBaseContext(Context base) {
     super.attachBaseContext(context);
     Multidex.install(this);
  }
}
```
