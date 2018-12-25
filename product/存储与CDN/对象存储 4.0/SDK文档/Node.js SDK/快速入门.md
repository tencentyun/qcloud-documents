## 开发准备
### SDK 获取

对象存储服务的 XML JS SDK 资源 github 地址：[tencentyun/cos-nodejs-sdk-v5](https://github.com/tencentyun/cos-nodejs-sdk-v5) 。

演示示例 Demo 下载地址：[XML Node.js SDK Demo](https://github.com/tencentyun/cos-nodejs-sdk-v5/tree/master/demo) 。

### npm 引入
开发前需先安装环境依赖： [npm 地址](https://www.npmjs.com/package/cos-nodejs-sdk-v5)。
 
```
npm i cos-nodejs-sdk-v5 --save
```

### 开发环境

1. 使用 SDK 需要您的运行环境包含 nodejs 以及 npm，nodejs 版本建议 7.0 版本以上。
2. 在安装完成 npm 后，您还需要安装 npm 依赖包，在 SDK 的解压目录执行`npm install`。
3.  到 [控制台密钥管理](https://console.cloud.tencent.com/capi) 获取您的项目 SecretId 和 SecretKey。

>?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

## 快速入门	

1. 到 [COS 对象存储控制台](https://console.cloud.tencent.com/cos4) 创建存储桶，得到 Bucket（存储桶名称） 和 [Region](https://cloud.tencent.com/document/product/436/6224)（地域名称）。
2. 到 [控制台密钥管理](https://console.cloud.tencent.com/capi) 获取您的项目 SecretId 和 SecretKey。
3. 初始化有两种方式，使用永久密钥初始化和使用临时密钥初始化。
 - 使用永久密钥初始化
将 SecretId、SecretKey、Bucket 和 Region 修改为您实际开发环境下的值，测试上传文件，请参考以下示例代码。
```javascript
// 引入模块
var COS = require('cos-nodejs-sdk-v5');
// 使用永久密钥创建实例
var cos = new COS({
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
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

 - 使用临时密钥初始化。
	临时密钥生成和使用请参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。Node.js SDK 支持通过传入临时密钥进行初始化，请参考以下示例代码。
```
// 使用临时密钥创建实例
var cos = new COS({
    getAuthorization: function (options, callback) {
        // 异步获取签名
        $.get('../server/sts.php', {
            bucket: options.Bucket,
            region: options.Region,
        }, function (data) {
            callback({
                 TmpSecretId: data.credentials.tmpSecretId, 
                 TmpSecretKey: data.credentials.tmpSecretKey, 
                 XCosSecurityToken: data.credentials.sessionToken, 
                 ExpiredTime: data.expiredTime
            });
        });
    }
});
```

## 相关文档 

1. 更多例子请参阅 [XML Node.js SDK Demo](https://github.com/tencentyun/cos-nodejs-sdk-v5/blob/master/demo/) 。
2. 完整接口文档请参阅 [XML Node.js SDK 接口文档](https://cloud.tencent.com/document/product/436/12264)。

