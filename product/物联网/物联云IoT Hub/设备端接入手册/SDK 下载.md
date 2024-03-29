

## C 语言 SDK

### 代码托管
- 自 v1.0.0 版本开始，设备端 SDK 代码使用 Github 托管
  [https://github.com/tencentyun/qcloud-iot-sdk-embedded-c](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c)
- 下载最新版 
  [https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases)
	
### 版本 v3.2.1

- 发布日期：2020/08/04
- 开发语言：C语言
- 开发环境：Linux/Windows
- 内容：
  1、新增 rrpc 同步通信功能及示例。
  2、新增广播功能及示例。
  3、网关增加绑定/解绑子设备接口。
  4、更新文档。

### 版本 v3.2.0

- 发布日期：2020/04/30
- 开发语言：C语言
- 开发环境：Linux/Windows
- 内容：
  1、合并 mtmc 分支代码，支持多设备连接，优化多线程接口。
  2、修复一些潜在的内存泄漏及越界问题，以及跨平台编译运行问题。
  3、使用 clang-format 格式化代码，引入代码检查工具 clang-tidy 及 cpplint。

### 版本 v3.1.3

- 发布日期：2020/03/06
- 开发语言：C语言
- 开发环境：Linux/Windows
- 内容：
  1、优化 ota_mqtt_sample，将 OTA 流程以及需要文件操作的地方解耦分离，并且 sample 支持 MQTT 断开重连之后仍然可以恢复下载。
  2、优化 gateway_sample，并增加代理一个以上子设备示例代码。
  3、增加查询 MQTT 主题是否订阅成功的接口。
  4、优化及更新文档。
  5、修复一些编译警告及 bug。
  6、统一代码缩进风格。

### 版本 v3.1.2

- 发布日期：2019/11/11
- 开发语言：C语言
- 开发环境：Linux/Windows
- 内容：
  1、移除对 IoT Explorer 平台相关代码及文档，仅支持 IoT Hub。优化文档描述。
  2、Bug 修复：OTA 模块内存泄漏问题，device_info.json 文件解析问题及 Windows 平台时间格式问题。
  3、避免文件名冲突，ca.c/h 重命名为 qcloud_iot_ca.c/h，device.c/h 重命名为 qcloud_iot_device.c/h。

### 版本 v3.1.0

- 发布日期：2019/09/19
- 开发语言：C语言
- 开发环境：Linux/Windows
- 内容：
  C-SDK 重构：
  1、优化代码架构及目录层级，采用英文注释，完善文档说明，提高可用性和可移植性。
  2、在原 makefile 编译基础上增加 cmake 编译方式和代码抽取方式，适应多种编译环境。
  3、增加 Windows 平台支持，支持在 Microsoft Visual Studio 下开发。
  4、增加 AT_socket 网络层以支持 MCU+TCP AT 模组设备的开发移植。
  5、增加 FreeRTOS+lwIP 平台的移植适配。

### 版本 v3.0.3

- 发布日期：2019/08/26
- 开发语言：C语言
- 开发环境：Linux，GNU Make
- 内容：
  1、支持 OTA 断点续传：ota_mqtt_sample.c 示例增加本地固件版本信息管理（版本、断点、MD5），固件下载建立 HTTPS 连接时支持 range 参数。
  2、SDK 版本号更新为 v3.0.3。

### 版本 v3.0.2

- 发布日期：2019/07/18
- 开发语言：C语言
- 开发环境：Linux，GNU Make
- 内容：
  1、数据模板字符串类型支持转义字符处理。
  2、设备影子去除设备侧 version 管理。
  3、优化数据模板相关示例。

### 版本 v3.0.1

- 发布日期：2019/06/11
- 开发语言：C语言
- 开发环境：Linux，GNU Make
- 内容：
  1、日志上报功能优化，动态分配缓冲区内存，支持较大日志分段上报，适合多种使用场景。
  2、MQTT 增加 subscribe 的 event handler 回调，及时通知订阅 topic 的状态变化。
  3、修复一些代码问题，例如对 MQTT API 的返回值判断不当问题。

### 版本 v3.0.0

- 发布日期：2019/05/17
- 开发语言：C语言
- 开发环境：Linux，GNU Make
- 内容
  1、基于影子增加数据模板功能。
  2、增加事件上报功能。
  3、增加数据模板代码生成脚本工具。
  4、修复 JSON 处理的若干 bug。
  5、新增数据模板示例、事件示例、数据模板智能灯场景示例。
  6、调整文档结构，增加文档目录 docs 及平台 SDK 应用说明。
  7、版本 v3.0.0 及以后版本同时支持物联网通信及物联网开发两个物联网平台。

### 版本 v2.3.5

- 发布日期：2019/05/15
- 开发语言：C语言
- 开发环境：Linux，GNU Make
- 内容:
  1、增加设备动态注册功能。
  2、增加设备动态注册示例。
  3、增加设备信息读写 HAL 接口。
  4、增加 AES 加解密 API。
  5、修改各 Sample 设备信息获取方式为 HAL 层接口实现。

### 版本 v2.3.3

- 发布日期：2019/05/06
- 开发语言：C语言
- 开发环境：Linux，GNU Make
- 内容:
  1、优化 MQTT keep alive 连接机制及 PING request 发包策略。
  2、修改 MQTT 订阅/取消订阅的 topic name 使用动态内存方式存储，方便接口调用者使用。
  3、修改 topic name 最大长度为128，与云端后台保持一致。
  4、修复 HTTPC 以及 MQTT 获取 sys 及 log 消息的 bug。
  5、优化错误码类型。

### 版本 v2.3.2

- 发布日期：2019/04/12
- 开发语言：C语言
- 开发环境：Linux，GNU Make
- 内容：
  1、修复体验问题：在 make.settings 里增加网关编译选项（默认关闭）以及修改固件升级打印级别。
  2、修复 MQTT 接收缓冲区在影子消息下行时容易丢失问题：增加接收缓冲区不足时的错误提示，更改 MQTT 发送及接收缓冲区默认大小为2048字节。
  3、修改成功订阅主题的最大个数为10条。

### 版本 v2.3.1

- 发布日期：2019/03/12
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
1、SDK 增加设备端日志上报功能，方便用户通过云端控制台远程监控及诊断设备联网状况。目前仅支持 MQTT 模式。
2、精简 SDK 日志打印内容，修复若干 Bug，优化部分代码设计。
3、修改设备名称最大长度为48位，与 IoT Hub 云端控制台保持一致。





### 版本 v2.3.0

- 发布日期：2019/02/25
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
 1、增加网关功能，支持网关设备基于 MQTT 协议代理子设备上下线及收发消息。
 2、针对多线程应用，优化线程安全设计，在 samples 中增加多线程例程及注意事项说明。
 3、优化 MQTT 重连机制及心跳包定时器刷新策略。
 4、若干 Bug 的修复，部分内存操作增加合法性检查。
 5、去除若干结构体采用位域操作方式，减少跨平台错误。


​	
​	

### 版本 v2.2.0  
- 发布日期：2018/07/20
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
	1、新增 NBIoT 设备接入能力。
	2、适配 TOPIC 的通配符 “#” 和 “+”。
	3、整理第三方库的目录结构。
	4、若干 bug 的修复。
  
	
### 版本 v2.1.0
- 发布日期：2018/05/02
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
	1、新增固件升级（OTA-CoAP 通道）能力。
	2、新增低端资源受限设备 hmac-sha1 鉴权接入能力。
	3、新增获取后台时间的能力。


### 版本 v2.0.0
- 发布日期：2018/03/12
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
	1、新增固件升级（OTA-MQTT 通道）能力。
	2、修复设备影子心跳间隔失效的问题。
	3、修复 MQTT 接收的数据长度在临界值时导致缓冲区溢出的问题。
  
### 版本 v1.2.2
- 发布日期：2018/02/07
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
	1、新增 MQTT/CoAP 对称加密连接支持。
	2、Linux c 编译优化。

### 版本 v1.2.1
- 发布日期：2018/02/02
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：修复 Publish 消息超时回调的错误逻辑。


### 版本 v1.2.0
- 发布日期：2018/1/17
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
  1、改造发布/订阅消息的 ACK 通过回调接收，不会阻塞发送线程。
  2、增加终端与后台关于连接、日志对应的能力。
  3、新增 CoAP 通道，基于 UDP，采用 DTLS 非对称加密，在纯上报数据场景耗能更少。

### 版本 v1.0.0
- 发布日期：2017/11/15
- 开发语言：C 语言
- 开发环境：Linux，GNU Make
- 内容：
  1、MQTT 协议支持：支持设备快捷轻便的链接 IoT Hub 云端服务器，可查看 [MQTT 协议详解](https://github.com/mcxiaoke/mqtt)。
  2、设备影子功能支持：具体可查看 [设备影子详情](https://cloud.tencent.com/document/product/634/11918)。
  3、提供对称和非对称两种加密方式支持。

## Android SDK

### 代码托管
- 自 v1.0.0 版本开始，Android 设备端 SDK 代码使用 Github 托管。
  [https://github.com/tencentyun/qcloud-iot-sdk-android](https://github.com/tencentyun/qcloud-iot-sdk-android)
  
### 版本v2.0.0
- 发布日期：2018/03/12
- 内容：新增固件升级（OTA-MQTT 通道）能力。
	

### 版本v1.2.0
- 发布日期：2018/1/17
- 内容：
  1、MQTT 协议支持：支持设备快捷轻便的链接 IoT Hub 云端服务器，可查看 [MQTT 协议详解](https://github.com/mcxiaoke/mqtt)。
  2、设备影子功能支持：具体可查看 [设备影子详情](https://cloud.tencent.com/document/product/634/11918)。
  3、MQTT 和设备影子均提供跨进程调用 API。
  4、提供非对称加密方式支持。
