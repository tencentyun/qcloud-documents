## 简介

为了能让您更高效地使用日志服务（Cloud Log Service，CLS），日志服务专门为日志上传量身打造了多个语言版本的 SDK（Software Development Kit），您可以根据业务需求选择语言版本使用。

## 使用前须知

1. SDK 对日志服务的数据接入接口做了统一封装，降低了使用上传日志的难度，您可以使用对应语言的 SDK 进行日志上传。
2. 实现日志服务日志的 ProtoBuffer 格式封装，让您在写入日志时不需要关心 ProtoBuffer 格式的具体细节。
3. 实现日志服务 API 中定义的压缩方法，让您不用关心压缩实现的细节。部分语言的 SDK 支持启用压缩模式写入日志（默认为使用压缩方式）。
4. 提供统一的异步发送、资源控制、自动重试、优雅关闭、感知上报等功能，使上报日志功能更完善。


## SDK 列表

下表列举了日志服务不同语言 SDK GitHub 源码：


| SDK 语言 | GitHub 源码 |
|---------|---------|
| Java | [tencentcloud-cls-sdk-java](https://github.com/TencentCloud/tencentcloud-cls-sdk-java)  |
| Go | [tencentcloud-cls-sdk-go](https://github.com/TencentCloud/tencentcloud-cls-sdk-go)  |
| Node.js | [tencentcloud-cls-sdk-js](https://github.com/TencentCloud/tencentcloud-cls-sdk-js)   |
| Android | [tencentcloud-cls-sdk-android](https://github.com/TencentCloud/tencentcloud-cls-sdk-android) |

