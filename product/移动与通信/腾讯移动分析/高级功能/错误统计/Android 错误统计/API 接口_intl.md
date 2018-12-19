For ease of use, the latest Crash module is encapsulated into the class StatCrashReporter to provide external service, and also compatible with the old API. For the convenience of management, it is recommended to replace the old API with the new one. For more information on API upgrade, please see the following.

### Java Crash Exception Capturing
```
void setJavaCrashHandlerStatus (boolean enable)
```

1. Description
Enable or disable java exception capturing. No traffic or performance is consumed during initialization. After this service takes effect, DefaultUncaughtExceptionHandler is registered. Information captured when crash occurs is stored locally and reported. You can add StatCrashCallback to monitor the occurrence of Crash.
2. Parameter
enable: Whether to enable java exception capturing. Default is true.
true: Enable
false: Disable
Corresponding get API: `getJavaCrashHandlerStatus()`
Location where API is called: This API is called when the App is initialized, for example, Application.onCreate or MainActivity.onCreate.
3. Example
```java
StatCrashReporter.getStatCrashReporter(getApplicationContext()).setJavaCrashHandlerStatus(true);
```

### Native Crash Exception Capturing
```
void setJniNativeCrashStatus (boolean enable)
```
1. Description
Enable or disable Native exception capturing. No traffic or performance is consumed during initialization. After this service takes effect, signal is registered on the native layer. Information captured when crash occurs is stored locally and reported. You can add StatCrashCallback to monitor the occurrence of Crash.
2. Parameter
enable: Whether to enable Native exception capturing. Default is false.
true: Enable
false: Disable
Corresponding get API: `getJniNativeCrashStatus ()`
Location where API is called: This API is called when the App is initialized, for example, Application.onCreate or MainActivity.onCreate.
3. Example
```java
StatCrashReporter.getStatCrashReporter(getApplicationContext()).setJniNativeCrashStatus(true);
```

### Monitoring the Occurrence of Crash

```
void addCrashCallback(StatCrashCallback cb)
```
1. Description
Add StatCrashCallback to monitor the occurrence of Crash for Java or Native
2. Parameter
Callback for StatCrashCallback when crash occurs.
```java
public interface StatCrashCallback {
// thread: Thread information of crash
// throwable: Stack information of crash
public abstract void onJavaCrash(Thread thread, Throwable throwable);
// nativeCrashStacks: The tombstone file for native crash
public abstract void onJniNativeCrash(String nativeCrashStacks);
}
```
Corresponding remove API: `removeCrashCallback(StatCrashCallback cb)`
Location where API is called: This API is called when the App is initialized, for example, Application.onCreate or MainActivity.onCreate.
3. Example
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

### Reporting Policy

When Crash occurs, exceptions are reported 3 seconds after the MTA is initialized at the next startup of App by default. This can be done via setReportDelaySecOnStart(int reportDelaySecOnStart). The value range is [0, 10*60] (in sec). You can also set real-time reporting by configuring setEnableInstantReporting. That is, report exceptions immediately if the network is available when crash occurs. If reporting fails, it will start at the next startup.

To help developers debug, real-time reporting policy is used under the Debug mode, that is, StatConfig.setDebugEnable is set to true.

### Multi-process Environment

In a multi-process environment, if you need to capture exceptions in multiple processes, you should initialize the MTA or Native Crash API in each process, which is recommended to be done when Application.onCreate is called.

### A Complete Example

In this example, major APIs will be called. You can call any of these APIs based on your needs.

```java
// Set appkey, the unique identifier of the application. You can apply for it on MTA official website, or configure it using Manifest.
// Be sure to replace the appkey with yours
StatConfig.setAppKey(app, "A91LM44JGFLV");
// Set release channel, i.e., App market, or configure using Manifest.
StatConfig.setInstallChannel(app, "MyApp");
StatService.setContext(app);
// Enable statistics of Mta
StatService.registerActivityLifecycleCallbacks(app);

StatCrashReporter crashReporter = StatCrashReporter.getStatCrashReporter(app);
// Enable real-time reporting when exception occurs
crashReporter.setEnableInstantReporting(true);
// Enable java exception capturing
crashReporter.setJavaCrashHandlerStatus(true);
// Enable Native c/c++, i.e. so exception capturing
// Add it as needed. Be sure to add so file
crashReporter.setJniNativeCrashStatus(true);

// Callback when crash occurs. You can add businesses based on your own needs
crashReporter.addCrashCallback(new StatCrashCallback() {

@Override
public void onJniNativeCrash(String tombstoneString) {
// Content of native dump, including exception signals, processes, threads, registers, stacks and other information
// For more information, please see Android native tombstone file format
log("MTA StatCrashCallback onJniNativeCrash:\n" + tombstoneString);
}

@Override
public void onJavaCrash(Thread thread, Throwable ex) {
// thread: Thread information of crash
// ex:crash stack
log("MTA StatCrashCallback onJavaCrash:\n", ex);
}
});
```

