
## 操作场景

### 基本原理

1. 设备进入 Wi-Fi 混杂模式（promiscuous mode）以监听捕获周围的 Wi-Fi 报文。由于设备暂未联网，且 Wi-Fi 网络的数据帧已通过加密，设备无法获取payload 的内容，但可以获取报文的某些特征数据，例如，每个报文的长度，同时对于某些数据帧，例如，UDP 的广播包或多播包，其报文的帧头结构比较固定，较容易识别。
2. 此时在手机 App 或者小程序侧，即可通过发送 UDP 的广播包或多播包，并利用报文的特征，例如，长度变化进行编码。
3. 将目标 Wi-Fi 路由器的 SSID/PSW 字符以约定的编码方式发送出去，设备端在捕获到 UDP 报文后，按约定的方式进行解码，即可得到目标 Wi-Fi 路由器的相关信息并进行联网。

### 设备绑定流程

一键配网方式配网，每个厂商编码方式和报文选择上有自己的协议，对于 RTK8720CF，采用的协议是 Realtek simpleConifg 协议，参考文档 Realtek 提供的文档 `AN0011 Realtek wlan simple configuration.pdf`。

- 基于该协议，设备端在连接 Wi-Fi 路由器成功后，会告知手机端自己的 IP 地址。
- 此时手机端可以通过数据通道，例如，TCP/UDP 通讯将后台提供的配网 Token 发送给设备，并由设备转发至物联网后台，依据 Token 可以进行设备绑定。

