## 输入参数
| 域名                        | 含义        | 备注                                                                                                                               |
| ------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Bcc                       | 暗送地址      | 目前不支持                                                                                                                            |
| Cc                        | 抄送地址      | 目前不支持                                                                                                                            |
| Content-Transfer-Encoding | 内容的传输编码方式 | 目前没有用到，不用传，除了附件内容之外，其他的内容无需加密                                                                                                    |
| Content-Type              | 内容的类型     | 目前必须传 text/plain; charset=UTF-8,text/html; charset=UTF-8 multipart/mixed, multipart/related 和 multipart/alternative 中的一种，传其他的会报错 |
| Date                      | 日期和时间     | 目前没有用到                                                                                                                           |
| Delivered-To              | 发送地址      | 目前没有用到                                                                                                                           |
| From                      | 发件人地址     | 必传                                                                                                                               |
| Message-ID                | 消息 ID     | 目前没有用到                                                                                                                           |
| MIME-Version              | MIME 版本   | 目前没有用到，不传或者传1.0。否则会报错                                                                                                            |
| Received                  | 传输路径      | 目前没有用到                                                                                                                           |
| Reply-To                  | 回复地址      | 目前没有用到                                                                                                                           |
| Return-Path               | 回复地址      | 目前没有用到                                                                                                                           |
| Subject                   | 主题        | 必传                                                                                                                               |
| To                        | 收件人地址     | 必传                                                                                                                               |

### 附件部分参数（发送附件时）
| 域名                        | 含义        | 备注                             |
| ------------------------- | --------- | ------------------------------ |
| Content-Type              | 段体的类型     | 文件建议传 application/octet-stream  |
| Content-Transfer-Encoding | 段体的传输编码方式 | 目前仅支持传 base64，传其他的会报错           |
| Content-Disposition       | 段体的安排方式   | 目前仅支持传 attachment，传其他的会导致无法发送附件 |
| Content-ID                | 段体的 ID    | 目前不支持                          |
| Content-Location          | 段体的位置(路径) | 目前不支持                          |
| Content-Base              | 段体的基位置    | 目前不支持                          |

>?输入参数校验要求总体与 [发信接口](https://cloud.tencent.com/document/product/1288/51034) 保持一致：包含收件人邮箱数量，邮件正文大小，附件格式，附件大小等限制。

## 返回参数
SMTP 接口无返回参数，仅支持返回 err 信息。若返回 nil，则标识调用接口成功，但实际发信不一定成功，获取邮件的发送状态可参见 [获取邮件发送的状态](https://cloud.tencent.com/document/product/1288/51832)。

## 错误码
### 系统级错误
1. body 部分单行超过2000，或以上更多
`554 5.0.0 Error: transaction failed, blame it on the weather: smtp: too longer line in input stream` 或其他包含 `too longer` 的日志。
`write tcp *.*.*.*:60575->*.*.*.*:25: write: broken pipe`

2. 附件大小过大
附件9M左右 返回 EOF，建议附件总大小低于8M，整体报文大小不能超过10M，否则内容会截断，会报 base64 解码失败等其他异常错误。
				
### 业务级错误
业务报错形式如下：
`
554 5.0.0 Error: transaction failed, blame it on the weather: ##SES-response-json: {"Response":{"RequestId":"bee4e9fb-8127-48cc-b606-bbb1e801596b","QcloudError":{"Error":{"Code":"FailedOperation.MissingEmailContent.操作失败。缺少发信内容（TemplateData和Simple不能同时为空)。
`
 `##SES-response-json:`之后的是发信接口返回的结构体的 `json` 形式，字段说明如下：

| 字段          | 字段类型   | 含义    |
| ----------- | ------ | ----- |
| RequestId   | string | 请求 LD  | 
| QcloudError | stuct  | 错误结构体 | 

QcloudError:

| 字段          | 字段类型   | 含义    | 
| ----------- | ------ | ----- | 
| Code   | string | 错误码  | 
| Message | string  | 错误信息 | 



一般业务错误说明：

| 错误码                                | 错误描述                                                               | 备注                                    |
| ---------------------------------- | ------------------------------------------------------------------ | ------------------------------------- |
| FailedOperation                    | msg.From is null                                                   | 发信人为空                                 |
| FailedOperation                    | msg.Subject is null                                                | 发信主题为空                                |
| FailedOperation                    | msg.Body is null                                                   | 发信内容为空                                |
| FailedOperation                    | Content-Transfer-Encoding must in...                               | 检查附件的 Content-Transfer-Encoding，参照入参说明 |
| FailedOperation                    | Content-Type must in...                                            | 检查 Header 中的 Content-Type，参照入参说明         |
| FailedOperation                    | Mime-Version must in...                                            | 检查 Header 中的 Mime-Version，参照入参说明         |
| FailedOperation                    | The email is too large. Remove some content...                     | 除了附件之外的邮件正文不能超过1M                     |
| FailedOperation                    | Incorrect attachment content. Make sure the base64 content is...   | 附件的内容需要base64加密                       |
| FailedOperation                    | The attachments are too large. Make sure they do not exceed the... | 单个附件超过5M。或所有附件大小超过10M(具体大小可能会调整)      |
| RequestLimitExceeded.SmtpRateLimit | smtp sending frequency limit...                                    | 触发 SMTP 调用频率限制                          |

### 其他业务报错：
您可参见 [发送邮件](https://cloud.tencent.com/document/product/1288/51034) 中错误码描述。
