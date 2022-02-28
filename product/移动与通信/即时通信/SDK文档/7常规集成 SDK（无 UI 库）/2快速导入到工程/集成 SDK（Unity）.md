### 集成SDK（Unity）

本文主要介绍如何快速地将腾讯云即时通信 IM SDK 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

#### 开发环境要求

#### 方案一：UPM集成（推荐）

#### 修改manifest.json

![img](https://qcloudimg.tencent-cloud.cn/raw/4ea52e320700dc37770a5405ac14d1a7.jpg)

#### 修改如下

```json
{
    "dependencies":{
    "com.tencent.imsdk.unity":"1.6.4" // 指定到最新版本即可,所有版本：https://www.npmjs.com/package/com.tencent.imsdk.unity
  },
  "registry": "https://registry.npmjs.org"
}
```

#### 加载依赖

在 Unity Editor 中打开项目，等候依赖加载完毕，确认Tencent Cloud IM 已经加载完成。

![img](https://qcloudimg.tencent-cloud.cn/raw/d98dfb17bbee6c0319e370de6f2ba9dd.jpg)

#### 测试

您可 [下载测试脚本](https://imgcache.qq.com/operation/dianshi/other/Demo.1fdc6bd474aa3d12f0f3061155d4a5accdf30c7b.zip)，将文件解压后，放入项目中，并绑定 TestApi.cs 到任意场景上。

![img](https://qcloudimg.tencent-cloud.cn/raw/b4d770775523fdd76b75f1d80f07c925.jpg)

![img](https://qcloudimg.tencent-cloud.cn/raw/940da8044cd80db27d08a7b0dff45b94.png)

#### 方案二：集成unitypackage

#### 下载unity package

下载地址[Unity Package](https://comm.qq.com/im/sdk/unity_plus/im_unity_sdk_plus_v1.6.0.unitypackage)

#### 导入到项目中

通过Asset-> Import package导入下载的.unitypackage到项目中。
