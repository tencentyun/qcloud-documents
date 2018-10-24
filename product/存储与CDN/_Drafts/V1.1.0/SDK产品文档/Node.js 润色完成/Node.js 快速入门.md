## 开发准备
### SDK 获取
对象存储服务的 XML JS SDK 资源下载地址：[XML Node.js SDK](https://github.com/tencentyun/cos-nodejs-sdk-v5) 。
演示示例 Demo 下载地址：[XML Node.js SDK Demo](https://github.com/tencentyun/cos-nodejs-sdk-v5/tree/master/demo) 。

### npm 引入
开发前需先安装环境依赖： [npm 地址](https://www.npmjs.com/package/cos-nodejs-sdk-v5)
 
```
npm i cos-nodejs-sdk-v5 --save
```

### 开发环境

1. 使用 SDK 需要您的运行环境包含 nodejs 以及 npm，nodejs 版本建议 7.0 版本以上。
2. 安装好 npm 之后记得在 sdk 的解压目录 npm install 一次（安装依赖包）；
3.  到 [控制台密钥管理](https://console.cloud.tencent.com/capi) 获取您的项目 SecretId 和 SecretKey。

> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

## 快速入门	

1. 到 [COS 对象存储控制台](https://console.cloud.tencent.com/cos4) 创建存储桶，得到 Bucket（存储桶名称） 和 Region（地域名称）。
2. 到 [控制台密钥管理](https://console.cloud.tencent.com/capi) 获取您的项目 SecretId 和 SecretKey。
3. 参照以下代码，修改 SecretId、SecretKey、Bucket、Region，测试上传文件。

```javascript
// 引入模块
var COS = require('cos-nodejs-sdk-v5');
// 创建实例
var cos = new COS({
    AppId: '1250000000',
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
});
// 分片上传
cos.sliceUploadFile({
    Bucket: 'test',
    Region: 'ap-guangzhou',
    Key: '1.zip',
    FilePath: './1.zip'
}, function (err, data) {
    console.log(err, data);
});
```

## 相关文档 
更多例子请参阅 [XML Node.js SDK](https://github.com/tencentyun/cos-nodejs-sdk-v5) 。
完整接口文档请参阅 [Node.js SDK 接口文档](https://cloud.tencent.com/document/product/436/8629)。

