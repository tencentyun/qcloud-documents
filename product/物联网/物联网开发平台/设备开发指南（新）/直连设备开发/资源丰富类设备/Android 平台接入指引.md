

Android SDK 依赖开源社区实现的 MQTT 协议 **eclipse.paho**，并在之上封装 [数据模板协议](https://cloud.tencent.com/document/product/1081/34916) 以便更好的接入腾讯云物联网开发平台。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [iot-device-java](https://github.com/tencentyun/iot-device-java)。

## 接入指引

Android 平台接入腾讯云物联网开发平台可以分为以下2个步骤。
### 模块添加
在 App 的 build.gradle 中增加 eclipse.paho 的编译依赖：
```gradle
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    compile "org.eclipse.paho:org.eclipse.paho.client.mqttv3"
}
```

### 应用开发
可根据 [SDK](https://github.com/tencentyun/iot-device-java) 中提供的示例进行应用开发。
- 数据模板基本功能，可参见 `IoTDataTemplateFragment.java`和`DataTemplateSample.java`。
- 直连设备接入，可参见 `IoTLightFragment.java`和`LightSample.java`。
- 网关设备和子设备接入，可参见 `IoTGatewayFragment.java`、`GatewaySample.java`、`ProductLight.java`和`ProductAirconditioner.java`。

## SDK 使用参考

请参见 [Andorid SDK 使用参考](https://cloud.tencent.com/document/product/1081/48368)。

