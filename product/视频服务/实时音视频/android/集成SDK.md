## 集成SDK

### 导语
欢迎来到集成SDK教程!

在学习iLiveSDK之前，我们将先学习如何集成iLiveSDK。

### 预备知识
本课程要求用户对Android Studio有仓库集成的概念

### 创建一个Android工程
打开Android Studio,点击File菜单选择New Project新建一个工程:

![创建工程](https://main.qcloudimg.com/raw/88068e0adae563cbc3841832370ce62a.png)

创建一个空工程

![空工程](https://main.qcloudimg.com/raw/c575e469c49a7ce6985fbd231a67fa00.png)

### 添加依赖(集成SDK)
修改build.gradle文件，在dependencies中添加iLiveSDK的依赖:
```
compile 'com.tencent.ilivesdk:ilivesdk:1.8.3'
```

### 创建一个应用
在layout中创建一个简单布局main.xml资源
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
同时创建一个Activity应用

![空应用](https://main.qcloudimg.com/raw/356fb5a781a30f854bde3aabcbe0a589.png)

在应用创建中使用布局并输出iLiveSDK的版本号：
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
在AndroidManifest.xml中声明应用:
```
<activity android:name=".MainActivity" android:screenOrientation="portrait" >
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```


### 编译运行
编译运行，可以看到效果:

```
iLiveSDK:1.8.5
IMSDK:2.5.6.11073.11080
AVSDK:1.9.8.2
```

恭喜，至此说明iLiveSDK已经成功集成！


### 常见问题
- 下载aar失败
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
先检测网络是否正常，并通过上面链接，确认可以访问jcenter网站，同时如果网络需要代理检测是否有在gradle.properties中配置


[下一课 登录](登录.md)