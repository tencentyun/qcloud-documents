## 概述

C SDK 已经提供了 Windows 下基于 MSVC 的适配， 开发人员可以通过安装 Visio Studio 环境根据指引快速接入腾讯云物联网开发平台。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [C-SDK](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c)。

## 接入指引

Windows 平台接入腾讯云物联网开发平台可以分为以下3个步骤：

1. 开发环境安装
2. 应用开发
3. 编译并运行

### 开发环境安装

获取和安装 Visio Studio 2019开发环境

1.请访问 [Visual Studio 下载网站](https://visualstudio.microsoft.com/zh-hans/downloads/)，下载并安装 Visio Studio 2019，本文档下载安装的是16.2版本 Community。

![](https://main.qcloudimg.com/raw/2fd5a35c66683b62f09a93575ad29036.png)

2.选择【使用 C++ 的桌面开发】，并确保勾选【用于 Windows 的 C++ CMAKE 工具】。

![](https://main.qcloudimg.com/raw/45914188fe5b51fc8b89cca7d9d03f02.png)

### 应用开发

可参考 SDK samples 目录下的例程进行开发。

### 编译并运行

1.运行 Visual Studio，选择【打开本地文件夹】，并选择下载的 C SDK 目录。

![](https://main.qcloudimg.com/raw/b245adf8ccfe14f78c862d62516ec3c8.png)

2.将在腾讯云物联网通信控制台创建的设备的设备信息（以密钥认证设备为例），填写到 device_info.json 中，示例代码如下：

```json
"auth_mode":"KEY",
"productId":"S3xxxxxAZW",
"deviceName":"test_device",
"key_deviceinfo":{
    "deviceSecret":"vX6PQqa12****f5SMfs6OA6y"
}
```

3.双击打开根目录的 CMakeLists.txt，并确认编译工具链中设置的平台为 **Windows** 和编译工具为 **MSVC**。

![](https://main.qcloudimg.com/raw/d4ef02feb3304c99dbfb02fe37996870.png)

```cmake
# 编译工具链
   #set(COMPILE_TOOLS "gcc")
   #set(PLATFORM   "linux")

   set(COMPILE_TOOLS "MSVC")
   set(PLATFORM   "windows")
```

4.Visual Studio 会自动生成 cmake 缓存，请等待 cmake 缓存生成完毕。

![](https://main.qcloudimg.com/raw/52f0f35974ad0503b6f45a09f69420ac.jpg)

5.缓存生成完毕后，选择【生成】>【全部生成】。

![](https://main.qcloudimg.com/raw/dc985f71fdb4b882ce2d12d01c5b7e73.png)

6.选择相应的示例运行，示例应与用户信息相对应。

![](https://main.qcloudimg.com/raw/5c3f0fe31182b8dc7b805ce7578ae0ad.jpg)

## SDK 使用参考

请参见[C SDK 使用参考](设备开发指南\设备端SDK说明\SDK 使用参考\C SDK 使用参考\C SDK 使用参考)。
