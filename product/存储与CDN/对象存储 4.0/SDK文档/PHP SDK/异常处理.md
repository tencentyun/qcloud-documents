## 简介

调用 SDK 接口请求 COS 服务失败时，如返回码为4xx或者5xx，系统将抛出 （Qcloud\Cos\Exception\ServiceResponseException）异常。

## 服务端异常

CosServerException 包含了服务端返回的状态码、requestid 和出错明细等。捕获异常后，建议对整个异常进行打印，异常包含了必须的排查因素。以下是异常成员变量的描述以及异常捕获示例：

| 成员         | 描述             | 类型   |
| ----------- | ---------------- | ------ |
| requestId    | 请求 ID，用于表示一个请求，对于排查问题十分重要              | string |
| statusCode   | response 的 status 状态码，更多详情请参阅 [COS 错误码](https://cloud.tencent.com/document/product/436/7730) | string |
| errorCode    | 请求失败时 body 返回的 Error Code，更多详情请参阅 [COS 错误码](https://cloud.tencent.com/document/product/436/7730) | string |
| errorMessage | 请求失败时 body 返回的 Error Message，更多详情请参阅 [COS 错误码](https://cloud.tencent.com/document/product/436/7730) | string |


### 异常捕获示例

```php
try {
   $cosClient->listBuckets() 
} catch (\Exception $e) {
    $statusCode = $e->getStatusCode(); // 获取错误码
    $errorMessage = $e->getMessage(); // 获取错误信息
    $requestId = $e->getRequestId(); // 获取错误的 requestId
    $errorCode = $e->getCosErrorCode(); // 获取错误名称
    $request = $e->getRequest(); // 获取完整的请求
    $response = $e->getResponse(); // 获取完整的响应
｝
```
