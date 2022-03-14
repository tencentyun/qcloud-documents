
本文为您介绍 TencentOS tiny 接入腾讯物联网开发平台相关的准备工作。 
 ##   步骤一：准备目标硬件（开发板/芯片/模组）

TencentOS tiny 目前主要支持 ARM Cortex M 核芯片的移植，例如 STM32、NXP 芯片支持 Cortex M 核全系列。本教程将使用 TencentOS tiny 官方开发板 EVB_MX_Plus 演示如何移植，其他 ARM Cortex M 系列开发板和芯片移植方法类似。

调试 ARM Cortex M 核还需要仿真器， 由于 EVB_MX_Plus 开发板没有板载 ST-Link 调试器，需要连接外置的仿真器，例如 J-Link、U-Link 等，本教程中使用 ST-Link。


##    步骤二：准备编译器环境

TencentOS tiny 支持 Keil MDK、IAR、Gcc 三种开发环境，本文中以 Keil MDK 作为开发环境。
1. 移植内核前需要先安装能编译 ARM Cortex M 核的 Keil 编译器（Keil 编译器别名也称为 MDK），可下载 [最新版本5.31](https://www.keil.com/demo/eval/arm.htm) 进行使用。
>?填写注册信息即可下载，下载完成在 Windows 环境下按照提示安装即可，安装完成后需要自行购买软件 License，避免 32K Flash 下载限制。
>
2. 由于新版本的 MDK 编译器和芯片支持包分离，所以 MDK 安装完成后，还需要安装对应芯片的器件支持包（PACK 包）。例如本教程示例的 EVB_MX_Plus 开发板的芯片是 STM32L431RCT6，则需要安装 [Keil.STM32L0xx_DFP.2.0.1.pack](https://www.keil.com/dd2/Pack/#/eula-container) 系列器件支持包。
>?您只需根据您的芯片型号，下载对应的 PACK 包即可，同时您也可以在 MDK 集成开发环境中进行在线下载安装。


##   步骤三：准备芯片对应的裸机工程

移植 TencentOS tiny 基础内核需要您提前准备一个芯片对应的裸机工程，裸机工程包含基本的芯片启动文件、基础配置（时钟、主频等）、以及串口和基本 GPIO 驱动，用于进行 RTOS 测试。

本教程使用 ST 官方的 [STM32CubeMX](https://www.st.com/content/st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.html) 软件进行自动化生成 MDK 裸机工程，同时，安装 STM32CubeMx 需确保已安装好 JDK 环境。CubeMX 安装完成后，使用 CubeMX 在 EVB_MX_Plus 开发板上生成裸机工程。
>?如果您的芯片不是 STM32，而是其他厂商的 ARM Cortex M 系列，您可以根据产商的指导准备裸机工程，但后续内核移植步骤一致。

###  1. 启动 STM32CubeMX，新建工程

![](https://main.qcloudimg.com/raw/57ccf4d9c61a7c7a8e9373836de7e076.png)

### 2. 选择 MCU 型号

![](https://main.qcloudimg.com/raw/05631464719c1149cd11d351a1042963.png)
     
如上图所示：通过 MCU 筛选来找到自己开发板对应的芯片型号，双击后弹出工程配置界面，如下图：
     
![](https://main.qcloudimg.com/raw/e0ad1cc08bb2dd8d82d69bd836620e99.png)

### 3. Pin 设置界面配置时钟源     

![](https://main.qcloudimg.com/raw/6b0b7cbf4c2ace45dcbe4d67e177eb51.png)

### 4. Pin 设置界面配置串口

EVB_MX_Plus 开发板用于日志打印 USART2 串口，配置 USART2 如下图：

![](https://main.qcloudimg.com/raw/048ca146332a163eb07c1a679791980c.png)

EVB_MX_Plus 开发板用于与通信模组通信的 LPUART1 串口，配置 LPUART1 如下图：

![](https://main.qcloudimg.com/raw/ef8ab610d9dabd3de22a2028d80936fa.png)

配置使能串口中断，如下图：

![](https://main.qcloudimg.com/raw/df71d5efb0b077733464c63dd9a3993f.png)

### 5. Pin 设置界面配置 GPIO

EVB_MX_Plus 开发板板载一颗 LED，连接在 PC13 引脚，相关配置如下图：

![](https://main.qcloudimg.com/raw/304e452cf97aca619e99bd27ee9c9089.png)

EVB_MX_Plus 开发板板载四个按键，其中 KEY1 连接在 PB12，相关配置如下图：

![](https://main.qcloudimg.com/raw/40cc206d1d20f487ee7c855475930165.png)
     

### 6. 配置总线时钟

![](https://main.qcloudimg.com/raw/6bfec9b3f426c2bee062be13187d65c9.png)
     
### 7. 工程生成参数配置

![](https://main.qcloudimg.com/raw/0ada3908c0d0359d9b1a6eaefb1927ab.png)
     

### 8. 代码生成方式配置

![](https://main.qcloudimg.com/raw/3c1e152aeb0f68910f8a12cfcb3b68fb.png)
     

### 9. 生成工程

![](https://main.qcloudimg.com/raw/a4bf1b6f838aedd6d0e98f5ea20b09db.png)

### 10.  keil 的裸机工程

打开生成的裸机工程效果如下：

![](https://main.qcloudimg.com/raw/77bddafe88d32f90e3eebe93d1c4c15f.png)
     
编译工程下载之后，EVB_MX_Plus 开发板的裸机工程生成完成，该工程可直接编译并烧写在开发板上运行。
     

##    步骤四：准备 TencentOS tiny 的源码

TencentOS tiny 的源码已经开源，可从[ GitHub](https://github.com/Tencent/TencentOS-tiny) 文件库中下载使用。
>?由于下一步骤只介绍 TencentOS tiny 的内核移植，所以这里只需要用到 arch、board、kernel、osal 四个目录下的源码。
>
<table>
<thead>
<tr>
<th>一级目录</th>
<th>二级目录</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>arch</td>
<td>arm</td>
<td>TencentOS tiny 适配的 IP 核架构（含 M 核中断、调度、tick 相关代码）</td>
</tr>
<tr>
<td>board</td>
<td>...</td>
<td>移植目标芯片的工程文件</td>
</tr>
<tr>
<td rowspan=2>kernel</td>
<td>core</td>
<td>TencentOS tiny 内核源码</td>
</tr>
<tr>
<td>pm</td>
<td>TencentOS tiny 低功耗模块源码</td>
</tr>
<tr>
<td>osal</td>
<td>cmsis_os</td>
<td>TencentOS tiny 提供的 cmsis os 适配</td>
</tr>
<tr>
<td rowspan=5>net</td>
<td>at</td>
<td>AT 框架源码</td>
</tr>
<tr>
<td>sal_module_wrapper</td>
<td>SAL 框架源码</td>
</tr>
<tr>
<td>socket_wrapper</td>
<td>socket 封装封装层源码</td>
</tr>
<tr>
<td>tencent_firmware_module_wrapper</td>
<td>腾讯云定制固件封装层源码</td>
</tr>
<tr>
<td>lora_module_wrapper</td>
<td>lora 封装层源码</td>
</tr>
<tr>
<td>devices</td>
<td>...</td>
<td>各种通信模组的驱动适配层</td>
</tr>
</tbody></table>

##  步骤五：下一步操作
请前往 [内核移植](https://cloud.tencent.com/document/product/1081/47956) 进行内核移植操作。
