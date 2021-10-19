本文主要介绍如何快速地将腾讯云即时通信 IM SDK 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。
## 开发环境要求
- JDK 1.6。
- Android 4.1（SDK API 16）及以上系统。

## 集成 SDK（aar）
您可以选择使用 Gradle 自动加载的方式，或者手动下载 aar 再将其导入到您当前的工程项目中。

### 方法一：自动加载（aar）
由于 JCenter 官方将停止服务，后续的 IM SDK 会发布到 Maven Central 库，您可以通过配置 gradle 自动下载更新。
只需要用 Android Studio 打开需要集成 SDK 的工程，然后通过如下三个步骤修改 app/build.gradle 文件，就可以完成 SDK 集成：

- **第一步：添加 SDK 依赖**

 找到 app 的 build.gradle，首先在 repositories 中添加 mavenCentral() 的依赖：
```
 repositories {
        google()
        jcenter()
        // 增加 mavenCentral 仓库
        mavenCentral()
 }
```
 然后在 dependencies 中添加 IM SDK 的依赖：
 如果使用基础版 IM SDK，请添加如下依赖。
```
dependencies {
		api 'com.tencent.imsdk:imsdk:版本号'
}
```
如果使用增强版 IM SDK，请添加如下依赖。
```
dependencies {
		api 'com.tencent.imsdk:imsdk-plus:版本号'
}
```
>?“版本号”应替换为 SDK 的实际版本号，建议使用 [最新版本]( https://github.com/tencentyun/TIMSDK/tree/master/Android/IMSDK)。
>以版本号是`5.4.666`为例：
>```
dependencies {
		api 'com.tencent.imsdk:imsdk-plus:5.4.666'
}
```
>
 
- **第二步：指定 App 使用架构**
在 defaultConfig 中，指定 App 使用的 CPU 架构（从 IM SDK 4.3.118 版本开始支持 armeabi-v7a，arm64-v8a，x86，x86_64）：
```
   defaultConfig {
        ndk {
            abiFilters "arm64-v8a"
        }
    }
```

- **第三步：同步 SDK**
单击 Sync 按钮，如果您的网络连接 jcenter 没有问题，SDK 就会自动下载集成到工程里。
![](https://main.qcloudimg.com/raw/99c145e1bfdc78b1af5c6fb8cebde90b.png)


### 方法二：手动下载（aar）
如果您的网络连接 jcenter 有问题，也可以手动下载 SDK 集成到工程里：
- **第一步：下载 IM SDK**
在 Github 上可以下载到最新版本的 [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/Android/IMSDK)。

- **第二步：拷贝 IM SDK 到工程目录**
将下载到的 aar 文件拷贝到 app 工程的 **/libs** 目录下：
![](https://main.qcloudimg.com/raw/4175f483d55c2f99b99c993ada8dd5a0.png)

- **第三步：指定 App 使用架构并编译运行**
在 app/build.gradle的defaultConfig 中，指定 App 使用的 CPU 架构（从 IM SDK 4.3.118 版本开始支持 armeabi-v7a，arm64-v8a，x86，x86_64）：
```
defaultConfig {
	ndk {
		abiFilters "arm64-v8a"
	}
}
```


## 集成 SDK
如果您不想集成 aar 库，也可以通过导入 jar 和 so 库的方式集成 IM SDK：

- **第一步：下载解压 IM SDK**
在 Github 上可以 [下载](https://github.com/tencentyun/TIMSDK/tree/master/Android/IMSDK) 到最新版本的 aar 文件。解压后的目录里面主要包含 jar 文件和 so 文件夹，把其中的 **classes.jar** 重命名成 **imsdk.jar** 。
![](https://main.qcloudimg.com/raw/ecc6ae484565b0170c42698825951eba.png)

- **第二步：拷贝 SDK 文件到工程目录**
将重命名后的 jar 文件和各个架构的 so 文件分别拷贝到 Android Studio 默认加载的目录下：
![](https://main.qcloudimg.com/raw/237b44da2ec04ba87a6cef66aa0b5321.png)

- **第三步：指定 App 使用架构并编译运行**
在 app/build.gradle 的 defaultConfig 中，指定 App 使用的 CPU 架构（从 IM SDK 4.3.118 版本开始支持 armeabi-v7a，arm64-v8a，x86，x86_64）：
```
   defaultConfig {
        ndk {
            abiFilters "arm64-v8a"
        }
    }
```

## 配置 App 权限
在 AndroidManifest.xml 中配置 App 的权限，IM SDK 需要以下权限：

```
	<uses-permission android:name="android.permission.INTERNET" />
	<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
	<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

## 设置混淆规则
在 proguard-rules.pro 文件，将 IM SDK 相关类加入不混淆名单：

```
-keep class com.tencent.imsdk.** { *; }
```
