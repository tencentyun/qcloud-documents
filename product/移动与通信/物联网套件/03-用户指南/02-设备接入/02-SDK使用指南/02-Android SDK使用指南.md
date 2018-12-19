本文介绍如何基于Android SDK接入腾讯云物联网套件，实现基于 MQTT 协议的上下行请求。其中 IotSDK 是腾讯云 iotsuite 的 设备端SDK ，IotSample 是使用 IotSDK 的 demo。

##  引入SDK

###  两种引入方式

1、下载SDK，然后本地依赖

    implementation project(path: ':IotSDK')

2、直接依赖jcenter上的库

    implementation 'com.tencent.qcloud:iot-android-sdk:1.1.3'

##  编译运行Demo
在github下载Android版SDK后，使用Android Studio 打开工程`tencent-cloud-iotsuite-android`
###  配置参数
在腾讯云IoT Suite控制台创建产品与设备，选择鉴权模式**（注意，选择不同模式则需要在device_config.h中配置不同的设备参数）**，获取到对应的`MQTT Server Host、Product ID、Product key、DeviceName、DeviceSecret`参数，用于填写配置文件
- 选择鉴权模式
  ![](https://main.qcloudimg.com/raw/c6fcf2a3df74e70893962399cb0e2216.png)
- 直连模式下product相关参数*(MQTT Server Host、Product ID、Product key)*
  ![](https://main.qcloudimg.com/raw/50d1e01c991a2666e9e8c6a96148fb31.png)
- token模式下product相关参数*（MQTT Server Host、Product ID、Product key、mqtt username、mqttpassword）*
  ![](https://main.qcloudimg.com/raw/c245e861caee92fd71428d688f7732cd.png)
- 在设备管理—设备证书下获取设备相关参数*(DeviceName、DeviceSecret)*
  ![](https://main.qcloudimg.com/raw/763b931897398dc63b2e55089c014a99.png)

一个设备仅支持直连或临时token一种连接模式。
1.选择直连模式：需要把控制台获取的`mqttHost、productKey、productId、deviceName、deviceSecret、mqtt username、mqtt password`填入下列配置参数
```
//直连模式参数
    private String mDirectMqttHost = "mqtt-m2i58z3s.ap-guangzhou.mqtt.tencentcloudmq.com";
    private String mDirectProductKey = "mqtt-m2i58z3s";
    private String mDirectProductId = "iot-6xzr8ap8";
    private String mDirectDeviceName = "test_android_1";
    private String mDirectDeviceSecret = "48bf05179b6f1be3b38c89f27c804f11";
    private String mDirectUserName = "AKIDNgssgTw1pW2NahKR4oRt9D6ofNuGgSKG";
    private String mDirectPassword ="085Nmo6yhgR/TMjSPfFWP+TEVrggjVNFtAyvZUCxp0U=";
```
2.选择临时token模式：需要把控制台获取的`mqttHost、productKey、productId、deviceName、deviceSecret`填入下列配置，SDK内部会自动根据以上参数获取mqtt建连所需的username和password
```
//token模式参数
    private String mTokenMqttHost = "mqtt-5oo05hhn8.ap-guangzhou.mqtt.tencentcloudmq.com";
    private String mTokenProductKey = "mqtt-5oo05hhn8";
    private String mTokenProductId = "iot-kaqvlhxc";
    private String mTokenDeviceName = "test_android_2";
    private String mTokenDeviceSecret = "4a3a3b49c5103f8d4cfea154169f6b25";
```
###  运行Demo

在ConnectionFragment中填好配置参数后，编译运行Demo。选择连接模式并连接成功后，就可以订阅和发布topic。

##  SDK说明

腾讯云iotsuite Android SDK提供mqtt connect、disconnec、subscribe、unsubscribe、publish 能力，另外提供失败重连的参数配置，相应的调用示例可以参见Demo中的Connection.java。

###  mqtt部分

- 建立mqtt连接

        void connect(final IMqttConnectStateCallback connectStateCallback)

    IMqttConnectStateCallback用于监听连接状态变化。

- 断开mqtt连接

        void disconnect()

- 订阅topic

        void subscribe(final MqttSubscribeRequest request)

    MqttSubscribeRequest中可设置回调，监听请求结果。

- 取消订阅topic

        void unSubscribe(final MqttUnSubscribeRequest request)

    MqttUnSubscribeRequest中可设置回调，监听请求结果。

- 向topic发布消息

        void publish(final MqttPublishRequest request)

    MqttPublishRequest中可设置回调，监听请求结果。

- 监听已订阅topic发来的消息

        void setMqttMessageListener(IMqttMessageListener listener)

###  影子操作

- 获取影子

        void getShadow()

- 设备端更新影子

        void reportShadow(JSONObject report)

- 删除影子部分属性或全部属性

        void deleteShadow(JSONObject delete)

- 设置监听影子消息，必须在connect调用之后

        void setShadowMessageListener(IShadowListener shadowListener)

###  其他

- 设置log等级

        QLog.setLogLevel(QLog.QLOG_LEVEL_DEBUG);

- 自动重连逻辑

    SDK可配置minRetryTime、maxRetryTime、maxRetryTimes。

    两次重连之间的时间间隔retryInterval按2的幂次方增长，并且满足 minRetryTime<=retryInterval<=maxRetryTime，当重连次数达到maxRetryTimes后，停止重连。