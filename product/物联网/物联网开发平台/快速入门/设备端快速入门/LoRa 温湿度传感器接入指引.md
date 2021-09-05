
## 操作场景
假设一款 LoRa 温湿度传感器 接入到物联网开发平台，通过物联网开发平台可以远程查看传感器的温度、湿度，并可远程配置传感器的上报周期。本文档主要指导您如何在物联网开发平台控制台，接入 LoRa 温湿度传感器。

## 前提条件
为了通过下面的步骤快速理解该业务场景，需要做好以下准备工作：
- 申请物联网开发平台服务。
- 意法半导体 (ST) P-Nucleo-LRWAN3 开发套件。
- 拥有一台物理或虚拟的 Windows 环境，并根据 [基于 TencentOS tiny 的 LoRaWAN 开发入门指南](https://github.com/Tencent/TencentOS-tiny/blob/master/doc/16.TencentOS_tiny_LoRaWAN_Getting_Started_Guide.md) 的介绍完成开发环境搭建，包括 MDK 软件的安装及配置、ST-Link 驱动安装、串口软件的安装。


## 控制台操作 LoRa 节点

#### 创建项目
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择【新建项目】。
2. 在新建项目页面，填写项目基本信息后，单击【保存】
    - 项目名称：输入“LoRa 温湿度传感器演示”或其他名称。
    - 项目描述：按照实际需求填写项目描述。
3. 项目新建成功后，即可新建产品。

#### 新建产品
1. 进入该项目的产品列表页面，单击【新建产品】。
2. 在新建产品页面，填写产品基本信息后，单击【保存】。
    - 产品名称：输入“温湿度传感器”或其他产品名称。
    - 产品类型：选择“用户自定义”。
    - 设备类型：选择“设备”。
    - 认证方式：选择“密钥认证”。
    - 通信方式：选择“LoRaWAN”。
![](https://main.qcloudimg.com/raw/e1d8add09289d020a3ea3b9a8e93c501.jpg)
3. 产品新建成功后，您可在产品列表页查看“LoRa 温湿度传感器”。

#### 创建数据模板
单击产品名称，进入产品配置页，在【数据模板】的“自定义功能”配置项下，单击【新建功能】，自定义产品功能。
![](https://main.qcloudimg.com/raw/df88f053e5316049df4ee3f1c68edb71.jpg)

#### 配置 LoRaWAN 参数
在设备开发页面中，按需调整 LoRaWAN 参数配置。本示例中使用默认的 OTAA 配置。
![](https://main.qcloudimg.com/raw/a830f63360ce2c450236158b6fc56b61.png)

#### 设备数据解析
在设备开发页面中，按需调整设备数据解析。由于 LoRa 类资源有限设备不适合直接传输 JSON 格式数据，使用“设备数据解析”可以将设备原始数据转化为产品 JSON 数据。

#### 设备数据协议
在本示例中，设备上行数据共4字节：
- 第1字节：温度。
- 第2字节：相对湿度。
- 第3、4字节：表示上报周期（单位秒）。

设备下行数据为2字节：上报周期（单位秒）。

#### 数据解析脚本
上行数据解析的脚本主函数为 RawToProtocol，其带有 fPort、bytes 两个入参：
- fPort：设备上报的 LoRaWAN 协议数据的 FPort 字段。
- bytes：设备上报的 LoRaWAN 协议数据的 FRMPayload 字段。

脚本主函数的出参为产品数据模版协议格式的对象。

在上行数据解析部分，javascript 示例代码如下：
<dx-codeblock>
:::  javascript
function RawToProtocol(fPort, bytes) {
    var data = {
        "method": "report",
        "clientToken" : new Date(),
        "params" : {}
    };
    data.params.temperature = bytes[0];
    data.params.humidity = bytes[1];
    data.params.period = bytes[2] | (bytes[3] << 8);
    return data;
}
:::
</dx-codeblock>

下行数据解析的脚本主函数为 ProtocolToRaw，其入参为产品数据模版协议格式的对象，其出参为至少3个字节的数组：
- 第1字节：下发给设备的 LoRaWAN 协议数据的 FPort 字段。
- 第2字节：bytes 为下发给设备的 LoRaWAN 协议数据的 MType（0表示 Unconfirmed Data Down，1表示 Confirmed Data Down）。
- 第3字节：开始为下发给设备的 LoRaWAN 协议数据的 FRMPayload 字段。

在下行数据解析部分，javascript 示例代码如下：
<dx-codeblock>
:::  JavaScript
function ProtocolToRaw(obj) {
    var data = new Array();
    data[0] = 5;// fport=5
    data[1] = 0;// unconfirmed mode
    data[2] = obj.params.period & 0x00FF;
    data[3] = (obj.params.period >> 8) & 0x00FF;
    return data;
}
:::
</dx-codeblock>

![](https://main.qcloudimg.com/raw/83318c5e53ecd928ee960ba4a20ca63c.png)

#### 脚本模拟测试
您也可使用数据解析页面下方的模拟调试工具，如需开发更多的功能，请使用以下模拟脚本。
- 上行消息
设备原始数据为 0x11451E00，我们将其转化为数组，即上行模拟数据为：[17,69,30,0]，填入设备上行数据的编辑框中。单击【运行】，即可在模拟调试界面右侧查看结果。
![](https://main.qcloudimg.com/raw/5acd842a170a06f68610629715d238d7.png)
- 下行消息
模拟测试数据如下，将其填入设备下行数据的编辑框中：
<dx-codeblock>
:::  JSON
{
  "params": {
    "period": 15
  }
}
:::
</dx-codeblock>

![](https://main.qcloudimg.com/raw/55fb6d32d23f3f3a26e01316c7c2025c.png)


#### 创建测试设备

在设备调试页面中，单击【新建设备】，设备名为 dev001。
![](https://main.qcloudimg.com/raw/6b868147e1d5758df6e81e9a5a2b8ddb.jpg)
## 控制台操作 LoRa 网关

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择上文 “控制台操作 LoRa 节点” 中对应的项目。
2. 在左侧工具列表中，选择【网络管理】>【LoRa 网关管理】。
3. 进入 LoRa 网关管理页面，选择【社区网络】>【添加网关】。
![](https://main.qcloudimg.com/raw/13aef97fa1e940e2e95cf839ee849c14.jpg)
4. 在新建网关页面，填写网关基本信息。
    - 网关名称：本示例中填写 GW1。
    - GwEUI：为网关唯一 ID。本例中根据 ST NUCLEO LoRa GW 背部的 MAC 地址，将6字节 MAC 地址的中间补足 0xffff。  
![](https://main.qcloudimg.com/raw/4942c0663367a38f5ef090c62fcba5b3.png)
    - 是否公开：选择“是”，表示社区开发者可在社区网络查看该网关，并可通过这个网关进行 LoRa 节点接入；选择“否”，则仅用户自己能查看该网关。
![](https://main.qcloudimg.com/raw/db456fdbd41f0f667655eec4065f397a.jpg)
5. 网关新建成功后，您可在网关列表页查看“GW1”。



## LoRa 网关实物操作

### 硬件连接

整个系统搭建需要由 LRWAN_GS_LF1 网关（网关模组和 STM32F746 Nucleo 核心板）、5V 适配器和电脑组成。

1. 先使用 5V 适配器通过 USB 线连接到 LRWAN_GS_LF1 网关的网关模组上的 Micro USB 接口，给整个网关供电。
2. Nucleo 核心板上的 Micro USB 口（非以太网口那边的 Micro USB 口），通过 USB 线连接到 PC 端，可以实现虚拟串口的功能。
3. 网关开发板通过网线连接到上一级路由器的 LAN 口，从而可以实现 DHCP 的方式连接以太网。
![](https://main.qcloudimg.com/raw/a9bb54a371621a5085f2b1632bb71262.png)

### 串口准备

1. 硬件连接成功后，打开 PC 上的设备管理器，即可查看网关所对应的串口（请确保已安装 stlink 驱动）。
![](https://main.qcloudimg.com/raw/5219609aac65729562a9bdf9bbf7906d.png)
2. 打开串口工具，做好相应配置后，打开串口。
   - 端口号。本例中为 COM5。
   - 波特率。本例中为 115200。
![](https://main.qcloudimg.com/raw/0ddf029ee09642f8a24f20e0d5fa7e50.png)


### 配置修改

请按照如下步骤完成相关配置：
1. 按照上图完成硬件连接和系统搭建。  
2. 配置服务器地址。本示例中设置的是腾讯云物联网开发平台的 LoRa 服务器地址（接入域名：`loragw.things.qcloud.com`，接入端口：1700）。 
```
AT+PKTFWD=loragw.things.qcloud.com,1700,1700  
```
3. 配置频率计划。调整频点信息到486.3MHz - 487.7 MHz，指令修改如下（需要逐条发送）：
```
AT+CH=0,486.3,A
AT+CH=1,486.5,A
AT+CH=2,486.7,A
AT+CH=3,486.9,A
AT+CH=4,487.1,B
AT+CH=5,487.3,B
AT+CH=6,487.5,B
AT+CH=7,487.7,B
AT+CH=8,OFF
AT+CH=9,OFF
```
示例截图如下所示：
![](https://main.qcloudimg.com/raw/d47c4a4eb317be8eaf7d6580f7693ec6.png)
4. 其他指令。  
 - 通过“AT+log=on”打开网关日志。  
 - 通过“AT+EUI”查询网关的 ID。  


### 运行

通过 AT+Reset 即可复位网关，开始服务器连接。

从串口日志查看：
```
LORAWAN SERVER: loragw.things.qcloud.com 
```
表明服务器地址修改成功。
```
Ethernet started
DHCP IP: 192.168.3.249
Downlink UDP Connected
Uplink UDP Connected
```
表明网关 DHCP 入网成功，网络连接正常。


## LoRa 节点实物操作
### 编译及下载

#### Step 1. 下载 LoRaWAN 例程
1. 请下载 TencentOS tiny 官方开源仓 [下载源码](https://github.com/Tencent/TencentOS-tiny) 。
2. 进入`<TencentOS-tiny\board\NUCLEO_STM32L073RZ\KEIL\lorawan>`目录，打开 TencentOS_tiny.uvprojx 工程。
3. 示例工程包含 STM32L073 外设驱动、TencentOS tiny 内核、AT 框架、RHF76 LoRaWAN 模组驱动、LoRaWAN 示例案例。

#### Step 2. 代码修改
1. 请先修改`\examples\LoRaWAN\lora_demo.c.`。
```c
tos_lora_module_join_otaa("8cf957200000f806", "8cf957200000f8061b39a****d204a72");
```
填入节点相应的 DevEUI 和 AppKEY，可从 LoRa 节点开发板背面贴纸上获取。
2. 修改`\devices\rhf76_lora\RHF76.h`。
```c
#define RHF76_ATCMD_SET_CHANNEL                 "at+ch=num,0-7\r\n"
```
由于本示例中计划使用80 - 87信道，因此调整为：
```c
#define RHF76_ATCMD_SET_CHANNEL                 "at+ch=num,80-87\r\n"
```

#### Step 3. 编译
单击 MDK 工具栏【Rebuild All】，编译整个工程。


#### Step 4. 下载
单击 MDK 工具栏【Download】，下载编译好的固件。

### 查看运行结果

1. 节点下载好固件后，会自动重启运行，从串口即可查看设备的运行日志。
![](https://main.qcloudimg.com/raw/00be29ef29119f368e393784800762ce.png)
2. 当您看到串口打印如下日志，即说明 LoRa 节点已经通过网关成功入网。
```
--->+JOIN: Network joined
--->+JOIN: NetID 000035 DevAddr 6B:CC:9B:5D
```

## 查看设备状态

1. 保持 LoRa 节点和 LoRa 网关 为运行状态。
2. 进入【控制台】>【产品开发】>【设备调试】，可查看到设备 "dev001" 。
3. 单击【调试】，可进入设备详情页。
![](https://main.qcloudimg.com/raw/a1db99a803be3e01c0e161ef7509a5bb.jpg)
4. 单击【设备属性】，可查询设备上报到开发平台的最新数据及历史数据。
 - 设备属性的最新值：会显示设备上报的最新数据。
 - 设备属性的更新时间：显示数据的更新时间。
5. 单击【查看】，可查看某个属性的历史上报数据。

## 查看设备通信日志

单击【设备日志】，可查询该设备某段时间范围的所有上下行数据。
 - 上行：上行指设备端上报到开发平台的数据。
 - 下行：下行指从开发平台下发到设备的数据。

## 在线调试

1. 当 LoRa 节点 成功连接到物联网开发平台后，您可在控制台【设备调试】列表，单击【调试】，进入在线调试。
2. 将“上报周期”设置为15秒，单击【发送】。
3. 查看 LoRa 节点的串口日志，可查看已成功接收到下发的数据。
<dx-alert infotype="explain" title="">
 - 由于本示例中 LoRa 节点是 LoRaWAN Class A 类设备，这类设备不会立即下发数据，需要在有数据上行后，服务器才会向该设备下行数据。
 - 因此在 LoRa 节点上报数据之后，才能查看下发的周期调整命令。
 </dx-alert>
LoRa 节点的串口会显示如下日志，表示成功下发了指令到设备端。
```
rhf76_incoming_data_process 4: 0F00
len: 2
data[0]: 15
data[1]: 0
report_period: 15

```
