## Procedure
### Create an Android project
Open Android Studio, click the **File** menu, and select **New Project** to create a project:
![](https://main.qcloudimg.com/raw/83b3807d3e5d0f35d767565ffafd5552.png)
Create an empty project:
![](https://main.qcloudimg.com/raw/84964fad3a47905fb20c7a411ce74f52.png)
### Add a dependency (integrate SDK)
Modify the build.gradle file and add the dependency of iLiveSDK in "dependencies":

compile 'com.tencent.ilivesdk:ilivesdk:latest.release'  //latest.release refers to the latest iLiveSDK version number
### Create an application
Create a simple layout main.xml in "layout":
```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/tv_version"
        android:textColor="@color/colorAccent"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />
</LinearLayout>
```
At the same time, create an Activity project:
![](https://main.qcloudimg.com/raw/b71de0a52807fcbbc88c5ec5df5817a5.png)
Use the layout in application creation and output the version number of the iLiveSDK:
```
public class MainActivity extends Activity {
    private TextView tvVersion;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        tvVersion = (TextView)findViewById(R.id.tv_version);

        tvVersion.setText(" iLiveSDK: "+ILiveSDK.getInstance().getVersion()+"\n IMSDK:"+
                TIMManager.getInstance().getVersion()+"\n AVSDK:"+
                AVContext.sdkVersion);
    }
}
```
### Declare the application
Declare the application in AndroidManifest.xml:
```
<activity android:name=".MainActivity" android:screenOrientation="portrait" >
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```
### Compile and run the project
Compile and run the project, and then the following displays:
```
iLiveSDK:1.8.5
IMSDK:2.5.6.11073.11080
AVSDK:1.9.8.2
```
You have successfully integrated iLiveSDK.
## FAQ
### Failed to download aar
```
Error:Could not resolve all files for configuration ':app:debugCompileClasspath'.
> Could not resolve com.tencent.ilivesdk:ilivesdk:1.8.3.
 Required by:
   project :app
 > Could not resolve com.tencent.ilivesdk4:ilivesdk:1.8.3.
  > Could not get resource 'https://jcenter.bintray.com/com/tencent/ilivesdk/ilivesdk/1.8.4/ilivesdk-1.8.3.pom'.
   > Could not GET 'https://jcenter.bintray.com/com/tencent/ilivesdk/ilivesdk/1.8.4/ilivesdk-1.8.3.pom'.
    > Connect to jcenter.bintray.com:443 [jcenter.bintray.com/75.126.118.188] failed: Connection timed out: connect
Check the network first. Then, check whether the jcenter website is accessible by clicking on the above link. If a proxy is required, check if it is configured in gradle.properties.
```
### Methods not found due to proguard
When calling some APIs, add the following configurations to enable the proguard for your project:
```
-keep class com.tencent.**{*;}
-dontwarn com.tencent.**

-keep class tencent.**{*;}
-dontwarn tencent.**

-keep class qalsdk.**{*;}
-dontwarn qalsdk.**
```
### Crash due to multiple architectures
Only the armeabi architecture is supported (arm-v7a is supported for version 1.0.5 or later). If the project (or dependent library) has multiple architectures, the following configurations are required in build.gradle:
```
android{
    defaultConfig{
        ndk{
            abiFilters 'armeabi', 'armeabi-v7a'
        }
    }
}
```
## Email
If you have any questions, send us an email to trtcfb@qq.com.

