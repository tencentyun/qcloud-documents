# 应用云 Crash 服务 Android 集成指南

## 准备工作

在开始使用应用云 Crash 服务前，确保您已经完成：

 1. [安装和配置SDK](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/_Drafts/ApplicationBoard/%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Core/Android/GettingStarted.md)

## 添加 SDK

如果希望将 Crash 库集成至自己的某个项目中，可以通过 gradle 远程依赖或者 jar 包两种方式集成。

### 通过gradle远程依赖集成

如果您使用 Android Studio 作为开发工具或者使用 gradle 编译系统，**我们推荐您使用此方式集成依赖。**

#### 1. 使用jcenter作为仓库来源

在工程根目录下的 build.gradle 使用 jcenter 作为远程仓库：

```
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        ...
    }
}

allprojects {
    repositories {
         jcenter()
    }
}
```

#### 2. 添加 Crash 库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加 Crash 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-crash:1.0.0'
}
```

然后，点击您 IDE 的 gradle 同步按钮，会自动将依赖包同步到本地。

### 手动集成

如果您使用 Eclipse 作为开发工具并且使用 Ant 编译系统，您可以通过以下方式手动集成。

#### 1. 下载服务资源压缩包

下载请点击[应用云 Crash 服务资源]()，并解压。

#### 2. 集成jar包

1. 将资源文件中的 libs 目录下的文件拷贝到您工程的 libs 目录。
2. 如果您的工程有Native代码（C/C++）或者集成了其他第三方SO库，将解压后的 jniLibs 目录拷贝到您工程的 libs 目录。

#### 3. 修改您工程的 AndroidManifest.xml 文件

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件

```
<!-- 添加 Crash 需要的权限 -->
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_LOGS" />
```

## 避免混淆

如果您的应用开启了混淆，请在Proguard混淆文件中增加以下配置，避免 Crash 被混淆：

```
-dontwarn com.tencent.bugly.**
-keep public class com.tencent.bugly.**{*;}
```

## 添加符号表和mapping文件上传插件

如果您的工程使用了 so 文件或者对代码进行了混淆，您需要添加插件来上传符号表和mapping文件。

### 1. 在工程根目录下的 build.gradle 文件中添加依赖

```
buildscript {
	 ......
    dependencies {
        ......
        classpath 'com.tencent.tac:crash-plugin:1.0.0'
    }
}
```

### 2. 在您应用 module 下的 build.gradle 文件中添加插件依赖

请加在您 build.gralde 文件的头部。

```
apply plugin: 'com.android.application'
// 添加这一行
apply plugin: 'com.tencent.tac.crash'
```


## 配置服务

Crash 服务使用默认参数即可，不需要额外配置。如果您已经配置好 TACApplication 单例，这个过程已经自动完成。

### 高级配置

如果您需要自定义服务的策略，您可以使用 TACCrashOptions 修改一些具体的策略：

```
TACApplicationOptions applicationOptions = TACApplication.options();

TACCrashOptions crashOptions = applicationOptions.sub("crash");
```

具体的 API 请参考 TACCrashOptions 的API文档。

**请在 Crash 服务启动前完成它对应的参数配置。一旦服务启动，后续所有对它的参数修改都不会生效**。
