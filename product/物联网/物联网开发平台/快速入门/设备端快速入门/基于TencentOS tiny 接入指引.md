## 操作场景

假设一款智能灯接入到物联网开发平台，通过物联网开发平台可以远程控制灯的亮度、颜色、开关，并实时获取智能灯上报到物联网开发平台的数据。本文档主要指导您如何基于 TencentOS-tiny 物联网操作系统，使用 MQTT 协议在物联网开发平台控制台接入智能灯。

## 前提条件

为了通过下面的步骤快速理解该业务场景，需要做好以下准备工作：
- 申请 [物联网开发平台服务](https://console.cloud.tencent.com/iotexplorer)，详情请参见 [购买指南](https://cloud.tencent.com/document/product/1081/51938)。
- 准备 TencentOS-tiny 官方 EVB_MX_Plus 开发板以及一个 ESP8266 Wi-Fi 模组。

## 控制台操作

### 创建项目

1. 登录 [物联网开发平台控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)。 单击【新建项目】，填写“项目名称”和“项目描述”。
 - 项目名称：输入“智能灯演示”或其他名称。
 - 项目描述：按照实际需求填写项目描述。
![](https://main.qcloudimg.com/raw/a696eca1c331421602e5d099c985d252.jpg)
2. 项目基本信息填写完成后，单击【保存】，即可完成项目创建。
3. 项目创建成功后，即可新建产品。

### 新建产品

1. 进入该项目的产品列表页面，单击【新建产品】.
2. 在新建产品页面，填写产品基本信息。
  - 产品名称：输入“智能灯”或其他产品名称。
  - 产品品类：选择【智慧城市】>【公共事业】>【路灯照明】。
  - 设备类型：选择“设备”。
  - 认证方式：选择“密钥认证”。
  - 通信方式：按需选择。
  - 数据协议：默认为“数据模板”。
  - 描述：按照实际需求填写项目描述。
![](https://main.qcloudimg.com/raw/6f79d468a05c1bd5dd7dd7357a5c0971.jpg)
3. 产品信息填写完成后，单击【保存】，即可完成产品创建。
4. 产品创建成功后，可在产品列表页查看到“智能灯”。


### 创建数据模板

当新建产品将“产品类型”选择为【路灯照明】时，此时单击该产品进入产品详情页，系统将会自动生成标准功能。
![](https://main.qcloudimg.com/raw/f78bde95fd38ce6b7e27c65a81742dea.png)

### 创建测试设备

在【设备调试】页面中，单击【新建设备】，设备名为 dev001。

![](https://main.qcloudimg.com/raw/4f7f39df544ce19cf38126ddd79a49b3.png)

## 开发板实物操作

### 硬件连接

开发板实物如下：

![](https://main.qcloudimg.com/raw/4f47e4d3ba910e4528c9738c0ed65010.png)

1. 使用 USB 线连接到开发板顶端的 USB 接口，在为开发板供电的同时，可以在 PC 端通过串口调试助手查看输出日志。
2. 使用 ST-Link 下载器连接开发板右侧的接口，为开发板下载程序。
3. 将开发板配套的 ESP8266 模组插入到开发板右侧的通信模组接口。

### 串口准备
1. 硬件连接成功后，打开 PC 端上的设备管理器，即可查看开发板所对应的串口（请确保已安装[ CH340 驱动](https://sparks.gogo.co.nz/ch340.html)）。
![](https://main.qcloudimg.com/raw/5c44a520e8d0bc22d0e9849d8bcf3868.png)

2. 打开串口工具，做好相应配置后，打开串口。
  - 端口号：本例中为 COM20。
  - 波特率：本例中为 115200。
![](https://main.qcloudimg.com/raw/7c81c38f438aaef596d8afbab537c3f6.png)

### 属性上报和控制命令下发

#### 步骤1：下载官方例程

1. 使用 git 工具下载 TencentOS-tiny 源码，也可以访问 [Github](https://github.com/Tencent/TencentOS-tiny) 官方仓库下载。
```bash
git clone https://github.com/Tencent/TencentOS-tiny.git
```
2. 下载之后，进入 `TencentOS-tiny\board\TencentOS_tiny_EVB_MX_Plus\KEIL\qcloud_iot_explorer_sdk_data_template` 目录。
![](https://main.qcloudimg.com/raw/5233e111b7caa55d9f1b87ad63de5089.png)
3. 示例工程中包含 STM32L431 外设驱动、TencentOS-tiny 内核、AT 框架、SAL 框架、腾讯云 C-SDK，以及示例程序。

#### 步骤2：配置修改

1. 双击 `TencentOS_tiny.uvprojx` 打开工程（请确保已经安装好 Keil-MDK 开发环境）。
2. 在 `TencentOS-tiny\components\connectivity\qcloud-iot-explorer-sdk\port\TencentOS_tiny` 目录：
 1. 修改 `HAL_Device_tencentos_tiny.c` 文件。
 2. 登录 [物联网开发控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)，单击【项目】>【产品开发】>【设备调试】，单击【调试】进入设备详情页，将下图红色线框中的数据分别替换为“设备详情页”中的参数并保存。
    -  产品 ID： 将控制台的产品 ID ，复制到下图 sg_product_id。
    -  设备名称： 将控制台的设备名称，复制到下图 sg_device_name。
    -  设备密钥：将控制台的设备密钥，复制到下图 sg_device_secret。
  ![](https://main.qcloudimg.com/raw/cadab6199c68fc70debc7e02a6580731.png)
 3. 修改 entry.c 中的 Wi-Fi 网络接入配置信息。
![](https://main.qcloudimg.com/raw/d1dc0309a19ff454112f64fbc3111da2.png)

#### 步骤3：编译

单击 MDK 工具栏【Rebuild All】，编译整个工程。

#### 步骤4：下载

单击 MDK 工具栏【Download】，下载编译完成的固件。

#### 步骤5：查看运行结果

在串口助手中可以看到设备在上报之后处于等待平台下发控制指令的状态。
![](https://main.qcloudimg.com/raw/1a5c4c6cc1e3c7e913a92a3e9949dafb.png)

### 物联网平台查看上报数据

1. 保持系统处于运行状态。
2.  登录 [物联网开发控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)，单击【项目】>【产品开发】>【设备调试】，可查看到设备 "dev001" 。
3. 单击【调试】，可进入设备详情页。
![](https://main.qcloudimg.com/raw/b873b65c618480ede6485073090bc1f2.png)
4. 单击【设备属性】，可查询设备上报到开发平台的最新数据及历史数据。
  - 最新值：显示设备上报的最新数据。
  - 更新时间：显示数据的更新时间。
  - 历史数据：单击【查看】，可查看某个属性的历史上报数据。

![](https://main.qcloudimg.com/raw/c08da8cf2b2748d93368059740cbe6fa.png)

### 物联网平台在线调试

1. 在控制台【设备调试】列表，单击【在线调试】，进入在线调试。
2. 设置电灯开关为 on，颜色为 Green，亮度为3，单击【发送】。
![](https://main.qcloudimg.com/raw/0251c905751df941afde8063c07006dd.png)
3. 在串口上查看系统打印的串口日志，判断出系统成功收到并响应了下发的控制指令。
![](https://main.qcloudimg.com/raw/2f490b4a236c230c3aaed973c59ccc75.png)
4. 同时，在开发板的OLED显示屏幕上，可以看到系统模拟出的智能灯状态。
![](https://main.qcloudimg.com/raw/7f2d51718313d34a050e1ba2a9992d18.png)

### 设备行为调用

1. 在【物联网开发控制台】>【项目】>【产品开发】>【数据模板】>【新建功能】，手动新建一个 [设备行为功能](https://cloud.tencent.com/document/product/1081/47958)。
![](https://main.qcloudimg.com/raw/7736a6f45b43acf218fd5e49cbb44f27.jpg)
2. 修改工程文件，在 `data_template_sample.c` 文件中使能 Action。
![](https://main.qcloudimg.com/raw/8f605b70838ae7c12133617977d95c0b.png)
3. 重新编译下载，在开发板上按下【复位】键使系统运行。
4. 在物联网开发控制台上下发设备行为调用。
![](https://main.qcloudimg.com/raw/4320c5a421a5c8d54ac7ee9120e5912c.png)
5. 在串口助手中可查看到设备行为被调用。
![](https://main.qcloudimg.com/raw/5b185b7aa8cf7243956a53e536a668b6.png)

### 设备事件上报

1. 修改工程文件中的 `config.h` 文件，将设备行为调用支持屏蔽，开启设备事件上报支持。
![](https://main.qcloudimg.com/raw/602e0f0d6d6049f74b30c9b46dd7aa46.png)
2. 修改工程文件中的 `data_template_sample.c` 文件，关闭设备行为调用示例，开启事件上报示例。
![](https://main.qcloudimg.com/raw/9dfd57b19dd6ce96b4e24704905b48a4.png)
3. 编译程序，下载到开发板中，在开发板上按【复位】使系统运行。
4. 在串口助手中可查看到设备上报事件的日志。
![](https://main.qcloudimg.com/raw/9b50a4d07439b0162d790672850aed8d.png)
5. 在物联网开发控制台上可查看到设备上报事件的日志。
![](https://main.qcloudimg.com/raw/86b8032eccfd6a1901f70ad828ec3cdb.png)

  

