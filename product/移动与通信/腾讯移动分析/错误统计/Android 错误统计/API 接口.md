为了方便使用，最新的 Crash 模块统一封装成类 StatCrashReporter 对外提供服务，同时兼容旧的接口。为了方便管理，建议以新的 API 调用替换旧的接口，具体的 API 升级见下文。

### Java Crash 异常捕获
```
void setJavaCrashHandlerStatus (boolean enable)
```

1. 说明
开启或禁用 java 异常捕获，初始化不会带来任何的流量和性能消耗，生效后会注册 DefaultUncaughtExceptionHandler，crash 时捕获相关信息存储在本地并上报，可通过添加 StatCrashCallback 监听 Crash 发生。
2. 参数
enable：是否开启java异常捕获，默认开启；
true：开启；
false：禁用；
对应的 get 接口：`getJavaCrashHandlerStatus()`；
调用位置：App 初始化时调用，比如 Application.onCreate 或 MainActivity.onCreate。
3. 示例
```java
StatCrashReporter.getStatCrashReporter(getApplicationContext()).setJavaCrashHandlerStatus(true);
```

### Native Crash 异常捕获
```
void setJniNativeCrashStatus (boolean enable)
```
1. 说明
开启或禁用 Native 异步捕获，初始化不会带来任何的流量和性能消耗。生效后会注册 signal 到 native 层，crash 时捕获相关信息存储在本地并上报，可通过添加 StatCrashCallback 监听 Crash 发生。
2. 参数
enable：是否开启 Native 异常捕获，默认为 false；
true：开启；
false：禁用；
对应的 get 接口：`getJniNativeCrashStatus ()`；
调用位置：App 初始化时调用，比如 Application.onCreate 或 MainActivity.onCreate。
3. 示例
```java
StatCrashReporter.getStatCrashReporter(getApplicationContext()).setJniNativeCrashStatus(true);
```

### 监听 Crash 发生

```
void addCrashCallback(StatCrashCallback cb)
```
1. 说明
添加 StatCrashCallback 监听 Java 或 Native 的 Crash 发生。
2. 参数
StatCrashCallback crash 发生时的 StatCrashCallback 回调。
```java
public interface StatCrashCallback {
// thread：crash的线程信息
// throwable：crash的堆栈信息
public abstract void onJavaCrash(Thread thread, Throwable throwable);
// nativeCrashStacks：native crash的tombstone格式文件
public abstract void onJniNativeCrash(String nativeCrashStacks);
}
```
对应的 remove 接口：`removeCrashCallback(StatCrashCallback cb)`；
调用位置：App 初始化时调用，比如 Application.onCreate 或 MainActivity.onCreate。
3. 示例
```java
StatCrashReporter.getStatCrashReporter(getApplicationContext()).addCrashCallback(
new StatCrashCallback() {
@Override
public void onJniNativeCrash(String nativeCrashStacks) { // native crash happened
// do something
}
@Override
public void onJavaCrash(Thread thread, Throwable ex) {// java crash happened
// do something
}
});
```

### 上报策略

Crash 产生时，默认下次 App 启动时初始化 MTA 后的 3 秒开始上报，可通过 setReportDelaySecOnStart(int reportDelaySecOnStart) ，reportDelaySecOnStart 的单位为秒，范围 [0, 10*60]，也可以通过设置 setEnableInstantReporting 设置实时上报，即 crash 时有网络的条件下尽量立即上报，若上报失败，则下次启动时上报。

为方便开发者调试，在 Debug 模式，即 StatConfig.setDebugEnable(true)，采用实时上报策略。

### 多进程环境

在多进程环境中，若需要在多个进程捕获异常，需要在每个进程都初始化 MTA 或 Native Crash 接口，建议在 Application.onCreate 进行。

### 一个完整的示例

示例包括以上主要 API 调用，请根据需要自行决定调用哪些 API。

```java
// 设置appkey，应用的唯一标识，在MTA官网申请得到，也可通过Manifest配置
// 记得把以下appkey替换成自己的
StatConfig.setAppKey(app, "A91LM44JGFLV");
// 设置投放渠道，即应用市场，也可通过Manifest配置
StatConfig.setInstallChannel(app, "应用宝");
StatService.setContext(app);
// 这个是开启Mta的统计功能
StatService.registerActivityLifecycleCallbacks(app);

StatCrashReporter crashReporter = StatCrashReporter.getStatCrashReporter(app);
// 开启异常时的实时上报
crashReporter.setEnableInstantReporting(true);
// 开启java异常捕获
crashReporter.setJavaCrashHandlerStatus(true);
// 开启Native c/c++，即so的异常捕获
// 请根据需要添加，记得so文件
crashReporter.setJniNativeCrashStatus(true);

// crash时的回调，业务可根据需要自选决定是否添加
crashReporter.addCrashCallback(new StatCrashCallback() {

@Override
public void onJniNativeCrash(String tombstoneString) {
// native dump内容，包含异常信号、进程、线程、寄存器、堆栈等信息
// 具体请参考：Android原生的tombstone文件格式
log("MTA StatCrashCallback onJniNativeCrash:\n" + tombstoneString);
}

@Override
public void onJavaCrash(Thread thread, Throwable ex) {
//thread:crash线程信息
// ex:crash堆栈
log("MTA StatCrashCallback onJavaCrash:\n", ex);
}
});
```
