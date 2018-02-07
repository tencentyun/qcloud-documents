# 应用云 Crashlytics Android 编程手册

## 启动 Crash 服务

要想使用 Crash 服务，您需要先启动 Crash 服务，我们建议您放在 Application 的 onCreate 方法中执行该操作，具体代码如下：

```
// 首先获取 TACCrashService 实例
TACCrashService crashService = TACCrashService.getInstance();

// 调用 start 接口启动 Crash 服务，context 这里最好是使用 application context。
crashService.start(context);
```

服务启动之后，会在应用程序崩溃后自动收集信息上报，不需要再另外配置。**为了数据正确，请在主线程启动服务。**


## MultiDex 注意事项

如果使用了MultiDex，建议通过 Gradle 的 "multiDexKeepFile" 配置等方式把 Crash 的类放到主 Dex，另外建议在 Application 类的 "attachBaseContext" 方法中主动加载非主 dex：

```
public class MyApplication extends SomeOtherApplication {
  @Override
  protected void attachBaseContext(Context base) {
     super.attachBaseContext(context);
     Multidex.install(this);
  }
}
```

## 增加上报进程控制

如果App使用了多进程且各个进程都会初始化Crash（例如在Application类onCreate()中初始化Crash），那么每个进程下都会进行数据上报，造成不必要的资源浪费。

你可以通过以下方法控制只在主线程上报数据，首先通过以下方法获取当前进程是否为主进程：

```
public boolean isMainProcess() {
		ActivityManager am = ((ActivityManager) getSystemService(Context.ACTIVITY_SERVICE));
		List<ActivityManager.RunningAppProcessInfo> processInfos = am.getRunningAppProcesses();
		String mainProcessName = getPackageName();
		int myPid = android.os.Process.myPid();
		for (ActivityManager.RunningAppProcessInfo info : processInfos) {
			if (info.pid == myPid && mainProcessName.equals(info.processName)) {
				return true;
			}
		}
		return false;
	}
```

然后，在你启动服务的地方，加上进程的判断：

```
if (isMainProcess()) {
	crashService.start(context);
}
```

## 模拟异常

您可以通过以下方法主动触发异常，以便测试SDK是否正常工作。

```
// 模拟java异常
TACCrashSimulator.testJavaCrash();

// 模拟ANR异常
TACCrashSimulator.testANRCrash();

// 模拟Native异常
TACCrashSimulator.testNativeCrash();
```


## 定制 Crash 服务

我们提供了一些高级配置项，您可以通过这些配置项定制化您的 Crash 服务。**请注意，您需要在启动服务前完成配置。**

### 获取 Options

```
final TACApplicationOptions tacApplicationOptions = TACApplication.options();
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
```

### 设置上报延时时间

Crash 会在启动10s后联网同步数据。若您有特别需求，可以修改这个时间。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.setReportDelay(20000);   //改为20s
```

### 设置Crash回调

您可以设置 Crash 发生时的回调，回调返回的数据将伴随 Crash 一起上报到 Crash 平台，并展示在附件中：

Crash 回调类的定义如下：

```
public interface TACCrashHandleCallback {

    public static final int CRASHTYPE_JAVA_CRASH = 0; // Java crash
    public static final int CRASHTYPE_JAVA_CATCH = 1; // Java caught exception
    public static final int CRASHTYPE_NATIVE = 2; // Native crash
    public static final int CRASHTYPE_U3D = 3; // Unity error
    public static final int CRASHTYPE_ANR = 4; // ANR
    public static final int CRASHTYPE_COCOS2DX_JS = 5; // Cocos JS error
    public static final int CRASHTYPE_COCOS2DX_LUA = 6; // Cocos Lua error


    /**
     * 处理 Crash ，并上传自定义 key-values
     *
     * @param crashType Crash 类型
     * @param errorCode 错误码
     * @param errorMessage 错误信息
     * @param errorStack 错误堆栈
     * @return 需要上传给控制台的信息
     */
    Map<String, String> onCrashUploadKeyValues(int crashType, String errorCode, String errorMessage, String errorStack);

