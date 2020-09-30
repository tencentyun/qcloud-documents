
C SDK 已提供 Windows 下基于 MSVC 的适配， 开发人员可以通过安装 Visio Studio 环境根据指引快速接入腾讯云物联网开发平台。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [C SDK](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c/releases)。

## 接入指引

Windows 平台接入腾讯云物联网开发平台可以分为以下3个步骤。

### 开发环境安装

获取和安装 Visio Studio 2019开发环境，详情请参见 [编译环境说明](https://cloud.tencent.com/document/product/1081/48372#windows-.E7.BC.96.E8.AF.91.E7.8E.AF.E5.A2.83)。

### 应用开发

请参见 [SDK samples](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/tree/master/samples) 目录下的例程进行开发。

### 编译并运行

1. 运行 Visual Studio，单击【打开本地文件夹】，并选择下载的 C SDK 目录。
![](https://main.qcloudimg.com/raw/b245adf8ccfe14f78c862d62516ec3c8.png)
2. 将在腾讯云物联网通信控制台创建的设备的设备信息（以密钥认证设备为例），填写到 device_info.json 中，示例代码如下：
```json
"auth_mode":"KEY",
"productId":"S3*****AZW",
"deviceName":"test_device",
"key_deviceinfo":{
    "deviceSecret":"vX6PQqa12****f5SMfs6OA6y"
}
```

3. 双击打开根目录的 CMakeLists.txt，并确认编译工具链中设置的平台为 **Windows** 和编译工具为 **MSVC**。
![](https://main.qcloudimg.com/raw/d4ef02feb3304c99dbfb02fe37996870.png)
示例代码如下：
```cmake
# 编译工具链
   #set(COMPILE_TOOLS "gcc")
   #set(PLATFORM   "linux")

   set(COMPILE_TOOLS "MSVC")
   set(PLATFORM   "windows")
```

4. Visual Studio 会自动生成 cmake 缓存，请等待 cmake 缓存生成完毕。
![](https://main.qcloudimg.com/raw/52f0f35974ad0503b6f45a09f69420ac.jpg)

5. 缓存生成完毕后，单击【生成】>【全部生成】。
![](https://main.qcloudimg.com/raw/dc985f71fdb4b882ce2d12d01c5b7e73.png)
6. 选择相应的示例运行，示例应与用户信息相对应。
![](https://main.qcloudimg.com/raw/5c3f0fe31182b8dc7b805ce7578ae0ad.jpg)

## SDK 使用参考

请参见 [C SDK 使用参考](https://cloud.tencent.com/document/product/1081/48377)。
