# 快速接入腾讯云短视频SDK
本篇文档讲述了如何在已有的项目中快速集成短视频SDK，完成从录制、预览到编辑的完整过程。
文中所需要的代码及资源文件均在资源下载中SDK的压缩包中提供。

# 接入步骤
1、创建一个空的Android Studio工程，工程名为UGC，且包名与下方图片中包名(com.tencent.liteav.demo)一致，保证新建的空工程编译通过。这里注意，如果您不跟我们的包名保持一致，需要申请license。 如果没有license依然可以完成以下步骤集成UI，但部分功能会无法使用。
![](https://main.qcloudimg.com/raw/e6b08ecfca9d6d789da7cc99d501c69d.png)

2、拷贝SDK开发包中的lib_tccommon、lib_tcvideoediter、lib_tcvideorecord、lib_tcvideojoiner四个Android Studio module放入新建的工程UGC/下

- lib_tccommon ： 资源公共库
- lib_tcvideoediter：SDK开发包中短视频编辑UI组件
- lib_tcvideorecord：SDK开发包中短视频录制UI组件
- lib_tcvideojoiner：SDK开发包中短视频合成UI组件

在新建的工程UGC/settings.gradle 下指明引入这四个module

```
include ':app'
# 拷贝这段代码起始位置
include ':lib_tcvideorecord'
include ':lib_tcvideoediter'
include ':lib_tcvideojoiner'
include ':lib_tccommon'
# 拷贝这段代码结束位置
```

在新建的工程module：app的build.gradle下指明引入这四个module
```
apply plugin: 'com.android.application'

android {
    compileSdkVersion 25
    buildToolsVersion "25.0.2"
    defaultConfig {
        applicationId "ugc.demo.com.ugc"
        minSdkVersion 15
        targetSdkVersion 23
        versionCode 1
        versionName "1.0"
        // 拷贝这段代码起始位置
        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
        // 拷贝这段代码结束位置
        testInstrumentationRunner "android.support.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
    // 拷贝这段代码起始位置
    sourceSets {
        main {
            jniLibs.srcDirs = ['libs']
        }
    }
    // 拷贝这段代码结束位置
}

dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    // 拷贝这段代码起始位置
    compile project(':lib_tccommon')
    compile project(':lib_tcvideoediter')
    compile project(':lib_tcvideojoiner')
    compile project(':lib_tcvideorecord')
    // 拷贝这段代码结束位置
}
```
4、拷贝sdk：/SDK/LiteAVSDK_UGC_1.1.10.aar 到新建的工程UGC/lib_tccommon/libs/下，修改lib_tccommon:build.gradle中的SDK版本号

```
apply plugin: 'com.android.library'

android {
    compileSdkVersion 25
    buildToolsVersion "25.0.2"

    defaultConfig {
        minSdkVersion 15
        targetSdkVersion 23
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
    // 拷贝这段代码起始位置
    sourceSets {
        main {
            jniLibs.srcDirs = ['libs']
        }
    }
    // 拷贝这段代码结束位置
}

dependencies {
    compile fileTree(include: ['*.jar'], dir: 'libs')
    compile 'com.android.support:appcompat-v7:25.+'
    // 拷贝这段代码起始位置
    compile 'com.android.support:recyclerview-v7:25.+'
    // 这里注意：根据拷贝的aar文件，修改sdk的版本号
    compile(name: 'LiteAVSDK_UGC_1.1.10', ext: 'aar')
    compile files('libs/glide-3.7.0.jar')
     // 拷贝这段代码结束位置
}
```
5、修改Project:build.gradle的配置，保证使用了lib_tccommon中的sdk版本
``` 
buildscript {
    
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:2.2.3'
    }
}

allprojects {
    repositories {
        jcenter()
         // 拷贝这段代码起始位置
        flatDir {
            dirs 'libs'
            dirs project(':lib_tccommon').file('libs')
        }
        // 拷贝这段代码结束位置
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
```
6、请确保Android Gradle Plugin版本和本地Gradle版本的兼容性。

```
The versions of the Android Gradle plugin and Gradle are not compatible.
```
可以按照如下给出的代码配置，保证Gradle版本兼容性，修改gradle-wrapper.properties文件的Gradle版本

```
distributionUrl=https\://services.gradle.org/distributions/gradle-3.3-all.zip
```
7、license配置
新建DemoApplication类，用于设置license，并在AndroidManifest.xml中声明此Application

```
//DemoApplication.java 
import com.tencent.ugc.TXUGCBase;

public class DemoApplication extends Application {
    String ugcLicenceUrl = "http://download-1252463788.cossh.myqcloud.com/xiaoshipin/licence_android/TXUgcSDK.licence";
    String ugcKey = "731ebcab46ecc59ab1571a6a837ddfb6";

    @Override
    public void onCreate() {
        super.onCreate();

        TXUGCBase.getInstance().setLicence(this, ugcLicenceUrl, ugcKey);

        String string = TXUGCBase.getInstance().getLicenceInfo(this);
        Log.i("SDK", "string=" + string);
    }
}

// AndroidManifest.xml
<application
        android:name=".DemoApplication"
       ...
</application>
```

8、短视频模块的调用
在activity_main.xml中建立三个Button
```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/record"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Record" />

    <Button
        android:id="@+id/editer"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Editer" />

    <Button
        android:id="@+id/joiner"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Joiner" />
</LinearLayout>
```
在MainActivity.java中启动各模块的类即可
```
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button1 = (Button) findViewById(R.id.record);
        Button button2 = (Button) findViewById(R.id.editer);
        Button button3 = (Button) findViewById(R.id.joiner);

        button1.setOnClickListener(this);
        button2.setOnClickListener(this);
        button3.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.record:
                Intent intent1 = new Intent(this, TCVideoSettingActivity.class);
                startActivity(intent1);
                break;
            case R.id.editer:
                Intent intent2 = new Intent(this, TCVideoEditChooseActivity.class);
                startActivity(intent2);
                break;
            case R.id.joiner:
                Intent intent3 = new Intent(this, TCVideoJoinChooseActivity.class);
                startActivity(intent3);
                break;
        }
    }
}

```
9、clean工程，运行即可看到效果

# 相关文件简介
### 短视频录制

``` 
lib_tcvideorecord
└── videorecord
    ├── RecordDef.java(背景音选择接口)
    ├── TCBGMRecordAdapter.java(背景音列表适配器)
    ├── TCBGMRecordChooseLayout.java(背景音列表界面)
    ├── TCBGMRecordManager.java(背景音管理类)
    ├── TCBGMRecordView.java(录制界面的背景音操作面板)
    ├── TCVideoRecordActivity.java(录制主界面)
    ├── TCVideoRecordSmartActivity.java(UGC_Smart版本，录制主界面)
    ├── TCVideoSettingActivity.java(录制设置界面)
    └── view
        ├── ComposeRecordBtn.java(自定义的录制按钮)
        ├── MusicListView.java
        ├── RecordProgressView.java(自定义录制进度条)
        ├── TCAudioControl.java
        └── TCMusicSelectView.java
```
### 短视频编辑
``` 
└── videoediter
    ├── PictureChooseFragment.java(图片选择界面)
    ├── TCVideoEditChooseActivity.java(单视频编辑文件选择界面)
    ├── TCVideoEditerActivity.java(编辑主界面)
    ├── TCVideoEditerWrapper.java(接口类信息保存)
    ├── TCVideoPreprocessActivity.java(编辑预处理界面)
    ├── TabFragmentPagerAdapter.java(图片/视频 界面适配器)
    ├── VideoChooseFragment.java(视频文件选择界面)
    ├── bgm
    │   ├── TCBGMSettingFragment.java(背景音设置界面)
    │   ├── TCMusicAdapter.java(背景音适配器)
    │   └── utils
    │       └── TCMusicManager.java(背景音管理类)
    ├── bubble
    │   ├── TCWordEditActivity.java(气泡字幕主界面)
    │   │   ├── others
    │   │   │   └── TCWordInputDialog.java(字幕输入框)
    ├── common
    │   ├── TCConfirmDialog.java(确认对话框)
    │   ├── TCToolsView.java(编辑界面下方工具条)
    │   └── widget
    │       ├── RangeSeekBar.java(左右拖动控件)
    │       └── videotimeline(缩略图控件包)
    ├── cutter
    │   └── TCCutterFragment.java(视频裁剪设置界面)
    ├── filter
    │   └── TCStaticFilterFragment.java(静态滤镜设置界面)
    ├── motion
    │   ├── TCMotionFragment.java(动态滤镜设置界面)
    │   └── view
    │       └── TCColorfulSeekBar.java(动态滤镜带颜色的进度条)
    ├── paster
    │   ├── AnimatedPasterConfig.java(动态贴纸配置)
    │   ├── TCPasterActivity.java(贴纸界面)
    ├── time
    │   ├── TCTimeFragment.java(时间特效设置界面)
    └── transition
        └── TCTransitionFragment.java(图片转场设置界面)
```
### 短视频合成
``` 
└── videojoiner
    ├── TCVideoJoinerActivity.java(多视频合成顺序调整界面)
    ├── TCVideoJoinerPreviewActivity.java(多视频预览、生成界面)
    └── swipemenu(多视频长按拖动，左滑删除控件)
```

# 详细介绍
以下为各模块的详细说明
1. [视频录制](https://cloud.tencent.com/document/product/584/9369)
2. [视频编辑](https://cloud.tencent.com/document/product/584/9502)
3. [视频拼接](https://cloud.tencent.com/document/product/584/9503)
4. [视频上传](https://cloud.tencent.com/document/product/584/15535)
5. [视频播放](https://cloud.tencent.com/document/product/584/9373)
6. [动效变脸(商业版)](https://cloud.tencent.com/document/product/584/13510)