    /**
     * 处理 Crash ，并上传自定义二进制文件
     *
     * @param crashType Crash 类型
     * @param errorCode 错误码
     * @param errorMessage 错误信息
     * @param errorStack 错误堆栈
     * @return 需要上传给控制台的信息
     */
    byte[] onCrashUploadBinary(int crashType, String errorCode, String errorMessage, String errorStack) ;

}
```

设置方法如下：

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.setHandleCallback(new TACCrashHandleCallback() {
            @Override
            public Map<String, String> onCrashUploadKeyValues(int crashType, String errorCode, String errorMessage, String errorStack) {
            	   LinkedHashMap<String, String> map = new LinkedHashMap<String, String>();
        		   map.put("Key", "Value");
                return null;
            }

            @Override
            public byte[] onCrashUploadBinary(int crashType, String errorCode, String errorMessage, String errorStack) {
                	try {
			            return "Extra data.".getBytes("UTF-8");
			        } catch (Exception e) {
			            return null;
			        }
            }
        });
```

### 关闭Native Crash上报

默认会上报Native Crash，如果您需要，可以关闭该功能。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.enableNativeCrashMonitor(false);
```

### 关闭ANR上报

默认会上报ANR，如果您需要，可以关闭该功能。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.enableANRCrashMonitor(false);
```

## 用户策略行为

### 设置标签
自定义标签，用于标明App的某个“场景”。在发生Crash时会显示该Crash所在的“场景”，以最后设置的标签为准，标签id需大于0。例：当用户进入界面A时，打上9527的标签：

```
TACCrashService.getInstance().setUserSceneTag(context, 9527); // 上报后的Crash会显示该标签
```
打标签之前，需要在Bugly产品页配置中添加标签，取得标签ID后在代码中上报。

### 设置自定义Map参数

自定义Map参数可以保存发生Crash时的一些自定义的环境信息。在发生Crash时会随着异常信息一起上报并在页面展示。

```
TACCrashService.getInstance().putUserData(context, "userkey", "uservalue");
```

最多可以有9对自定义的key-value（超过则添加失败）；
key限长50字节，value限长200字节，过长截断；
key必须匹配正则：[a-zA-Z[0-9]]+。


## Javascript的异常捕获功能

Crash 提供了Javascript的异常捕获和上报能力，以便开发者可以感知到 WebView中发生的Javascript异常。

```
TACCrashService.getInstance().setJavascriptMonitor(Webview);
```

由于Android 4.4以下版本存在反射漏洞，接口默认只对Android 4.4及以上版本有效。

如果您是采用自动集成SDK的方式，可以选择自动注入或者手动注入两种方式。

### 自动注入

建议在WebChromeClient的onProgressChanged函数中调用接口，例子如下：

```
WebView webView = new WebView(this);
// 设置WebChromeClient
webView.setWebChromeClient(new WebChromeClient() {
    @Override
    public void onProgressChanged(WebView webView, int progress) {
        // 增加Javascript异常监控
        TACCrashService.getInstance().setJavascriptMonitor(webView, true);
        super.onProgressChanged(webView, progress);
    }
});
// 加载HTML
webView.loadUrl(url);
```

### 手动注入

将下载的SDK资源包中的 Bugly.js 文件添加到需要监控Javascript异常的HTML中：

```
<html>
  <script src="bugly.js" ></script>
<body>
    ...
</body>
</html>
在WebView加载完该HTML后设置Javascript的异常捕获功能：
WebView webView = new WebView(this);
// 加载HTML
webView.loadUrl(url);
// 增加Javascript异常监控
TACCrashService.getInstance().setJavascriptMonitor(webView, false);
```

在捕获到Javascript异常后，默认会上报以下信息：

* Android设备的相关信息；
* Javascript异常堆栈和其他信息；
* Java堆栈；
* WebView的信息，目前只包括ContentDescription。

## 主动上报异常

主动上报开发者Catch的异常 您可能会关注某些重要异常的Catch情况。我们提供了上报这类异常的接口。 

```
try {
    //...
} catch (Throwable thr) {
    TACCrashService.getInstance().postCatchedException(thr); 
}
```

## 自定义日志

我们提供了自定义Log的接口，用于记录一些开发者关心的调试日志，可以更全面地反应App异常时的前后文环境。使用方式与android.util.Log一致。用户传入TAG和日志内容。该日志将在Logcat输出，并在发生异常时上报。上报Log最大30K。

```
TACCrashService.getInstance().log(TACCrashLogLevel.VERBOSE, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.DEBUG, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.INFO, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.WARNING, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.ERROR, tag, log);
```