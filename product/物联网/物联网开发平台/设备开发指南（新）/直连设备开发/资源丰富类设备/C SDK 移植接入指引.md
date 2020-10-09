
本文为您介绍如何将设备端 C SDK 移植到目标硬件平台。C SDK 采用模块化设计，分离核心协议服务与硬件抽象层，在进行跨平台移植时，一般只需对硬件抽象层进行修改适配即可。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [C SDK](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c/releases)。

## 接入指引

非典型平台接入腾讯云物联网开发平台可以分为以下2个步骤。

### 硬件抽象层移植

HAL 层主要有几大块的移植，分别是 OS 相关、网络及 TLS 相关、时间及打印相关、设备信息相关。
SDK 在 [platform/os](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/tree/master/platform/os) 目录下示例了 Linux、Windows、FreeRTOS 及 nonOS 四个场景的硬件抽象层实现，详情可参考 [直连设备接入类型说明](https://cloud.tencent.com/document/product/1081/48383#.E8.B5.84.E6.BA.90.E4.B8.B0.E5.AF.8C.E7.B1.BB.E8.AE.BE.E5.A4.87) 对应平台的接入指引。

- #### OS 相关接口
<table>
<thead>
<tr>
<th>序号</th>
<th>函数名</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>HAL_Malloc</td>
<td>动态申请内存块</td>
</tr>
<tr>
<td>2</td>
<td>HAL_Free</td>
<td>释放内存块</td>
</tr>
<tr>
<td>3</td>
<td>HAL_ThreadCreate</td>
<td>线程创建</td>
</tr>
<tr>
<td>4</td>
<td>HAL_ThreadDestroy</td>
<td>线程销毁</td>
</tr>
<tr>
<td>5</td>
<td>HAL_MutexCreate</td>
<td>创建互斥锁</td>
</tr>
<tr>
<td>6</td>
<td>HAL_MutexDestroy</td>
<td>销毁互斥锁</td>
</tr>
<tr>
<td>7</td>
<td>HAL_MutexLock</td>
<td>mutex 加锁</td>
</tr>
<tr>
<td>8</td>
<td>HAL_MutexUnlock</td>
<td>mutex 解锁</td>
</tr>
<tr>
<td>9</td>
<td>HAL_SemaphoreCreate</td>
<td>创建信号量</td>
</tr>
<tr>
<td>10</td>
<td>HAL_SemaphoreDestroy</td>
<td>销毁信号量</td>
</tr>
<tr>
<td>11</td>
<td>HAL_SemaphoreWait</td>
<td>等待信号量</td>
</tr>
<tr>
<td>12</td>
<td>HAL_SemaphorePost</td>
<td>释放信号量</td>
</tr>
<tr>
<td>13</td>
<td>HAL_SleepMs</td>
<td>休眠</td>
</tr>
</tbody></table>

- #### 网络及 TLS 相关的 HAL 接口
网络相关接口提供二选一的适配移植。对于具备网络通讯能力并且本身集成 TCP/IP 网络协议栈的设备，需要实现 [POSIX_socket](#POSIX_socket) 的网络 HAL 接口，使用 TLS/SSL 加密通讯的还需要实现 TLS 相关的 HAL 接口；而对于 **MCU+ 通用 TCP_AT 模组** 的设备，则可以选择 SDK 提供的 [AT_Socket](#AT_socket) 框架，并实现相关的 AT 模组接口。
<span id="POSIX_socket"></span>
 - 基于 POSIX_socket 的 HAL 接口
 其中 TCP/UDP 相关接口基于 POSIX socket 函数实现。TLS 相关接口依赖于 **mbedtls** 库，移植之前必须确保系统上有可用的 **mbedtls** 库。如果采用其他 TLS/SSL 库，可参考 [platform/tls/mbedtls](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/tree/master/platform/tls/mbedtls) 相关实现进行移植适配。其中，UDP/DTLS 相关的函数仅在使能 **CoAP** 通讯的时候才需要移植。
<table>
<thead>
<tr>
<th>序号</th>
<th>函数名</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>HAL_TCP_Connect</td>
<td>建立 TCP 连接</td>
</tr>
<tr>
<td>2</td>
<td>HAL_TCP_Disconnect</td>
<td>断开 TCP 连接</td>
</tr>
<tr>
<td>3</td>
<td>HAL_TCP_Write</td>
<td>TCP 写</td>
</tr>
<tr>
<td>4</td>
<td>HAL_TCP_Read</td>
<td>TCP 读</td>
</tr>
<tr>
<td>5</td>
<td>HAL_TLS_Connect</td>
<td>建立 TLS 连接</td>
</tr>
<tr>
<td>6</td>
<td>HAL_TLS_Disconnect</td>
<td>断开 TLS 连接</td>
</tr>
<tr>
<td>7</td>
<td>HAL_TLS_Write</td>
<td>TLS 写</td>
</tr>
<tr>
<td>8</td>
<td>HAL_TLS_Read</td>
<td>TLS 读</td>
</tr>
<tr>
<td>9</td>
<td>HAL_UDP_Connect</td>
<td>建立 TCP 连接</td>
</tr>
<tr>
<td>10</td>
<td>HAL_UDP_Disconnect</td>
<td>断开 TCP 连接</td>
</tr>
<tr>
<td>11</td>
<td>HAL_UDP_Write</td>
<td>UDP 写</td>
</tr>
<tr>
<td>12</td>
<td>HAL_UDP_Read</td>
<td>UPD 读</td>
</tr>
<tr>
<td>13</td>
<td>HAL_DTLS_Connect</td>
<td>建立 DTLS 连接</td>
</tr>
<tr>
<td>14</td>
<td>HAL_DTLS_Disconnect</td>
<td>断开 DTLS 连接</td>
</tr>
<tr>
<td>15</td>
<td>HAL_DTLS_Write</td>
<td>DTLS 写</td>
</tr>
<tr>
<td>16</td>
<td>HAL_DTLS_Read</td>
<td>DTLS 读</td>
</tr>
</tbody></table>

 <span id="AT_socket"></span>
 
   - 基于 AT_socket 的 HAL 接口
  通过使能编译宏 **AT_TCP_ENABLED** 选择 AT_socket，则 SDK 将会调用 `network_at_tcp.c` 的 `at_socket` 接口， at_socket 层不需要移植，需要实现 AT 串口驱动及 AT 模组驱动，AT 模组驱动只需要实现 AT 框架中 at_device 的驱动结构体 `at_device_op_t` 的驱动接口即可，详情可参考 [at_device](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/tree/master/platform/at_device/esp8266) 目录下的已支持的模组。AT 串口驱动需要实现串口的中断接收，然后在中断服务程序中调用回调函数 `at_client_uart_rx_isr_cb` 即可，可以参考 `HAL_AT_UART_freertos.c` 实现目标平台的移植。
<table>
<thead>
<tr>
<th>序号</th>
<th>函数名</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>HAL_AT_Uart_Init</td>
<td>初始化 AT 串口</td>
</tr>
<tr>
<td>2</td>
<td>HAL_AT_Uart_Deinit</td>
<td>去初始化 AT 串口</td>
</tr>
<tr>
<td>3</td>
<td>HAL_AT_Uart_Send</td>
<td>AT 串口发送数据</td>
</tr>
<tr>
<td>4</td>
<td>HAL_AT_UART_IRQHandler</td>
<td>AT 串口接收中断服务程序</td>
</tr>
</tbody></table>


- #### 时间及打印相关的 HAL 接口
<table>
<thead>
<tr>
<th>序号</th>
<th>函数名</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>HAL_Printf</td>
<td>将格式化的数据写入标准输出流中</td>
</tr>
<tr>
<td>2</td>
<td>HAL_Snprintf</td>
<td>将格式化的数据写入字符串</td>
</tr>
<tr>
<td>3</td>
<td>HAL_UptimeMs</td>
<td>检索自系统启动以来已运行的毫秒数</td>
</tr>
<tr>
<td>4</td>
<td>HAL_DelayMs</td>
<td>阻塞延时，单位毫秒</td>
</tr>
</tbody></table>

- #### 设备信息相关的 HAL 接口
接入 IoT 平台需要在平台创建产品和设备信息，同时需要将产品及设备信息保存在设备侧的非易失存储介质。可以参考  [platform/os/linux/HAL_Device_linux.c](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/blob/master/platform/os/linux/HAL_Device_linux.c) 示例实现。
<table>
<thead>
<tr>
<th>序号</th>
<th>函数名</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>HAL_GetDevInfo</td>
<td>设备信息读取</td>
</tr>
<tr>
<td>2</td>
<td>HAL_SetDevInfo</td>
<td>设备信息保存</td>
</tr>
</tbody></table>

### 应用开发

请参考 [SDK samples](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/tree/master/samples) 目录下的例程进行开发。

## SDK 使用参考

请参考 [C SDK 使用参考](https://cloud.tencent.com/document/product/1081/48377)。
