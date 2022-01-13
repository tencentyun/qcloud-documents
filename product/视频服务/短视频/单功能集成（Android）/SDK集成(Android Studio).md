## Android 工程配置
### 系统要求
SDK 支持 在 Android 4.0.3（API 15）及以上系统上运行，但只有（Android 4.3）API 18 以上的系统才能开启硬件编码。

### 开发环境
以下是 SDK 的开发环境，App 开发环境不需要与 SDK 一致，但要保证兼容：

- Android NDK：android-ndk-r12b
- Android SDK Tools：android-sdk_25.0.2
- minSdkVersion：15
- targetSdkVersion：26
- Android Studio（推荐您也使用 Android Studio，当然您也可以使用 Eclipse + ADT）


[](id:step1)
### 步骤1：集成 SDK
<dx-tabs>
::: aar 方式集成
1. **新建工程**
![](https://main.qcloudimg.com/raw/ca473c3bf484da3d7d959dbb83b192b1.png)
2. **工程配置**
  1. 在工程 App 目录下的 build.gradle 中，添加引用 aar 包的代码：
```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    // 导入短视频 SDK aar，LiteAVSDK_UGC_x.y.zzzz 请自行修改为最新版本号
    compile(name: 'LiteAVSDK_UGC_7.4.9211', ext: 'aar')
    ...
}
```
  2. 在工程目录下的 build.gradle 中，添加 flatDir，指定本地仓库：
```
allprojects {
  repositories {
      jcenter()
      flatDir {
          dirs 'libs'
      }
  }
}
```
  3. 在 App 工程目录下的 build.gradle 的 defaultConfig 里面，指定 ndk 兼容的架构：
```
defaultConfig {
    ...
    ndk {
        abiFilters "armeabi", "armeabi-v7a"
    }
}
```
  4. 最后单击 **Sync Now**，编译工程。
:::
::: jar+so 方式集成
1. **库说明**
解压 zip 压缩包后得到 libs 目录，里面主要包含 jar 文件和 so 文件，文件清单如下：
<table>
<tr><th>jar 文件</th><th>说明</th></tr>
<tr><td>liteavsdk.jar </td><td >短视频 SDK Android 核心库 </td>
</tr></tbody>
</table>
<table>
<tr><th>so 文件  </th><th>说明</th></tr>
<tr><td> libliteavsdk.so</td><td >短视频 SDK 核心组件 </td></tr>
<tr><td>libtxffmpeg.so</td><td >ffmpeg 基础库（ijk 版本），用于点播播放功能，解决一些视频格式的兼容问题  </td>
</tr><tr><td>libtxplayer.so</td><td >ijkplayer 开源库，用于点播播放功能，解决一些视频格式的兼容问题   </td>
</tr><tr><td>  libtxsdl.so</td><td > ijkplayer 开源库，用于点播播放功能，解决一些视频格式的兼容问题 </td>
</tr></table>
2. **拷贝文件**
    如果您的工程之前没有指定过 jni 的加载路径，推荐您将刚才得到的 jar 包和 so 库拷贝到 **Demo\app\src\main\jniLibs** 目录下，这是 Android Studio 默认的 jni 加载目录。
    如果您使用的是企业版，那么解压 zip 包后，除了 jar 包和 so 库增加了以外，还多了 assets 目录下的文件，这些是动效所需要的，需要全部拷贝到工程的 assets 目录下，请参见 [动效变脸 - 工程配置](https://cloud.tencent.com/document/product/584/13510#.E5.B7.A5.E7.A8.8B.E8.AE.BE.E7.BD.AE)。
3. **工程配置**
在工程 App 目录下的 build.gradle 中，添加引用 jar 包和 so 库的代码。
```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    // 导入腾讯云短视频SDK jar
    compile fileTree(dir: 'src/main/jniLibs', includes: ['*.jar'])
    ...
}
```
4. **减少 APK 体积**
整个 SDK 的体积主要来自于 so 文件，这些 so 文件是 SDK 正常运行所依赖的音视频编解码库、图像处理库以及声学处理组件，如果短视频 SDK 的功能不是 App 的核心功能，您可以考虑采用在线加载的方式减少最终 apk 安装包的大小。
  1. **上传 so 文件**
将 SDK 压缩包中的 so 文件上传到 COS，并记录下载地址，例如 `http://xxx-appid.cossh.myqcloud.com/so_files.zip`。
  2. **启动准备**
在用户启动 SDK 相关功能前，例如开始播放视频之前，先用 loading 动画提示用户“正在加载相关的功能模块”。
  3. **下载 so 文件**
在用户等待过程中，App 就可以到 `http://xxx-appid.cossh.myqcloud.com/so_files.zip` 下载 so 文件，并存入应用目录下（例如应用根目录下的 files 文件夹），为了确保这个过程不受运营商 DNS 拦截的影响，请在文件下载完成后校验 so 文件的完整性。
  4. **加载 so 文件**
等待所有 so 文件就位以后，调用 TXLiveBase 的 setLibraryPath 将下载的目标 path 设置给 SDK， 然后再调用 SDK 的相关功能。之后，SDK 会到这些路径下加载需要的 so 文件并启动相关功能。
:::
::: gradle 集成方式
1. 在 dependencies 中添加 LiteAVSDK_UGC 的依赖。
	- 若使用3.x版本的 com.android.tools.build:gradle 工具，请执行以下命令：
```
dependencies {
   implementation 'com.tencent.liteav:LiteAVSDK_UGC:latest.release'
}
```
	- 若使用2.x版本的 `com.android.tools.build:gradle` 工具，请执行以下命令：
```
dependencies {
   compile 'com.tencent.liteav:LiteAVSDK_UGC:latest.release'
}
```
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
   ndk {
       abiFilters "armeabi", "armeabi-v7a"
   }
}
```
>?目前 SDK 支持 armeabi、armeabi-v7a 和 arm64-v8a。
3. 单击 **Sync Now**，自动下载 SDK 并集成到工程里。
:::
</dx-tabs>

[](id:step2)
### 步骤2：配置 App 权限

在 AndroidManifest.xml 中配置 App 的权限，音视频类 App 一般需要以下权限：

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.CALL_PHONE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```

[](id:step3)
### 步骤3：设置 License
1. 参考 [License 申请](https://cloud.tencent.com/document/product/584/20333) 的指引申请 License 后，从 [云点播控制台](https://console.cloud.tencent.com/vod/license/video) 复制 License Key 和 License URL，如下图所示：
![](https://main.qcloudimg.com/raw/0b50ff439f2c4aaf656e535f814c7ba2.png)
2. 在您的应用中使用短视频功能之前，建议在 `- Application onCreate()`中进行如下设置：
```
public class DemoApplication extends Application {
    String ugcLicenceUrl = ""; // 填入您从控制台申请的 licence url
    String ugcKey = "";        // 填入您从控制台申请的 licence key

    @Override
    public void onCreate() {
        super.onCreate();
        TXUGCBase.getInstance().setLicence(instance, ugcLicenceUrl, ugcKey);
    }
}
```

> ?对于使用4.7版本 License 的用户，如果您升级了 SDK 到4.9版本，您可以登录控制台，单击下图的**切换到新版 License** 按钮生成对应的 License Key 和 License URL，切换后的 License 必须使用4.9及更高的版本，切换后按照上述操作集成即可。
> <img src="https://main.qcloudimg.com/raw/570c3a7bb4b6c8b2cf7fe162572b1c48.png" width=600px>

[](id:step4)
### 步骤4：打印 log
在  TXLiveBase 中可以设置 log 是否在控制台打印以及 log 的级别，具体代码如下：
- **setConsoleEnabled**
设置是否在 Android Studio 的控制台打印 SDK 的相关输出。
- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到 sdcard 上，**Android/data/com.tencent.liteav.demo/files/log/tencent/liteav** 文件夹下。如果您需要我们的技术支持，建议将此开关打开，在重现问题后提供 log 文件，非常感谢您的支持。
- **log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。
```
TXLiveBase.setConsoleEnabled(true);
TXLiveBase.setLogLevel(TXLiveConstants.LOG_LEVEL_DEBUG);
```

[](id:step5)
### 步骤5：编译运行

在工程中调用 SDK 接口，获取 SDK 版本信息，以验证工程配置是否正确。

1. **引用 SDK**：
在 MainActivity.java 中引用 SDK 的 class：
```
import com.tencent.rtmp.TXLiveBase;
```
2. **调用接口**：
在 onCreate 中调用 getSDKVersioin 接口获取版本号：
```
String sdkver = TXLiveBase.getSDKVersionStr();
Log.d("liteavsdk", "liteav sdk version is : " + sdkver);
```
3. **编译运行**：
如果前面各步骤都操作正确，Demo工程将顺利编译通过，运行之后将在 logcat 中看到如下 log 信息：
`09-26 19:30:36.547 19577-19577/ D/liteavsdk: liteav sdk version is : 7.4.9211`

[](id:que1)
### 问题排查
如果您将 SDK 导入到您的工程，编译运行出现类似以下错误：

```
Caused by: android.view.InflateException:
Binary XML file #14:Error inflating class com.tencent.rtmp.ui.TXCloudVideoView
```

可以按照以下流程来排查问题：

1. 确认是否已经将 SDK 中的 jar 包和 so 库放在 jniLibs目录下。
2. 如果您使用 aar 集成方式的完整版本，在工程目录下的 build.gradle 的 defaultConfig 里面确认下是否将 x64 架构的 so 库过滤掉。因为完整版本中连麦功能所使用的声学组件库暂时不支持 x64 架构的手机。
```
defaultConfig {
    ...   
    ndk {
        abiFilters "armeabi", "armeabi-v7a"
    }
}
```
3. 检查下混淆规则，确认已将 SDK 的相关包名加入了不混淆名单。
```
-keep class com.tencent.** { *; }
```
4. [配置](https://cloud.tencent.com/document/product/584/9366) App 打包参数。
![](https://main.qcloudimg.com/raw/b2dd9bde1cdf13ad5c77c1e00c4092aa.png)

[](id:module)
## 快速接入短视频功能模块
下述内容主要讲解如何在已有的项目中快速集成短视频 SDK，完成从录制，编辑，合成的完整过程。文中所需要的代码及资源文件均在 [资源下载](https://cloud.tencent.com/document/product/584/9366) 中 SDK 的压缩包中以及 [短视频 Demo ](https://github.com/tencentyun/UGSVSDK)提供。

[](id:integrated)
### 集成 UGCKit

[](id:UGCKit_step1)
#### 步骤1：新建工程（Empty Activity）
1. 创建一个空的 Android Studio 工程，工程名可以为 `ugc`，包名可自定义，保证新建的空工程编译通过。
2. 配置 Project 的 `build.gradle`。
```
// Top-level build file where you can add configuration options common to all sub-projects/modules.
buildscript {
    repositories {
        google()
        jcenter()

    }
    dependencies {
        # 拷贝开始
        classpath 'com.android.tools.build:gradle:3.6.1'
        # 拷贝结束
        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

allprojects {
    repositories {
        google()
        jcenter()
        # 拷贝开始
        flatDir {
            dirs 'src/main/jniLibs'
            dirs project(':ugckit').file('libs')
        }
        # 拷贝结束
        jcenter() // Warning: this repository is going to shut down soon
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}

# 拷贝开始
ext {
    compileSdkVersion = 25
    buildToolsVersion = "25.0.2"
    supportSdkVersion = "25.4.0"
    minSdkVersion = 16
    targetSdkVersion = 23
    versionCode = 1
    versionName = "v1.0"
    proguard = true
    rootPrj = "$projectDir/.."
    ndkAbi = 'armeabi-v7a'
    noffmpeg = false
    noijkplay = false
    aekit_version = '1.0.16-cloud'
    liteavSdk="com.tencent.liteav:LiteAVSDK_Professional:latest.release"
}
# 拷贝结束
```
3. 配置 app 的 build.gradle 。
```
plugins {
    id 'com.android.application'
}

android {
    # 拷贝开始
    compileSdkVersion = rootProject.ext.compileSdkVersion
    buildToolsVersion = rootProject.ext.buildToolsVersion
    # 拷贝结束
    defaultConfig {
        applicationId "com.yunxiao.dev.liteavdemo"
        # 拷贝开始
        minSdkVersion rootProject.ext.minSdkVersion
        targetSdkVersion rootProject.ext.targetSdkVersion
        versionCode rootProject.ext.versionCode
        versionName rootProject.ext.versionName
        renderscriptTargetApi = 19
        renderscriptSupportModeEnabled = true
        multiDexEnabled = true
        ndk {
            abiFilters rootProject.ext.ndkAbi
        }
         # 拷贝结束
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

    # 如果您使用的是商业版或商业版Pro，请加如下这段，基础版/精简版不需要
    packagingOptions {
        pickFirst '**/libc++_shared.so'
        doNotStrip "*/armeabi/libYTCommon.so"
        doNotStrip "*/armeabi-v7a/libYTCommon.so"
        doNotStrip "*/x86/libYTCommon.so"
        doNotStrip "*/arm64-v8a/libYTCommon.so"
    }
    # 如果您使用的是商业版或商业版Pro，请加如上这段，基础版/精简版不需要

dependencies {
    # 拷贝开始
    compile fileTree(include: ['*.jar'], dir: 'libs')
    compile fileTree(include: ['*.jar'], dir: 'src/main/jniLibs')
    compile 'com.mcxiaoke.volley:library:1.0.19'
    compile 'com.android.support:design:25.3.1'
    compile 'com.android.support:recyclerview-v7:25.3.1'
    compile 'com.google.code.gson:gson:2.3.1'
    compile 'com.github.bumptech.glide:glide:3.7.0'
    compile 'com.github.ctiao:dfm:0.4.4'
    compile project(':ugckit')
    compile 'com.android.support.constraint:constraint-layout:1.1.3'
    # 拷贝结束
}
```
4. 配置 Gradle 版本：
```
distributionUrl=https\://services.gradle.org/distributions/gradle-5.6.4-bin.zip
```



[](id:UGCKit_step2)
#### 步骤2：导入相关 module
1. 拷贝 `ugckit module` 到 您新建的工程 ugc 目录下。
2. 拷贝 `beautysettingkit module` 到 您新建的工程 ugc 目录下。
3. 在工程的 `settings.gradle`中导入 ugckit。
4. 在新建的工程 `UGC/settings.gradle` 下指明引入这几个 module：
```
include ':ugckit'
include ':beautysettingkit'
```
5. 在工程 app module 中依赖 UGCKit module：
```
compile project(':ugckit')
```

[](id:UGCKit_step3)
#### 步骤3：申请 Licence
在使用 UGCKit 之前要先设置 License，License 的获取方法请参见 [License申请](https://cloud.tencent.com/document/product/584/20333)。


[](id:fun)

### 实现录制、导入、裁剪、特效编辑功能

[](id:initialize)
#### 1. 设置 Licence，初始化 UGCKit
在 `Application.java` 中设置 Licence，初始化 UGCKit。

```
// 设置Licence
TXUGCBase.getInstance().setLicence(this, ugcLicenceUrl, ugcKey);
// 初始化UGCKit
UGCKit.init(this);
```

[](id:record)
#### 2. 视频录制
1. 新建录制 xml， 加入如下配置：
``` xml
<com.tencent.qcloud.ugckit.UGCKitVideoRecord
    android:id="@+id/video_record_layout"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```
2. 在 `res/values/styles.xml`中新建空的录制主题，继承 UGCKit 默认录制主题。
```
<style name="RecordActivityTheme" parent="UGCKitRecordStyle"/>
```
3. 新建录制 Activity ，继承 `FragmentActivity`，实现接口 `ActivityCompat.OnRequestPermissionsResultCallback`，获取 UGCKitVideoRecord 对象并设置回调方法。
```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // 必须在代码中设置主题(setTheme)或者在AndroidManifest中设置主题(android:theme)
    setTheme(R.style.RecordActivityTheme);
    setContentView(R.layout.activity_video_record);
    // 获取UGCKitVideoRecord 
    mUGCKitVideoRecord = (UGCKitVideoRecord) findViewById(R.id.video_record_layout);
    // 设置录制监听
    mUGCKitVideoRecord.setOnRecordListener(new IVideoRecordKit.OnRecordListener() {
        @Override
        public void onRecordCanceled() {
            // 录制被取消
        }

        @Override
        public void onRecordCompleted(UGCKitResult result) {
            // 录制完成回调
        }
    });
}

@Override
protected void onStart() {
    super.onStart();
    // 判断是否开启了“相机”和“录音权限”(如何判断权限，参考Github/Demo示例)
    if (hasPermission()) {
        // UGCKit接管录制的生命周期（关于更多UGCKit接管录制生命周期的方法，参考Github/Demo示例）
        mUGCKitVideoRecord.start();
    }
}

@Override
public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
    if (grantResults != null && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
        mUGCKitVideoRecord.start();
    }
}
```

**效果如下**：
![图片描述](https://main.qcloudimg.com/raw/6d2996c86edf6a796b681580f3c1fb05.png)

[](id:v_import)
####  3. 视频导入
1. 新建 xml，加入如下配置：
```xml
 <com.tencent.qcloud.ugckit.UGCKitVideoPicker
        android:id="@+id/video_picker"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
```
2. 在 `res/values/styles.xml` 中新建空的主题，继承 UGCKit 默认视频导入主题。
```
<style name="PickerActivityTheme" parent="UGCKitPickerStyle"/>
```
3. 新建 activity，继承 Activity，获取 UGCKitVideoPicker 对象，设置对象回调。
``` java
@Override
public void onCreate(Bundle icicle) {
    super.onCreate(icicle);
    // 必须在代码中设置主题(setTheme)或者在AndroidManifest中设置主题(android:theme)
    setTheme(R.style.PickerActivityTheme);
    setContentView(R.layout.activity_video_picker);
    // 获取UGCKitVideoPicker
    mUGCKitVideoPicker = (UGCKitVideoPicker) findViewById(R.id.video_picker);
    // 设置视频选择监听
    mUGCKitVideoPicker.setOnPickerListener(new IPickerLayout.OnPickerListener() {
        @Override
        public void onPickedList(ArrayList<TCVideoFileInfo> list) {
            // UGCKit返回选择的视频路径集合
        }
    });
}
```

**效果如下**：
![图片描述](https://main.qcloudimg.com/raw/a06caa5a974ff7b129255710840148e1.png)

[](id:v_cut)
#### 4. 视频裁剪
1. 新建 xml ，加入如下配置：
```xml
<com.tencent.qcloud.ugckit.UGCKitVideoCut
        android:id="@+id/video_cutter"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
```
2. 在 `res/values/styles.xml` 中新建空的主题，继承 UGCKit 默认编辑主题。
```
<style name="EditerActivityTheme" parent="UGCKitEditerStyle"/>
```
3. 新建 Activity ，实现接口 `FragmentActivity`，获取 UGCKitVideoCut 对象，并设置回调方法。
```java
@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // 必须在代码中设置主题(setTheme)或者在AndroidManifest中设置主题(android:theme)
    setTheme(R.style.EditerActivityTheme);
    setContentView(R.layout.activity_video_cut);
    mUGCKitVideoCut = (UGCKitVideoCut) findViewById(R.id.video_cutter);
    // 获取上一个界面视频导入传过来的视频源路径
    mVideoPath = getIntent().getStringExtra(UGCKitConstants.VIDEO_PATH);
    // UGCKit设置视频源路径
    mUGCKitVideoCut.setVideoPath(mVideoPath);
    // 设置视频生成的监听
    mUGCKitVideoCut.setOnCutListener(new IVideoCutKit.OnCutListener() {
        
        @Override
        public void onCutterCompleted(UGCKitResult ugcKitResult) {
            // 视频裁剪进度条执行完成后调用
        }

        @Override
        public void onCutterCanceled() {
            // 取消裁剪时被调用
        }
    });
}

@Override
protected void onResume() {
    super.onResume();
    // UGCKit接管裁剪界面的生命周期（关于更多UGCKit接管裁剪生命周期的方法，参考Github/Demo示例）
    mUGCKitVideoCut.startPlay();
}
```

**效果如下**：
![图片描述](https://main.qcloudimg.com/raw/b7ada99f174e21e09e7b9c78e96c1858.png)

[](id:v_effect_edit)
#### 5. 视频特效编辑
1. 在编辑 activity 的 xml 中加入如下配置：
``` xml
<com.tencent.qcloud.ugckit.UGCKitVideoEdit
        android:id="@+id/video_edit"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
```
2. 新建编辑 Activity ，继承 `FragmentActivity`，获取 UGCKitVideoEdit 对象并设置回调方法 。
```java
@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // 必须在代码中设置主题(setTheme)或者在AndroidManifest中设置主题(android:theme)
    setTheme(R.style.EditerActivityTheme);
    setContentView(R.layout.activity_video_editer);
    // 设置视频源路径（非必须，如果上个界面是裁剪界面，且设置setVideoEditFlag(true)则可以不用设置视频源）
    mVideoPath = getIntent().getStringExtra(UGCKitConstants.VIDEO_PATH);
    mUGCKitVideoEdit = (UGCKitVideoEdit) findViewById(R.id.video_edit);
    if (!TextUtils.isEmpty(mVideoPath)) {
        mUGCKitVideoEdit.setVideoPath(mVideoPath);
    }
    // 初始化播放器
    mUGCKitVideoEdit.initPlayer();
    mUGCKitVideoEdit.setOnVideoEditListener(new IVideoEditKit.OnEditListener() {
        @Override
        public void onEditCompleted(UGCKitResult ugcKitResult) {
            // 视频编辑完成
        }

        @Override
        public void onEditCanceled() {
            
        }
    });
}

@Override
protected void onResume() {
    super.onResume();
    // UGCKit接管编辑界面的生命周期（关于更多UGCKit接管编辑生命周期的方法，参考Github/Demo示例）
    mUGCKitVideoEdit.start();
}
```

**效果如下**：
![图片描述](https://main.qcloudimg.com/raw/dbe2669117f1015bf994705cc76deed8.jpg)

### 详细介绍

以下为各模块的详细说明：
- [视频录制](https://cloud.tencent.com/document/product/584/9369)
- [视频编辑](https://cloud.tencent.com/document/product/584/9502)
- [视频拼接](https://cloud.tencent.com/document/product/584/9503)
- [视频上传](https://cloud.tencent.com/document/product/584/15535)
- [视频播放](https://cloud.tencent.com/document/product/584/9373)
- [动效变脸（企业版）](https://cloud.tencent.com/document/product/584/13510)


[](id:que2)

## 常见问题

[](id:que2_1)

### 是否支持 AndroidX？
 因为服务客户较多，且大部分客户的工程中目前仍在使用 support 包，基于此，目前 UGCKit 暂时还是基于 support 包。但是考虑到客户对 Androidx 的需求，现提供 UGCKit 迁移 Androidx 方案文档。

为了方便说明，以腾讯云 UGSVSDK 为例，此 Demo 中同样使用了 UGCKit 模块。
1. **前提准备：**
	- 将Android Studio更新至 Android Studio 3.2及以上。
	- Gradle 插件版本改为 4.6及以上。
	<img src="https://main.qcloudimg.com/raw/4d71f185511450a40bf1e569d903d37d.png" width="700">
	- compileSdkVersion 版本升级到 28 及以上。
	- buildToolsVersion 版本改为 28.0.2 及以上。
	<img src="https://main.qcloudimg.com/raw/9a31ee56da63f6ca397a8ec2aae6564d.png" width="700">
2. **开启迁移：**
	1. 使用 Android Studio 导入项目后，从菜单栏中依次选择 **Refactor > Migrate to AndroidX**。
<img src="https://main.qcloudimg.com/raw/2df246f4fcbb616aca744c8ad65877ff.png" width="700">
	2. 单击 **Migrate**，即可将现 有项目迁移到 AndroidX。
<img src="https://main.qcloudimg.com/raw/aefcbe1331037db4e0bea585c090cf1c.png" width="700">

[](id:que2_2)
### UGCKit 编译版本错误？

- **报错信息**：
```
ERROR: Unable to find method 'org.gradle.api.tasks.compile.CompileOptions.setBootClasspath(Ljava/lang/String;)V'.
Possible causes for this unexpected error include:
```
- **问题原因**：UGCKit 使用的 Gradle 插件版本为 2.2.3 ，Gradle版本为 3.3。
- **解决方法**：请检查 ` Android Studio Gradle` 插件版本和 Gradle 版本是否匹配，具体请参见 [查看 Gradle 插件对应Gradle版本](https://developer.android.google.cn/studio/releases/gradle-plugin.html#updating-plugin)。

[](id:que2_3)
### UGCKit 包编译时出现报错？
- **报错信息**：
![](https://main.qcloudimg.com/raw/d072f6f6e92422ec1ba7c7b7b32e0733.png)
- **问题原因**：主要是 `ugckit module` 缺少  `renderscript-v8.jar`。这个库主要是对图形的处理，模糊，渲染。
- **解决方法**： `renderscript-v8.jar` 包的目录在 `\sdk\build-tools\` 里，您需在 `ugckit module` 下新建一个 libs 包，然后将 `renderscript-v8.jar` 加入 libs 包即可。

