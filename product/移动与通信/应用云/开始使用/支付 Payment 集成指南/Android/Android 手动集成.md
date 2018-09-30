如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载服务资源压缩包
 
- 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.file.myqcloud.com/tac-core.zip) 并解压。
- 下载 [移动开发平台（MobileLine） Payment 资源包](http://tac-android-libs-1253960454.file.myqcloud.com/tac-payment.zip) 并解压。
                             
### 2. 集成 QQ 支付

如果您需要同时接入 QQ 支付，那么必须将 [mqqopenpay.jar](http://tac-android-libs-1253960454.file.myqcloud.com/jars/mqqopenpay.jar) 也添加到您工程的 `libs` 目录。

### 3. 修改 AndroidManifest.xml 文件

如果您不是通过 aar 集成，首先添加如下 `permission` 声明：

```
<!-- 必选权限 -->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.GET_TASKS"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

<!-- 可选权限 -->
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
```

然后添加如下 `Activity` 声明：

```
<activity
    android:name="com.tencent.openmidas.proxyactivity.APMidasPayProxyActivity"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:configChanges="orientation|keyboardHidden|screenSize"
    android:process=":openMidas"
    android:screenOrientation="portrait"/>
<activity
    android:name="com.tencent.openmidas.wx.APMidasWXPayActivity"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
android:process=":openMidas"
android:exported="true" />
<activity
    android:name="com.tencent.openmidas.qq.APMidasQQWalletActivity"
    android:launchMode="singleTop"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:configChanges="orientation|keyboardHidden"
    android:process=":openMidas"
    android:exported="true" >
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.BROWSABLE"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:scheme="qwallet100703379"/>
    </intent-filter>
</activity>
```
