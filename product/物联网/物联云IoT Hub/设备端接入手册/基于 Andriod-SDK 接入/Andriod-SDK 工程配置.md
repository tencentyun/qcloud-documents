## 引用方式
####  集成 SDK 方式
若不需要将 IoT SDK 运行在 service 组件中，则只需要依赖 [iot_core](https://github.com/tencentyun/iot-device-java/tree/master/hub-device-android/iot_core)。
 - 依赖 maven 远程构建，示例如下：
   ``` gr
   dependencies {
       compile 'com.tencent.iot.hub:hub-device-android-core:3.2.0-SNAPSHOT'
       compile 'com.tencent.iot.hub:hub-device-android-service:3.2.0-SNAPSHOT'
   }
   ```
>!snapshot 版本会静默更新，用户需评估设备使用时的风险。	
>
 - 依赖本地 SDK 源码构建：
   修改应用模块的 [build.gradle](https://github.com/tencentyun/iot-device-java/blob/master/hub-device-android/hub-demo/build.gradle)，使应用模块依赖 [iot_core](https://github.com/tencentyun/iot-device-java/tree/master/hub-device-android/iot_core) 和 [iot_service](https://github.com/tencentyun/iot-device-java/tree/master/hub-device-android/iot_service) 源码，示例如下：
    ```gr
   dependencies {
       implementation project(':hub-device-android:iot_core')
       implementation project(':hub-device-android:iot_service')
   }
    ```

## 认证连接

编辑 [app-config.json](https://github.com/tencentyun/iot-device-java/blob/master/hub-device-android/app-config.json) 文件中的配置信息，可在 [IoTMqttFragment.java](https://github.com/tencentyun/iot-device-java/blob/master/hub-device-android/hub-demo/src/main/java/com/tencent/iot/hub/device/android/app/IoTMqttFragment.java) 读取对应以下数据：

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

SDK 提供证书认证与密钥认证两种认证方式。
- 密钥认证须在 [app-config.json](https://github.com/tencentyun/iot-device-java/blob/master/hub-device-android/app-config.json) 配置信息中填入 PRODUCT_ID、DEVICE_NAME、DEVICE_PSK 所对应的参数。SDK 会根据设备配置信息自动生成签名，作为接入物联网通信的凭证。
- 证书认证须在 [app-config.json](https://github.com/tencentyun/iot-device-java/blob/master/hub-device-android/app-config.json) 配置信息中填入 PRODUCT_ID、DEVICE_NAME 等内容并读取设备证书、设备私钥文件的内容。读取方式分为两种：
 - 通过 AssetManager 进行读取，此时需在工程 `hub-device-android/hub-demo/src/main` 路径下创建 assets 目录并将设备证书、私钥放置在该目录中。
 - 通过 InputStream 进行读取，此时需传入设备证书、私钥的全路径信息。
   1. 成功读取证书文件与私钥文件之后，需在 [IoTMqttFragment.java](https://github.com/tencentyun/iot-device-java/blob/master/hub-device-android/hub-demo/src/main/java/com/tencent/iot/hub/device/android/app/IoTMqttFragment.java) 中设置 mDevCertName 证书名称与 mDevKeyName 私钥名称。
```
    private String mDevCertName = "YOUR_DEVICE_NAME_cert.crt";
    private String mDevKeyName  = "YOUR_DEVICE_NAME_private.key";
```
   2. 配置完成之后，在工程中调用 SDK 中 MQTT 连接的相关接口，即可完成设备的接入。
   ``` java
    mMqttConnection = new TXGatewayConnection(mContext, mBrokerURL, mProductID, mDevName, mDevPSK,null,null ,mMqttLogFlag, mMqttLogCallBack, mMqttActionCallBack);
    mMqttConnection.connect(options, mqttRequest);
   ```

