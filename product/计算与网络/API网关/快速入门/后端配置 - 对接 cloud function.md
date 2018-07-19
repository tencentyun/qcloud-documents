当用户选择API网关到SCF不开启响应集成时（现有使用模式）时，在API网关向SCF发送请求时，会以固定的结构体对request信息进行组合。SCF收到的为此固定结构体。返回保持透传不做处理。

配置说明：
1）当后端对接 SCF 时，需要配置您在 SCF 上创建的函数。

2）配置超时时间，单击【完成】。
![](https://main.qcloudimg.com/raw/65d08771bd3f792ddabdc8cc74aed23f.png)

当用户选择API网关到SCF开启响应时，API网关向SCF发送请求时会以固定结构体对request信息进行组合，SCF返回的也需要为固定结构体。API 网关再将SCF返回的内容映射到 statusCode、header、body 等位置返回给客户端。
![](https://main.qcloudimg.com/raw/dc157e3bc40ffd6c7daff5f62766b1ab.png)

这种情况下，需要用户以如下数据格式返回数据给API网关，以便API网关解析：
```
{ "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headerName": "headerValue", ... },
    "body": "..."
}
```
API网关发往SCF的结构体格式为：
```
{
  
  "requestContext": {
    "serviceId": "123456",
    "path": "/{proxy+}",
    "method": "POST",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs",
      "sourceIp": "10.0.2.14"
    },
    "sourceIp": "10.0.2.14",
    "stage": "prod"
  },
  
  "headers": {
    "Accept-Language": "en-US,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
    "User-Agent": "Custom User Agent String"
  },
  "body": "{\"test\":\"body\"}",

  "pathParameters": {
    "proxy": "path/to/resource"
  },
  "queryStringParameters": {
    "foo": "bar"
  },
  "headerParameters":{
    "Refer": "10.0.2.14"
  },
  
  "stageVariables": {
    "baz": "qux"
  },
  
  "path": "/path/to/call"
  "method": "POST",
}
```

