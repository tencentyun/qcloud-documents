## 概述

腾讯云物联网开发平台针对不同的设备开发场景，提供了多版本语言的设备 SDK 供客户使用：

|SDK|说明|应用场景|使用参考|
|---|---|---|---|
|[qcloud-iot-explorer-sdk-embedded-c](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c)|设备端C语言SDK|面向基于C语言开发的平台，提供多种平台下接入并使用物联网开发平台的适配指引|[C SDK 使用参考](设备开发指南\设备端SDK说明\SDK 使用参考\C SDK 使用参考\C SDK 使用参考)|
|[qcloud-iot-explorer-5G-sdk-embedded](https://github.com/tencentyun/qcloud-iot-explorer-5G-sdk-embedded)|设备端C语言SDK-5G|面向基于C语言的开发平台，在物联网开发平台的基础上引入5G和边缘计算特性|[C SDK 5G 使用参考](暂缺)|
|[iot-device-java](https://github.com/tencentyun/iot-device-java)|设备端Java语言SDK|面向基于Java语言开发的平台，提供安卓等平台下接入并使用物联网开发平台的示例|<li>[Android SDK 使用参考](设备开发指南\设备端SDK说明\SDK 使用参考\C SDK 使用参考\Android SDK 使用参考)<li>[Java SDK 使用参考](设备开发指南\设备端SDK说明\SDK 使用参考\C SDK 使用参考\Java SDK 使用参考)|
|[qcloud-iot-sdk-tencent-at-based](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based)|设备端AT模组SDK|面向基于腾讯云定制AT模组开发的平台，提供MCU+腾讯定制AT模组接入物联网开发平台的示例|[AT SDK 使用参考](设备开发指南\设备端SDK说明\SDK 使用参考\C SDK 使用参考\AT SDK 使用参考)|
|[qcloud-iot-esp-wifi](https://github.com/tencentyun/qcloud-iot-esp-wifi)|设备端ESP8266 SDK|面向基于ESP8266开发的平台，提供腾讯云ESP8266定制固件接入流程，以及SoftAp、SmartConfig等多种配网协议接入腾讯连连小程序的示例|[ESP8266 SDK 使用参考](设备开发指南\设备端SDK说明\SDK 使用参考\C SDK 使用参考\ESP8266 SDK 使用参考)|

## 代码托管

### C SDK 代码托管

- 自 V3.1.0 版本开始，使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c.git) 托管 C 设备 SDK 代码。
- 请下载最新版 [C-SDK](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c/releases)。
- SDK 3.1.0之前的 C SDK 版本 [访问此处](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases)。

>! V3.1.0之前的版本相较于3.1.0及以后的版本代码 Git 路径不一样，同时与平台交互协议有较大区别。

### AT SDK 代码托管

在 iot-explorer 平台创建产品和设备后，选择基于 MQTT AT 定制模组开发的方式，会自动生成 MCU 侧的 [AT SDK](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based.git) 代码，并且把在平台创建的数据模板和事件生成了对应的配置及初始化代码。

### ESP8266 SDK 代码托管

ESP8266 SDK 使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c) 托管代码。

### Android SDK 代码托管

自 V3.1.0 版本开始，使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-sdk-android) 托管 Android 设备 SDK 代码。

### Java SDK 代码托管

Java SDK 使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-sdk-android) 托管 Java 设备 SDK 代码。

### C SDK 5G 代码托管

- 腾讯云物联开发平台 （IoT Explorer） 5G SDK 是腾讯5G物联开发套件的设备端组件，通过与 IoT Explorer 配合，为宽带物联应用提供5G模组远程运维，接入腾讯边缘接入和网络加速平台（TSEC）实现 VPN 组网，空口加速等功能，降低用户使用5G网络及边缘计算的门槛。
- 自 V0.1.0 版本开始，使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-5G-sdk-embedded) 托管 5G SDK 代码。
