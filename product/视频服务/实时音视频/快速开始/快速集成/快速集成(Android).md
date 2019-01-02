本文主要介绍如何快速地将腾讯云 TRTC SDK 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。


## 开发环境要求
- Android Studio 2.0+
- Android 4.1（SDK API 16）及以上系统

## 集成 TRTC SDK
您可以选择使用 Gradle 自动加载的方式，或者先下载 SDK 再将其导入到您当前的工程项目中。

### aar集成攻略
####1 自动下载
**1.1 添加SDK依赖**  
修改 build.gradle 文件，在 dependencies 中添加 TRTCSDK 的依赖

```
//其中latest.release表示最新trtcsdk版本号
compile 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'
```

**1.2. 指定NDK架构**

在工程目录下的 build.gradle 的 defaultConfig 里面，指定 ndk 兼容的架构：

```
   defaultConfig {

        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
    }
```

**1.3. 同步 SDK**  

点击 Sync Project With Gradle Files 按钮，直到同步完成：


####2 手动集成
**2.1. 下载解压 TRTC-SDK**  
去官网下载SDK，如 LiteAVSDK_TRTC_5.0.1469.aar

**2.2. 拷贝文件**  
将 aar 包拷贝到工程 libs 目录下

**2.3. 修改工程配置**

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
- 在工程 app 目录下的 build.gradle 中，添加引用 aar 包的代码：

```
dependencies {
      compile fileTree(dir: 'libs', include: ['*.jar'])
      // 导入腾讯TRTC SDK aar
      compile(name: 'LiteAVSDK_TRTC_5.0.1469.aar', ext: 'aar')
  }
```

- 在工程目录下的 build.gradle 的 defaultConfig 里面，指定 ndk 兼容的架构：

```
   defaultConfig {
        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
    }
```


### jar集成攻略
**1. 下载解压 TRTC-SDK**

去官网下载SDK，如 LiteAVSDK_TRTC_5.0.1469.zip， 解压后得到 libs 目录，里面主要包含 so 文件和 jar 文件，文件清单如下：

| 文件名称                       | 说明                    |
| ---------------------------- | ----------------------- |
| liteavsdk.jar                | TRTC SDK 核心 JAVA JAR   |
| armeabi              			 | TRTC SDK Native 库       |
| armeabi-v7a                  | TRTC SDK Native 库       |


**2. 拷贝文件**

如果您的工程之前没有指定过 jni 的加载路径，推荐您将刚才解压的 jar 包和 armeabi， armeabi-v7a文件夹拷贝到 /src/main/jniLibs 目录下，这是 android studio 默认的 jni 加载目录。

**3. 修改工程配置**

在工程 app 目录下的 build.gradle 中，添加引用 jar 包和 so 库的代码。

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    // 导入腾讯云TRTC SDK jar
    compile fileTree(dir: 'src/main/jniLibs', includes: ['*.jar'])
}
```

## 配置 APP 权限
在 AndroidManifest.xml 中配置 APP 的权限，TRTC SDK需要以下权限：

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```


## 其它设置
### 不混淆SDK
在proguard-rules.pro文件，将TRTC SDK相关类加入不混淆名单：

```
-keep class com.tencent.** { *; }
```
## 常见问题
如果您将 SDK 导入到您的工程，编译运行出现类似以下错误：
```
No implementation found for void com.tencent.liteav.basic.log.TXCLog.nativeLogInit()
```
可以按照以下流程来排查问题：

- 如果您使用 jar 集成方式，确认是否已经将 SDK 中的 jar 包和 so 库放在 jniLibs 目录下。

- 如果您使用 aar 集成方式，在工程目录下的 build.gradle 的 defaultConfig 里面确认下是否设置正确的abiFilters。

```
 defaultConfig {
        applicationId "com.tencent.liteav.demo"
        minSdkVersion 16
        targetSdkVersion 23
        versionCode 1
        versionName "1.0"

        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
  }
```


