## 简介

您可以登录对象存储（Cloud Object Storage，COS）控制台，为存储桶开启CLS日志服务的实时日志功能。 CLS提供**存储桶对象操作**相关的各种请求日志的分钟粒度的上报、实时检索、可视化与告警的强大功能。 开启实时日志功能，可以帮助您更好的分析当前存储桶的访问情况，并且在访问异常时，快速定位问题。


<dx-alert infotype="notice" title="前提条件">
<li>目前 COS 的实时日志功能开启需要开启白名单， 请前往 <a href="https://cloud.tencent.com/online-service?from=connect-us">联系我们</a> 申请开启实时日志功能。</li>
<li>为 COS 存储桶开启实时日志功能，需先 <a href="https://cloud.tencent.com/product/cls">开通 CLS 日志服务</a>。</li>
</dx-alert>





## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航栏中， 单击【存储桶列表】， 进入存储桶列表管理页面。
3. 找到需要开启实时日志功能的存储桶， 单击该存储桶名称， 进入该存储桶管理页面。
4. 在左侧导航栏中， 选择【日志管理】> 【日志检索】。
5. 页面将提示“当前Bucket未开通实时日志功能”， 单击【立即开通】开启。
   ![](https://main.qcloudimg.com/raw/b863a781357e668b098408ad62f3c5da.png)
6. 完成开通后，该存储桶的访问日志将被投递至CLS同地域下的日子主题中，日志主题名称为cos-log-store。
7. 在【日志管理】> 【日志检索】下， 输入检索分析语句，选择时间范围，单击检索分析即可检索该存储桶上报到 CLS 的访问日志。 CLS检索与分析语句的使用介绍请参见  [检索语法](https://cloud.tencent.com/document/product/614/47044)。
   ![](https://main.qcloudimg.com/raw/b80f23cd5efdcf63cd4e75f6751d497c.png)
8. 针对存储桶访问日志分析方法， 可参见 [COS 访问日志分析最佳实践](https://cloud.tencent.com/document/product/614/61406)。
9. 若要进一步对存储桶访问日志进行可视化与告警的配置， 请前往 [CLS 控制台](https://console.cloud.tencent.com/cls)。

## 日志格式与变量说明

存储桶访问日志记录了源存储桶，用户 id，请求方法等信息

| 字段序号 | 名 称              | 含 义                                                        | 示例                                                         |
| :------- | :----------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1        | eventVersion       | 记录版本                                                     | 1.0                                                          |
| 2        | bucketName         | 存储桶名称                                                   | examplebucket-1250000000                                     |
| 3        | qcsRegion          | 请求地域                                                     | ap-beijing                                                   |
| 4        | eventTime          | 事件时间（请求结束时间，UTC 0时 时间戳）                     | 2018-12-01T11:02:33Z                                         |
| 5        | eventSource        | 用户访问的域名                                               | examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com       |
| 6        | eventName          | 事件名称                                                     | UploadPart                                                   |
| 7        | remoteIp           | 来源 IP                                                      | 192.168.0.1                                                  |
| 8        | userSecretKeyId    | 用户访问 KeyId                                               | AKIDNYVCdoJQyGJ5brTf                                         |
| 9        | reservedFiled      | 保留字段                                                     | 保留字段，显示为`-`。                                        |
| 10       | reqBytesSent       | 请求字节数（Bytes）                                          | 83886080                                                     |
| 11       | deltaDataSize      | 请求对存储量的改变（Bytes）                                  | 808                                                          |
| 12       | reqPath            | 请求的文件路径                                               | /folder/text.txt                                             |
| 13       | reqMethod          | 请求方法                                                     | put                                                          |
| 14       | userAgent          | 用户 UA                                                      | cos-go-sdk-v5.2.9                                            |
| 15       | resHttpCode        | HTTP 返回码                                                  | 404                                                          |
| 16       | resErrorCode       | 错误码                                                       | NoSuchKey                                                    |
| 17       | resErrorMsg        | 错误信息                                                     | The specified key does not exist.                            |
| 18       | resBytesSent       | 返回字节数（Bytes）                                          | 197                                                          |
| 19       | resTotalTime       | 请求总耗时（毫秒，等于响应末字节的时间-请求首字节的时间）    | 4295                                                         |
| 20       | logSourceType      | 日志源类型                                                   | USER（用户访问请求），CDN（CDN 回源请求）                    |
| 21       | storageClass       | 存储类型                                                     | STANDARD，STANDARD_IA，ARCHIVE                               |
| 22       | accountId          | 存储桶所有者ID                                               | 100000000001                                                 |
| 23       | resTurnAroundTime  | 请求服务端耗时（毫秒，等于响应首字节的时间-请求末字节的时间） | 4295                                                         |
| 24       | requester          | 访问者                                                       | 主账号 ID：子账号 ID，如果是匿名访问则显示`-`。              |
| 25       | requestId          | 请求 ID                                                      | NWQ1ZjY4MTBfMjZiMjU4NjRfOWI1N180NXXXX=                     |
| 26       | objectSize         | 对象大小（Bytes）                                            | 808，如果您使用分块上传，objectSize 字段只会在完成上传的时候显示，各个分块上传期间该字段显示`-` |
| 27       | versionId          | 对象版本 ID                                                  | 随机字符串                                                   |
| 28       | targetStorageClass | 目标存储类型，发起复制操作的请求会记录该字段                 | STANDARD，STANDARD_IA，ARCHIVE                               |
| 29       | referer            | 请求的 HTTP referer                                          | `*.example.com` 或者111.111.111.1                             |
| 30       | requestUri         | 请求 URI                                                     | "GET /fdgfdgsf%20/%E6%B5%AE%E7%82%B9%E6%95%B0 HTTP/1.1"      |
