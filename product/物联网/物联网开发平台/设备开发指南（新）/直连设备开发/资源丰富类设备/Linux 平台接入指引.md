
C SDK 已提供 Ubuntu Linux 基于 gcc 的适配，开发人员安装相应软件并根据指引快速接入腾讯云物联网开发平台。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [C SDK](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c/releases)。

## 接入指引

Linux 平台接入腾讯云物联网开发平台可以分为以下3个步骤。

### 开发环境安装

>?本文演示使用 Ubuntu 的版本为 v16.04。

SDK 需要 cmake 版本在 v3.5 以上，默认安装的 cmake 版本较低，若编译失败，请单击 [下载](https://cmake.org/download/) 并参考 [安装说明](https://gitlab.kitware.com/cmake/cmake) 进行 cmake 特定版本的下载与安装。

```bash
$ sudo apt-get install -y build-essential make git gcc cmake
```

### 应用开发

可参考 [SDK samples](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based/tree/master/sample) 目录下的例程进行开发。

### 编译与运行

#### 1. 配置修改

修改 SDK 根目录下的 CMakeLists.txt 文件，并确保以下选项存在（以密钥认证设备为例）：

```cmake
set(BUILD_TYPE                   "release")
set(COMPILE_TOOLS                "gcc") 
set(PLATFORM 	                "linux")
set(FEATURE_MQTT_COMM_ENABLED ON)
set(FEATURE_AUTH_MODE "KEY")
set(FEATURE_AUTH_WITH_NOTLS OFF)
set(FEATURE_DEBUG_DEV_INFO_USED  OFF)  
```

#### 2. 执行脚本编译

- 编译库和示例
```bash
./cmake_build.sh
```
- 只编译示例（完整编译后）
```bash
./cmake_build.sh samples
```

输出的库文件、头文件及示例在`output/release`文件夹中。

#### 3. 填写设备信息

将在腾讯云物联网平台创建的设备的设备信息（以密钥认证设备为例），填写到 SDK 根目录下 device_info.json 中，示例代码如下：

```json
"auth_mode":"KEY",	
"productId":"S3ExxxxxAZW",
"deviceName":"test_device",	
"key_deviceinfo":{    
    "deviceSecret":"vX6PQqa1****6f5SMfs6OA6y"
}
```

#### 4. 运行示例

示例输出位于 `output/release/bin` 文件夹中，例如运行 data_template_sample 示例，输入 `./output/release/bin/data_template_sample` 即可。

## SDK 使用参考

请参见 [C SDK 使用参考](https://cloud.tencent.com/document/product/1081/48377)。
