 qcloudapi-sdk 是腾讯云 API 2.0 的 node.js SDK 工具包。

### 使用方法
1. 使用之前请在腾讯云的 [云 API 控制台](https://console.cloud.tencent.com/yunso/qcloud_open.cgi) 中创建自己的安全凭证（SecretId 和 SecretKey）。 SecretKey 要严格保管, 避免泄露。
2. 下载 SDK，放入到程序目录，使用方法请参考下面的示例。

```
var Capi = require('qcloudapi-sdk')

//通过构造函数传入的参数将作为默认配置
var capi = new Capi({
    SecretId: 'Your SecretId here',
    SecretKey: 'Your SecretKey here',
    serviceType: 'account'
})

capi.request({
    Region: 'gz',
    Action: 'DescribeProject',
    otherParam: 'otherParam'
}, function(error, data) {
    console.log(data)
})

//传入配置以覆盖默认项
capi.request({
    Region: 'gz',
    Action: 'DescribeInstances',
    otherParam: 'otherParam'
}, {
    serviceType: 'cvm'
}, function(error, data) {
    console.log(data)
})

//生成 querystring
var qs = capi.generateQueryString({
    Region: 'gz',
    Action: 'DescribeInstances',
    otherParam: 'otherParam'
}, {
    serviceType: 'cvm'
})
 ```

### API 资源
 [API 列表](https://cloud.tencent.com/doc/api)
