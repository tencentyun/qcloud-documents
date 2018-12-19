## 概述

此文将为您介绍请求出错时返回的错误码和对应错误信息。您可以根据 HTTP 的 StatusCode 和 Body 来确定问题。其中 Body 的格式如下：
```
{
    "errorcode" : <ErrorCode>,
    "errormessage" : <ErrorMessage>
}
```
## 错误码详情

| HTTP 状态码（StatusCode） | 错误码（ErrorCode）  | 描述（ErrorMessage）                                         |
| ------------------------- | -------------------- | ------------------------------------------------------------ |
| 400                       | InvalidAuthorization | 签名串格式不合法                                             |
| 400                       | InvalidCompressType  | 指定的x-cls-compress-type不支持                              |
| 400                       | InvalidContent       | 消息体错误，解压失败或者解析失败                             |
| 400                       | InvalidContentType   | 指定的Content-Type不支持                                     |
| 400                       | InvalidParam         | 缺少必要参数或者个别参数不合法                               |
| 400                       | MissingAgentIp       | 缺少x-cls-agent-ip                                           |
| 400                       | MissingAgentVersion  | 缺少x-cls-agent-version                                      |
| 400                       | MissingAuthorization | 缺少Authorization                                            |
| 400                       | MissingContent       | 消息体是空的                                                 |
| 400                       | MissingContentType   | 缺少Content-Type                                             |
| 400                       | TopicClosed          | 指定的Topic已经关闭采集功能                                  |
| 401                       | Unauthorized         | 鉴权未通过，可能是ID错误，重复使用的签名，签名本身计算错误等 |
| 403                       | LogsetExceed         | 日志集数量超出限制，最多10个                                 |
| 403                       | LogSizeExceed        | 提交的日志超出最大限制，最大5MB                              |
| 403                       | NotAllowed           | 不允许此操作                                                 |
| 403                       | TopicExceed          | 日志主题数量超出限制，最多20个                               |
| 404                       | IndexNotExist        | 指定的索引规则不存在                                         |
| 404                       | LogsetNotExist       | 指定的日志集不存在                                           |
| 404                       | MachineGroupNotExist | 指定的机器组不存在                                           |
| 404                       | ShipperNotExist      | 指定的投递规则不存在                                         |
| 404                       | TopicNotExist        | 指定的日志主题不存在                                         |
| 405                       | NotSupported         | 不支持此操作                                                 |
| 409                       | IndexConflict        | 相同的索引规则已存在                                         |
| 409                       | LogsetConflict       | 相同的日志集已存在                                           |
| 409                       | MachineGroupConflict | 相同的机器组已存在                                           |
| 409                       | ShipperConflict      | 相同的投递规则已存在                                         |
| 409                       | TopicConflict        | 相同的日志主题已存在                                         |
| 500                       | InternalError        | 内部错误                                                     |
