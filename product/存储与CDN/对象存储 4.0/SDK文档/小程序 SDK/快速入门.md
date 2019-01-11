## 下载与安装

### 相关资源

小程序 SDK 资源下载地址：[GitHub 下载](https://github.com/tencentyun/cos-wx-sdk-v5)。

### 环境依赖

适用于微信小程序环境。

### 安装 SDK
安装小程序 SDK 有两种方式，手动安装和 npm 安装，具体安装方法如下。

- 手动安装
复制源码里的 [cos-wx-sdk-v5.js](https://github.com/tencentyun/cos-wx-sdk-v5/blob/master/demo/lib/cos-wx-sdk-v5.js) 到自己小程序代码目录里，代码可以通过相对路径引用：
```shell
var COS = require('./cos-wx-sdk-v5.js')
```
- npm 安装
如果小程序代码使用了 webpack 打包，通过 npm 安装依赖即可：
```shell
npm install cos-wx-sdk-v5
```
其中小程序代码使用`var COS = require('cos-wx-sdk-v5');`进行引用。

### 前期准备

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos4) 创建存储桶，获取 Bucket（存储桶名称） 和 Region（地域名称）。
2. 通过管理控制台的 [密钥管理](https://console.cloud.tencent.com/capi) 获取您的项目 SecretId 和 SecretKey。

#### 计算签名

若把签名计算放在前端，会暴露 SecretId 和 SecretKey，为此我们需要把签名计算过程放在后端实现。前端通过 ajax 向后端获取临时密钥，正式部署时请在后端加一层自己网站本身的权限检验。

这里提供 PHP 和 Node.js 的 [签名示例](https://github.com/tencentyun/cos-js-sdk-v5/blob/master/server/)，其他语言使用临时密钥，详情请查阅 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。

## 快速入门

### 初始化

```js
var cos = new COS({
    // ForcePathStyle: true, // 如果使用了很多存储桶，可以通过打开后缀式，减少配置白名单域名数量，请求时会用地域域名
    getAuthorization: function (options, callback) {
        // 异步获取签名
        wx.request({
            url: 'https://example.com/sts.php',
            data: {
                Method: options.Method,
                Key: options.Key
            },
            dataType: 'text',
            success: function (result) {
                var data = result.data;
                var credentials = data.credentials;
                callback({
                    TmpSecretId: credentials.tmpSecretId,
                    TmpSecretKey: credentials.tmpSecretKey,
                    XCosSecurityToken: credentials.sessionToken,
                    ExpiredTime: data.expiredTime, // SDK 在 ExpiredTime 时间前，不会再次调用 getAuthorization
                });
            }
        });
    }
});
```

更详细的初始化方法可以参考 [demo](https://github.com/tencentyun/cos-wx-sdk-v5/blob/master/demo/demo-sdk.js) 示例。

### 创建存储桶

```js
cos.putBucket({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: filename,
}, function (err, data) {
    console.log(err || data);
});
```

>!如果需要在小程序创建存储桶，但存储桶名称未知时，无法将存储桶名称配置为域名白名单，相关处理措施请查看 [常见问题](https://cloud.tencent.com/document/product/436/30746#.E5.B0.8F.E7.A8.8B.E5.BA.8F.E9.87.8C.E8.AF.B7.E6.B1.82.E5.A4.9A.E4.B8.AA.E5.9F.9F.E5.90.8D.EF.BC.8C.E6.88.96.E8.80.85.E5.AD.98.E5.82.A8.E6.A1.B6.E5.90.8D.E7.A7.B0.E4.B8.8D.E7.A1.AE.E5.AE.9A.EF.BC.8C.E6.80.8E.E4.B9.88.E8.A7.A3.E5.86.B3.E7.99.BD.E5.90.8D.E5.8D.95.E9.85.8D.E7.BD.AE.E5.92.8C.E9.99.90.E5.88.B6.E9.97.AE.E9.A2.98.EF.BC.9F)。

### 查询存储桶列表

```js
cos.getService(function (err, data) {
    console.log(err || data);
});
```

### 上传对象

小程序上传接口 wx.uploadFile 只支持 POST 请求，SDK 上传文件则需要使用 postObject 接口，如果小程序里只需要用到上传文件接口，建议不引用 SDK，请直接参考简单例子 [demo](https://github.com/tencentyun/cos-wx-sdk-v5/blob/master/demo/demo-no-sdk.js)。

```js
// 先选择文件，得到临时路径
wx.chooseImage({
    count: 1, // 默认9
    sizeType: ['original'], // 可以指定是原图还是压缩图，默认用原图
    sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
    success: function (res) {
        var filePath = res.tempFiles[0].path;
        var filename = filePath.substr(filePath.lastIndexOf('/') + 1);
        cos.postObject({
            Bucket: 'examplebucket-1250000000',
            Region: 'ap-beijing',
            Key: filename,
            FilePath: filePath,
            onProgress: function (info) {
                console.log(JSON.stringify(info));
            }
        }, function (err, data) {
            console.log(err || data);
        });
    }
});
```

### 查询对象列表

```js
cos.getBucket({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Prefix: 'exampledir/',
}, function (err, data) {
    console.log(err || data);
});
```

### 获取对象 Url

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.png',
}, function (err, data) {
    console.log(err || data.Url);
});
```

### 上传文本内容到对象

上传文本内容可以通过 putObject 接口完成，该接口实际调用的是 wx.request 接口。

```js
cos.putObject({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.txt',
    Body: 'hello',
    onProgress: function (info) {
        console.log(JSON.stringify(info));
    }
}, function (err, data) {
    console.log(err || data);
});
```

### 读取对象的文本内容

```js
cos.getObject({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.txt',
}, function (err, data) {
    console.log(err || data.Body);
});
```

### 删除对象

```js
cos.deleteObject({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.png',
}, function (err, data) {
    console.log(err || data.Body);
});
```

## 常见问题
若您在使用小程序 SDK 过程中，有相关的疑问，请参阅 [常见问题](https://cloud.tencent.com/document/product/436/30746#.E5.B0.8F.E7.A8.8B.E5.BA.8F.E9.87.8C.E8.AF.B7.E6.B1.82.E5.A4.9A.E4.B8.AA.E5.9F.9F.E5.90.8D.EF.BC.8C.E6.88.96.E8.80.85.E5.AD.98.E5.82.A8.E6.A1.B6.E5.90.8D.E7.A7.B0.E4.B8.8D.E7.A1.AE.E5.AE.9A.EF.BC.8C.E6.80.8E.E4.B9.88.E8.A7.A3.E5.86.B3.E7.99.BD.E5.90.8D.E5.8D.95.E9.85.8D.E7.BD.AE.E5.92.8C.E9.99.90.E5.88.B6.E9.97.AE.E9.A2.98.EF.BC.9F) 文档小程序部分。


## 相关文档

完整文档正在完善中，目前小程序不支持分片相关接口。若您需要使用上传、下载相关功能，请查看 [源码](https://github.com/tencentyun/cos-wx-sdk-v5) 和 [demo](https://github.com/tencentyun/cos-wx-sdk-v5/blob/master/demo/demo-no-sdk.js)。其他接口文档请参考 JavaScript SDK 的 [接口文档](https://cloud.tencent.com/document/product/436/12260)。
