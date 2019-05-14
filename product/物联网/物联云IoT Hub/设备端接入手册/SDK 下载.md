## C 语言 SDK
### 代码托管
- 自 v1.0.0 版本开始，设备端 SDK 代码使用 Github 托管
  [https://github.com/tencentyun/qcloud-iot-sdk-embedded-c](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c)
- 下载最新版 
  [https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases)
	

### v2.3.1

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
- 开发环境：Linux, GNU Make
- 内容：
 1、增加网关功能，支持网关设备基于 MQTT 协议代理子设备上下线及收发消息。
 2、针对多线程应用，优化线程安全设计，在 samples 中增加多线程例程及注意事项说明。
 3、优化 MQTT 重连机制及心跳包定时器刷新策略。
 4、若干  bug 的修复，部分内存操作增加合法性检查。
 5、去除若干结构体采用位域操作方式，减少跨平台错误。


	
	
  
### 版本 v2.2.0  
- 发布日期：2018/07/20
- 开发语言：C 语言
- 开发环境：Linux, GNU Make
- 内容：
	1、新增 NBIoT 设备接入能力。
	2、适配 TOPIC 的通配符 “#” 和 “+”。
	3、整理第三方库的目录结构。
	4、若干 bug 的修复。
  
	
### 版本 v2.1.0
- 发布日期：2018/05/02
- 开发语言：C 语言
- 开发环境：Linux, GNU Make
- 内容：
	1、新增固件升级（OTA-CoAP 通道）能力。
	2、新增低端资源受限设备 hmac-sha1 鉴权接入能力。
	3、新增获取后台时间的能力。


### 版本 v2.0.0
- 发布日期：2018/03/12
- 开发语言：C 语言
- 开发环境：Linux, GNU Make
- 内容：
	1、新增固件升级（OTA-MQTT 通道）能力。
	2、修复设备影子心跳间隔失效的问题。
	3、修复 MQTT 接收的数据长度在临界值时导致缓冲区溢出的问题。
  
### 版本 v1.2.2
- 发布日期：2018/02/07
- 开发语言：C 语言
- 开发环境：Linux, GNU Make
- 内容：
	1、新增 MQTT/CoAP 对称加密连接支持。
	2、Linux c 编译优化。

### 版本 v1.2.1
- 发布日期：2018/02/02
- 开发语言：C 语言
- 开发环境：Linux, GNU Make
- 内容：修复 Publish 消息超时回调的错误逻辑。


### 版本 v1.2.0
- 发布日期：2018/1/17
- 开发语言：C 语言
- 开发环境：Linux, GNU Make
- 内容：
  1、改造发布/订阅消息的 ACK 通过回调接收，不会阻塞发送线程。
  2、增加终端与后台关于连接、日志对应的能力。
  3、新增 CoAP 通道，基于 UDP，采用 DTLS 非对称加密，在纯上报数据场景耗能更少。

### 版本 v1.0.0
- 发布日期：2017/11/15
- 开发语言：C 语言
- 开发环境：Linux, GNU Make
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
