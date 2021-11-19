为方便 Android 开发者调试和接入腾讯云游戏多媒体引擎产品 API，本文档主要为您介绍如何在 Android 项目工程中集成 GME SDK。

## SDK 文件准备

1. 请下载相关 Demo 及 SDK，详情请参见 [下载指引](https://cloud.tencent.com/document/product/607/18521)。
2. 解压获取到的 SDK 资源。
3. 文件夹内容 libs 为开发 SDK 资源。



<dx-alert infotype="explain" title="">
SDK 支持 在 Android 4.2 及以上系统上运行，但只有（Android 4.3）API 18 以上的系统才能开启硬件编码。
</dx-alert>



## 配置指引

#### 导入 SDK 文件

1. 将 libs 目录下的 gmesdk.jar 文件复制到 Android 工程的 libs 目录下。
2. **按照工程需求复制相应架构的库文件**，例如工程需要 armeabi-v7a 架构，请将 armeabi-v7a 目录下的库文件拷贝至工程中的 armeabi-v7a 目录下（如果工程没有 armeabi-v7a 目录，请自行创建）。

#### 工程配置

在工程 App 目录下的 build.gradle 中，添加引用库的代码。  
```
sourceSets {
        main {
            jniLibs.srcDirs = ['libs']
        }
}
```

