Two integration methods are available to connect Android SDK: one-click import by dependency (automatic integration) and manual integration. During connection, it is recommended to call the registration API with callback and enable XGPush debug log output. For more information, please see [Enabling debug log data] (link to be added when release).
### One-click Import by Dependency
It is recommended to connect Android Studio automatically via jcenter. If you use this method, you do not need to configure XGPush nodes in the configuration file, and all imports are completed by dependency. You can use remote jcenter warehouse to connect Android Studio without importing any jar package and so files in the project. You also do not need to configure XGPush-related information in AndroidManifest.xml, because jcenter will import it automatically.
After you import by dependency, modify the application configuration and write the registration code to connect XGPush quickly. The dependency version numbers are the latest versions on the official website.
The user-defined recevier still needs to be configured with relevant nodes in Androidmianfest.xml.
Configure the followings in the App build.gradle file:
```
android {
    ......
    defaultConfig {
        //The name of the package registered on the XGPush official website. Note that the application ID, the current application package name, and the name of the application package registered on the XGPush official website must be consistent.
        applicationId "your package name" 
        ......
        ndk {
            //Add the .so library for cpu as needed. 
            abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a' 
            //You can also add 'x86', 'x86_64', 'mips', and 'mips64'
        }
        manifestPlaceholders = [
            XG_ACCESS_ID: "accessid of the registered application",
            XG_ACCESS_KEY: "accessskey of the registered application",
        ]
        ......
    }
    ......
}

dependencies {
    ......
    //A complete XGPush must have three dependencies. If a dependency conflict occurs, select the highest version based on the dependent version number. Check that there is no XGPush-related jar packages in libs before you use jcenter for automatic connection.

    //Collect installation list
    compile 'com.tencent.xinge:xinge:3.1.2-release' 
    //wup package 
    compile 'com.tencent.wup:wup:1.0.0.E-release'
    //mid package
    compile 'com.tencent.mid:mid:3.9.0-release'
    ......
}
```

>**Notes**
>If the following prompt appears on Android Studio after you add the above abiFilter configurations:
`NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin.`
>Add the following in the gradle.properties file in the Project root directory:
`Android.useDeprecatedNdk=true`
> If you need to listen to messages, please see the XGBaseReceiver API or the MessageReceiver type of demo. You can inherit XGBaseReceiver and configure the followings in the configuration file:
```
  <receiver android:name="Complete type name, such as com.qq.xgdemo.receiver.MessageReceiver"
      android:exported="true" >
      <intent-filter>
          <!-- Receive transparent transmitted messages -->
          <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
          <!-- Listen to the results of registration, deregistration, tag configuration/deletion, and notification of clicks -->
          <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter>
  </receiver>
```

