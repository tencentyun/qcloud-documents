为方便Node.js开发者调试和接入云API， 我们提供了基于 Node.js 的 SDK。

[从 Github 访问 >>](https://github.com/CFETeam/qcloudapi-sdk) 
[点击下载 Node.js SDK >>](https://mc.qcloudimg.com/static/archive/0903b39539c6759cb61c797ae06da259/qcloudapi-sdk-master.zip)

qcloudapi-sdk 是腾讯云 API 2.0 的 node.js SDK 工具包。

## 1. 资源

见不同模块API的公共参数、API概览、错误码。如[云服务器API公共参数](http://cloud.tencent.com/document/api/213/6976)、[云服务器API概览](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88)、[云服务器API错误码](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81)。

## 2. 安装

```
npm i qcloudapi-sdk --save
```


## 3. 入门

1) [获取安全凭证](https://console.cloud.tencent.com/capi)。在第一次使用云API之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretId 和 SecretKey, SecretId 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

2) 安装并使用本SDK。详细使用方法请参考下面的示例。

## 4. 示例

```
var Capi = require('qcloudapi-sdk')

// 通过构造函数传入的参数将作为默认配置
var capi = new Capi({
    SecretId: 'Your SecretId here',
    SecretKey: 'Your SecretKey here',
    serviceType: 'account'
});

capi.request({
    Region: 'gz',
    Action: 'DescribeProject',
    otherParam: 'otherParam'
}, function(error, data) {
    console.log(data)
})

// 传入配置以覆盖默认项
capi.request({
    Region: 'gz',
    Action: 'DescribeInstances',
    otherParam: 'otherParam'
}, {
    serviceType: 'cvm'
}, function(error, data) {
    console.log(data)
});

// 生成 querystring
var qs = capi.generateQueryString({
    Region: 'gz',
    Action: 'DescribeInstances',
    otherParam: 'otherParam'
}, {
    serviceType: 'cvm'
});
// 'Region=gz&SecretId=&Timestamp=1449461969&Nonce=20874&Action=DescribeInstances&otherParam=otherParam&Signature=r%2Fa9nqMxEIn5RsMjqmIksQ5XcYc%3D'
```

## 5. SDK API
请访问 [api.md](https://github.com/CFETeam/qcloudapi-sdk/blob/master/api.md)
