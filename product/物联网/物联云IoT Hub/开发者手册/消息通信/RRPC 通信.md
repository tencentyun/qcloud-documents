
## 功能概述

因MQTT 协议基于发布/订阅的异步通信模式，服务器控制设备后，将无法同步感知设备的返回结果。为解决此问题，物联网通信平台利用 RRPC（Revert RPC）实现同步通信机制。

## 通信原理

### 通信 Topic

* 订阅消息 Topic： `$rrpc/rxd/${productID}/${deviceName}/+`用于订阅云端下发（下行）的 RRPC 请求消息。
* 请求消息 Topic：`$rrpc/rxd/${productID}/${deviceName}/${processID}`用于云端发布（下行）RRPC 请求消息。
* 应答消息 Topic：`$rrpc/txd/${productID}/${deviceName}/${processID}`用于发布（上行）RRPC 应答消息。

>? 
- `${productID}`：产品 ID。
- `${deviceName}`：设备名称。
- `${processID}`： 服务器生成的唯一的消息 ID，用来标识不同 RRPC 消息。可以通过 RRPC 应答消息中携带的 processID 找到对应的 RRPC 请求消息。


### 通信流程

1. 设备端订阅 RRPC 订阅消息 Topic。
2. 服务器通过调用 [PublishRRPCMessage](https://cloud.tencent.com/document/product/634/47078) 接口发布 RRPC 请求消息。
3. 设备端接收到消息之后截取请求消息 Topic 中云端下发的 processID，设备将应答消息 Topic 的 processID 设置为截取的 processID，并向应答消息 Topic 发布设备的返回消息 。
4. 物联网通信平台接收到设备端返回消息之后，根据 processID 对消息进行匹配并将设备返回消息发送给服务器。

>! **RRPC 请求10s超时**，即10s内设备端没有应答就认为请求超时。

流程示意图如下：
![image.png](https://main.qcloudimg.com/raw/1e83a60cb7b6438ebb5927b7237b77ba.png)

## RRPC 通信示例

示例为基于 Linux 平台利用设备端 [C-SDK](https://cloud.tencent.com/document/product/634/11928) 完成接入，并结合腾讯云 API Explorer 工具完成接口的调用，具体使用步骤如下。

### 控制台创建设备

#### 创建产品和设备

请参考 [设备互通](https://cloud.tencent.com/document/product/634/11913)  创建空调产品，并创建 airConditioner1 空调设备。

### 编译运行示例程序（以密钥认证设备为例）

#### 1. 编译 SDK

修改`CMakeLists.txt`确保以下选项存在：

```
set(BUILD_TYPE                   "release")
set(COMPILE_TOOLS                "gcc") 
set(PLATFORM 	                 "linux")
set(FEATURE_MQTT_COMM_ENABLED ON)
set(FEATURE_RRPC_ENABLED ON)
set(FEATURE_AUTH_MODE "KEY")
set(FEATURE_AUTH_WITH_NOTLS OFF)
set(FEATURE_DEBUG_DEV_INFO_USED  OFF)
```

执行脚本编译：

```
./cmake_build.sh 
```

示例输出`rrpc_sample`位于`output/release/bin`文件夹中。

#### 2. 填写设备信息

将上面创建的 airConditioner1 设备的设备信息填写到 JSON 文件`aircond_device_info1.json`中:

```
{
    "auth_mode":"KEY",	
    "productId":"KL4J2****8",
    "deviceName":"airConditioner1",	
    "key_deviceinfo":{    
        "deviceSecret":"zOZXUaycuwleP****78dBA=="
    }
}
```

#### 3. 执行`rrpc_sample`示例程序

可以看到设备airConditioner1订阅了RRPC消息，然后处于等待状态。

```
./rrpc_sample -c ./aircond_device_info1.json -l 1000
INF|2020-08-03 23:57:55|qcloud_iot_device.c|iot_device_info_set(50): SDK_Ver: 3.2.0, Product_ID: KL4J2****8, Device_Name: airConditioner1
DBG|2020-08-03 23:57:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(200): Setting up the SSL/TLS structure...
DBG|2020-08-03 23:57:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(242): Performing the SSL/TLS handshake...
DBG|2020-08-03 23:57:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(243): Connecting to /KL4J2****8.iotcloud.tencentdevices.com/8883...
INF|2020-08-03 23:57:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(265): connected with /KL4J2****8.iotcloud.tencentdevices.com/8883...
INF|2020-08-03 23:57:56|mqtt_client.c|IOT_MQTT_Construct(113): mqtt connect with id: 2**** success
INF|2020-08-03 23:57:56|rrpc_sample.c|main(206): Cloud Device Construct Success
DBG|2020-08-03 23:57:56|mqtt_client_subscribe.c|qcloud_iot_mqtt_subscribe(142): topicName=$rrpc/rxd/KL4J2****8/airConditioner1/+|packet_id=****
INF|2020-08-03 23:57:56|rrpc_sample.c|_mqtt_event_handler(49): subscribe success, packet-id=*****
DBG|2020-08-03 23:57:56|rrpc_client.c|_rrpc_event_callback(104): rrpc topic subscribe success
```

#### 4. 调用云 API `PublishRRPCMessage` 发送 RRPC 请求消息

打开腾讯云 [API控制台](https://console.cloud.tencent.com/api/explorer?Product=iotcloud&Version=2018-06-14&Action=PublishRRPCMessage&SignVersion=)，填写个人密钥和设备参数信息，选择在线调用并发送请求。
![](https://main.qcloudimg.com/raw/6b0b68f49c04f3dc35c253bbeb373132.png)

#### 5. 观察 RRPC 请求消息

观察设备 airConditioner1 的打印输出，可以看到已经收到 RRPC 请求消息，`process id`为***。

```
DBG|2020-08-04 00:07:36|rrpc_client.c|_rrpc_message_cb(85): topic=$rrpc/rxd/KL4J2****8/airConditioner1/***
INF|2020-08-04 00:07:36|rrpc_client.c|_rrpc_message_cb(86): len=6, topic_msg=closed
INF|2020-08-04 00:07:36|rrpc_client.c|_rrpc_get_process_id(76): len=3, process id=***
INF|2020-08-04 00:07:36|rrpc_sample.c|_rrpc_message_handler(137): rrpc message=closed
```

#### 6. 观察RRPC应答消息

观察设备 airConditioner1 的打印输出，可以看到已经处理了 RRPC 请求消息，并回复了 RRPC 应答消息，`process id`为***。

```
DBG|2020-08-04 00:07:36|mqtt_client_publish.c|qcloud_iot_mqtt_publish(340): publish packetID=0|topicName=$rrpc/txd/KL4J2****8/airConditioner1/***|payload=ok
```

#### 7. 观察服务器响应结果

观察服务器的响应结果，可以看到已经收到了 RRPC 应答消息。`MessageId`为\*\*\*，`Payload`经过`base64`编码后为****，其与客户端实际应答消息经过`base64`编码后一致。可以确认收到了应答消息。
![](https://main.qcloudimg.com/raw/4ace5de4a2c348054665c8aed16135e2.png)



