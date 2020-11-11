

Real Time-Thread（以下简称 RT-Thread）是一个嵌入式实时多线程操作系统，C SDK 支持以 [软件包](https://github.com/tencentyun/tencent-cloud-iot-package-for-rtthread) 的形式应用到 RT-Thread 操作系统，本文向您介绍如何使用 RT-Thread 快速接入腾讯云物联网开发平台。

## 操作步骤

RT-Thread 接入腾讯云物联网开发平台可以分为以下4个步骤。

### 步骤一：开发环境安装

安装 RT-Thread 开发环境，详情请参见 [RT-Thread 开发环境搭建](https://www.rt-thread.org/document/site/application-note/setup/standard-project/an0017-standard-project/)。

### 步骤二：软件包下载

1. 执行 `scons --menuconfig` 命令打开配置面板。
勾选 `【RT-Thread online packages】>【IoT - internet of things】>【IoT Cloud】>【tencent-iot-sdk】`。
```c
[ ] OneNET: China Mobile OneNet cloud SDK for RT-Thread  ----                        
[ ] GAgent: GAgent of Gizwits in RT-Thread  ----                                     
[ ] Ali-iotkit: Aliyun cloud sdk 'iotkit-embedded' for RT-Thread  ----               
[ ] Azure IoT SDK: Microsoft azure cloud SDK for RT-Thread  ----                     
[*] Tencent-IoT:  Tencent Cloud IoT Explorer Platform SDK for RT-Thread  --->        
[ ] jiot-c-sdk: JIGUANG IoT Cloud Client SDK for RT_Thread  ----                     
[ ] ucloud_iot_sdk: Ucloud iot sdk for uiot-core platform.  ----                     
[ ] Joylink Cloud SDK for IoT platform  ----     
```
2. 执行 `pkgs --update` 命令更新软件包，腾讯云物联网 C SDK 将被下载到 packages 目录。


### 步骤三：编译与运行

1. 执行 `scons --menuconfig` 命令打开配置面板，对 C SDK 进行配置。
 - **选择路径**：`RT-Thread online packages => IoT - internet of things => IoT Cloud => tencent-iot-sdk `。
```plaintext
--- Tencent-IoT:  Tencent Cloud IoT Explorer Platform SDK for RT-Thread        
(0WUKPUCOTC) Config Product Id                                                 
(dev001) Config Device Name                                                    
(N6B8M91PB4YDTRCpqvOp4w==) Config Device Secret                                
[ ]   Enable dynamic register                                                  
[ ]   Enable err log upload                                                    
[ ]   Enable multi thread function                                             
[*]   Enable TLS/DTLS                                                          
           Select Product Type (Data template protocol)  --->                       
[*]   Enable Event                                                             
[*]   Enable Action                                                            
[*]   Enable Smart_light Sample                                                
[*]   Enable OTA                                                               
             Config OTA download by https or http (Download by http)  --->          
[ ]   Enable GateWay                                                           
		   Version (latest)  ---> 
```

 - **参数说明**
    - **Config Product Id**：配置产品 ID，平台创建生成。
    - **Config Device Name**：配置设备名，平台创建生成。
    - **Config Device Secret**：配置设备密钥，平台创建生成。考虑到嵌入式设备大多没有文件系统，暂时没有支持证书设备配置。
    - **Enable dynamic register**： 是否使能动态注册功能及示例，若使能，需配置动态注册的产品密钥。
    - **Enable err log upload**： 是否使能错误日志上传云端。
    - **Enable TLS/DTLS**： 是否使能 TLS，若使能，则会关联选中 mbedTLS 软件包。
    - **Select Product Type**：产品类型为自定义或者数据模板协议产品。
    - **Enable event**：选用数据模板的前提下，是否使能事件功能。
    - **Enable Action**：选用数据模板的前提下，是否使能行为功能。
    - **Enable Smart_light Sample**：是否使能智能灯场景示例。
    - **Enable OTA**：是否使能 OTA 示例。若使能 OTA 可进一步选择下载使用 HTTPS 或者 HTTP。
    - **Enable GateWay**：是否使能网关示例。
    - **Version**：软件包版本选择，v3.1.2及其以后的版本只支持物联网开发平台，若需使用物联网通信平台，请选择 v3.0.2 及其之前的版本。
2. 编译并运行示例程序。
本文以数据模板智能灯 + TLS 为例进行介绍，展示设备和物联网开发平台基于 [数据模板协议](https://cloud.tencent.com/document/product/1081/34916) 的通信示例使能 TLS。物联网开发平台下发控制灯为红色的命令，设备端收取消息，打印颜色，并上报对应消息。
 - 配置选项
     ```plaintext
     --- Tencent-IoT:  Tencent Cloud IoT Explorer Platform SDK for RT-Thread     
     --- Tencent-IoT:  Tencent Cloud IoT Explorer Platform SDK for RT-Thread               
        (0WUKPUCOTC) Config Product Id                                                     
        (dev001) Config Device Name                                                        
        (N6B8M91PB4YDTRCpqvOp4w==) Config Device Secret                                    
        [ ]   Enable dynamic register                                                      
        [ ]   Enable err log upload                                                        
        [ ]   Enable multi thread function                                                 
        [*]   Enable TLS/DTLS                                                              
              Select Product Type (Data template protocol)  --->                           
        [*]   Enable Event                                                                 
        [*]   Enable Action                                                                
        [*]   Enable Smart_light Sample                                                    
        [ ]   Enable OTA                                                                   
        [ ]   Enable GateWay                                                               
              Version (latest)  --->   
     ```
 - 运行示例
     ```c
      \ | /
     - RT -     Thread Operating System
      / | \     4.0.3 build Jun 15 2020
      2006 - 2020 Copyright by rt-thread team
     lwIP-2.0.2 initialized!
     [I/sal.skt] Socket Abstraction Layer initialize success.
     [I/SDIO] SD card capacity 65536 KB.
     hello rt-thread
     msh />tc_data_template_light_example start
     INF|20|qcloud_iot_device.c|iot_device_info_set(65): SDK_Ver: 3.1.1, Product_ID: 0WUKPUCOTC, Device_Name: dev001
     msh />DBG|20|HAL_TLS_mbedtls.c|HAL_TLS_Connect(228):  Connecting to /0WUKPUCOTC.iotcloud.tencentdevices.com/8883...
     DBG|21|HAL_TLS_mbedtls.c|HAL_TLS_Connect(233):  Setting up the SSL/TLS structure...
     DBG|21|HAL_TLS_mbedtls.c|HAL_TLS_Connect(285): Performing the SSL/TLS handshake...
     INF|21|mqtt_client.c|IOT_MQTT_Construct(127): mqtt connect with id: qPU1e success
     DBG|21|mqtt_client_subscribe.c|qcloud_iot_mqtt_subscribe(141): topicName=$thing/down/property/0WUKPUCOTC/dev001|packet_id=64736
     DBG|21|data_template_client.c|_template_mqtt_event_handler(242): template subscribe success, packet-id=64736
     INF|21|light_data_template_sample.c|event_handler(321): subscribe success, packet-id=64736
     INF|21|data_template_client.c|IOT_Template_Construct(785): Sync device data successfully
     DBG|21|mqtt_client_subscribe.c|qcloud_iot_mqtt_subscribe(141): topicName=$thing/down/event/0WUKPUCOTC/dev001|packet_id=64737
     DBG|21|mqtt_client_subscribe.c|qcloud_iot_mqtt_subscribe(141): topicName=$thing/down/action/0WUKPUCOTC/dev001|packet_id=64738
     INF|21|light_data_template_sample.c|data_template_light_thread(650): Cloud Device Construct Success
     DBG|21|light_data_template_sample.c|_usr_init(354): add your init code here
     INF|21|light_data_template_sample.c|_register_data_template_property(432): data template property=power_switch registered.
     INF|21|light_data_template_sample.c|_register_data_template_property(432): data template property=color registered.
     INF|21|light_data_template_sample.c|_register_data_template_property(432): data template property=brightness registered.
     INF|21|light_data_template_sample.c|_register_data_template_property(432): data template property=name registered.
     INF|21|light_data_template_sample.c|data_template_light_thread(676): Register data template propertys Success
     INF|21|light_data_template_sample.c|_register_data_template_action(294): data template action=blink registered.
     INF|21|light_data_template_sample.c|data_template_light_thread(686): Register data template actions Success
     DBG|21|mqtt_client_publish.c|qcloud_iot_mqtt_publish(340): publish packetID=0|topicName=$thing/up/property/0WUKPUCOTC/dev001|payload={"method":"report_info", "clientToken":"0WUKPUCOTC-0", "params":{"module_hardinfo":"ESP8266","module_softinfo":"V1.0","fw_ver":"3.1.1","imei":"11-22-33-44","lat":"22.546015","lon":"113.941125", "device_label":{"append_info":"your self define info"}}}
     DBG|21|data_template_client.c|_template_mqtt_event_handler(242): template subscribe success, packet-id=64737
     INF|21|light_data_template_sample.c|event_handler(321): subscribe success, packet-id=64737
     DBG|21|data_template_client.c|_template_mqtt_event_handler(242): template subscribe success, packet-id=64738
     INF|21|light_data_template_sample.c|event_handler(321): subscribe success, packet-id=64738
     DBG|21|data_template_client.c|_reply_ack_cb(169): replyAck=0
     DBG|21|data_template_client.c|_reply_ack_cb(172): Received Json Document={"method":"report_info_reply","clientToken":"0WUKPUCOTC-0","code":0,"status":"success"}
     DBG|21|mqtt_client_publish.c|qcloud_iot_mqtt_publish(340): publish packetID=0|topicName=$thing/up/property/0WUKPUCOTC/dev001|payload={"method":"get_status", "clientToken":"0WUKPUCOTC-1"}
     DBG|21|data_template_client.c|_get_status_reply_ack_cb(185): replyAck=0
     DBG|21|data_template_client.c|_get_status_reply_ack_cb(189): Received Json Document={"method":"get_status_reply","clientToken":"0WUKPUCOTC-1","code":0,"status":"success","data":{"reported":{"power_switch":0,"color":0,"brightness":0,"name":"dev001"}}}
     DBG|21|light_data_template_sample.c|data_template_light_thread(709): Get data status success
     DBG|22|mqtt_client_publish.c|qcloud_iot_mqtt_publish(340): publish packetID=0|topicName=$thing/up/property/0WUKPUCOTC/dev001|payload={"method":"report", "clientToken":"0WUKPUCOTC-2", "params":{"power_switch":0,"color":0,"brightness":0,"name":"dev001"}}
     INF|22|light_data_template_sample.c|data_template_light_thread(761): data template reporte success
     INF|23|light_data_template_sample.c|OnReportReplyCallback(416): recv report_reply(ack=0): {"method":"report_reply","clientToken":"0WUKPUCOTC-2","code":0,"status":"success"}
     DBG|27|mqtt_client_publish.c|qcloud_iot_mqtt_publish(340): publish packetID=0|topicName=$thing/up/property/0WUKPUCOTC/dev001|payload={"method":"report", "clientToken":"0WUKPUCOTC-3", "params":{"power_switch":0,"color":0,"brightness":0,"name":"dev001"}}
     ```

### 步骤四：应用开发

  详情请参见 [软件包](https://github.com/tencentyun/tencent-cloud-iot-package-for-rtthread) 中的示例程序进行开发。

## SDK 使用参考
详情请参见 [C SDK 使用参考](https://cloud.tencent.com/document/product/1081/48377) 。
