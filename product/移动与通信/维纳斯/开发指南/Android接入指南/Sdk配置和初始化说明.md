## Sdk 配置和初始化说明
### 引入 Wns Sdk
将/libs 下的 assets 和 libs 目录分别复制到工程根目录对应的目录中，如下图
![](https://mccdn.qcloud.com/static/img/dca5498f8a97efd6050f0ac4e3610ab9/wns_and_lib.png)
**注意：需要将 jar 文件和对应的 so 添加 到工程中。
这里的 armeabi 的 so 文件夹是必须添加，其它 so 文件夹可以按需添加，如果你的工程中有对应的 so 文件夹就必须加入相应文件夹的 so。例如工程libs目录下已经有 arm64-v8a 目录，则需要添加到 WNSsdk 中相关的  arm64-v8a 文件夹下的 64 位系统的相关 so，否则 64 位上的机器会崩溃。**

### 配置 AndroidManifest.xml
wns_SDK  需要使用的系统权限如下图（可参考示例工程）：
注意：加到根目录 manifest 下面。
```
<!-- demo中使用某些高级API简化编程，使用者需要根据自己情况设置sdk version -->
<uses-sdk
    android:minSdkVersion="10"
    android:targetSdkVersion="18" />

<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

```

### 配置 WnsSdk 服务
注册 Service：

```
<!-- service -->

<!-- WNS service,注意进程名为  :wns ，其它组件请不要使用这个进程名 -->
<service
        android:name="com.tencent.wns.service.WnsMain"
        android:exported="false"
        android:process=":wns">
    <intent-filter>
        <action android:name="com.tencent.wns.service.WnsMain"/>
    </intent-filter>
</service>

<!-- 注册WNS心跳接收器 -->
<receiver
        android:name="com.tencent.base.os.clock.AlarmClockReceiver"
        android:exported="false"
        android:process=":wns">
    <intent-filter>
        <action android:name="wns.heartbeat"/>
    </intent-filter>
</receiver>

```
注意:
  (1)  进程名“:wns”为 wns 服务使用，请不要占用
  (2)  以上部分位于 application 分支下。

### 初始化 APP 信息并启动服务
修改 MyBaseApplication，onCreate（）变为如下内容：

```
public class MyBaseApplication extends Application
{
    private final static String TAG = "BaseApplication";

    private WnsService wns = WnsClientFactory.getThirdPartyWnsService();;

    @Override
    public void onCreate()
    {
        super.onCreate();

        WnsAppInfo info = new WnsAppInfo()
             //[修改] 云平台上申请获取的APPID
              .setAppId(1000244)  
               //[修改] App的版本信息 - 建议填写，方便以后提供详细细分统计（这里的“1.0.0”代表版本                                 号，业务可以按照自己规则填写）
              .setAppVersion("1.0.0") 
              //[修改] APP的渠道信息 - 建议填写，方便以后提供详细细分统计。（这里的“yyb”代表应用宝，业务可以按照自己规则填写）
                .setChannelId("yyb"); 
         wns.initAndStartWns(this, info);
     }
}

```

同时在 AndroidManifes.xml 中配置实现：

```
<application android:name=".MyBaseApplication" .... 
```

### 代码混淆
sdk 已经混淆，建议不要再次混淆。如果需要混淆，请务必在脚本中加入以下配置

```
-keep class com.tencent.wns.openssl.OpenSSLNative
{ private long pkey;
}
-keep class com.tencent.wns.network.ConnectionImpl  {*;
}
-keep class * implements com.qq.taf.jce.JceStruct {
}
-keep class com.tencent.wns.service.WnsMain

```
