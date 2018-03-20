##  开发准备

开发前请前往github下载最新版C-SDK：https://github.com/tencentyun/tencent-cloud-iotsuite-embedded-c.git

## 开发环境

1.安装 cmake 工具 http://www.cmake.org/download/

2.在腾讯云 IoT Suite 控制台创建产品与设备，选择鉴权模式**（注意，选择不同模式则需要在device_config.h中配置不同的设备参数）**，获取到对应的`MQTT Server Host、Product ID、Product key、DeviceName、DeviceSecret`参数，用于填写配置文件

- 选择鉴权模式

![](https://main.qcloudimg.com/raw/c6fcf2a3df74e70893962399cb0e2216.png)

- 直连模式下product相关参数*(MQTT Server Host、Product ID、Product key)*

  ![](https://main.qcloudimg.com/raw/50d1e01c991a2666e9e8c6a96148fb31.png)


- token模式下product相关参数*（MQTT Server Host、Product ID、Product key、mqtt username、mqttpassword）*

  ![](https://main.qcloudimg.com/raw/c245e861caee92fd71428d688f7732cd.png)


- 在设备管理页面中选择设备—设备证书下获取设备相关参数*(DeviceName、DeviceSecret)*

![](https://main.qcloudimg.com/raw/763b931897398dc63b2e55089c014a99.png)



3.打开`examples/linux/tc_iot_device_config.h`配置文件，配置设备参数

- 必填项

```

// 以下配置需要先在官网创建产品和设备，然后获取相关信息更新~

// MQ服务地址，可以在产品“基本信息”->“mqtt链接地址”位置找到。

#define TC_IOT_CONFIG_SERVER_HOST "<mqtt-xxx.ap-guangzhou.mqtt.tencentcloudmq.com>"

// MQ服务端口，直连一般为1883，无需改动

#define TC_IOT_CONFIG_SERVER_PORT 1883

// 产品id，可以在产品“基本信息”->“产品id”位置找到

#define TC_IOT_CONFIG_DEVICE_PRODUCT_ID "<iot-xxx>"

// 设备密钥，可以在产品“设备管理”->“设备证书”->“Device Secret”位置找到

#define TC_IOT_CONFIG_DEVICE_SECRET "<0000000000000000>"

// 设备名称，可以在产品“设备管理”->“设备名称”位置找到

#define TC_IOT_CONFIG_DEVICE_NAME "<device001>"

// client id，

// 由两部分组成，组成形式为“Instanceid@DeviceID”，ClientID 的长度不超过 64个字符

// ，请不要使用不可见字符。其中

// Instanceid 为 IoT MQ 的实例 ID，可以在“基本信息”->“产品 key”位置找到。

// DeviceID 为每个设备独一无二的标识，由业务方自己指定，需保证全局唯一，例如，每个

// 传感器设备的序列号，或者设备名称等。

#define TC_IOT_CONFIG_DEVICE_CLIENT_ID "mqtt-xxx@" TC_IOT_CONFIG_DEVICE_NAME 
```

- 选填项（仅在选择直连模式时填写）

将控制台获取到的mqtt username,mqtt password填写到配置文件中的如下位置

```

#define TC_IOT_CONFIG_DEVICE_USER_NAME ""

#define TC_IOT_CONFIG_DEVICE_PASSWORD ""

```



### 编译及运行

1.执行下面的命令，编译示例程序：



```shell

cd tencent-cloud-iotsuite-embedded-c

mkdir -p build

cd build

cmake ../

make

```



2.编译后，build目录下的关键输出及说明如下：



```shell

bin

|-- demo_mqtt               # MQTT 连接云服务演示程序

|-- demo_shadow             # Shadow 影子设备操作演示程序

lib

|-- libtc_iot_suite.a       # SDK 的核心层, libtc_iot_hal、libtc_iot_common 提供连接云服务的能力

|-- libtc_iot_common.a      # SDK 基础工具库，负责http、json、base64等解析和编解码功能

|-- libtc_iot_hal.a         # SDK 的硬件及操作系统抽象，负责内存、定时器、网络交互等功能

```



3.执行示例程序：



```shell

cd bin

# 运行demo程序

./demo_mqtt

# or

./demo_shadow

```



### C-SDK的API功能列表

以下为V1.0.6版本的C-SDK所提供的功能与API LIST，用户可基于接口编写业务逻辑，封装AT命令，更加详细的说明请查看`include/tc_iot_export.h`中的注释。

##### 1.日志接口

| 序号   | 函数名                      | 说明        |
| ---- | ------------------------ | --------- |
| 1    | tc_iot_set_log_level     | 设置打印的日志等级 |
| 2    | tc_iot_get_log_level     | 返回日志输出的等级 |
| 3    | tc_iot_log_level_enabled | 返回日志输出的等级 |



##### 2.MQTT接口

| 序号   | 函数名                             | 说明                                 |
| ---- | ------------------------------- | ---------------------------------- |
| 1    | tc_iot_mqtt_client_construct    | 构造 MQTT client，并连接MQ服务器            |
| 2    | tc_iot_mqtt_client_destroy      | 关闭 MQTT client 连接，并销毁 MQTT client  |
| 3    | tc_iot_mqtt_client_yield        | 在当前线程为底层 MQTT client，让出一定 CPU 执行时间 |
| 4    | tc_iot_mqtt_client_publish      | 向指定的 Topic 发布消息                    |
| 5    | tc_iot_mqtt_client_subscribe    | 订阅指定 Topic 的消息                     |
| 6    | tc_iot_mqtt_client_unsubscribe  | 取消订阅已订阅的 Topic                     |
| 7    | tc_iot_mqtt_client_is_connected | 判断 MQTT client 目前是否已连接             |
| 8    | tc_iot_mqtt_client_disconnecd   | 断开 MQTT client 与服务端的连接             |

