本文档主要介绍如何在腾讯云物联网通信 IoT Hub 控制台创建设备和权限，并结合 C-SDK 的 **mqtt_sample** 快速体验设备端通过 MQTT 协议连接到腾讯云 IoT Hub，进行消息发送和接收。

## 控制台操作

### 创建产品和设备
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，单击左侧菜单【产品列表】。
2. 进入产品列表页面，单击【创建新产品】。
3. 在弹出的添加新产品页面中，选择节点类型和产品类型，输入产品名称，选择认证方式和数据格式，并输入产品描述，
然后单击【确定】。（对于普通直连设备，可按下图选择）
![](https://main.qcloudimg.com/raw/1c76747cd324aa3b25810f055cd1bf1a.jpg)
4. 产品创建完成后，在生成的产品页面下，单击【设备列表】。
5. 在设备列表页面，单击【添加新设备】。
 - 如果产品认证方式为证书认证，输入设备名称成功后，切记单击弹窗中的【下载按钮】，下载所得包中的设备密钥文件和设备证书用于设备连接物联网通信的鉴权。
![](https://main.qcloudimg.com/raw/d49979433cab6852b2919f049e818a5c.png)
 - 如果产品认证方式为密钥认证，输入设备名称成功后，会在弹窗中显示新添加设备的密钥。
![](https://main.qcloudimg.com/raw/b544ebdd175993147a71a4dfe2af2b80.jpg)





### 创建 Topic
1. 在生成的产品页面下，单击【权限列表】。
2. 进入权限列表页面，单击【添加 Topic 权限】。
3. 在弹出的 Topic 权限页面中，输入 data，并设置操作权限为**发布和订阅**，单击【确定】
![](https://main.qcloudimg.com/raw/1a7fdffc12b9154e6455e7c2cbdecc22.jpg)
4. 随后将会创建出`productID/\${deviceName}/data`的 Topic，在产品页面的权限列表中即可查看该产品的所有权限。


## 编译运行示例程序

下面讲述在 Linux 环境编译运行 mqtt_sample 示例（以密钥认证设备为例）

#### 1. 编译 SDK
（1）修改 CMakeLists.txt 确保以下选项存在：
```
set(BUILD_TYPE                   "release")
set(COMPILE_TOOLS                "gcc") 
set(PLATFORM 	                "linux")
set(FEATURE_MQTT_COMM_ENABLED ON)
set(FEATURE_AUTH_MODE "KEY")
set(FEATURE_AUTH_WITH_NOTLS OFF)
set(FEATURE_DEBUG_DEV_INFO_USED  OFF)
```
（2）执行脚本编译。
```
./cmake_build.sh 
```
（3）示例输出位于`output/release/bin`文件夹中。

#### 2. 填写设备信息
将上面在腾讯云物联网 IoT Hub 创建的设备的设备信息，填写到 device_info.json 中。
```
"auth_mode":"KEY",	
"productId":"S3EUVBRJLB",
"deviceName":"test_device",	
"key_deviceinfo":{    
"deviceSecret":"vX6PQqazsGsMyf5SMfs6OA6y"
    }
```

#### 3. 执行 mqtt_sample 示例程序
```
./output/release/bin/mqtt_sample 
INF|2019-09-12 21:28:20|device.c|iot_device_info_set(67): SDK_Ver: 3.1.0, Product_ID: S3EUVBRJLB, Device_Name: test_device
DBG|2019-09-12 21:28:20|HAL_TLS_mbedtls.c|HAL_TLS_Connect(204): Setting up the SSL/TLS structure...
DBG|2019-09-12 21:28:20|HAL_TLS_mbedtls.c|HAL_TLS_Connect(246): Performing the SSL/TLS handshake...
DBG|2019-09-12 21:28:20|HAL_TLS_mbedtls.c|HAL_TLS_Connect(247): Connecting to /S3EUVBRJLB.iotcloud.tencentdevices.com/8883...
INF|2019-09-12 21:28:20|HAL_TLS_mbedtls.c|HAL_TLS_Connect(269): connected with /S3EUVBRJLB.iotcloud.tencentdevices.com/8883...
INF|2019-09-12 21:28:20|mqtt_client.c|IOT_MQTT_Construct(125): mqtt connect with id: p8t0W success
INF|2019-09-12 21:28:20|mqtt_sample.c|main(303): Cloud Device Construct Success
DBG|2019-09-12 21:28:20|mqtt_client_subscribe.c|qcloud_iot_mqtt_subscribe(138): topicName=$sys/operation/result/S3EUVBRJLB/test_device|packet_id=1932
INF|2019-09-12 21:28:20|mqtt_sample.c|_mqtt_event_handler(71): subscribe success, packet-id=1932
DBG|2019-09-12 21:28:20|system_mqtt.c|_system_mqtt_sub_event_handler(80): mqtt sys topic subscribe success
DBG|2019-09-12 21:28:20|mqtt_client_publish.c|qcloud_iot_mqtt_publish(337): publish packetID=0|topicName=$sys/operation/S3EUVBRJLB/test_device|payload={"type": "get", "resource": ["time"]}
DBG|2019-09-12 21:28:20|system_mqtt.c|_system_mqtt_message_callback(63): Recv Msg Topic:$sys/operation/result/S3EUVBRJLB/test_device, payload:{"type":"get","time":1568294900}
INF|2019-09-12 21:28:21|mqtt_sample.c|main(316): system time is 1568294900
DBG|2019-09-12 21:28:21|mqtt_client_subscribe.c|qcloud_iot_mqtt_subscribe(138): topicName=S3EUVBRJLB/test_device/data|packet_id=1933
INF|2019-09-12 21:28:21|mqtt_sample.c|_mqtt_event_handler(71): subscribe success, packet-id=1933
DBG|2019-09-12 21:28:21|mqtt_client_publish.c|qcloud_iot_mqtt_publish(329): publish topic seq=1934|topicName=S3EUVBRJLB/test_device/data|payload={"action": "publish_test", "count": "0"}
INF|2019-09-12 21:28:21|mqtt_sample.c|_mqtt_event_handler(98): publish success, packet-id=1934
INF|2019-09-12 21:28:21|mqtt_sample.c|on_message_callback(195): Receive Message With topicName:S3EUVBRJLB/test_device/data, payload:{"action": "publish_test", "count": "0"}
INF|2019-09-12 21:28:22|mqtt_client_connect.c|qcloud_iot_mqtt_disconnect(437): mqtt disconnect!
INF|2019-09-12 21:28:22|system_mqtt.c|_system_mqtt_sub_event_handler(98): mqtt client has been destroyed
INF|2019-09-12 21:28:22|mqtt_client.c|IOT_MQTT_Destroy(186): mqtt release!
```

#### 4. 观察消息发送
如下日志信息显示示例程序通过 MQTT 的 Publish 类型消息，上报数据到 `/{productID}/{deviceName}/data`， 服务器已经收到并成功完成了该消息的处理。 
```
INF|2019-09-12 21:28:21|mqtt_sample.c|_mqtt_event_handler(98): publish success, packet-id=1934
```

#### 5. 观察消息接收
如下日志信息显示该消息因为是到达已被订阅的 Topic，所以又被服务器原样推送到示例程序，并进入相应的回调函数。
```
INF|2019-09-12 21:28:21|mqtt_sample.c|on_message_callback(195): Receive Message With topicName:S3EUVBRJLB/test_device/data, payload:{"action": "publish_test", "count": "0"}
```

#### 6. 观察控制台日志
登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，单击该产品名称，单击上方菜单【云日志】，即可查看刚上报的消息。
![](https://main.qcloudimg.com/raw/c6f7b9b71a96a1efc7611f38871c0ea0.jpg)




