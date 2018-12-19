### Access Guide
1. Ensure that the normal version of MTA is properly accessed;
>**Note:**
>For future visual connection, you must set TA_APPKEY in AndroidManifest.xml and may not set it dynamically in the codes.

2. Add track-sdk_v3.2.1.jar, libthrift-0.10.0.jar, slf4j-api-1.7.24.jar packages;
3. Add URL Scheme.
i. Copy the content of scheme on APP management page of MTA official website;
ii. Add the startup API below to LAUNCHER Activity in your AndroidManifest.xml so that we can wake up your program.
```
<activity
    android:name=".LauncherActivity"
    android:label="@string/app_name"
    android:theme="@style/AppTheme.NoActionBar">
    <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
    <!-- MTA visual startup connection API -->
    <intent-filter>
        <data android:scheme="Scheme on configuration management page"/>
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
    </intent-filter>
</activity>
```
Add a whole intent-filter block, and make sure there is only one "data" field in it.
>**Note:**
>Do not copy spaces when configuring Scheme, otherwise the link will be invalid.
![](//mc.qcloudimg.com/static/img/ac5b407da039b3ac842a229c693b58b4/image.jpg)

4. Initialize SDK, and add StatisticsDataAPI.instance(this) in onCreat of Application.
