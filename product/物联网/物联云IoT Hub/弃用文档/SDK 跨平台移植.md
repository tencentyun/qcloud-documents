
本文档介绍如何将设备端 C-SDK 移植到目标硬件平台。

SDK 根据代码结构可以大致分成四部分：
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/SDK代码结构v1.2.jpg)

1、硬件平台抽象层（HAL 层）
这里是抽象不同嵌入式设备操作系统对我们 SDK 的支撑函数，比方说网络功能，内存申请以及 TLS/DTLS 通道的建立。

>!
 - 在任何跨平台移植时, 实现这部分是需要完成的第一步工作。
 - 在进行移植操作时候，请首先实现 HAL 层。C-SDK 中提供的 HAL 层是基于 Linux 桌面 OS（Ubuntu14.04）上的参考实现。
		
2、SDK 内核实现层
这里是 C-SDK 的核心实现部分, 它基于 HAL 层接口完成了 MQTT 通道等的功能封装。

>!只要把 HAL 层实现好，那么除了进行 Debug，一般情况下无需关注这层代码的具体实现。
	
 
3、SDK 接口声明层
 - 这里包括了一系列 C 函数的原型声明, 用于编写业务逻辑，实现和腾讯云通信的 API。
 - 	sample 里面提供了 demo 代码，可以借此参考如何使用这些 API。

4、SDK Sample Program（例程）
 这部分提供了场景化 demo 的实现代码，以供参考。
 
下面对各层次进行更加详细的说明。

### 硬件平台抽象层（HAL 层）

所有 HAL 层函数都在 `src/sdk-impl/qcloud_iot_import.h` 中进行声明，以下是需要实现的 HAL 层接口，详细信息可以参考注释。
<!--2. `src/sdk-impl/qcloud_iot_import.h` 包含了 `imports ` 目录下的子文件,
--><!--`3. 各功能点引入的 HAL 层接口依赖在 `src/sdk-impl/imports/qcloud_iot_import_*.h` 中列出`-->

**必须实现：**

| 序号 | 函数名                 | 说明                                     |
| ---- | ---------------------- | ---------------------------------------- |
| 1    | HAL_Free               | 释放内存块                               |
| 2    | HAL_Malloc             | 分配一块的内存，返回一个指向块开始的指针 |
| 3    | HAL_Printf             | 将格式化的数据写入标准输出流中           |
| 4    | HAL_Snprintf           | 将格式化的数据写入字符串                 |
| 5    | HAL_UptimeMs           | 检索自系统启动以来已运行的毫秒数         |
| 6    | HAL_SleepMs            | 休眠                                     |
| 7    | HAL_Timer_init         | 初始化定时器结构体                       |
| 8    | HAL_Timer_remain       | 检查给定定时器还剩余时间                 |
| 9    | HAL_Timer_expired      | 判断定时器时间是否已经过期               |
| 10   | HAL_Timer_countdown    | 根据定时器开始计时, 单位：s               |
| 11   | HAL_Timer_countdown_ms | 根据定时器开始计时, 单位：ms              |
| 12   | HAL_Timer_current | 获取当前时间格式化字符串              |
| 13    | HAL_TLS_Connect    | 为 MQTT 客户端建立 TLS 连接 |
| 14    | HAL_TLS_Disconnect | 断开 TLS 连接             |
| 15    | HAL_TLS_Write      | 从一个 TLS 连接中写数据   |
| 16    | HAL_TLS_Read       | 从一个 TLS 连接中读数据   |
| 17    | HAL_MutexCreate    | 创建 mutex |
| 18    | HAL_MutexDestroy | 销毁 mutex            |
| 19    | HAL_MutexLock      | mutex 加锁   |
| 20    | HAL_MutexUnlock       | mutex 解锁   |

**仅在使用 CoAP 必须实现：**

| 序号 | 函数名                 | 说明                                     |
| ---- | ---------------------- | ---------------------------------------- |
| 1    | HAL_DTLS_Connect    | 为 CoAP 客户端建立 DTLS 连接，仅在需要使用 CoAP 时实现 |
| 2    | HAL_DTLS_Disconnect | 断开 DTLS 连接             |
| 3    | HAL_DTLS_Write      | 从一个 DTLS 连接中写数据   |
| 4    | HAL_DTLS_Read       | 从一个 DTLS 连接中读数据   |


### SDK 内核实现层
1、所有被提供的函数的声明都在 `src/sdk-impl/qcloud_iot_export.h` 这个头文件中列出。
2、这些 exports 目录下的子文件, 都被 `src/sdk-impl/qcloud_iot_export.h` 包含。
3、`src/sdk-impl/exports/qcloud_iot_export_*.h` 中列出各功能点提供的 API。


### SDK 接口声明层+例程
1、接口说明：[SDK 接口文档](https://cloud.tencent.com/document/product/634/38255)
2、例程介绍：[快速开始](https://cloud.tencent.com/document/product/634/11912)
