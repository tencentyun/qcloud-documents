如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：


#### 1. 下载服务资源压缩包

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.file.myqcloud.com/tac-core.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Authorization 资源包](http://tac-android-libs-1253960454.file.myqcloud.com/tac-authorization.zip)，并解压。

#### 2. 集成 QQ SDK 

下载 [QQ SDK](http://tac-android-libs-1253960454.file.myqcloud.com/jars/open_sdk_r5923_lite.jar) ，并拷贝到应用模块的 `libs` 文件夹下。

#### 3. 修改您工程的 AndroidManifest.xml 文件。

请把下载的 QQ open jar 包添加到 classpath 中，并在 AndroidManifest.xml 文件中添加以下权限和 Activity：

```
	<uses-permission android:name="android.permission.INTERNET" />
   	<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

    <application>
    	...
    	
        <activity
            android:name="com.tencent.tauth.AuthActivity"
            android:launchMode="singleTask"
            android:noHistory="true">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />

                <!--<data android:scheme="tencent${应用在QQ互联的app id}" />-->
            </intent-filter>
        </activity>

        <activity
            android:name="com.tencent.connect.common.AssistActivity"
            android:screenOrientation="behind"
            android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:configChanges="orientation|keyboardHidden">
        </activity>
    </application>
```

#### 4. 配置第三方渠道

登录 SDK 需要配置QQ、微信等第三方渠道才能正常工作，关于如何配置第三方渠道，请参见 [配置第三方渠道](https://cloud.tencent.com/document/product/666/17846)。

到此您已经成功接入了 MobileLine 登录与授权服务。
