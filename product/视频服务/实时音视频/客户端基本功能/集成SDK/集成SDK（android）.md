## 操作步骤
### 创建一个 Android 工程
打开 Android Studio，单击【 File 】菜单选择【 New Project 】新建一个工程：
![创建工程](https://main.qcloudimg.com/raw/88068e0adae563cbc3841832370ce62a.png)
创建一个空工程：
![空工程](https://main.qcloudimg.com/raw/c575e469c49a7ce6985fbd231a67fa00.png)

### 添加依赖( 集成 SDK )
修改 build.gradle 文件，在 dependencies 中添加 iLiveSDK 的依赖：
```
compile 'com.tencent.ilivesdk:ilivesdk:latest.release'  //其中latest.release指代最新iLiveSDK版本号
```

[最新版本说明](https://github.com/zhaoyang21cn/iLiveSDK_Android_LiveDemo)

### 创建一个应用
在 layout 中创建一个简单布局 main.xml 资源：
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
同时创建一个 Activity 应用：
![空应用](https://main.qcloudimg.com/raw/356fb5a781a30f854bde3aabcbe0a589.png)

在应用创建中使用布局并输出 iLiveSDK 的版本号：
```Java
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
### 声明应用
在 AndroidManifest.xml 中声明应用：
```
<activity android:name=".MainActivity" android:screenOrientation="portrait" >
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```


### 编译运行
编译运行，可以看到效果：

```
iLiveSDK:1.8.7
IMSDK:2.5.6.11073.11080
AVSDK:1.9.8.2
```
恭喜，至此说明 iLiveSDK 已经成功集成。


### 常见问题
#### 下载 aar 失败
```
Error:Could not resolve all files for configuration ':app:debugCompileClasspath'.
> Could not resolve com.tencent.ilivesdk:ilivesdk:1.8.3.
 Required by:
   project :app
 > Could not resolve com.tencent.ilivesdk4:ilivesdk:1.8.3.
  > Could not get resource 'https://jcenter.bintray.com/com/tencent/ilivesdk/ilivesdk/1.8.4/ilivesdk-1.8.3.pom'.
   > Could not GET 'https://jcenter.bintray.com/com/tencent/ilivesdk/ilivesdk/1.8.4/ilivesdk-1.8.3.pom'.
    > Connect to jcenter.bintray.com:443 [jcenter.bintray.com/75.126.118.188] failed: Connection timed out: connect
```
先检测网络是否正常，并通过上面链接，确认可以访问 jcenter 网站，同时如果网络需要代理检测是否有在 gradle.properties 中配置。

#### 混淆导致方法找不到
由于内部有一些接口调用需要，在用户工程需要混淆时，请添加以下配置：
```
-keep class com.tencent.**{*;}
-dontwarn com.tencent.**

-keep class tencent.**{*;}
-dontwarn tencent.**

-keep class qalsdk.**{*;}
-dontwarn qalsdk.**
```

#### 多架构导致Crash
目前只支持 armeabi 架构(1.0.5 版本之后支持 arm-v7a)，如果工程(或依赖库)中有多架构，需要在 build.gradle 中添加以下配置：
```
android{
    defaultConfig{
        ndk{
            abiFilters 'armeabi', 'armeabi-v7a'
        }
    }
}
```
