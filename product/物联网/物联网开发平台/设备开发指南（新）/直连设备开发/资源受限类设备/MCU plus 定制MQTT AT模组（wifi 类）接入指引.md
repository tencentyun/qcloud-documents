
腾讯云物联网与主流的模组厂商进行深度合作，将 SDK 的核心协议移植到 Wi-Fi 模组中，模组对外封装统一的腾讯云物联网 AT 指令，并提供配合使用的 [AT SDK](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based.git)。

## SDK 获取

在 iot-explorer 平台 [创建产品和设备](https://cloud.tencent.com/document/product/1081/34739) 后，选择基于 MQTT AT 定制模组开发的方式，将会自动生成 MCU 侧的 [AT SDK](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based.git) 代码，并且把在平台创建的数据模板和事件生成了对应的配置及初始化代码。

## 接入指引

MCU+ 定制 MQTT AT 模组（Wi-Fi 类）接入腾讯云物联网开发平台可以分为以下4个步骤。
### 平台适配移植

根据所选的嵌入式平台，适配 hal_export.h 头文件对应的 HAL 层 API 的移植实现。主要有串口收发（中断接收）、模组开关机、任务/线程创建、动态内存申请/释放、时延、打印等 API。详细操作可参考基于 STM32+FreeRTOS 的 AT-SDK [移植示例](https://github.com/tencentyun/tc-iot-at-sdk-stm32-freertos-based-example)。

移植部分需要实现的 HAL 层适配接口请参考 hal_export.h，需要实现串口的收发接口（中断接收），延时函数，模组上下电及 OS 相关接口适配（互斥锁、动态内存申请释放、线程创建），适配层接口单独剥离在 port 目录。

#### 1. hal_export.h

该源文件主要提供 HAL 层对外的 API 接口及 HAL 层宏开关控制。

| 序号 | 宏定义                  | 说明                                                         |
| ---- | ----------------------- | ------------------------------------------------------------ |
| 1    | PARSE_THREAD_STACK_SIZE | 串口 AT 解析线程栈大小。                                     |
| 2    | OS_USED                 | 是否使用 OS，目前的 AT-SDK 是基于多线程框架的，所以 OS 是必须的。 |
| 3    | AUTH_MODE_KEY           | 认证方式，证书认证还是密钥认证。                             |
| 4    | DEBUG_DEV_INFO_USED     | 默认使能该宏，设备信息使用调试信息，正式量产关闭该宏，并实现设备信息存取接口。 |

#### 2. hal_os.c

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

#### 3. hal_at.c

该源文件主要实现 AT 串口初始化、串口收发、模组开关机。

| 序号  | HAL_API                         | 说明                                 |
| ---- | -------------------------------| ----------------------------------|
| 1    | module_power_on                | 模组开机，AT 串口初始化，必选实现。      |
| 1    | module_power_off               | 模组关机，低功耗需要，可选实现。                |
| 2    | AT_UART_IRQHandler             | 串口接收中断 ISR，将收取到的数据放入 ringbuff 中，AT 解析线程会实时解析数据，必选实现。|
| 3    | at_send_data                   | AT 串口发送接口。                             |

#### 4. module_api_inf.c

该源文件主要实现了配网/注网 API 业务适配和基于腾讯云物联网 AT 指令的 MQTT 交互，但有一个关于联网/注网的 API（module_register_network）需要根据模组适配。代码基于 [ESP8266 腾讯云物联网定制 AT 固件](https://main.qcloudimg.com/raw/6811fc7631dcf0ce5509ccbdba5c72b7.zip) 实现了 Wi-Fi 直连的方式连接网络，但更常用的场景是根据特定事件（例如：按键）触发配网（softAP/一键配网），这块的逻辑各具体业务逻辑需自行实现。

ESP8266 有封装配网指令和示例 App。对于蜂窝模组，则是使用特定的网络注册指令。请参照 [module_handshake](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based/blob/master/include/module_api_inf.h) 函数应用 AT-SDK 的 AT 框架添加和模组的 AT 指令交互。
```c
//模组联网（NB/2/3/4G注册网络）、wifi配网（一键配网/softAP）暂时很难统一,需要用户根据具体模组适配。
//开发者参照 module_handshake API使用AT框架的API和模组交互，实现适配。
eAtResault module_register_network(eModuleType eType)
{
    eAtResault result = AT_ERR_SUCCESS;

#ifdef MODULE_TYPE_WIFI
    if(eType == eMODULE_ESP8266)
    {
        #define WIFI_SSID "test_****"
        #define WIFI_PW "********"

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

### 设备信息修改

调试时，在 hal_export.h 将设备信息调试宏定义打开。量产时需要关闭该宏定义，实现 hal-os 中序列 17-26 的设备信息存取 API。

```c
#define DEBUG_DEV_INFO_USED
```

修改下面宏定义的设备信息，则系统将会使用调试信息。

```c
#ifdef DEBUG_DEV_INFO_USED

static char sg_product_id[MAX_SIZE_OF_PRODUCT_ID + 1] = "03UKN1****";
static char sg_device_name[MAX_SIZE_OF_DEVICE_NAME + 1] = "at****";

#ifdef AUTH_MODE_CERT
static char sg_device_cert_file_name[MAX_SIZE_OF_DEVICE_CERT_FILE_NAME + 1]      = "YOUR_DEVICE_NAME_cert.crt";
static char sg_device_privatekey_file_name[MAX_SIZE_OF_DEVICE_KEY_FILE_NAME + 1] = "YOUR_DEVICE_NAME_private.key";
#else
char sg_device_secret[MAX_SIZE_OF_DEVICE_SERC + 1] = "ttOARy0PjYgzd9OSs1****==";
#endif

#endif
```

### 上下行业务逻辑开发

自动生成的代码 data_template_usr_logic.c，已实现数据、事件收发及响应的通用处理逻辑。但是具体数据处理的业务逻辑需要用户自己根据业务逻辑添加，上下行业务逻辑添加的入口函数分别为 `deal_up_stream_user_logic` 、`deal_down_stream_user_logic`。

#### 1. 下行业务逻辑实现
```c
/*用户需要实现的下行数据的业务逻辑,pData除字符串变量已实现用户定义的所有其他变量值解析赋值，待用户实现业务逻辑*/
static void deal_down_stream_user_logic(ProductDataDefine   * pData)
{
    Log_d("someting about your own product logic wait to be done");
}
```

#### 2. 上行业务逻辑实现
```c
/*用户需要实现的上行数据的业务逻辑,此处仅供示例*/
static int deal_up_stream_user_logic(DeviceProperty *pReportDataList[], int *pCount)
{
    int i, j;

     for (i = 0, j = 0; i < TOTAL_PROPERTY_COUNT; i++) {
        if(eCHANGED == sg_DataTemplate[i].state) {
            pReportDataList[j++] = &(sg_DataTemplate[i].data_property);
            sg_DataTemplate[i].state = eNOCHANGE;
        }
    }
    *pCount = j;

    return (*pCount > 0)?AT_ERR_SUCCESS:AT_ERR_FAILURE;
}
```

### 应用开发

Sample 目录一共有3个示例，用户可以参考各示例根据业务逻辑进行应用开发，分别是 mqtt_sample.c、shadow_sample.c、light_data_template_sample.c。
各示例说明如下：

| 序号  | 示例名称                        | 说明|
| ---- | -------------------------------| ----------------------------------|
| 1    | mqtt_sample.c                  | MQTT 示例，该示例示例基于定制的 AT 指令如何便捷的接入腾讯物联网平台及收发数据。|
| 2    | shadow_sample.c                | 影子示例，基于 AT 实现的 MQTT 协议，进一步封装的影子协议。               |
| 3    | light_data_template_sample.c   | 基于智能灯的控制场景，示例具体的产品如何应用数据模板及事件功能。        |

更多详情请参见 [数据模板协议](https://cloud.tencent.com/document/product/1081/34916)。

## SDK 使用参考

请参见 [AT SDK 使用参考](https://cloud.tencent.com/document/product/1081/48366)。
