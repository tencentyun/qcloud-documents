腾讯云物联网设备端 Andriod SDK 依靠安全且性能强大的数据通道，为物联网领域开发人员提供设备端快速接入云端，并和云端进行双向通信的能力。开发人员只需完成工程的相应配置即可完成设备的接入。

## 前提条件
已按照 [设备接入准备](https://cloud.tencent.com/document/product/634/14442) 创建好产品和设备。

## 引用方式
####  集成 SDK 方式

 - 依赖 maven 远程构建，示例如下：
```gr
dependencies {
			implementation 'com.tencent.iot.hub:hub-device-android:x.x.x'
}
```
>?用户可根据 [版本说明](https://cloud.tencent.com/document/product/634/48712) 把上述x.x.x设置成最新版本。
>
 - 依赖本地 SDK 源码构建：
  修改应用模块的 [build.gradle](https://github.com/tencentyun/iot-device-java/blob/master/hub/hub-android-demo/build.gradle)，使应用模块依赖源码，示例如下：
```gr
dependencies {
			implementation project(':hub:hub-device-android')
}
```

## 认证连接

编辑 [app-config.json](https://github.com/tencentyun/iot-device-java/blob/master/hub/hub-android-demo/app-config.json) 文件中的配置信息，可在 [IoTMqttFragment.java](https://github.com/tencentyun/iot-device-java/blob/master/hub/hub-android-demo/src/main/java/com/tencent/iot/hub/device/android/app/IoTMqttFragment.java) 读取对应以下数据：

``` gr
{
			"PRODUCT_ID":        "",
			"DEVICE_NAME":       "",
			"DEVICE_PSK":        "",
			"SUB_PRODUCT_ID":    "",
			"SUB_DEV_NAME":      "",
			"SUB_PRODUCT_KEY":   "",
			"TEST_TOPIC":        "",
			"SHADOW_TEST_TOPIC": "",
			"PRODUCT_KEY":       ""
 }
```

SDK 提供证书认证与密钥认证两种认证方式，需按照已创建的产品认证类型进行选择设置。
- 密钥认证须在 [app-config.json](https://github.com/tencentyun/iot-device-java/blob/master/hub/hub-android-demo/app-config.json) 配置信息中填入 PRODUCT_ID、DEVICE_NAME、DEVICE_PSK 所对应的参数。SDK 会根据设备配置信息自动生成签名，作为接入物联网通信的凭证。
- 证书认证须在 [app-config.json](https://github.com/tencentyun/iot-device-java/blob/master/hub/hub-android-demo/app-config.json) 配置信息中填入 PRODUCT_ID、DEVICE_NAME 等内容并读取设备证书、设备私钥文件的内容。读取方式分为两种：
 - 通过 AssetManager 进行读取，此时需在工程 `hub/hub-android-demo/src/main` 路径下创建 assets 目录并将设备证书、私钥放置在该目录中。
 - 通过 InputStream 进行读取，此时需传入设备证书、私钥的全路径信息。
   1. 成功读取证书文件与私钥文件之后，需在 [IoTMqttFragment.java](https://github.com/tencentyun/iot-device-java/blob/master/hub/hub-android-demo/src/main/java/com/tencent/iot/hub/device/android/app/IoTMqttFragment.java) 中设置 mDevCertName 证书名称与 mDevKeyName 私钥名称。
```
	private String mDevCertName = "YOUR_DEVICE_NAME_cert.crt";
	private String mDevKeyName  = "YOUR_DEVICE_NAME_private.key";
```
   2. 配置完成之后，在工程中调用 SDK 中 MQTT 连接的相关接口，即可完成设备的接入。
   ``` java
    mMqttConnection = new TXGatewayConnection(mContext, mBrokerURL, mProductID, mDevName, mDevPSK,null,null ,mMqttLogFlag, mMqttLogCallBack, mMqttActionCallBack);
    mMqttConnection.connect(options, mqttRequest);
   ```

