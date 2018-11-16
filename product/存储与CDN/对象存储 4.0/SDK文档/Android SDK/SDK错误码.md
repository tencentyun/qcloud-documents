#概述

在使用 Android、ios 等 SDK 提供的COS API 服务过程中，出现失败可以归为客户端错误和服务端返回的错误。服务端返回的错误指服务端处理一些不符合要求的客户端请求所返回的错误，如访问不存在的文件，没有访问文件的权限等，更多错误码详细信息，请参阅[错误码](https://cloud.tencent.com/document/product/436/7730)。客户端错误，主要是指网络异常、文件读写IO异常、参数校验失败等。此文将列举客户端定义的错误码信息。

#客户端错误码列表
|错误码|描述|状态码|
| ------ | --------- | ---- |
|InvalidArgument|参数校验失败，如必填参数为空|10000|
|InvalidCredentials|密钥信息校验失败，如密钥为空|10001|
|BadRequest|SDK配置错误，如APPID|10002|
|SinkSourceNotFound|输入源或者输出源错误，如上传的文件不存在|10003|
|InternalError|内部错误，如xml格式数据解析失败|20000|
|ServerError|服务错误,如返回了非xml格式数据|20001|
|IOError|流读写IO异常，如文件读写IO异常|20002|
|NetworkError|网络出现异常，如网络不可用，dns解析失败等|20003|
|UserCancelled|用户已取消了请求|30000|
|AlreadyFinished|已执行过请求|30001|