
## 简介
欢迎使用腾讯云开发者工具套件（SDK）。为方便 Node.js 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 Node.js 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 Node.js SDK 并开始调用。

## 依赖环境
1. 从 [腾讯云控制台](https://console.cloud.tencent.com) 开通相应产品，
2. [获取 SecretID、SecretKey](https://console.cloud.tencent.com/capi) 具体参考各产品说明。
3. 下载相关资料并做好相关文件配置。

## 获取安装
安装 Node.js SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 通过 GitHub 获取源码安装
打开腾讯云为您提供的 Node.js SDK GitHub 地址，[获取 GitHub 资源 >>](https://github.com/CFETeam/qcloudapi-sdk)。
1. 在 `qcloudapi-sdk`的 github 地址上下载源码
2. 解压源码到您项目合适的位置
3. 安装到项目：
```
    npm i qcloudapi-sdk --save
```

## 入门 DEMO
以 CVM 查询（DescribeInstances）为例：
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
