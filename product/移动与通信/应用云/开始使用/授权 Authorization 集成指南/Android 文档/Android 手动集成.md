如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：


#### 1. 下载服务资源压缩包

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.1.0/tac-core-1.1.0.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Authorization 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.1.0/tac-authorization-1.1.0.zip)，并解压。

#### 2. 集成 jar 包

将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。

#### 3. 集成 QQ SDK 

下载 [QQ SDK](http://tac-android-libs-1253960454.cosgz.myqcloud.com/jars/open_sdk_r5923_lite.jar) ，并拷贝到应用模块的 `libs` 文件夹下。

#### 4. 添加 SDK 依赖

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

#### 5. 配置第三方渠道

登录 SDK 需要配置QQ、微信等第三方渠道才能正常工作，关于如何配置第三方渠道，请参见 [配置第三方渠道](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E7%A7%BB%E5%8A%A8%E4%B8%8E%E9%80%9A%E4%BF%A1/%E5%BA%94%E7%94%A8%E4%BA%91/%E5%BC%80%E5%A7%8B%E4%BD%BF%E7%94%A8/%E6%8E%88%E6%9D%83%20Authorization%20%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Android%20%E6%96%87%E6%A1%A3/%E9%85%8D%E7%BD%AE%E7%AC%AC%E4%B8%89%E6%96%B9%E6%B8%A0%E9%81%93.md)。

到此您已经成功接入了 MobileLine 登录与授权服务。
