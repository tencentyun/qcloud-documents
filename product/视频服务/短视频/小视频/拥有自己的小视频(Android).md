### 1、快速集成小视频APP

- 小视频APP是根据SDK提供的功能完成的一个包括了短视频录制、视频编辑、视频上传、视频列表、视频播放等完整流程的APP。
- 您可以参考源码了解如何把SDK中的功能串接起来完成一个短视频APP；除了功能搭建，还包含UI代码，帮您快速集成到自己的APP中。
- 为了能快速运行小视频APP，您可以按照下面的流程编译工程。

### 2、APP源码

您可以在腾讯云官网更新 [小视频APP](https://cloud.tencent.com/document/product/454/7873) 源码

下载完源码解压后有以下几个部分：

![](https://main.qcloudimg.com/raw/940a93a3bdc7d8b132ef8967d33ef617.png)

| 文件名                             | 说明                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| LiteAVSDK_Professional_1.1.152.aar | aar 封装方式的 SDK，适用于 Android Studio 用户               |
| Demo                               | 基于 aar 方式的简化 Demo，包含简单的 UI 界面和 SDK 的主要功能演示，使用Android Studio可以快速导入并体验。 |

- 如果您的开发工具是Eclipse，选择jar + so封装方式的[SDK](https://cloud.tencent.com/document/product/454/7873)
- 如果您觉得 SDK 全量打包进 apk 会增大安装包体积，可以将 zip 包中的 so 文件上传到服务器，通过使用时再下载 so 文件的方式减少 apk 的体积，具体使用方法见 [如何减少 apk 体积](https://cloud.tencent.com/document/product/454/7877#8-.E5.87.8F.E5.B0.91-apk-.E4.BD.93.E7.A7.AF)？

### 3、 系统要求

SDK 支持 在 Android 4.0.3（API 15）及以上系统上运行，但只有 ( Android 4.3) API 18 以上的系统才能开启硬件编码。



### 4、开发环境

以下是 SDK 的开发环境，APP 开发环境不需要与 SDK 一致，但要保证兼容：

- Android NDK: android-ndk-r12b
- Android SDK Tools: android-sdk_26.0.2
  - minSdkVersion: 15
  - targetSdkVersion: 21
- Android Studio（推荐您也使用 Android Studio，当然您也可以使用 Eclipse+ADT）



### 5、集成攻略（aar）

##### 4.1 导入工程

- 使用Android Studio点击File-Import Project，选择Demo文件夹，

##### 4.2拷贝文件

- 将SDK目录下的aar文件拷贝到 libs 下

##### 4.3 工程配置

- 在工程 app 目录下的 build.gradle 中，添加引用 aar 包的代码：

```
dependencies {
  compile fileTree(dir: 'libs', include: ['*.jar'])
  // 导入腾讯云短视频 SDK aar
  compile(name: 'LiteAVSDK_Professional_1.1.152', ext: 'aar')
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
    }
}
```

- 最后编译一下工程 Rebuild Project。