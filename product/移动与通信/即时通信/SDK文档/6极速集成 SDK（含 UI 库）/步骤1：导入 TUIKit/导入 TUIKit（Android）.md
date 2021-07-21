## 开发环境要求

- Android Studio 3.6.1
- Gradle-5.1.1


## 集成说明

 `TUIKit` 支持以 `module` 源码的方式集成。

### module 源码集成
[TUIKit 源码下载地址](https://github.com/tencentyun/TIMSDK/tree/master/Android/tuikit)

1. 从 `GitHub` 下载 `Demo` 源码，把其中的 `tuikit` 文件夹拷贝到自己的工程目录下，作为工程中的一个模块。

2. 在 `settings.gradle` 中添加：
```groovy
include ':tuikit'
```
3. 在 `APP` 的 `build.gradle` 中添加:
```groovy
dependencies {
    implementation project(':tuikit')
    
    ......
}
```
4. 修改 `tuikit` 的 `build.gradle` 文件，替换其中的几个版本号为 `app` 的 `build.gradle` 中的版本号，例如：
```groovy
android {
    compileSdkVersion 30

    defaultConfig {
        minSdkVersion 19
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

   ......
}
```

5. 在 `gradle.properties` 文件中加入下行，表示使用 `AndroidX` 中的类替换 `support` 中的类：
```properties
android.enableJetifier=true
```
6. 添加 `maven` 仓库，在 `root` 工程的 `build.gradle` 文件中添加：
```properties
allprojects {
    repositories {
        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }

        ......
    }
}
```
7. 同步工程，编译运行。

## 初始化

在 `Application` 的 `onCreate` 中初始化：

```java
public class DemoApplication extends Application {

    public static final int SDKAPPID = 0; // 您的 SDKAppID

    @Override
    public void onCreate() {
        super.onCreate();

       // 配置 Config，请按需配置
       TUIKitConfigs configs = TUIKit.getConfigs();
       configs.setSdkConfig(new V2TIMSDKConfig());
       configs.setCustomFaceConfig(new CustomFaceConfig());
       configs.setGeneralConfig(new GeneralConfig());

       TUIKit.init(this, SDKAPPID, configs);
    }
}
```

`init` 方法的说明：

```java
/**
 * TUIKit 的初始化函数
 *
 * @param context  应用的上下文，一般为对应应用的 ApplicationContext
 * @param sdkAppID 您在腾讯云注册应用时分配的 SDKAppID
 * @param configs  TUIKit 的相关配置项，一般使用默认即可
 */
public static void init(Context context, int sdkAppID, TUIKitConfigs configs)
```

