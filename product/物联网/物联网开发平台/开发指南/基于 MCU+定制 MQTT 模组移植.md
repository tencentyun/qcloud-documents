## 简介

[tc-iot-at-sdk-stm32-freertos-based-example](https://github.com/tencentyun/tc-iot-at-sdk-stm32-freertos-based-example.git) 面向使用支持腾讯 AT 指令的模组（2/3/4/5G、NB、Wi-Fi 等）接入腾讯物联网平台的终端设备开发者，mcu 侧使用 [腾讯 AT_SDK](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based.git) 的移植示例，示例展示了基于 STM32F103 MCU 和 FreeRTOS 的软硬件环境如何实现 HAL 层的移植，主要有串口的收发接口（中断接收），延时函数及 OS 相关接口适配（互斥锁、动态内存申请释放、线程创建），适配层接口单独剥离在 port 目录。

### 代码工程框架

<img src="https://main.qcloudimg.com/raw/d161af7e13cf42536639936bf303a848.jpg"/>

### 目录结构

| 名称                              | 说明                                |
| --------------------------------- | ----------------------------------- |
| docs                              | 文档目录，包含硬件原理图。          |
| Drivers                           | STM32 F1xx HAL驱动。                |
| Inc                               | 头文件。                            |
| MDK-ARM                           | Keil 工程目录。                     |
| src                               | 板级初始化及驱动适配。              |
| Middlewares\Third_Party           | 第三方软件包。                      |
| ├─FreeRTOS                        | freeRTOS 软件包。                   |
| ├─qcloud-iot-sdk-tencent-at-based | AT_SDK 适配支持腾讯 AT 指令的模组。 |
| ├───── README.md                  | AT-SDK 代码目录说明。               |
| README.md                         | 代码工程目录说明。                  |

## 使用指导

**1. 软硬件环境说明**
硬件原理图在 docs 目录，为保证示例的通用性，示例代码除了 MCU 本身的资源没有无特定外设的访问。
软件的基础工程基于 ST 的开发工具 cubeMX 生成，cubeMX 工程参加目录下 Tc-Iot-STM32F103-Dev-Kit.ioc。

**2. AT-SDK 移植说明**

开发者可以参考 port 目录的 HAL 层 API 在 STM32 和 FreeRTOS 中移植，切换为新的软硬件平台的相关接口。

**2.1 hal_export.h**
HAL 层对外的 API 接口及 HAL 层宏开关控制。

| 序号 | 宏定义                  | 说明                                                         |
| ---- | ----------------------- | ------------------------------------------------------------ |
| 1    | PARSE_THREAD_STACK_SIZE | 串口 AT 解析线程栈大小。                                     |
| 2    | OS_USED                 | 是否使用 OS，目前的 AT-SDK 是基于多线程框架的，所以 OS 是必须的。 |
| 3    | AUTH_MODE_KEY           | 认证方式，证书认证还是密钥认证。                             |
| 4    | DEBUG_DEV_INFO_USED     | 默认使能该宏，设备信息使用调试信息，正式量产关闭该宏，并实现设备信息存取接口。 |

**2.2 hal_os.c**
该源文件主要实现打印、延时、时间戳、锁、线程创建、设备信息存取等。

| 序号 | HAL_API                  | 说明                                                         |
| ---- | ------------------------ | ------------------------------------------------------------ |
| 1    | HAL_Printf               | 打印函数，log 输出需要，可选实现。                           |
| 2    | HAL_Snprintf             | 格式化打印，JSON 数据处理需要，必须实现。                    |
| 3    | HAL_Vsnprintf            | 格式化输出， 可选实现。                                      |
| 4    | HAL_DelayMs              | 毫秒延时，必选实现。                                         |
| 5    | HAL_DelayUs              | 微妙延时，可选实现。                                         |
| 6    | HAL_GetTimeMs            | 获取毫秒数，必选实现。                                       |
| 7    | HAL_GetTimeSeconds       | 获取时间戳，必须实现，时戳不需绝对准确，但不可重复。         |
| 8    | hal_thread_create        | 线程创建，必选实现。                                         |
| 9    | hal_thread_destroy       | 线程销毁，必选实现。                                         |
| 10   | HAL_SleepMs              | 放权延时，必选实现。                                         |
| 11   | HAL_MutexCreate          | 互斥锁创建，必选实现。                                       |
| 12   | HAL_MutexDestroy         | 互斥锁销毁，必选实现。                                       |
| 13   | HAL_MutexLock            | 获取互斥锁，必选实现。                                       |
| 14   | HAL_MutexUnlock          | 释放互斥锁，必选实现。                                       |
| 15   | HAL_Malloc               | 动态内存申请，必选实现。                                     |
| 16   | HAL_Free                 | 动态内存释放，必选实现。                                     |
| 17   | HAL_GetProductID         | 获取产品 ID，必选实现。                                      |
| 18   | HAL_SetProductID         | 设置产品 ID，必须存放在非易失性存储介质，必选实现。          |
| 19   | HAL_GetDevName           | 获取设备名，必选实现。                                       |
| 20   | HAL_SetDevName           | 设置设备名，必须存放在非易失性存储介质，必选实现。           |
| 21   | HAL_GetDevSec            | 获取设备密钥，密钥认证方式为必选实现。                       |
| 22   | HAL_SetDevSec            | 设置设备密钥，必须存放在非易失性存储介质，密钥认证方式为必选实现。 |
| 23   | HAL_GetDevCertName       | 获取设备证书文件名，证书认证方式为必选实现。                 |
| 24   | HAL_SetDevCertName       | 设置设备证书文件名，必须存放在非易失性存储介质，证书认证方式为必选实现。 |
| 25   | HAL_GetDevPrivateKeyName | 获取设备证书私钥文件名，证书认证方式为必选实现。             |
| 26   | HAL_SetDevPrivateKeyName | 设置设备证书私钥文件名，必须存放在非易失性存储介质，证书认证方式为必选实现。 |

**2.3 hal_at.c**
该源文件主要实现 AT 串口初始化、串口收发、模组开关机。

| 序号  | HAL_API                        | 说明                                 		|
| ---- | -------------------------------| ----------------------------------		|
| 1    | module_power_on                | 模组开机，AT 串口初始化，必选实现              |
| 1    | module_power_off               | 模组关机，低功耗需要，可选实现                |
| 2    | AT_UART_IRQHandler          | A T串口接收中断 ISR，将收取到的数据放入 ringbuff 中，AT 解析线程会实时解析数据，必选实现|
| 3    | at_send_data                   | AT 串口发送接口                             |

**2.4 module_api_inf.c**
配网/注网 API 业务适配，该源文件基于腾讯定义的 AT 指令实现了 MQTT 的交互，但有一个关于联网/注网的 API（module_register_network）需要根据模组适配。

示例基于 [ESP8266 腾讯定制 AT 固件](https://main.qcloudimg.com/raw/6811fc7631dcf0ce5509ccbdba5c72b7.zip) 示例了 Wi-Fi 直连的方式连接网络，但更常用的场景是根据特定事件（譬如按键）触发配网（softAP/一键配网），这块的逻辑各具体业务逻辑自行实现。ESP8266 有封装配网指令和示例 App。对于蜂窝模组，则是使用特定的网络注册指令。开发者参照 module_handshake 应用 AT-SDK 的 AT 框架添加和模组的 AT 指令交互。 

```
//模组联网（NB/2/3/4G注册网络）、wifi配网（一键配网/softAP）暂时很难统一,需要用户根据具体模组适配。
//开发者参照 module_handshake API使用AT框架的API和模组交互，实现适配。
eAtResault module_register_network(eModuleType eType)
{
	eAtResault result = AT_ERR_SUCCESS;
	
#ifdef MODULE_TYPE_WIFI	
	if(eType == eMODULE_ESP8266)
	{
		#define WIFI_SSID	"youga_wifi"
		#define WIFI_PW		"Iot@2018"

		/*此处示例传递热点名字直接联网，通常的做法是特定产品根据特定的事件（譬如按键）触发wifi配网（一键配网/softAP）*/
		result = wifi_connect(WIFI_SSID, WIFI_PW);
		if(AT_ERR_SUCCESS != result)
		{
			Log_e("wifi connect fail,ret:%d", result);	
		}
	}
#else	
	if(eType == eMODULE_N21)
	{
	
		/*模组网络注册、或者wifi配网需要用户根据所选模组实现*/			
		result = N21_net_reg();
		if(AT_ERR_SUCCESS != result)
		{
			Log_e("N21 register network fail,ret:%d", result);	
		}	
	}
#endif	


	return result;
}
```

**2.5 设备信息修改**

调试时，在 hal_export.h 将设备信息调试宏定义打开。量产时需要关闭该宏定义，实现 hal-os 中序列 17-26 的设备信息存取 API。

```
#define 	DEBUG_DEV_INFO_USED
```

修改下面宏定义的设备信息，则系统将会使用调试信息。

```
#ifdef  DEBUG_DEV_INFO_USED

static char sg_product_id[MAX_SIZE_OF_PRODUCT_ID + 1]	 = "03UKNYBUZG";
static char sg_device_name[MAX_SIZE_OF_DEVICE_NAME + 1]  = "at_dev";

#ifdef AUTH_MODE_CERT
static char sg_device_cert_file_name[MAX_SIZE_OF_DEVICE_CERT_FILE_NAME + 1]      = "YOUR_DEVICE_NAME_cert.crt";
static char sg_device_privatekey_file_name[MAX_SIZE_OF_DEVICE_KEY_FILE_NAME + 1] = "YOUR_DEVICE_NAME_private.key";
#else
char sg_device_secret[MAX_SIZE_OF_DEVICE_SERC + 1] = "ttOARy0PjYgzd9OSs4Z3RA==";
#endif

#endif
```

**2.6 示例说明**

Smaple 目录一共有四个示例，分别是 mqtt_sample.c、shadow_sample.c、data_template_sample.c、light_data_template_sample.c。
通过 main.c 中宏定义 RUN_SAMPLE_TYPE 控制具体运行哪个个示例。

```
void demoTask(void)
{
	mem_info();
	
	if(SHADOW_SAMPLE == RUN_SAMPLE_TYPE)
	{
		shadow_sample();
	}
	else if(DATATEMPLATE_SAMPLE == RUN_SAMPLE_TYPE)
	{
		data_template_sample();
	}
	else if(LIGHT_SCENARY_SAMPLE == RUN_SAMPLE_TYPE)
	{
		light_data_template_sample();
	}
	else
	{
		mqtt_sample();
	}
}
```

各示例说明如下：

| 序号  | 示例名称                        | 说明                                 		|
| ---- | -------------------------------| ----------------------------------		|
| 1    | mqtt_sample.c                  | MQTT 示例，该示例示例基于定制的 AT 指令如何便捷的接入腾讯物联网平台及收发数据。|
| 1    | shadow_sample.c                | 影子示例，基于 AT 实现的 MQTT 协议，进一步封装的影子协议。               |
| 2    | data_template_sample.c         | 通用数据模板及事件功能示例，示例如何基于腾讯物联网平台的数据模板功能快速开发产品。|
| 3    | light_data_template_sample.c   | 基于智能灯的控制场景，示例具体的产品如何应用数据模板及事件功能。 | 

data_template_sample、light_data_template_sample为 [物联网开发平台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)示例，mqtt_sample和shadow_sample为[物联网通信平台](https://console.cloud.tencent.com/iotcloud/products) 示例。

**2.7 示例运行**

按照上述描述，修改宏定义 RUN_SAMPLE_TYPE 为目标示例，编译烧录后，即可运行。

**MQTT 示例**
修改宏定义 RUN_SAMPLE_TYPE 为 MQTT_SAMPLE，AT 串口接 ESP8266（已烧录腾讯定制 AT 固件），编译后运行日志如下：

```shell
===========Build Time 20190425===============
Board init over
Sysclk[8000000] TickFreq[1]DBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:0

Start test taskDBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:25896
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|mqtt_demo_task(101): mqtt_demo_task Entry...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\at_client.c|at_client_init(856): AT client(V1.0.0) initialize success.
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(172): at client init success
...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(189): WIFI CONNECTED
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|net_prepare(49): module init success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|net_prepare(64): Start shakehands with module...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_handshake(226): Module info(6):

AT version:1.3.0.0-dev(6ed31d7 - Apr 18 2019 04:15:44)
SDK version:v3.2-dev-224-g54d3106-dirty
compile time:Apr 24 2019 20:09:42
Bin version:QCloud IoT ESP AT v1.0(Unknown)
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|net_prepare(73): module connect success
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\device.c|iot_device_info_init(62): SDK_Ver: 1.0.0, Product_ID: 03UKNYBUZG, Device_Name: at_dev
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_wifi_conn_func(73): receve wifi conn urc(16):WIFI CONNECTED

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_conn_func(88): receve mqtt conn urc(16):+TCMQTTCONN:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|mqtt_demo_task(131): module mqtt conn success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_sub_func(101): receve mqtt sub urc(15):+TCMQTTSUB:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_mqtt_sub(391): 03UKNYBUZG/at_dev/data sub success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|mqtt_demo_task(151): module mqtt sub success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|mqtt_demo_task(165): pub_msg:{\"action\": \"publish_test\"\, \"count\": \"0\"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|mqtt_demo_task(174): module mqtt pub success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|dataTopic_cb(22): data topic call back:{"action":"publish_test","count":"0"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|mqtt_demo_task(165): pub_msg:{\"action\": \"publish_test\"\, \"count\": \"1\"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|mqtt_demo_task(174): module mqtt pub success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\mqtt_sample.c|dataTopic_cb(22): data topic call back:{"action":"publish_test","count":"1"}
```

**影子示例**

修改宏定义 RUN_SAMPLE_TYPE 为 SHADOW_SAMPLE，AT 串口接 ESP8266（已烧录腾讯定制 AT 固件），编译后运行日志如下：

```shell
===========Build Time 20190425===============
Board init over
Sysclk[8000000] TickFreq[1]DBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:0

Start test taskDBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:25888
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|shadow_demo_task(121): shadow_demo_task Entry...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\at_client.c|at_client_init(856): AT client(V1.0.0) initialize success.
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(172): at client init success
...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(189): WIFI CONNECTED
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|net_prepare(70): module init success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|net_prepare(85): Start shakehands with module...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_handshake(226): Module info(6):

AT version:1.3.0.0-dev(6ed31d7 - Apr 18 2019 04:15:44)
SDK version:v3.2-dev-224-g54d3106-dirty
compile time:Apr 24 2019 20:09:42
Bin version:QCloud IoT ESP AT v1.0(Unknown)
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|net_prepare(94): module connect success
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\device.c|iot_device_info_init(62): SDK_Ver: 1.0.0, Product_ID: 03UKNYBUZG, Device_Name: at_dev
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_wifi_conn_func(73): receve wifi conn urc(16):WIFI CONNECTED

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_conn_func(88): receve mqtt conn urc(16):+TCMQTTCONN:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|shadow_demo_task(151): module mqtt conn success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client_manager.c|subscribe_operation_result_to_cloud(168): shadow topic len:42
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_sub_func(101): receve mqtt sub urc(15):+TCMQTTSUB:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_mqtt_sub(402): $shadow/operation/result/03UKNYBUZG/at_dev sub success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|shadow_demo_task(169): shadow construct success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|IOT_Shadow_Get(303): GET Request Document: {\"clientToken\":\"03UKNYBUZG-0\"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(170): requestAck=0
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(173): Received Json Document={"clientToken":"03UKNYBUZG-0","payload":{"metadata":{"reported":{"param_bool":{"timestamp":1556379651134},"param_enum":{"timestamp":1556379651134},"param_float":{"timestamp":1556379651134},"param_int":{"timestamp":1556379651134},"param_string":{"timestamp":1556379651134},"updateCount":{"timestamp":1556379651134}}},"state":{"reported":{"param_bool":0,"param_enum":2,"param_float":4.1399999999999997,"param_int":1345,"param_string":"hello","updateCount":1}},"timestamp":1556379651134,"version":34126},"result":0,"timestamp":1556379659,"type":"get"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|IOT_Shadow_Update(239): UPDATE Request Document: {\"version\":34126\, \"state\":{\"reported\":{\"updateCount\":0}}\, \"clientToken\":\"03UKNYBUZG-1\"}
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|OnShadowUpdateCallback(42): recv shadow update response, response ack: 0
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|IOT_Shadow_Update(239): UPDATE Request Document: {\"version\":34127\, \"state\":{\"reported\":{\"updateCount\":1}}\, \"clientToken\":\"03UKNYBUZG-2\"}
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\shadow_sample.c|OnShadowUpdateCallback(42): recv shadow update response, response ack: 0
```

**影子协议说明**

影子基于 MQTT 的基础上，通过订阅特定的 topic，payload 部分基于为 JSON 格式实现数据协议交互，参见官网影子协议说明和影子快速入门。

**数据模板示例**
修改宏定义 RUN_SAMPLE_TYPE 为 DATATEMPLATE_SAMPLE，AT 串口接 ESP8266（已烧录腾讯定制 AT 固件），编译后运行日志如下：

```shell
===========Build Time 20190425===============
Board init over
Sysclk[8000000] TickFreq[1]DBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:0

Start test taskDBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:25888
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|data_template_demo_task(275): shadow_demo_task Entry...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\at_client.c|at_client_init(856): AT client(V1.0.0) initialize success.
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(172): at client init success
...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(189): WIFI CONNECTED
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|net_prepare(188): module init success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|net_prepare(203): Start shakehands with module...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_handshake(226): Module info(6):

AT version:1.3.0.0-dev(6ed31d7 - Apr 18 2019 04:15:44)
SDK version:v3.2-dev-224-g54d3106-dirty
compile time:Apr 24 2019 20:09:42
Bin version:QCloud IoT ESP AT v1.0(Unknown)
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|net_prepare(212): module connect success
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\device.c|iot_device_info_init(62): SDK_Ver: 1.0.0, Product_ID: V8YCF1RWFJ, Device_Name: dev004
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_wifi_conn_func(73): receve wifi conn urc(16):WIFI CONNECTED

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_conn_func(88): receve mqtt conn urc(16):+TCMQTTCONN:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|data_template_demo_task(306): module mqtt conn success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_sub_func(101): receve mqtt sub urc(15):+TCMQTTSUB:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_mqtt_sub(422): $template/operation/result/V8YCF1RWFJ/dev004 sub success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|data_template_demo_task(325): shadow construct success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_sub_func(101): receve mqtt sub urc(15):+TCMQTTSUB:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_mqtt_sub(422): $thing/down/event/V8YCF1RWFJ/dev004 sub success
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|_register_data_template_property(129): data template property=time registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|_register_data_template_property(129): data template property=float registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|_register_data_template_property(129): data template property=light_switch registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|_register_data_template_property(129): data template property=color registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|_register_data_template_property(129): data template property=brightness registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|_register_data_template_property(129): data template property=name registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|data_template_demo_task(345): Register data template propertys Success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|IOT_Shadow_Get(303): GET Request Document: {\"clientToken\":\"V8YCF1RWFJ-0\"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(170): requestAck=0
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(173): Received Json Document={"clientToken":"V8YCF1RWFJ-0","payload":{"metadata":{"reported":{"brightness":{"timestamp":1556452618075},"color":{"timestamp":1556452630362},"light_switch":{"timestamp":1556452630362},"name":{"timestamp":1556452378475}}},"state":{"reported":{"brightness":64,"color":1,"light_switch":0,"name":""}},"timestamp":1556452630362,"version":9},"result":0,"timestamp":1556459176,"type":"get"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|data_template_demo_task(398): No delta msg received...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\data_template_sample.c|data_template_demo_task(438): No device data need to be reported...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\event\qcloud_iot_event.c|_IOT_Construct_Event_JSON(218): 1024
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_mqtt_pub(331): PUBL cmd used
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\event\qcloud_iot_event.c|_on_event_reply_callback(99): Receive Reply Message: {"method":"event_reply","clientToken":"","version":"","code":403,"status":"","data":{}}

```

**基于数据模板功能的智能灯实例**
修改宏定义 RUN_SAMPLE_TYPE 为 LIGHT_SCENARY_SAMPLE，AT 串口接 ESP8266（已烧录腾讯定制 AT 固件），编译后运行日志如下：

```shell
===========Build Time 20190425===============
Board init over
Sysclk[8000000] TickFreq[1]DBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:0

Start test taskDBG|main.c|mem_info(74): 
Total_mem:30720 freeMem:25888
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|light_data_template_demo_task(454): shadow_demo_task Entry...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\at_client.c|at_client_init(856): AT client(V1.0.0) initialize success.
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(172): at client init success
...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_init(189): WIFI CONNECTED
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|net_prepare(366): module init success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|net_prepare(381): Start shakehands with module...
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_handshake(226): Module info(6):

AT version:1.3.0.0-dev(6ed31d7 - Apr 18 2019 04:15:44)
SDK version:v3.2-dev-224-g54d3106-dirty
compile time:Apr 24 2019 20:09:42
Bin version:QCloud IoT ESP AT v1.0(Unknown)
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|net_prepare(390): module connect success
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\device.c|iot_device_info_init(62): SDK_Ver: 1.0.0, Product_ID: V8YCF1RWFJ, Device_Name: dev004
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_wifi_conn_func(73): receve wifi conn urc(16):WIFI CONNECTED

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_conn_func(88): receve mqtt conn urc(16):+TCMQTTCONN:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|light_data_template_demo_task(484): module mqtt conn success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_sub_func(101): receve mqtt sub urc(15):+TCMQTTSUB:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_mqtt_sub(422): $template/operation/result/V8YCF1RWFJ/dev004 sub success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|light_data_template_demo_task(503): shadow construct success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|urc_mqtt_sub_func(101): receve mqtt sub urc(15):+TCMQTTSUB:OK

DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\module_at\module_api_inf.c|module_mqtt_sub(422): $thing/down/event/V8YCF1RWFJ/dev004 sub success
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|_register_data_template_property(248): data template property=light_switch registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|_register_data_template_property(248): data template property=color registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|_register_data_template_property(248): data template property=brightness registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|_register_data_template_property(248): data template property=light_id registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|_register_data_template_property(248): data template property=name registered.
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|light_data_template_demo_task(523): Register data template propertys Success
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|IOT_Shadow_Get(303): GET Request Document: {\"clientToken\":\"V8YCF1RWFJ-0\"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(170): requestAck=0
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(173): Received Json Document={"clientToken":"V8YCF1RWFJ-0","payload":{"metadata":{"reported":{"brightness":{"timestamp":1556452618075},"color":{"timestamp":1556452630362},"light_switch":{"timestamp":1556452630362},"name":{"timestamp":1556452378475}}},"state":{"reported":{"brightness":64,"color":1,"light_switch":0,"name":""}},"timestamp":1556452630362,"version":9},"result":0,"timestamp":1556459366,"type":"get"}
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|OnDeltaTemplateCallback(224): Property=brightness changed
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|OnDeltaTemplateCallback(224): Property=color changed
[  lighting  ]|[color: RED ]|[brightness:|||||||||-----------]|[][0]
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|IOT_Shadow_Update(239): UPDATE Request Document: {\"version\":10\, \"state\":{\"desired\": null}\, \"clientToken\":\"V8YCF1RWFJ-1\"}
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(170): requestAck=0
DBG|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\src\shadow\shadow_client.c|_update_ack_cb(173): Received Json Document={"clientToken":"V8YCF1RWFJ-1","payload":{"metadata":null,"state":null,"timestamp":1556459380784,"version":11},"result":0,"timestamp":1556459380784,"type":"update"}
INF|..\Middlewares\Third_Party\qcloud-iot-sdk-tencent-at-based\sample\light_data_template_sample.c|light_data_template_demo_task(559): shadow update(desired) success
```

## 相关文档

- [影子协议说明](https://cloud.tencent.com/document/product/634/11918)  
- [影子快速入门](https://cloud.tencent.com/document/product/634/11914#c-sdk-.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)  
- [数据模板介绍](https://cloud.tencent.com/document/product/1081/34916)

## SDK接口说明

关于 AT-SDK 的更多使用方式及接口说明，请参阅 [腾讯 AT_SDK](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based.git)。
