如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载服务资源压缩包。

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Crash 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-crash-1.0.0.zip)，并解压。

### 2. 集成 jar 包。
- 将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。

### 3. 如果需要上报 Native 异常，集成 Native Crash 包。
 
如果您的工程有 Native 代码（C/C++）或者集成了其他第三方 SO 库，您可以集成 [native crash 上报库](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-nativecrash-1.0.0.zip)。
 
- 如果您是采用 Eclipse 开发，将 `native crash 上报库`解压后的 `jni` 目录下的内容 拷贝到您工程您工程的 `libs` 目录。
- 如果您是采用 Android Studio 开发，将`native crash 上报库`解压后的 `jni` 目录下的内容 拷贝到 app 模块的 `main` 文件夹下的 `jniLibs` 目录下 。如果不存在该目录，请新建一个。

### 4. 修改您工程的 AndroidManifest.xml 文件。

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件：

```
<!-- 添加 Crash 需要的权限 -->
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_LOGS" />
```
