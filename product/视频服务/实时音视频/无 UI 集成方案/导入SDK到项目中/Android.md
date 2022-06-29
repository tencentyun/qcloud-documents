本文介绍如何将 SDK 导入到您的项目中：
![](https://qcloudimg.tencent-cloud.cn/raw/49940081e803fb4534019ad5cb03dff8.png)

## 开发环境要求
- Android Studio 3.5+。
- Android 4.1（SDK API 16）及以上系统。

## 第一步：导入SDK

### 方案一：自动加载（aar）
TRTC SDK 已经发布到 mavenCentral 库，您可以通过配置 gradle 自动下载更新。
1. 在 dependencies 中添加 TRTCSDK 的依赖。
```
dependencies {
        implementation 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'
}
```
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
        ndk {
                abiFilters "armeabi-v7a", "arm64-v8a"
        }
}
```
>?目前 TRTC SDK 支持 armeabi-v7a 和 arm64-v8a。
3. 单击![](https://main.qcloudimg.com/raw/d6b018054b535424bb23e42d33744d03.png)**Sync Now**，自动下载 SDK 并集成到工程里。


### 方案二：下载 SDK 并手动导入
1. 下载 [SDK](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Android_latest.zip) 并解压到本地。
2. 将解压的 aar 文件拷贝到工程的 **app/libs** 目录下。
3. 在工程根目录下的 build.gradle 中，添加 **flatDir**，指定本地仓库路径。
![](https://main.qcloudimg.com/raw/3b07d38f105167ae52ffdda9a1712cec.png)
4. 在 app/build.gradle 中，添加引用 aar 包的代码。
![](https://main.qcloudimg.com/raw/a5658a2b3c888513215093a04dd76a25.png)
5. 在 app/build.gradle的defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
        ndk {
                abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
        }
}
```
>?目前 TRTC SDK 支持 armeabi ， armeabi-v7a 和 arm64-v8a。
6. 单击![](https://main.qcloudimg.com/raw/d6b018054b535424bb23e42d33744d03.png)**Sync Now**，完成 TRTC SDK 的集成工作。

## 第二步：配置 App 权限
在 AndroidManifest.xml 中配置 App 的权限，TRTC SDK 需要以下权限：
```java
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.camera.autofocus" />
```

>! 请勿设置 `android:hardwareAccelerated="false"`，关闭硬件加速之后，会导致对方的视频流无法渲染。

## 第三步：设置混淆规则
在 proguard-rules.pro 文件，将 TRTC SDK 相关类加入不混淆名单：
```java
-keep class com.tencent.** { *; }
```

[](id:using_cpp)
## 通过 C++ 接口使用 SDK（可选）
如果您更倾向于使用 C++ 接口，而不是 Java 进行开发，可以执行此步骤；如果您仅使用 Java 语言来调用 TRTC SDK，请忽略此步。
1. 首先需要根据上文的指引，通过导入 jar 和 so 库的方式集成 TRTC SDK。
2. 拷贝头文件：将 SDK 中的 C++ 头文件拷贝到项目中（路径为：`SDK/LiteAVSDK_TRTC_xxx/libs/include`），并在 CMakeLists.txt 中配置 include 文件夹路径及 so 库的动态链接。
```java
cmake_minimum_required(VERSION 3.6)

# 配置 C++ 接口头文件路径
include_directories(
        ${CMAKE_CURRENT_SOURCE_DIR}/include  # 拷贝自 SDK/LiteAVSDK_TRTC_xxx/libs/include
)

add_library(
        native-lib
        SHARED
        native-lib.cpp)

# 配置 libliteavsdk.so 动态库路径
add_library(libliteavsdk SHARED IMPORTED)
set_target_properties(libliteavsdk  PROPERTIES IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/../../../libs/${ANDROID_ABI}/libliteavsdk.so)

find_library(
        log-lib
        log)

# 配置 libliteavsdk.so 动态链接
target_link_libraries(
        native-lib
        libliteavsdk
        ${log-lib})
```
3. 使用命名空间：C++ 全平台接口的方法、类型等均定义在 trtc 命名空间中，为了让代码更加简洁，建议您直接使用 trtc 命名空间
```
using namespace trtc;
```

>?
>- 配置 Android Studio C/C++ 开发环境具体可以参考 Android Studio 官方文档：[向 Android 项目添加 C 和 C++ 代码](https://developer.android.com/studio/projects/add-native-code) 。 
>- 目前只有 TRTC 版本的 SDK 支持 C++ 接口；对于 C++ 接口的使用方式，请参见 [全平台（C++）API 概览](https://cloud.tencent.com/document/product/647/32268)。


