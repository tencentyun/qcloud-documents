### 如何关闭TPNS的保活功能？

TPNS默认开启联合保活能力，请在应用初始化的时候，如Application或LauncherActivity 的onCreate中 调用如下接口，并传递 false 值:
```java
XGPushConfig.enablePullUpOtherApp(Context context, boolean pullUp);
```
若您使用 gradle 自动集成方式，请在自身应用的 AndroidManifest.xml 文件 <application> 标签下配置如下结点，其中 ```xxx``` 为任意自定义名称；如果使用手动集成方式，请修改如下节点属性：
 
```xml
   <!-- 在自身应用的AndroidManifest.xml文件中添加如下结点，其中 xxx 为任意自定义名称: -->     
   <!-- 关闭与 TPNS 应用的联合保活功能，请配置 -->
   <provider
       android:name="com.tencent.android.tpush.XGPushProvider"
       tools:replace="android:authorities"
       android:authorities="应用包名.xxx.XGVIP_PUSH_AUTH"
       android:exported="false" />    
```

### 推送消息为何收不到？
登录 [腾讯移动推送控制台](https://console.cloud.tencent.com/tpns) ，使用已获取的 Token 进行推送。如无法收到推送，请根据以下情况进行排查：
- 请确保 SDK 版本是否为最新版本，如是旧版本出现问题，在新版本可能已经修复。
- 如遇到 Web 端推送报错，请刷新页面重试。


### 为何注册成功，无法收到推送？
- 请查看当前应用包名，是否与注册腾讯移动推送应用时填写的应用包名不一致。如果不一致，推送时，建议开启多包名推送。
- 检查手机网络是否异常，切换4G网络，进行测试。
- 腾讯移动推送分为通**知栏消息**和**应用内消息**（透传消息），通知栏消息可以展示到通知栏，应用内消息不能展示到通知栏。
- 确认手机当前模式是正常模式，部分手机在低电量，勿扰模式，省电模式下，会对后台腾讯移动推送进程进行一系列网络和活动的限制。
- 查看设备是否开启通知栏权限，OPPO，vivo 等手机，需要手动开启通知栏权限。


### 设备注册失败的原因？
- 新创建的 App 会有一分钟左右的数据同步过程，在此期间，注册可能返回20错误码，稍后重试即可。
- **参数填写有误**：Access ID 和 Access Key 是否正确配置，常见错误是误用 Secret key ，或者 Access key 头尾有空格。
- **注册返回错误**：若控制台返回10004、10002、20等错误码，请参见 [Android SDK 错误码](https://cloud.tencent.com/document/product/548/36660)。
- **注册无回调**：确认当前网络情况是否良好，建议使用4G网络测试，Wi-Fi 由于使用人数过多可能造成网络带宽不足。
- **努比亚品牌的手机**：在2015年下半年和2016年出的机器均无法注册，具体机型包括 Nubia Z11 系列，NubiaZ11S 系列，NubiaZ9S 系列。

### 为何关闭应用后，无法收到推送？
- 目前第三方推送都无法保证关闭应用后，仍可收到推送消息，该问题为手机定制 ROM 对腾讯移动推送 Service 的限制问题，腾讯移动推送的一切活动，都需要建立在腾讯移动推送的 Service 能够正常联网运行，Service 被终止后，由系统、安全软件和用户操作限定是否能够再次启动。
- QQ 和微信是系统级别的应用白名单，相关的 Service 不会因为关闭应用而退出，所以用户感知推出应用过后，仍可收到消息，其实相关的 Service 还是能够在后台存活的。
- Android 端在应用退出腾讯移动推送 Service 和腾讯移动推送的服务器断开连接后，此时给这个设备下发的消息，会变成离线消息，离线消息最多保存72小时，每个设备最多保存两条，如果有多条离线消息。在关闭应用期间推送的消息，如开启应用无法收到，请检查是否调用了反注册接口：XGPushManager.unregisterPush\(this\)。




### 如何设置消息点击事件？
TPNS 推荐使用 Intent 方式进行跳转（注：SDK 点击消息默认支持点击事件，触发后打开主界面，如果在 onNotifactionClickedResult 设置跳转操作会与管理台/API中指定的自定义跳转冲突，导致自定义的跳转失效）。
**使用 Intent 方式跳转指引：**
在客户端 App 的 manifest 上，配置需要跳转的页面：
 - 如要跳转 AboutActivity 指定页面，示例代码如下：
```
<activity
android:name="com.qq.xg.AboutActivity"
android:theme="@android:style/Theme.NoTitleBar.Fullscreen" >
<intent-filter >
<action android:name="android.intent.action.VIEW" />
<category android:name="android.intent.category.DEFAULT"/>
<data android:scheme="xgscheme"
android:host="com.xg.push"
android:path="/notify_detail" />
</intent-filter>
</activity>
```
 - 若使用腾讯移动推送管理台设置 Intent 进行跳转，填写方式如下：
![](https://main.qcloudimg.com/raw/58bb9b0105dd6ba00f6524e29efb12fb.png)
 - 若使用服务端 SDK ，设置 Intent 进行跳转，可设置 Intent 为（以 Java SDK 为例）：
```
action.setIntent("xgscheme://com.xg.push/notify_detail");
```
 - 若需要带上 param1 和 param2 等参数，您可以做如下设置：
```
action.setIntent("xgscheme://com.xg.push/notify_detail?param1=aa&param2=bb");
```

**终端获取参数**：
1. 在您跳转指定的页面 onCreate 方法里，添加如下代码：
```
Uri uri = getIntent().getData();
    if (uri != null) {                
String url = uri.toString();
String p1= uri.getQueryParameter("param1");
String p2= uri.getQueryParameter("param2");
 }
```
2. 如果传参包含有特殊字符，如 # 、& 等，可以参考使用如下方式解析：
```
Uri uri = getIntent().getData();
    if (uri != null) {                
 String url = uri.toString();
 UrlQuerySanitizer sanitizer = new UrlQuerySanitizer();
 sanitizer.setUnregisteredParameterValueSanitizer(UrlQuerySanitizer.getAllButNulLegal());
   sanitizer.parseUrl(url);
   String value1 = sanitizer.getValue("key1");
   String value2 = sanitizer.getValue("key2");
   Log.i("XG" , "value1 = " + value1 + " value2 = " + value2);
}
```






### 厂商通道的回调支持哪些？
- 小米通道支持抵达回调，不支持点击回调，支持透传。
- 华为通道不支持抵达回调，支持点击回调（需要自定义参数），支持透传（但忽略自定义参数）。
- 魅族通道支持抵达回调，支持点击回调，不支持透传。
- vivo 通道不支持抵达回调，支持点击回调，不支持透传
- OPPO 通道不支持点击和抵达回调，不支持透传

>?如果需要通过点击回调获取参数或者跳转自定义页面，可以通过使用 Intent 来实现。



### 在调试过程中遇到 otherpushToken = null 的问题，如何解决？
#### 小米通道排查路径
- 检查 App 包名是否和小米开放推送平台的包名一致。
- 检查是否在小米小米开放推送平台开启消息推送服务。
- 如果是手动接入的方式请根据开发文档检查 manifest 文件配置，尤其是需要修改包名的地方是否修改：
```
<permission android:name="com.example.mipushtest.permission.MIPUSH_RECEIVE" android:protectionLevel="signature" />
<!-- 这里com.example.mipushtest改成app的包名 -->
<uses-permission android:name="com.example.mipushtest.permission.MIPUSH_RECEIVE" />
<!-- 这里com.example.mipushtest改成app的包名 -->
```
- 在腾讯移动推送注册前是否设置了小米的 AppID 和 AppKey，以及第三方推送有没有启动：
```
//打开第三方推送
XGPushConfig.enableOtherPush(this,true);
// 设置小米的Appid和Appkey
XGPushConfig.setMiPushAppId(this,MIPUSH_APPID);
XGPushConfig.setMiPushAppKey(this,MIPUSH_APPKEY);
```
- 通过实现自定义继承 PushMessageReceiver 的广播，监听小米的注册结果，查看注册返回码。
- 启动 logcat，观察 tag 为 PushService 的日志，查看是否有错误信息。

#### 华为通道排查路径
- 检查华为手机中【设置】>【应用管理】>【华为移动服务】的版本信息是否大于2.5.3。
- 检查是否为签名包。
- 华为官网是否配置 SHA256 证书指纹。
- 按照开发文档华为通道接入指南部分检查 manifest 文件配置。
- 在腾讯移动推送注册之前是否启动了第三方推送，以及华为 AppID 是否配置正确。
- App 的包名和华为推送官网、腾讯移动推送管理台注册包名是否一致。
- 在注册代码之前调用：XGPushConfig.setHuaweiDebug\(true\)，手动确认给应用存储权限，然后查看 SD 卡目录下的 huawei.txt 文件内输出的华为注册失败的错误原因，然后根据华为开发文档对应的 [错误码](https://developer.huawei.com/consumer/cn/doc/development/HMS-2-References/hmssdk_huaweipush_api_reference_errorcode ) 查找原因。
- cmd 里执行 ```adb shell setprop log.tag.hwpush VERBOSE 和
  adb shell logcat -v time &gt; D:/log.txt``` 开始抓日志，然后进行测试，测完再关闭 cmd 窗口。将 log 发给技术支持。


#### 魅族通道排查路径
与小米通道的排查方法类似，参考小米通道的排查路径即可。



### 魅族 Flyme6.0 及低版本手机，为何消息抵达设备却不在通知栏展示？
高版本魅族手机不再需要设置状态栏图标，如果 Android SDK 版本低于1.1.4.0，请在相应的 drawable 不同分辨率文件夹下放置一张名称必须为 stat_sys_third_app_notify 的图片。


### 集成华为推送通道时遇到组件依赖冲突如何解决?
项目使用了华为 HMS 2.x.x 游戏、支付、账号等其他服务组件，因依赖 `com.tencent.tpns:huawei:1.1.x.x-release` 集成华为推送通道而遇到组件依赖冲突时，请按照以下步骤集成华为厂商通道：
1. 取消项目对 `"com.tencent.tpns:huawei:[VERSION]-release"` 此单个依赖包的依赖。
2. 在参照华为开发者平台官方文档集成华为官方 SDK 时，请同时勾选 push 模块，为华为 SDK 添加 push 功能。
3. 在 HMSAgent 模块的源代码中，就工具类 `com.huawei.android.hms.agent.common.StrUtils`做以下修改，以解决华为 SDK 内部一处异常造成的华为厂商 token 注册失败问题。
修改前：
```java
package com.huawei.android.hms.agent.common;
public final class StrUtils {
    public static String objDesc(Object object) {
        return object == null ? "null" : (object.getClass().getName()+'@'+ Integer.toHexString(object.hashCode()));
    }
}
```
修改后：
```java
package com.huawei.android.hms.agent.common;
public final class StrUtils {
    public static String objDesc(Object object) {
        String s = "";
        try {
            s = Integer.toHexString(object.hashCode());
        } catch (Throwable e) {
        }
        return object == null ? "null" : (object.getClass().getName()+'@'+ s);
    }
}
```


### 使用控制台快速集成时出现异常，如何解决？
1. 如果集成出现异常， 则将 `tpns-configs.json `文件中的 `"debug"` 字段置为` true`,  运行命令： 
```
./gradlew --rerun-tasks :app:processReleaseManifest 
```
并通过` "TpnsPlugin" `关键字进行分析。
2. 点击 sync projects。
![](https://main.qcloudimg.com/raw/5fecbe6b63374e7e0e58c4b2cd215acb.png)

3. 在项目的 External Libraries 中查看是否有相关依赖。
![](https://main.qcloudimg.com/raw/485c7595f1b478a6fad725d38deb87b4.png)