目前腾讯连连小程序已支持 simpleConfig 配网，并提供相应的 [小程序 SDK](https://www.npmjs.com/package/qcloud-iotexplorer-appdev-sdk)。

simpleConfig 方式配网及设备绑定的示例流程图如下：
![](https://main.qcloudimg.com/raw/37a61124c551c69621ca9bbc052b1b3f.png)
## 操作步骤
### simpleConfig 配网步骤

simpleConfig 配网设备端与腾讯连连小程序及后台交互的数据协议操作如下：

1. 腾讯连连小程序进入配网模式后，则可以在物联网开发平台服务获取到当次配网的 Token。小程序相关操作可以参考 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044)。
2. 使 Wi-Fi 设备进入 SmartConfig 配网模式，若设备有指示灯在快闪，则说明进入配网模式成功。
3. 小程序按照提示依次获取 Wi-Fi 列表，输入家里目标路由器的 SSID/PSW，按下一步后，将通过 SmartConfig 方式发送报文。
4. 设备端通过监听捕获 SmartConfig 报文，解析出目标路由器的 SSID/PSW 并进行联网，联网成功后，设备会告知小程序自己的 IP 地址，同时开始连接物联网后台。
5. 小程序作为 UDP 客户端会连接 Wi-Fi 设备上面的 UDP 服务（默认端口为**8266**）。给设备发送配网 Token，JSON 格式为：
```json
   {"cmdType":0,"token":"6xx82618a9d529a2ee777****528a0fd"} 
```
发送完成后，等待设备 UDP 回复设备信息及配网协议版本号：
```json  
   {"cmdType":2,"productId":"OSPB5ASRWT","deviceName":"dev_01","protoVersion":"2.0"}
```
6. 如果2秒之内未收到设备回复，则重复步骤5，UDP 客户端重复发送配网 Token。（如果重复发送5次都没有收到回复，则认为配网失败，Wi-Fi 设备有异常）
7. 如果步骤5收到设备回复，则说明设备端已经收到 Token，并准备上报 Token。此时小程序会开始通过 Token 轮询物联网后台来确认配网及设备绑定是否成功。小程序相关操作可以参考 [查询配网 Token 状态](https://cloud.tencent.com/document/product/1081/44045)。
8. 设备端在成功连接 Wi-Fi 路由器后，需要通过 MQTT 连接物联网后台，并将小程序发送来的配网 Token 通过下面 MQTT 报文上报给后台服务：
```json
    topic: $thing/up/service/ProductID/DeviceName
    payload: {"method":"app_bind_token","clientToken":"client-1234","params": {"token":"6xx82618a9d529a2ee777****528a0fd"}}
```
设备端也可以通过订阅主题 $thing/down/service/ProductID/DeviceName 来获取 Token 上报的结果。
9. 在以上5 - 7步骤中，需观察以下情况：
 - 如果小程序收到设备 UDP 服务发送过来的错误日志，且 deviceReply 字段的值为"Current_Error"，则表示当前配网绑定过程中出错，需要退出配网操作。
 - 如果 deviceReply 字段是"Previous_Error"，则为上一次配网的出错日志，只需要上报，不影响当此操作。
   错误日志 JSON 格式例子：

```json
{"cmdType":2,"deviceReply":"Current_Error","log":"ESP WIFI connect error! (10, 2)"} 
```

10. 如果设备成功上报了 Token，物联网后台服务确认了 Token 有效性，小程序会提示配网完成，设备添加成功。
11. 设备端会记录配网的详细日志，如果配网或者添加设备失败，可以让设备端创建一个特殊的 softAP 和 UDP 服务，通过小程序可以从设备端获取更多日志用于错误分析。

### 基于Ambz2 SDK使用 simpleConfig 与小程序配网

simpleConfig配网协议配合腾讯连连基于Ambz2 SDK的实现参见 GitHub 工程 [qcloud-iot-rtk-wifi-based-ambz2](https://github.com/tencentyun/qcloud-iot-rtk-wifi-based-ambz2.git)。

#### 配网代码示例

在 qcloud-iot-rtk-wifi-based-ambz2\component\common\example\qcloud_iot_c_sdk\wifi_config 目录下，提供 simpleConfig 配网在 Ambz2 SDK 上面的参考实现，配网接口说明请查看 wifi_config/qcloud_wifi_config.h。

配网框架对simpleConfig配网做了封装，开发者只要调用API启动simpleConfig配网，然后在配网结果回调中判断配网结果即可。`qcloud_demo_task` 中介绍 simpleConfig 配网的使用：

```c
static void qcloud_demo_task(void *arg)
{
    int ret;

    set_wifi_config_result(false);
    while (!wifi_is_up(RTW_STA_INTERFACE)) {
        HAL_SleepMs(1000);
    }
#if WIFI_PROV_SOFT_AP_ENABLE
    Log_d("start softAP wifi provision");
    eSoftApConfigParams apConf = {"RTK8720-SAP", "12345678", 6};
    ret = qiot_wifi_config_start(WIFI_CONFIG_TYPE_SOFT_AP, &apConf, _wifi_config_result_cb);
#elif WIFI_PROV_SIMPLE_CONFIG_ENABLE
    Log_d("start simple config wifi provision");
    ret = qiot_wifi_config_start(WIFI_CONFIG_TYPE_SIMPLE_CONFIG, NULL, _wifi_config_result_cb);
#else
    Log_e("not supported wifi provision method");
    ret = -1;
#endif
    if (ret) {
        Log_e("start wifi config failed: %d", ret);
        goto exit;
    }
}		

```

使能宏定义 `WIFI_PROV_SIMPLE_CONFIG_ENABLE`， 调用配网接口`qiot_wifi_config_start`，传入simpleConfig配网模式、配网结果回调，则配网结果回调函数中会返回配网的结果。

>! demo 需要关闭 softAP 的宏定义 `WIFI_PROV_SOFT_AP_ENABLE` 才会跑 simpleConfig 的配网方式。

#### 代码设计说明

配网代码将核心逻辑与平台相关底层操作分离，便于移植到不同的硬件设备上。

| 代码                         | 设计说明                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| `qcloud_wifi_config.c`       | 配网框架，统一各种配网方式，实现配网启动、配网停止、配网结果回调，用户只需要将特定配网方法注册到`sg_wifi_config_methods`即可，不依赖任何软硬件平台。 |
| `qiot_comm_service.c`        | 配网相关接口实现，实现 UDP 服务和与小程序的数据交互，主要依赖腾讯云物联网 C-SDK 及 FreeRTOS/lwIP 运行环境。 |
| `qiot_device_bind.c`         | 配网相关接口实现，实现配网过程的token交互与设备绑定，主要依赖腾讯云物联网 C-SDK 及 FreeRTOS/lwIP 运行环境 |
| `rtk_soft_ap.c`              | softAP Wi-Fi 操作相关接口实现，依赖于 Ambz2 SDK提供的WiFi相关操作接口，当使用其他硬件平台时，可以参考移植适配。 |
| `rtk_simple_config.c`        | simpleConfig Wi-Fi 操作相关接口实现，依赖于 Ambz2 SDK提供的WiFi相关操作接口，当使用其他硬件平台时，可以参考移植适配。 |
| `wifi_config_error_handle.c` | 设备错误日志处理，主要依赖于 FreeRTOS。                      |
| `wifi_config_log_handle.c`   | 设备配网日志收集和上报，主要依赖于 FreeRTOS。                |

