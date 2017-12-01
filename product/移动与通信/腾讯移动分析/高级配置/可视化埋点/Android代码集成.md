### 接入指引
1. 确保正确接入普通版本 MTA；
>**注意：**
>后续如果要接可视化，必须在 AndroidManifest.xml 里面设置 TA_APPKEY，不可以代码动态设置。

2. 添加 track-sdk_v3.2.1.jar，libthrift-0.10.0.jar，slf4j-api-1.7.24.jar 包；
3. 添加URL Scheme。
i.MTA 官网应用管理页面将 scheme 里面的内容拷贝出来；
ii. 将下面的启动接口添加到您的 AndroidManifest.xml 中的 LAUNCHER Activity 下以便我们唤醒您的程序。
```
<activity
    android:name=".LauncherActivity"
    android:label="@string/app_name"
    android:theme="@style/AppTheme.NoActionBar">
    <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
    <!-- MTA可视化启动连接接口 -->
    <intent-filter>
        <data android:scheme="配置管理页面中的shceme"/>
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
    </intent-filter>
</activity>
```
请添加一整个 intent-filter 区块，并确保其中只有一个 data 字段。
>**注意：**
>配置 Scheme 的时候不要复制空格，否则会链接不成功。
![](//mc.qcloudimg.com/static/img/ac5b407da039b3ac842a229c693b58b4/image.jpg)

4. 初始化SDK ，在应用 Application 的 onCreat 里面添加 StatisticsDataAPI.instance(this)。