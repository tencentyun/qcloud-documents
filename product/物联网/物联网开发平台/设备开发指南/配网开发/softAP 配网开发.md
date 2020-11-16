## 操作场景
设备通过 softAP 方式创建一个 Wi-Fi 热点，手机连接该热点，再通过数据通道例如 TCP/UDP 通讯，将目标 Wi-Fi 路由器的 SSID/PSW 传递该设备，设备获取后，即可连接 Wi-Fi 路由器从而连接互联网。同时，为了对设备进行绑定，手机 App 可以利用该 TCP/UDP 数据通道，将后台提供的配网 Token 发送给设备，并由设备转发至物联网后台，依据 Token 可以进行设备绑定。本文档主要指导您如何使用softAP 方式配网开发。

腾讯连连小程序已经支持 softAP 配网，并提供了相应的 [小程序 SDK](https://www.npmjs.com/package/qcloud-iotexplorer-appdev-sdk)。
基于 Token 的 softAP 方式配网及设备绑定的示例流程图，如下图所示：
![](https://main.qcloudimg.com/raw/5e30af733894a2fc1e5c36df817b5c51.png)

## 操作步骤
### softAP 配网协议示例 
本示例基于 ESP8266 腾讯云定制模组配合腾讯连连小程序。

1. 腾讯连连小程序进入配网模式后，则可以在物联网开发平台服务获取到当次配网的 Token。小程序相关操作可以参考 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044)。
2. 使 Wi-Fi 设备进入 softAP 配网模式，若设备有指示灯在快闪，则说明进入配网模式成功。    
3. 小程序按照提示依次获取 Wi-Fi 列表，输入家里目标路由器的 SSID/PSW，再选择设备 softAP 热点的 SSID/PSW。
4. 手机连接设备 softAP 热点成功后，小程序作为 UDP 客户端会连接 Wi-Fi 设备上面的 UDP 服务（默认 IP 为**192.168.4.1**，端口为**8266**）。
5. 小程序给设备 UDP 服务，发送目标 Wi-Fi 路由器的 SSID/PSW 以及配网 Token，JSON 格式为：
```
   {"cmdType":1,"ssid":"Home-WiFi","password":"abcd1234","token":"6aa11111x1x123x1aa546xx6x111xxxd"} 
```
发送完成后，等待设备 UDP 回复设备信息及配网协议版本号：
```   
   {"cmdType":2,"productId":"OSPB5ASRWT","deviceName":"dev_01","protoVersion":"2.0"}
```
6. 如果2秒之内，未收到设备回复，则重复步骤5，UDP 客户端重复发送目标 Wi-Fi 路由器的 SSID/PSW 及配网 Token。（如果重复发送5次，都没有收到回复，则认为配网失败，Wi-Fi 设备有异常）      
7. 如果步骤5收到设备回复，则说明设备端已收到 Wi-Fi 路由器的 SSID/PSW 及 Token，正在连接 Wi-Fi 路由器，并上报 Token。此时小程序会提示手机也将连接 Wi-Fi 路由器，并通过 Token 轮询物联网后台，来确认配网及设备绑定是否成功。小程序相关操作可以参考 [查询配网Token状态](https://cloud.tencent.com/document/product/1081/44045)。
8. 设备端在成功连接 Wi-Fi 路由器后，需要通过 MQTT 连接物联网后台，并将小程序发送的配网 Token，通过下面 MQTT 报文上报给后台服务：
```
    topic: $thing/up/service/ProductID/DeviceName
    payload: {"method":"app_bind_token","clientToken":"client-1234","params": {"token":"6xx12345x9x1234ee777xx6e528a0fd"}}
```
设备端也可以通过订阅主题 $thing/down/service/ProductID/DeviceName 来获取 Token 上报的结果。
>!如果设备需要通过动态注册来创建设备并获取设备密钥，则会先进行动态注册再连接 MQTT。
9. 在以上5 - 7步骤中，需观察以下情况：
  - 如果小程序收到设备 UDP 服务发送过来的错误日志，且 deviceReply 字段的值为"Current_Error"，则表示当前配网绑定过程中出错，需要退出配网操作。
  - 如果 deviceReply 字段是"Previous_Error"，则为上一次配网的出错日志，只需要上报，不影响当此操作。
错误日志 JSON 格式，示例如下：
```
{"cmdType":2,"deviceReply":"Current_Error","log":"ESP WIFI connect error! (10, 2)"} 
```
10. 如果设备成功上报了 Token，物联网后台服务已确认 Token 有效性，小程序会提示配网完成，设备添加成功。
11. 设备端会记录配网的详细日志，如果配网或者添加设备失败，可以让设备端创建一个特殊的 softAP 和 UDP 服务，通过小程序可以从设备端获取更多日志用于错误分析。

>!UDP 相比 TCP 是不可靠的通讯，存在丢包的可能，特别在比较嘈杂的无线 Wi-Fi 环境中，丢包率会比较大。为了保证小程序和设备之间的数据交互是可靠的，需要在应用层设计一些应答以及超时重发的机制。

### ESP8266 使用 softAP 配网接口
配网协议在 ESP8266 设备端的参考代码和 AT 固件，请参见 GitHub 工程 [qcloud-iot-esp-wifi](https://github.com/tencentyun/qcloud-iot-esp-wifi)。
#### 腾讯云 IoT AT 指令 ESP8266 定制固件
如果 ESP8266 烧写了腾讯云 IoT AT 指令 ESP8266 定制固件，则只要通过指令 AT+TCDEVINFOSET 配置好设备信息，再通过下面的指令启动 softAP 配网即可。
```
AT+TCSAP="ESP8266-SAP","12345678"
```
关于 AT 指令的详细说明，请参见 qcloud-iot-at-esp8266 目录文档。

#### 配网代码示例
在 qcloud-iot-esp8266-demo/main/wifi_config 目录下，提供了 softAP 配网 v2.0 在 ESP8266 上面的参考实现，您可以使用 qcloud-iot-esp8266-demo 工程进行体验。

#### 使用示例
配网接口说明请查看 wifi_config/qcloud_wifi_config.h，您可以按照以下方式使用：
```
/* 在微信小程序中使用WiFi配置和设备绑定 */
int wifi_config_state;
int ret = start_softAP("ESP8266-SAP", "12345678", 0);
if (ret) {
		Log_e("start wifi config failed: %d", ret);
} else {
		/* 最大等待时间: 150 * 2000ms */
		int wait_cnt = 150;
		do {
				Log_d("waiting for wifi config result...");
				HAL_SleepMs(2000);            
				wifi_config_state = query_wifi_config_state();
		} while (wifi_config_state == WIFI_CONFIG_GOING_ON && wait_cnt--);
}

wifi_connected = is_wifi_config_successful();
if (!wifi_connected) {
		Log_e("wifi config failed!");
		// 设置softAP向小程序上传log
		start_log_softAP();
}

```

#### 代码设计说明
配网代码将核心逻辑与平台相关底层操作分离，便于移植到不同的硬件设备上。

| 代码 | 设计说明 |
|---------|---------|
| `qcloud_wifi_config.c` | 配网相关接口实现，包括 UDP 服务及 MQTT 连接及 Token 上报，主要依赖腾讯云物联网 C-SDK 及 FreeRTOS/lwIP 运行环境。 |
|`wifi_config_esp.c`|设备硬件 Wi-Fi 操作相关接口实现，依赖于 ESP8266 RTOS，当使用其他硬件平台时，需要进行移植适配。|
|`wifi_config_error_handle.c`|设备错误日志处理，主要依赖于 FreeRTOS。|
|`wifi_config_log_handle.c`|设备配网日志收集和上报，主要依赖于 FreeRTOS。|



#### 配网代码示例及移植指引
配网协议的设备端代码和 AT 固件，详情请参见 [配网代码说明和移植指引](https://github.com/tencentyun/qcloud-iot-esp-wifi)。

