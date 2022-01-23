## 什么是 TUIKit？
TUIKit 是基于 IM SDK 实现的一套 UI 组件，其包含会话、聊天、搜索、关系链、群组、音视频通话等功能，基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
<img style="width:800px" src="https://qcloudimg.tencent-cloud.cn/raw/bb1176efcf5d9242e6ee56f335fa9a62.jpg"  /> 

>?
>1、会话（TUIConversation），主要用于拉取和展示会话列表。
>2、搜索（TUISearch），主要用于搜索和展示会话或消息。
>3、聊天（TUIChat），主要用于收发和展示消息。
>4、音视频通话（TUICalling），主要用于音视频通话。
>5、关系链（TUIContact），主要用于拉取和展示好友列表。
>6、群组（TUIGroup），主要用于拉取和展示群信息。
## 如何集成 TUIKit？
### 开发环境要求
- Android Studio 3.6.1
- Gradle-5.1.1
- Android Gradle Plugin Version-3.4.0

### module 源码集成

1. 从 [ GitHub 下载](https://github.com/tencentyun/TIMSDK/tree/master/Android) `TUIKit` 源码。使 `TUIKit` 文件夹跟自己的工程文件夹同级，例如：
<img src="https://qcloudimg.tencent-cloud.cn/raw/00bc0470857b850436663d9bf2ef9164.png" width="500"/>

2. 在 `settings.gradle` 中添加：
```groovy
// 引入上层应用模块
include ':app'

// 引入内部组件通信模块 (必要模块)
include ':tuicore'
project(':tuicore').projectDir = new File(settingsDir, '../TUIKit/TUICore/tuicore')

// 引入聊天功能模块 (基础功能模块)
include ':tuichat'
project(':tuichat').projectDir = new File(settingsDir, '../TUIKit/TUIChat/tuichat')

// 引入关系链功能模块 (基础功能模块)
include ':tuicontact'
project(':tuicontact').projectDir = new File(settingsDir, '../TUIKit/TUIContact/tuicontact')

// 引入会话功能模块 (基础功能模块)
include ':tuiconversation'
project(':tuiconversation').projectDir = new File(settingsDir, '../TUIKit/TUIConversation/tuiconversation')

// 引入搜索功能模块（需要购买旗舰版套餐）
include ':tuisearch'
project(':tuisearch').projectDir = new File(settingsDir, '../TUIKit/TUISearch/tuisearch')

// 引入群组功能模块
include ':tuigroup'
project(':tuigroup').projectDir = new File(settingsDir, '../TUIKit/TUIGroup/tuigroup')

// 引入音视频通话功能模块
include ':tuicalling'
project(':tuicalling').projectDir = new File(settingsDir, '../TUIKit/TUICalling/tuicalling')
```
3. 在 `APP` 的 `build.gradle` 中添加:
```groovy
dependencies {
    api project(':tuiconversation')
    api project(':tuicontact')
    api project(':tuichat')
    api project(':tuisearch')
    api project(':tuigroup')
    api project(':tuicalling')    
}
```

4. 在 `gradle.properties` 文件中加入下行，表示自动转换三方库以兼容 `AndroidX`：
```properties
android.enableJetifier=true
```
5. 添加 `maven` 仓库，在 `root` 工程的 `build.gradle` 文件中添加：
```groovy
allprojects {
    repositories {
        mavenCentral()
        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }
    }
}
```
6. 同步工程，编译运行。工程结构预期效果如图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/510872c1232f6cf81d6678c41092164d.png" width="400"/>

## 常见问题

### 1. Manifest merger failed : Attribute application@allowBackup value=(true) from AndroidManifest.xml
`IMSDK` 中默认 `allowBackup` 的值为 `false` ，表示关闭应用的备份和恢复功能。您可以在您的 `AndroidManifest.xml` 文件中删除 `allowBackup` 属性，表示关闭备份和恢复功能；也可以在 `AndroidManifest.xml` 文件的 `application` 节点中添加 `tools:replace="android:allowBackup"` 表示覆盖 `IMSDK` 的设置，使用您自己的设置。 例如：
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.tencent.qcloud.tuikit.myapplication">

    <application
        android:allowBackup="true"
        android:name=".MApplication"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.MyApplication"
        tools:replace="android:allowBackup">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

### 2. NDK at /Users/***/Library/Android/sdk/ndk-bundle did not have a source.properties file
出现此问题可能是您使用了较高版本的 `Gradle` 和 `Gradle 插件`，您可以使用推荐的版本：
<img style="width:600px" src="https://qcloudimg.tencent-cloud.cn/raw/ae3416874722fb086abcdfc8e2ed8a39.png" />

此外，您也可以继续使用您当前版本的 `Gradle`，只需要在 `local.properties` 文件中加入您的 `NDK` 路径，例如：
`ndk.dir=/Users/***/Library/Android/sdk/ndk/16.1.4479499`

### 3. Cannot fit requested classes in a single dex file
出现此问题可能是您的 `API` 级别设置比较低，需要在 `app` 的 `build.gradle` 文件中开启 `MultiDex` 支持, 添加 `multiDexEnabled true` 和对应依赖：
```groovy
android {
    defaultConfig {
        ...
        minSdkVersion 15
        targetSdkVersion 28
        multiDexEnabled true
    }
    ...
}
dependencies {
    implementation "androidx.multidex:multidex:2.0.1"
}
```
同时，在您的 `Application` 文件中添加以下代码：
```java
public class MyApplication extends SomeOtherApplication {
    @Override
    protected void attachBaseContext(Context base) {
        super.attachBaseContext(base);
        MultiDex.install(this);
    }
}
```
