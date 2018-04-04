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
