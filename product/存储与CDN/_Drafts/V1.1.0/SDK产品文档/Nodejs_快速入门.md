# Nodejs SDK 快速入门

腾讯云 COS Nodejs SDK（[XML API](https://cloud.tencent.com/document/product/436/7751)）

## install

 [npm 地址](https://www.npmjs.com/package/cos-nodejs-sdk-v5)
 
```
npm i cos-nodejs-sdk-v5 --save
```

## demo

1. 到 [COS对象存储控制台](https://console.cloud.tencent.com/cos4) 创建存储桶，得到 Bucket（存储桶名称） 和 Region（地域名称）
2. 到 [控制台密钥管理](https://console.cloud.tencent.com/capi) 获取您的项目 SecretId 和 SecretKey
3. 参照以下代码，修改 SecretId、SecretKey、Bucket、Region，测试上传文件

```javascript
// 引入模块
var COS = require('cos-nodejs-sdk-v5');
// 创建实例
var cos = new COS({
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
});
// 分片上传
cos.sliceUploadFile({
    Bucket: 'test-1250000000',
    Region: 'ap-guangzhou',
    Key: '1.zip',
    FilePath: './1.zip'
}, function (err, data) {
    console.log(err, data);
});
```

## 相关文档 

[更多例子](demo/demo.js)

[详细文档](https://cloud.tencent.com/document/product/436/8629)
