
腾讯云物联网开发平台 IoT Explorer 设备端 C SDK ，配合平台对设备数据模板化的定义，实现和云端基于数据模板协议的数据交互框架，开发者基于 IoT_Explorer C-SDK 数据模板框架，通过脚本自动生成模板代码，快速实现设备和平台、设备和应用之间的数据交互。


## 步骤1：创建云端设备

登录腾讯云 [物联网开发平台控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)，创建云端设备，详情可参考 [基于 TencentOS tiny 接入指引](https://cloud.tencent.com/document/product/1081/47886) 。

另外，数据模板是将物理实体设备进行数字化描述，构建其数字模型。在物联网开发平台定义数据模板即定义产品功能，完成功能定义后，系统将自动生成该产品的数据模板。进入 [物联网开发控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)，单击【项目】>【产品开发】>【智能灯产品】>【数据模板】>【新建功能】，填写功能信息。
![](https://main.qcloudimg.com/raw/3ac50f4b29ea551fac091d782e707610.jpg)
功能类型包含三种元素：

| 功能元素 | 功能描述                                                     |  功能标识符  |
| :------: | ------------------------------------------------------------ | :----------: |
|   属性   | 包括布尔型、整数型、字符型、浮点型、枚举型和时间型等6种基本数据类型；<br>用于描述设备的实时状态，支持读取和设置，如模式、亮度、开关等。 | PropertiesId |
|   事件   | 包括告警、故障和信息3种类型，事件型功能属性可以添加具体的事件参数，这些参数可以由属性中6种基本数据类型组成；<br>用于描述设备运行时的事件，包括告警、信息和故障等3种事件类型，可添加多个输出参数，如环境传感器检测到空气质量很差，空调异常告警等。 |   EventId    |
|   行为   | 用于描述复杂的业务逻辑，可添加多个调用参数和返回参数，可用于让设备执行某项定特定的任务。例如，开锁动作需要知道是哪个用户在什么时间开锁，锁的状态如何等。并且行为的输入参数和输出参数可添加上述6种属性的基本数据类型。 |   ActionId   |

数据类型支持以下6种：

- 布尔型：非真即假的二值型变量。例如，开关功能。
- 整数型：可用于线性调节的整数变量。例如，空调的温度。
- 字符型：以字符串形式表达的功能点，例如，灯的位置。
- 浮点型：精度为浮点型的功能点。例如，压力值的范围：0.0 - 24.0。
- 枚举型：自定义的有限集合值。例如，灯的颜色：白色、红色、黄色等。
- 时间型：string 类型的 UTC 时间戳（毫秒）。

数据模板是一个 JSON 格式的文件，使用数据模板协议，用户的设备需按数据模板定义要求传输设备数据到云端，并可使用基于数据模板的诸多业务功能，单击【查看 JSON】，可查看到已创建功能的 JSON 格式协议。
![](https://main.qcloudimg.com/raw/444e0a291390f93ab2ccb7b0fe743b39.jpg)
## 步骤2：移植 mbedtls

腾讯云 C SDK 对接云端时如果配置建立安全链接，将会用到 mbedtls 加密库，所以需要先移植 mbedtls。

1. TencentOS-tiny 中已经移植适配好 mbedtls 库，并作为 TencentOS-tiny 的一个组件，在 `components\security\mbedtls` 目录下，将此目录复制到工程目录中，复制过程中保持目录架构不变，并将其余的文件删除。
![](https://main.qcloudimg.com/raw/12eb2505fdc85d1209c617146edb9738.png)
2. 将 mbedtls 相关的 c 文件添加到 Keil-MDK 工程中：
 1. 在 Keil 工程中新建 mbedtls 目录分组。
 2. 将 `components\security\mbedtls\wrapper\src` 目录下的移植适配文件添加至 mbedtls 目录下。
 3. 将 `components\security\mbedtls\3rdparty\src` 目录下的源码文件添加至 mbedtls 目录下 。
![](https://main.qcloudimg.com/raw/c5e979c60ed6911cdf7dd6384191def3.png)
5. 将 mbedtls 相关的头文件路径都添加到 Keil-MDK 工程中，移植完成。
![](https://main.qcloudimg.com/raw/42d322db48174d2b8d45d1ac371b776b.png)

>!此时还没有指定 mbedtls 配置文件，编译会报错，继续按后续的步骤操作即可。

## 步骤3：移植腾讯云 C SDK

TencentOS-tiny 官方已经将 IoT_Explorer C SDK 移植适配完成，在 `components\connectivity\qcloud-iot-explorer-sdk` 目录下，其中：
- 3rdparty：IoT_Explorer C SDK 源码。
- port\TencentOS_tiny：移植适配文件 qcloud/port。

用于使用 TencentOS-tiny 物联网操作系统时，只需要添加相关文件，并修改云端设备对接信息即可，方便快捷。

接下来将介绍基于之前步骤已移植成功的网络工程，讲述如何移植 C SDK。

1. 将 TencentOS-tiny 源码中 `qcloud-iot-explorer-sdk` 整个目录复制到工程目录中，保持原有目录架构不变并删除其余的目录。
![](https://main.qcloudimg.com/raw/20b21e8a5f13cb19b9e2802abc8f8521.png)
2. 添加腾讯云 C SDK 移植到 TencentOS-tiny 的适配文件。
 1. 在Keil 工程下新增 qcloud/port 目录分组。
 2. 将 `components\connectivity\qcloud-iot-explorer-sdk\port\TencentOS_tiny` 分组下的部分文件添加至 qcloud/port 目录下。
![](https://main.qcloudimg.com/raw/98874628515ef2f81ac25cbd347a49bf.png)
3. 添加腾讯云 C SDK 中的 MQTT 协议相关源码。
 1. 在Keil 工程下新增 qcloud/protocol/mqtt 目录分组。
 2. 将  `components\connectivity\qcloud-iot-explorer-sdk\3rdparty\sdk_src\protocol\mqtt` 目录下的文件添加至 qcloud/protocol/mqtt 目录下。
![](https://main.qcloudimg.com/raw/b8ef97f3f8b4f9920a89635c99105d8a.png)
4. 添加腾讯云 C SDK 中的数据模板相关源码。
 1. 在Keil 工程下新增 qcloud/services/data_template 目录分组。
 2. 将 `components\connectivity\qcloud-iot-explorer-sdk\3rdparty\sdk_src\services\data_template` 目录下的文件添加至 qcloud/services/data_template 目录下。
![](https://main.qcloudimg.com/raw/bcf71662d4db21964ef51ca7fd420bd7.png)
5. 添加腾讯云 C SDK 中所使用到的工具源码。
 1. 在Keil 工程下新增 qcloud/utils 目录分组。
 2. 将 `components\connectivity\qcloud-iot-explorer-sdk\3rdparty\sdk_src\utils` 目录下的文件添加至 qcloud/utils 目录下。
![](https://main.qcloudimg.com/raw/6193f9c38d19673a60d828a414ca65a8.png)
6. 添加腾讯云 C SDK 中所用到网络封装层源。
 1. 在Keil 工程下新增 qcloud/network 目录分组。
 2. 将 `components\connectivity\qcloud-iot-explorer-sdk\3rdparty\sdk_src\network` 目录下的文件添加至 qcloud/network 目录下。
 3. 将 `components\connectivity\qcloud-iot-explorer-sdk\3rdparty\platform\tls\mbedtls` 目录下的文件添加至 qcloud/network 目录下。
![](https://main.qcloudimg.com/raw/06f9a9dabaf97d40a4afcbfcae0c40f5.png)
7. 添加所有用到的头文件路径。
![](https://main.qcloudimg.com/raw/f32de0894c46b4e71d52d157fc44c3d8.png)
8. 最后添加宏定义 `MBEDTLS_CONFIG_FILE=<qcloud/tls_psk_config.h>`，指定 mebedtls 库的配置文件。
![](https://main.qcloudimg.com/raw/b06347a849ebda241cd4f1360d601aa2.png)

移植完成，此时编译时未发现错误信息，其中警告可暂时忽略。

## 步骤4：修改端云对接信息

修改 `HAL_Device_tencentos_tiny.c` 文件。在 `TencentOS-tiny\components\connectivity\qcloud-iot-explorer-sdk\port\TencentOS_tiny` 目录中，将下图中的数据分别替换为控制台【设备详情页】中的参数并保存。
- 产品 ID： 将控制台的产品 ID ，复制到下图 sg_product_id。
- 设备名称： 将控制台的设备名称，复制到下图 sg_device_name。
- 设备密钥：将控制台的设备密钥，复制到下图 sg_device_secret。
![](https://main.qcloudimg.com/raw/38461264f3317e674b34aee86a8c8a33.png)

## 步骤5：加入示例代码

1. 由于腾讯云 C SDK 的测试代码较多，所以将直接使用官方仓库中提供的示例文件。
 1. 在 `examples\qcloud_iot_explorer_sdk_data_template` 目录下，将此目录复制到工程目录中，保持原有目录架构不变。
 ![](https://main.qcloudimg.com/raw/f4c02b60f205a6e2252de9c1569228f2.png)
 2. 将示例代码加入到 Keil-MDK 工程中。
 >!请勿将 `data_config.c` 文件加入。
 >
    1. 在 Keil 工程中新增 examples 目录分组。
    2. 将 `examples\qcloud_iot_explorer_sdk_data_template` 目录下的文件添加至 example 目录下。
![](https://main.qcloudimg.com/raw/9a8ff427fcc534716084e12e9f09ba7d.png)
 3. 修改 `entry.c` 中的配置信息。
![](https://main.qcloudimg.com/raw/634802ce66eed194119fafe3007fef55.png)

2. 示例代码中的任务入口函数为 application_entry，所以需要将 task1 任务的任务入口函数修改为 application_entry，并再次扩大 task1 的任务栈为4096字节，使示例程序正常运行。
![](https://main.qcloudimg.com/raw/eeaad945f1d3dd547e95696bc3be17e1.png)
3. 然后修改创建任务的代码。
![](https://main.qcloudimg.com/raw/0204d8b237e2c5ec1e3153332e8c0c5a.png)
4. 最后进行编译，将程序下载到开发板中，复位开发板后开始运行，便可以在串口助手中查看打印信息。

## 步骤6：查看设备状态

1.	保持 light Demo 程序为运行状态。
2.	进入【[控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)】>【产品开发】>【设备调试】，可查看到设备 "dev001" 的状态为“上线”状态，表示 Demo 程序已成功连接上开发平台。
![](https://main.qcloudimg.com/raw/a83eb554c2958e705d49451bfa217602.png)
3.	单击【查看】，可进入设备详情页。
![](https://main.qcloudimg.com/raw/c08da8cf2b2748d93368059740cbe6fa.png)

## 步骤7：下发控制指令
1. 在串口助手中看到设备查看到在等待平台下发控制指令。
![](https://main.qcloudimg.com/raw/cbc63e3dab5f777ea9101209035f88f1.png)
2. 然后在云端平台进入设备在线调试，下发控制指令。
![](https://main.qcloudimg.com/raw/7298a5f4b0c831f0814a4a59325e4d78.png)
3. 最后可以在串口助手中查看到设备收到后在串口打印控制指令。
![](https://main.qcloudimg.com/raw/e53d6c15dc441d4049b2a3e75888cdc6.png)

## 步骤8：设备行为调用
1. 在云端的数据模板中手动新建一个设备行为功能。
![](https://main.qcloudimg.com/raw/19ab99e774389887eac8338f5238e9bc.png)
2. 在 `data_template_sample.c` 文件中使能 Action。
![](https://main.qcloudimg.com/raw/8f605b70838ae7c12133617977d95c0b.png)
3. 重新编译下载，按复位运行。
 - 在云端下发设备行为调用：
![](https://main.qcloudimg.com/raw/4320c5a421a5c8d54ac7ee9120e5912c.png)
 - 在串口助手中可以看到设备行为被调用：
![](https://main.qcloudimg.com/raw/45ba81613db4951e9f023b0156bb3f72.png)

## 步骤9：设备事件调用

1. 修改 `config.h` 文件，将设备行为调用关闭，开启设备事件支持。
![](https://main.qcloudimg.com/raw/9acffe18e3fe691b59da9bb3e4e24ed5.png)
2. 修改 `data_template_sample.c` 文件，开启事件上报示例，屏蔽设备行为调用示例。
![](https://main.qcloudimg.com/raw/fec5cb657faba5cb805b1c1849bf46da.png)
3. 编译程序，下载到开发板中，复位。
 - 在串口助手中可以看到设备上报事件的日志：
![](https://main.qcloudimg.com/raw/c0e27c9ad677b2656fea7cf1091a8916.png)
 - 在平台端可以看到设备上报事件的日志：
![](https://main.qcloudimg.com/raw/86b8032eccfd6a1901f70ad828ec3cdb.png)


