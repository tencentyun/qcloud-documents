## Javascript 的异常捕获功能

Crash 提供了 Javascript 的异常捕获和上报能力，以便开发者可以感知到 WebView 中发生的 Javascript 异常。

```
TACCrashService.getInstance().setJavascriptMonitor(Webview);
```

由于 Android 4.4 以下版本存在反射漏洞，接口默认只对 Android 4.4 及以上版本有效。

如果您是采用自动集成 SDK 的方式，可以选择自动注入或者手动注入两种方式。

### 自动注入

建议在 WebChromeClient 的 onProgressChanged 函数中调用接口，例子如下：

```
WebView webView = new WebView(this);
// 设置WebChromeClient
webView.setWebChromeClient(new WebChromeClient() {
    @Override
    public void onProgressChanged(WebView webView, int progress) {
        // 增加 Javascript 异常监控
        TACCrashService.getInstance().setJavascriptMonitor(webView, true);
        super.onProgressChanged(webView, progress);
    }
});
// 加载 HTML
webView.loadUrl(url);
```

### 手动注入

将下载的 SDK 资源包中的 Bugly.js 文件添加到需要监控 Javascript 异常的 HTML 中：

```
<html>
  <script src="bugly.js" ></script>
<body>
    ...
</body>
</html>
在 WebView 加载完该 HTML 后设置 Javascript 的异常捕获功能：
WebView webView = new WebView(this);
// 加载 HTML
webView.loadUrl(url);
// 增加 Javascript 异常监控
TACCrashService.getInstance().setJavascriptMonitor(webView, false);
```

在捕获到 Javascript 异常后，默认会上报以下信息：

* Android 设备的相关信息；
* Javascript 异常堆栈和其他信息；
* Java 堆栈；
* WebView 的信息，目前只包括 ContentDescription。


## MultiDex 注意事项

如果使用了 MultiDex，建议通过 Gradle 的 "multiDexKeepFile" 配置等方式把 Crash 的类放到主 Dex，另外建议在 Application 类的 "attachBaseContext" 方法中主动加载非主 dex：

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

如果 App 使用了多进程且各个进程都会初始化 Crash（例如在 Application 类 onCreate()中初始化 Crash），那么每个进程下都会进行数据上报，造成不必要的资源浪费。
 
您可以通过以下方法控制只在主线程上报数据，首先通过以下方法获取当前进程是否为主进程：

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

然后，在您启动服务的地方，加上进程的判断：

```
if (isMainProcess()) {
	crashService.start(context);
}
```



