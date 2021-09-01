

腾讯云物联网设备端 Java SDK 依靠安全且性能强大的数据通道，为物联网领域开发人员提供设备端快速接入云端，并和云端进行双向通信的能力。开发人员只需完成工程的相应配置即可完成设备的接入。

## 前提条件
已按照 [设备接入准备](https://cloud.tencent.com/document/product/634/14442) 创建好产品和设备。
## 引用方式
- 如果您需要通过 jar 引用方式进行项目开发，可在 module 目录下的 `build.gradle` 中添加依赖，如下依赖：
```
dependencies {
    ...
    implementation 'com.tencent.iot.hub:hub-device-java:x.x.x'
}
```
>?用户可根据 [版本说明](https://cloud.tencent.com/document/product/634/48713) 把上述x.x.x设置成最新版本。
- 如果您需要通过代码集成方式进行项目开发，可访问 [Github](https://github.com/tencentyun/iot-device-java/tree/master/hub/hub-device-java) 下载 Java SDK 源码。

## 认证连接 ##

设备的身份认证支持两种认证方式，密钥认证和证书认证：
- 若使用密钥认证方式，需 ProductID，DevName 和 DevPSK。
- 若使用证书认证方式，需 ProductID，CertFile 和 PrivateKeyFile。

认证连接示例代码如下：
``` 
private String mProductID = "YOUR_PRODUCT_ID";
private String mDevName = "YOUR_DEVICE_NAME";
private String mDevPSK = "YOUR_DEV_PSK";
private String mCertFilePath = null;
private String mPrivKeyFilePath = null;
TXMqttConnection mqttconnection = new TXMqttConnection(mProductID, mDevName, mDevPSK, new callBack());
mqttconnection.connect(options, null);
try {
		Thread.sleep(20000);
} catch (InterruptedException e) {
	// TODO Auto-generated catch block
	e.printStackTrace();
}
mqttconnection.disConnect(null);
```
