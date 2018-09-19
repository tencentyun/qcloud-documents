我们提供了一些高级配置项，您可以通过这些配置项定制化您的 Crash 服务。
>**注意：**
>您需要在启动服务前完成配置。

## 获取 Options

```
final TACApplicationOptions tacApplicationOptions = TACApplication.options();
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
```

## 设置上报延时时间

Crash 会在启动 10s 后联网同步数据。如果您有特别需求，可以修改这个时间。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.setReportDelay(20000);   //改为 20s
```

## 设置 Crash 回调

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

## 关闭 Native Crash 上报

默认会上报 Native Crash，如果您需要，可以关闭该功能。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.enableNativeCrashMonitor(false);
```

## 关闭 ANR 上报

默认会上报 ANR，如果您需要，可以关闭该功能。

```
final TACCrashOptions tacCrashOptions = tacApplicationOptions.sub("crash");
tacCrashOptions.enableANRCrashMonitor(false);
```
