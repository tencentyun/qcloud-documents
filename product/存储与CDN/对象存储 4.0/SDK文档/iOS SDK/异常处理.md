

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。
返回错误码（封装在返回的 error 里）主要包括三类：设备本身因为网络原因等返回的错误码，SDK 网络层本地客户端自定义错误、以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 Foundation 框架中的 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于 COS 返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档寻求解决方案。
- 对于腾讯云 SDK 网络层本地客户端自定义错误：主要是指网络异常、证书无效、参数校验失败等，如下表所示：

|错误码|错误信息|错误描述|
| ---- | ---- | ---- |
|10000| InvalidArgument| 参数错误|
|10001| InvalidCredentials|  证书无效|
|10004| UnsupportOperation| 无法支持的操作|
|20001| InvalidArgument| 服务器返回了不合法的数据|
|20004| PoorNetwork| 数据完整性校验失败|
|30000|  UserCancelled| 用户取消|
|30002| AlreadyFinished| 任务已完成|
