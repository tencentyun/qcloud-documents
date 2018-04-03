### 手动集成 SDK

如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

#### 1. 下载服务资源压缩包。

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Crash 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-crash-1.0.0.zip)，并解压。

#### 2. 集成 jar 包。
- 将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。

#### 3. 如果需要上报 Native 异常，集成 Native Crash 包。
 
如果您的工程有 Native 代码（C/C++）或者集成了其他第三方 SO 库，您可以集成 [native crash 上报库](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-nativecrash-1.0.0.zip)。
 
- 如果您是采用 Eclipse 开发，将 `native crash 上报库`解压后的 `jni` 目录下的内容 拷贝到您工程您工程的 `libs` 目录。
- 如果您是采用 Android Studio 开发，将`native crash 上报库`解压后的 `jni` 目录下的内容 拷贝到 app 模块的 `main` 文件夹下的 `jniLibs` 目录下 。如果不存在该目录，请新建一个。

#### 4. 修改您工程的 AndroidManifest.xml 文件。

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件：

```
<!-- 添加 Crash 需要的权限 -->
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_LOGS" />
```

## 避免混淆

如果您的应用开启了混淆，请在 Proguard 混淆文件中增加以下配置，避免 Crash 被混淆：

```
-dontwarn com.tencent.bugly.**
-keep public class com.tencent.bugly.**{*;}
```

## 添加符号表和 mapping 文件上传插件

如果您的工程使用了 so 文件或者对代码进行了混淆，您需要添加插件来上传符号表和 mapping 文件。

### 通过 gradle 远程依赖上传

#### 1. 在工程根目录下的 build.gradle 文件中添加依赖。
 
```
buildscript {
	 ......
    dependencies {
        ......
        classpath 'com.tencent.tac:tac-crash-plugin:1.0.0'
    }
}
```

#### 2. 在您应用 module 下的 build.gradle 文件中添加插件依赖。
 
请加在您 build.gralde 文件的头部。

```
apply plugin: 'com.android.application'
// 添加这一行
apply plugin: 'com.tencent.tac.crash'
```

依赖完成之后，我们会在您编译打包的过程中自动上传符号表，您不需要其他操作。

### 手动上传

1. 下载 [符号表工具](https://bugly.qq.com/v2/sdk?id=37d1ad19-a4b0-4eed-9146-55d87fc79f8d)。
2. 根据 UUID 定位 Debug SO 文件，具体可参考工具包中的使用文档。
3. 使用工具生成符号表文件（zip 文件），具体的使用方法可参考工具包中的使用文档。
4. 在移动开发平台（MobileLine）的控制台上传符号表文件。
 
如果您的项目只使用了混淆代码 (Proguard)，而没有 Native 工程，只需要直接上传 Proguard 生成的 Mapping 文件即可。


## 配置服务

Crash 服务使用默认参数即可，不需要额外配置。如果您已经配置好 TACApplication 单例，这个过程已经自动完成。

### 高级配置

如果您需要自定义服务的策略，您可以使用 TACCrashOptions 修改一些具体的策略：

```
TACApplicationOptions applicationOptions = TACApplication.options();

TACCrashOptions crashOptions = applicationOptions.sub("crash");
```

具体的 API 请参考编程手册文档。

>**注意：**
>请在 Crash 服务启动前完成它对应的参数配置，一旦服务启动，后续所有对它的参数修改都不会生效。



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

## 模拟异常

您可以通过以下方法主动触发异常，以便测试 SDK 是否正常工作。

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

Crash 会在启动 10s 后联网同步数据。若您有特别需求，可以修改这个时间。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.setReportDelay(20000);   //改为 20s
```

### 设置 Crash 回调

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

### 关闭 Native Crash 上报

默认会上报 Native Crash，如果您需要，可以关闭该功能。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.enableNativeCrashMonitor(false);
```

### 关闭 ANR 上报

默认会上报 ANR，如果您需要，可以关闭该功能。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.enableANRCrashMonitor(false);
```

## 用户策略行为

### 设置标签
自定义标签，用于标明 App 的某个“场景”。在发生 Crash 时会显示该 Crash 所在的“场景”，以最后设置的标签为准，标签 ID 需大于 0。例：当用户进入界面A时，打上 9527 的标签：

```
TACCrashService.getInstance().setUserSceneTag(context, 9527); // 上报后的Crash会显示该标签
```
打标签之前，需要在 Bugly 产品页配置中添加标签，取得标签 ID 后在代码中上报。

### 设置自定义Map参数

自定义Map参数可以保存发生 Crash 时的一些自定义的环境信息。在发生 Crash 时会随着异常信息一起上报并在页面展示。

```
TACCrashService.getInstance().putUserData(context, "userkey", "uservalue");
```

最多可以有 9 对自定义的 key-value（超过则添加失败）；
key 限长 50 字节，value 限长 200 字节，过长截断；
key 必须匹配正则：[a-zA-Z[0-9]]+。


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

## 主动上报异常

主动上报开发者 Catch 的异常您可能会关注某些重要异常的 Catch 情况，我们提供了上报这类异常的接口。 

```
try {
    //...
} catch (Throwable thr) {
    TACCrashService.getInstance().postCatchedException(thr); 
}
```

## 自定义日志

我们提供了自定义 Log 的接口，用于记录一些开发者关心的调试日志，可以更全面地反应 App 异常时的前后文环境。使用方式与 android.util.Log 一致。用户传入 TAG 和日志内容。该日志将在 Logcat 输出，并在发生异常时上报，上报 Log 最大 30K。

```
TACCrashService.getInstance().log(TACCrashLogLevel.VERBOSE, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.DEBUG, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.INFO, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.WARNING, tag, log);
TACCrashService.getInstance().log(TACCrashLogLevel.ERROR, tag, log);
```
