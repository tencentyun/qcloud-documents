## Android 工程配置
### 1. 系统要求
SDK 支持 在 Android 4.0.3（API 15）及以上系统上运行，但只有 ( Android 4.3) API 18 以上的系统才能开启硬件编码。

### 2. 开发环境
以下是 SDK 的开发环境，App 开发环境不需要与 SDK 一致，但要保证兼容：

- Android NDK: android-ndk-r12b
- Android SDK Tools: android-sdk_25.0.2
- minSdkVersion: 15
- targetSdkVersion: 21
- Android Studio（推荐您也使用 Android Studio，当然您也可以使用 Eclipse + ADT）

### 3. 集成攻略
#### 3.1 集成攻略（aar）
##### 3.1.1. 新建工程
![](https://main.qcloudimg.com/raw/ca473c3bf484da3d7d959dbb83b192b1.png)

##### 3.1.2. 拷贝文件
将 aar 包放在工程 libs 目录下即可。

##### 3.1.3. 工程配置
- 在工程 App 目录下的 build.gradle 中，添加引用 aar 包的代码：
```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    // 导入短视频SDK aar，LiteAVSDK_UGC_x.x.xxxx 请自行修改为最新版本号
    compile(name: 'LiteAVSDK_UGC_3.9.2794', ext: 'aar')
}
```

- 在工程目录下的 build.gradle 中，添加 flatDir，指定本地仓库：
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

- 在工程目录下的 build.gradle 的 defaultConfig 里面，指定 ndk 兼容的架构：
```
defaultConfig {
    applicationId "com.tencent.liteav.demo"
    minSdkVersion rootProject.ext.minSdkVersion
    targetSdkVersion rootProject.ext.targetSdkVersion
    versionCode 1
    versionName "2.0"

    ndk {
        abiFilters "armeabi", "armeabi-v7a"
        // 如果您使用的是商业版，只能使用 armeabi 架构，即：
        // abiFilters "armeabi",
    }
}
```

- 最后编译一下工程 Rebuild Project。

#### 3.2 集成攻略（jar）
##### 3.2.1. 库说明
解压 zip 压缩包后得到 libs 目录，里面主要包含 jar 文件和 so 文件，文件清单如下：

| jar文件                           | 说明                      |
| ---------------------------- | ----------------------- |
| liteavsdk.jar                | 短视频 SDK android 核心库          |


| so文件                           | 说明                      |
| ---------------------------- | ----------------------- |
| libliteavsdk.so              | 短视频 SDK 核心组件              |
| libtxffmpeg.so               | ffmpeg 基础库（ijk 版本），用于点播播放功能，解决一些视频格式的兼容问题       |
| libtxplayer.so               | ijkplayer 开源库，用于点播播放功能，解决一些视频格式的兼容问题       |
| libtxsdl.so                  | ijkplayer 开源库，用于点播播放功能，解决一些视频格式的兼容问题        |

##### 3.2.2. 拷贝文件
如果您的工程之前没有指定过 jni 的加载路径，推荐您将刚才得到的 jar 包和 so 库拷贝到 **Demo\app\src\main\jniLibs** 目录下，这是 android studio 默认的 jni 加载目录。

如果您使用的是商业版，那么解压 zip 包后，除了 jar 包和 so 库增加了以外，还多了 assets 目录下的文件，这些是动效所需要的，需要全部拷贝到工程的 assets 目录下，参考 [动效变脸 - 工程配置](https://cloud.tencent.com/document/product/584/13510#.E5.B7.A5.E7.A8.8B.E8.AE.BE.E7.BD.AE)

##### 3.2.3. 工程配置

在工程 App 目录下的 build.gradle 中，添加引用 jar 包和 so 库的代码。

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    // 导入腾讯云短视频SDK jar
    compile fileTree(dir: 'src/main/jniLibs', includes: ['*.jar'])
}
```
##### 3.2.4. 减少 APK 体积
整个 SDK 的体积主要来自于 so 文件，这些 so 文件是 SDK 正常运行所依赖的音视频编解码库、图像处理库以及声学处理组件，如果短视频 SDK 的功能不是 App 的核心功能，您可以考虑采用在线加载的方式减少最终 apk 安装包的大小。

 **1. 上传 SO 文件**

 将 SDK 压缩包中的 so 文件上传到 COS，并记录下载地址，例如 `http://xxx-appid.cossh.myqcloud.com/so_files.zip`。

 **2. 启动准备**

 在用户启动 SDK 相关功能前，比如开始播放视频之前，先用 loading 动画提示用户“正在加载相关的功能模块”。

 **3. 下载 SO 文件**

 在用户等待过程中，App 就可以到 `http://xxx-appid.cossh.myqcloud.com/so_files.zip` 下载 so 文件，并存入应用目录下（例如应用根目录下的 files 文件夹），为了确保这个过程不受运营商 DNS 拦截的影响，请在文件下载完成后校验 so 文件的完整性。

 **4. 加载 SO 文件**

 等待所有 so 文件就位以后，调用 TXLiveBase 的 setLibraryPath 将下载的目标 path 设置给 SDK， 然后再调用 SDK 的相关功能。之后，SDK 会到这些路径下加载需要的 so 文件并启动相关功能。

#### 3.3 配置 App 权限

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
#### 3.4 License 设置
请参考 [License 申请](https://cloud.tencent.com/document/product/584/20333) 的指引申请 License 后，从 [控制台](https://console.cloud.tencent.com/vod/license) 复制 key 和 url，见下图。
![](https://main.qcloudimg.com/raw/cfbf370ecc3db1429e2d3ecf582a100c.png)
在您的应用中使用短视频功能之前（建议在 - Application onCreate() 中）进行如下设置
```
public class DemoApplication extends Application {
    String ugcLicenceUrl = "http://xxxxxxxx.cossh.myqcloud.com/xiaoshipin/licence_android/TXUgcSDK.licence"; //您从控制台申请的 licence url
    String ugcKey = "xxxxxxxxxxxxxxx";                                                                 //您从控制台申请的 licence key

    @Override
    public void onCreate() {
        super.onCreate();
        TXUGCBase.getInstance().setLicence(instance, ugcLicenceUrl, ugcKey);
    }
}
```

对于使用 4.7 版本 License 的用户，如果您升级了 SDK 到 4.9 版本，您可以登录控制台，单击下图的 **切换到新版 License** 按钮生成对应的 key 和 url，切换后的 License 必须使用 4.9 及更高的版本，切换后按照上述操作集成即可。
![](https://main.qcloudimg.com/raw/b296f9e2324806f07e0f7c91c82542ef.png)

#### 3.5 LOG 打印
在  TXLiveBase 中可以设置 log 是否在控制台打印以及 log 的级别，具体代码如下：
- **setConsoleEnabled**
设置是否在 Android Studio 的控制台打印 SDK 的相关输出。
- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到 sdcard 上的  **log / tencent / liteav** 文件夹下。
如果您需要我们的技术支持，建议将此开关打开，在重现问题后提供 log 文件，非常感谢您的支持。
- **Log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。
```
TXLiveBase.setConsoleEnabled(true);
TXLiveBase.setLogLevel(TXLiveConstants.LOG_LEVEL_DEBUG);
```


#### 3.6 编译运行

在工程中调用 SDK 接口，获取 SDK 版本信息，以验证工程配置是否正确。

##### 3.6.1 引用SDK
在 MainActivity.java 中引用 SDK 的 class：

```
import com.tencent.rtmp.TXLiveBase;
```

##### 3.6.2 调用接口
在 onCreate 中调用 getSDKVersioin 接口获取版本号：
```
String sdkver = TXLiveBase.getSDKVersionStr();
Log.d("liteavsdk", "liteav sdk version is : " + sdkver);
```
##### 3.6.3 编译运行
如果前面各步骤都操作正确，demo 工程将顺利编译通过，运行之后将在 logcat 中看到如下 log 信息：
`09-26 19:30:36.547 19577-19577/ D/liteavsdk: liteav sdk version is : 3.9.2794`

### 常见问题排查
如果您将 SDK 导入到您的工程，编译运行出现类似以下错误：

```
Caused by: android.view.InflateException:
Binary XML file #14:Error inflating class com.tencent.rtmp.ui.TXCloudVideoView
```

可以按照以下流程来排查问题：
- 确认是否已经将 SDK 中的 jar 包和 so 库放在 jniLibs目录下。
- 如果您使用 aar 集成方式的完整版本，在工程目录下的 build.gradle 的 defaultConfig 里面确认下是否将 x64 架构的 so 库过滤掉。因为完整版本中连麦功能所使用的声学组件库暂时不支持 x64 架构的手机。
```
defaultConfig {
    applicationId "com.tencent.liteav.demo"
    minSdkVersion rootProject.ext.minSdkVersion
    targetSdkVersion rootProject.ext.targetSdkVersion
    versionCode 1
    versionName "2.0"

    ndk {
        abiFilters "armeabi", "armeabi-v7a"
        // 如果您使用的是商业版，只能使用 armeabi 架构，即：
        // abiFilters "armeabi",
    }
}
```
- 检查下混淆规则，确认已将 SDK 的相关包名加入了不混淆名单。
```
-keep class com.tencent.** { *; }
```


## 快速接入功能模块
本篇文档讲述了如何在已有的项目中快速集成短视频SDK，完成从录制、预览到编辑的完整过程。
文中所需要的代码及资源文件均在 [资源下载](https://cloud.tencent.com/document/product/584/9366) 中 SDK 的压缩包中提供。

### 接入步骤
1. 创建一个空的 Android Studio 工程，工程名为 UGC，且包名与下方图片中包名(com.tencent.liteav.demo)一致，保证新建的空工程编译通过。这里注意，如果您不跟我们的包名保持一致，需要申请 License。 如果没有 License 依然可以完成以下步骤集成 UI，但部分功能会无法使用。
![](https://main.qcloudimg.com/raw/e6b08ecfca9d6d789da7cc99d501c69d.png)

2. 拷贝 SDK 开发包中的 lib_tccommon、lib_tcvideoediter、lib_tcvideorecord 及 lib_tcvideojoiner 四个 Android Studio module 放入新建的工程 UGC/ 下：
	- lib_tccommon ： 资源公共库
	- lib_tcvideoediter：SDK开发包中短视频编辑 UI 组件
	- lib_tcvideorecord：SDK开发包中短视频录制 UI 组件
	- lib_tcvideojoiner：SDK开发包中短视频合成 UI 组件
	
 在新建的工程 UGC/settings.gradle 下指明引入这四个 module：
```
include ':app'
# 拷贝这段代码起始位置
include ':lib_tcvideorecord'
include ':lib_tcvideoediter'
include ':lib_tcvideojoiner'
include ':lib_tccommon'
# 拷贝这段代码结束位置
```

	在新建的工程 module：app 的 build.gradle 下指明引入这四个 module：

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
3. 拷贝 sdk：/SDK/LiteAVSDK_UGC_1.1.10.aar 到新建的工程 UGC/lib_tccommon/libs/ 下，修改 lib_tccommon:build.gradle 中的 SDK 版本号：

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

4. 修改 Project:build.gradle 的配置，保证使用了 lib_tccommon 中的 sdk 版本：

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
5. 请确保 Android Gradle Plugin 版本和本地 Gradle 版本的兼容性。

	```
The versions of the Android Gradle plugin and Gradle are not compatible.
```
可以按照如下给出的代码配置，保证 Gradle 版本兼容性，修改 gradle-wrapper.properties 文件的 Gradle 版本

	```
distributionUrl=https\://services.gradle.org/distributions/gradle-3.3-all.zip
```
6. License 配置
新建 DemoApplication 类，用于设置 License，并在 AndroidManifest.xml 中声明此 Application。

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

7. 短视频模块的调用
在 activity_main.xml 中建立三个 Button。
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
在 MainActivity.java 中启动各模块的类即可。

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
8. clean 工程，运行即可看到效果。

### 相关文件简介
#### 短视频录制

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
#### 短视频编辑
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
#### 短视频合成
```
└── videojoiner
    ├── TCVideoJoinerActivity.java(多视频合成顺序调整界面)
    ├── TCVideoJoinerPreviewActivity.java(多视频预览、生成界面)
    └── swipemenu(多视频长按拖动，左滑删除控件)
```

### 详细介绍
以下为各模块的详细说明
1. [视频录制](https://cloud.tencent.com/document/product/584/9369)
2. [视频编辑](https://cloud.tencent.com/document/product/584/9502)
3. [视频拼接](https://cloud.tencent.com/document/product/584/9503)
4. [视频上传](https://cloud.tencent.com/document/product/584/15535)
5. [视频播放](https://cloud.tencent.com/document/product/584/9373)
6. [动效变脸(商业版)](https://cloud.tencent.com/document/product/584/13510)
