## 操作场景

AirKiss 是微信为 Wi-Fi 设备提供的配网技术，详情请参见 [AirKiss 概述及应用场景](https://iot.weixin.qq.com/wiki/new/index.html?page=4-1-1)

其配网原理跟 SmartConfig 一样，如下所述：



### 基本原理

1. 设备进入 Wi-Fi 混杂模式（promiscuous mode）以监听捕获周围的 Wi-Fi 报文。由于设备暂未联网，且 Wi-Fi 网络的数据帧已通过加密，设备无法获取 payload 的内容，但可以获取报文的某些特征数据，例如每个报文的长度，同时对于某些数据帧；例如 UDP 的广播包或多播包，其报文的帧头结构比较固定，较容易识别。
2. 此时在手机 App 或者小程序侧，即可通过发送 UDP 的广播包或多播包，并利用报文的特征，例如长度变化进行编码。
3. 将目标 Wi-Fi 路由器的 SSID/PSW 字符以约定的编码方式发送出去，设备端在捕获到 UDP 报文后，按约定的方式进行解码，即可得到目标 Wi-Fi 路由器的相关信息并进行联网。

### 设备绑定流程

基于 AirKiss 协议，设备端在连接 Wi-Fi 路由器成功后，会往手机端回复 UDP 报文，手机端获取设备端的 IP 地址之后，同样可以通过 UDP，将后台提供的配网 Token 发送给设备，并由设备转发至物联网后台，依据 Token 可以进行设备绑定。

腾讯连连小程序已支持采用 AirKiss 协议进行配网，并提供相应的 [小程序 SDK](https://github.com/tencentyun/qcloud-iotexplorer-appdev-miniprogram-sdk)。
AirKiss 方式配网及设备绑定的示例流程图如下：
![](https://main.qcloudimg.com/raw/8e7f638de7dc02853463a59e32dec223.png)


## 操作步骤

### AirKiss 配网协议示例

AirKiss 配网设备端与腾讯连连小程序及后台交互的数据协议操作如下：

1. 腾讯连连小程序进入配网模式后，则可以在物联网开发平台服务获取到当次配网的 Token。小程序相关详情操作请参见 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044)。
2. 使 Wi-Fi 设备进入 AirKiss 配网模式，若设备有指示灯在快闪，则说明进入配网模式成功。
3. 小程序按照提示依次获取 Wi-Fi 列表，输入家里目标路由器的 SSID/PSW，按下一步后，将通过 AirKiss 方式发送报文。
4. 设备端通过监听捕获 AirKiss 报文，解析出目标路由器的 SSID/PSW 并进行联网，联网成功后，设备会告知小程序自己的 IP 地址，同时开始连接物联网后台。
5. 小程序作为 UDP 客户端会连接 Wi-Fi 设备上面的 UDP 服务（默认端口为**8266**）。给设备发送配网 Token，JSON 格式为：
<dx-codeblock>
::: json json
{"cmdType":0,"token":"6aa12345a9d529a2****7aa6e528a0fd"} 
:::
</dx-codeblock>
发送完成后，等待设备 UDP 回复设备信息及配网协议版本号：
<dx-codeblock>
::: json json
{"cmdType":2,"productId":"AAAA5AAAAA","deviceName":"dev_01","protoVersion":"2.0"}
:::
</dx-codeblock>
6. 如果2秒之内没有收到设备回复，则重复步骤5，UDP 客户端重复发送配网 Token。（如果重复发送5次都没有收到回复，则认为配网失败，Wi-Fi 设备有异常。）
7. 如果步骤5收到设备回复，则说明设备端已经收到 Token，并准备上报 Token。此时小程序会开始通过 Token 轮询物联网后台来确认配网及设备绑定是否成功。小程序相关操作可以参考 [查询配网 Token 状态](https://cloud.tencent.com/document/product/1081/44045)。
8. 设备端在成功连接 Wi-Fi 路由器后，需要通过 MQTT 连接物联网后台，并将小程序发送来的配网 Token 通过下面 MQTT 报文上报给后台服务：
```json
	topic: $thing/up/service/ProductID/DeviceName
	payload: {"method":"app_bind_token","clientToken":"client-1234","params": {"token":"6aa12345a9d529****777aa6e528a0fd"}}
​```设备端可以通过订阅主题 $thing/down/service/ProductID/DeviceName 来获取 token 上报的结果。

>!如果设备需要通过动态注册来创建设备并获取设备密钥，则会先进行动态注册再连接 MQTT。
>
9. 在以上5-7步骤中，需观察以下情况：

 - 如果小程序收到设备 UDP 服务发送过来的错误日志，且 deviceReply 字段的值为"Current_Error"，则表示当前配网绑定过程中出错，需要退出配网操作。
 - 如果 deviceReply 字段是"Previous_Error"，则为上一次配网的出错日志，只需要上报，不影响当此操作。
   错误日志 JSON 格式例子：

​```json
{"cmdType":2,"deviceReply":"Current_Error","log":"ESP WIFI connect error! (10, 2)"} 
```

10. 如果设备成功上报了 Token，物联网后台服务确认了 Token 有效性，小程序会提示配网完成，设备添加成功。
11. 设备端会记录配网的详细日志，如果配网或者添加设备失败，可以让设备端创建一个特殊的softAP和UDP服务，通过小程序可以从设备端获取更多日志用于错误分析。


### ESP8266 使用 AirKiss 配网接口

配网协议在 ESP8266 设备端的参考代码和 AT 固件，请参见 GitHub 工程 [qcloud-iot-esp-wifi](https://github.com/tencentyun/qcloud-iot-esp-wifi)。

在ESP8266上面，AirKiss协议属于 SmartConfig 配网方式的一种，只需要按照下面启动SmartConfig模式就可以同时支持ESP-TOUCH和AirKiss

```c
esp_smartconfig_set_type(SC_TYPE_ESPTOUCH_AIRKISS);
```

#### 配网代码示例

在 qcloud-iot-esp8266-demo/main/wifi_config 目录下，提供了 AirKiss 配网在 ESP8266 上面的参考实现，用户可以使用 qcloud-iot-esp8266-demo 工程进行体验。

配网接口说明请查看 wifi_config/qcloud_wifi_config.h，可以按照下面方式使用：
<dx-codeblock>
::: c c
/* 在微信小程序中使用WiFi配置和设备绑定 */
int wifi_config_state;
int ret = start_smartconfig();
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
		//设置softAP向小程序上传log
		start_log_softAP();
}
:::
</dx-codeblock>

#### 代码设计说明

配网代码将核心逻辑与平台相关底层操作分离，便于移植到不同的硬件设备上。

| 代码                         | 设计说明                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| `qcloud_wifi_config.c`       | 配网相关接口实现，包括 UDP 服务及 MQTT 连接及 Token 上报，主要依赖腾讯云物联网 C SDK 及 FreeRTOS/lwIP运行环境。 |
| `wifi_config_esp.c`          | 设备硬件 Wi-Fi 操作相关接口实现，依赖于 ESP8266 RTOS，当使用其他硬件平台时，需要进行移植适配。 |
| `wifi_config_error_handle.c` | 设备错误日志处理，主要依赖于 FreeRTOS。                      |
| `wifi_config_log_handle.c`   | 设备运行上报日志处理，主要依赖于 FreeRTOS。                  |


