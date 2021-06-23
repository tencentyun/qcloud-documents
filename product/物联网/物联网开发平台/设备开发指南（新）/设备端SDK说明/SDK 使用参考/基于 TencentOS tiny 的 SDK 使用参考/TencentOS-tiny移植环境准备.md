


本文为您介绍 TencentOS tiny 接入腾讯物联网开发平台相关的准备工作。 
 ##   步骤1：准备目标硬件（开发板/芯片/模组）

TencentOS tiny 目前主要支持 ARM Cortex M 核芯片的移植，例如 STM32、NXP 芯片支持 Cortex M 核全系列。本教程将使用 TencentOS tiny 官方开发板 EVB_MX_Plus 演示如何移植，其他 ARM Cortex M 系列开发板和芯片移植方法类似。

调试 ARM Cortex M 核还需要仿真器， 由于 EVB_MX_Plus 开发板没有板载 ST-Link 调试器，需要连接外置的仿真器，例如 J-Link、U-Link 等，本教程中使用 ST-Link。


##    步骤2：准备编译器环境

TencentOS tiny 支持 Keil MDK、IAR、Gcc 三种开发环境，本文以 Keil MDK 作为开发环境。
1. 移植内核前需要先安装能编译 ARM Cortex M 核的 Keil 编译器（Keil 编译器别名也称为 MDK），可下载 [最新版本5.31](https://www.keil.com/demo/eval/arm.htm) 进行使用。
>?填写注册信息即可下载，下载完成在 Windows 环境下按照提示安装即可，安装完成后需要自行购买软件 License，避免 32K Flash 下载限制。
>
2. 由于新版本的 MDK 编译器和芯片支持包分离，所以 MDK 安装完成后，还需要安装对应芯片的器件支持包（PACK 包）。例如本教程示例 EVB_MX_Plus 开发板的芯片是 STM32L431RCT6，则需要安装 [Keil.STM32L0xx_DFP.2.0.1.pack](https://www.keil.com/dd2/Pack/#/eula-container) 系列器件支持包。
>?您只需根据您的芯片型号，下载对应的 PACK 包即可，同时您也可以在 MDK 集成开发环境中进行在线下载安装。


##   步骤3：准备芯片对应的裸机工程

移植 TencentOS tiny 基础内核需要您提前准备一个芯片对应的裸机工程，裸机工程包含基本的芯片启动文件、基础配置（时钟、主频等）、以及串口和基本 GPIO 驱动，用于进行 RTOS 测试。

本教程使用 ST 官方的 [STM32CubeMX](https://www.st.com/content/st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.html) 软件进行自动化生成 MDK 裸机工程，同时，安装 STM32CubeMx 需确保已安装好 JDK 环境。CubeMX 安装完成后，使用 CubeMX 在 EVB_MX_Plus 开发板上生成裸机工程。
>?如果您的芯片不是 STM32，而是其他厂商的 ARM Cortex M 系列，您可以根据厂商的指导准备裸机工程，但后续内核移植步骤一致。

###  3.1 启动 STM32CubeMX，新建工程
1. 创建新工程。
2. 打开 MCU 选择器。
![](https://main.qcloudimg.com/raw/9739b80a16ea3d755e2fb271f9e5c71a.png)

### 3.2 选择 MCU 型号
1. 在页面中输入对应 MCU 型号进行搜索筛选。
2. 选中对应型号的 MCU。
![](https://main.qcloudimg.com/raw/6b1bba4f57b220eeba20ead74e6e934f.png)    

如上图所示：通过 MCU 筛选来找到自己开发板对应的芯片型号，双击后弹出工程配置界面，如下所示：
 1. Pinout&Configuration 为引脚配置选项卡。
 2. clock Configuration 为时钟配置选项卡。
 3. Project Manager 为工程配置选项卡。
 4. 左侧菜单为外设配置分类选择。
![](https://main.qcloudimg.com/raw/96e208cf8d634188fe3f14dce5fe994c.png)

### 3.3 Pin 设置界面配置时钟源     
1. 选择 RCC 时钟配置选项。
2. 配置高速时钟 HSE 使用外部晶振。
![](https://main.qcloudimg.com/raw/a58257a919c4051a9d4fec09ea7b455f.png)

### 3.4 Pin 设置界面配置串口

EVB_MX_Plus 开发板用于日志打印 USART2 串口，根据以下步骤配置 USART2 ：
1. 选择 USART2 串口。
2. 设置串口工作模式为“异步模式”。
3. 设置串口波特率为 115200 Bits/s。
4. 选择CubeMX 软件自动配置的串口引脚。
![](https://main.qcloudimg.com/raw/6488733309d59beb88e76c0858753480.png)

EVB_MX_Plus 开发板用于与通信模组通信的 LPUART1 串口，配置 LPUART1 如下图：
1. 选择 LPUART1 串口进行配置。
2. 设置串口工作模式为“异步模式”。
3. 设置 LPUART1 串口基本参数
![](https://main.qcloudimg.com/raw/6ab0fd665a4d70416a456db11c02d9c0.png)

配置使能串口中断：
1. 使能 USART2 串口接收中断。
2. 使能 LPUART1 串口接收中断。
![](https://main.qcloudimg.com/raw/f7efeddfb6c9e4471eadc9dca0790a93.png)

### 3.5 Pin 设置界面配置 GPIO

EVB_MX_Plus 开发板板载一颗 LED，连接在 PC13 引脚，操作如下：
1. 设置 PC13 为 GPIO Output 模式。
2. 进入 GPIO 配置界面。
3. 设置引脚别名为“LED”。
![](https://main.qcloudimg.com/raw/0ba223ff424fe2f1fc5d55fbb29e7ce6.png)

EVB_MX_Plus 开发板板载四个按键，其中 KEY1 连接在 PB12，操作如下：
1. 设置 PB12 引脚为 GPIO Input 模式。
2. 进入 GPIO 配置界面。
3. 设置引脚别名为“KEY1”。
![](https://main.qcloudimg.com/raw/1f7bb6afc54e3fbebbaaa9c7ef2e5d18.png)
     

### 3.6 配置总线时钟
1. 选择系统时钟源为外部高速时钟 HSE。
2. 设置系统主频 HCLK 为最高主频 80Mhz。
![](https://main.qcloudimg.com/raw/661e3f702d16763c4cbed19e95e57e87.png)
     
### 3.7 工程生成参数配置
1. 进入工程配置页面。
2. 设置工程名称。
3. 选择工程存储位置。
4. 设置工程的 IDE 类型，TencentOS-tiny 支持 MDK、IAR、Gcc等，这里选择 MDK-V5。
![](https://main.qcloudimg.com/raw/df1718d50745866e419d5f8a7cf13d11.png)

### 3.8 代码生成方式配置
1. 选择代码生成配置选项。
2. 选择拷贝所有库文件。
3. 设置配置的芯片外设生成单独的初始化文件。
![](https://main.qcloudimg.com/raw/610243c5fc3fab6728a7b9ada0a5edb5.png)
     

### 3.9 生成工程
1. 单击生成代码按钮生成裸机工程。
2. 生成工程后，在弹出提示框中选择直接打开工程所在目录。
![](https://main.qcloudimg.com/raw/abdc43ec62b694cfe156a325e5689f87.png)

### 3.10  Keil 的裸机工程

打开生成的裸机工程效果如下：

![](https://main.qcloudimg.com/raw/77bddafe88d32f90e3eebe93d1c4c15f.png)
     
编译工程下载之后，EVB_MX_Plus 开发板的裸机工程生成完成，该工程可直接编译并烧写在开发板上运行。
     

##    步骤4：准备 TencentOS tiny 的源码

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

##  步骤5：下一步操作
请前往 [内核移植](https://cloud.tencent.com/document/product/1081/47956) 进行内核移植操作。
