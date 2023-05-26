## 简介

本文档介绍如何不依赖 SDK，用简单的代码，在小程序直传文件到对象存储（Cloud Object Storage，COS）的存储桶。

> ! 本文档内容基于 XML 版本的 API。

<span id="前期准备"></span>

## 前期条件

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5) ，创建存储桶，设置 BucketName（存储桶名称） 和 Region（地域名称），详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
2. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)，进入 API 密钥管理页面，获取您的项目 SecretId 和 SecretKey。
3. 配置小程序域名白名单

小程序里请求 COS 需要登录到微信公众平台，在“开发”->“开发设置”中，配置域名白名单。SDK 用到了两个接口：wx.uploadFile 和 wx.request。

- cos.postObject 使用 wx.uploadFile 发送请求。
- 其他方法使用 wx.request 发送请求。

两者都需要在对应白名单里，配置 COS 域名。白名单里配置的域名格式有两种：

- 如果只用到一个存储桶，可以配置 Bucket 域名作为白名单域名，例如`examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com`。
- 如果用到多个存储桶，可以选择后缀式请求 COS，把 bucket 放在 pathname 里请求，这种方式需要配置地域域名作为白名单，例如`cos.ap-guangzhou.myqcloud.com`。具体可参考下文代码中的注释。

## 方案说明

### 执行过程

1. 在前端选择文件，前端将后缀发送给服务端。
2. 服务端根据后缀，生成带时间的随机 COS 文件路径，并计算对应的签名，返回 URL 和签名信息给前端。
3. 前端使用 PUT 或 POST 请求，直传文件到 COS。

### 方案优势

- 权限安全：使用服务端签名可以有效限定安全的权限范围，只能用于上传指定的一个文件路径。
- 路径安全：由服务端决定随机的 COS 文件路径，可以有效避免已有文件被覆盖的问题和安全风险。

### 后缀式请求

COS API 一般的请求格式都类似`POST http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/`，请求的域名是存储桶域名。这样如果在小程序里用到多个存储桶，则需要配置这个存储桶域名作为白名单域名。解决方法如下：

COS 提供了后缀式请求格式`POST http://cos.ap-beijing.myqcloud.com/examplebucket-1250000000/`，请求的域名是地域域名，存储桶名称放在请求的路径里。在小程序里用到同一个地域多个存储桶，只需要配置一个域名`cos.ap-beijing.myqcloud.com`作为白名单域名。

后缀式请求格式需要注意，签名时使用的路径要用以存储桶名称作为前缀的路径，例如`/examplebucket-1250000000/`。

## 实践步骤

### 配置服务端实现签名

> ! 正式部署时服务端请加一层您的网站本身的权限检验。

如何计算签名可参考文档 [请求签名](https://cloud.tencent.com/document/product/436/7778)。
服务端使用 Nodejs 计算签名代码可参考 [Nodejs 示例](https://github.com/tencentyun/cos-js-sdk-v5/blob/master/server/sts.js)。

### 小程序上传示例

以下代码同时举例了 [PUT Object ](https://cloud.tencent.com/document/product/436/7749) 接口（推荐使用）和[POST Object ](https://cloud.tencent.com/document/product/436/14690) 接口，操作指引如下：

#### 使用 POST 上传

```js
var uploadFile = function () {
  // 对更多字符编码的 url encode 格式
  var camSafeUrlEncode = function (str) {
    return encodeURIComponent(str)
      .replace(/!/g, '%21')
      .replace(/'/g, '%27')
      .replace(/\(/g, '%28')
      .replace(/\)/g, '%29')
      .replace(/\*/g, '%2A');
  };

  // 获取签名
  var getAuthorization = function (options, callback) {
    wx.request({
      method: 'GET',
      // 替换为自己服务端地址 获取post上传签名
      url: 'http://127.0.0.1:3000/post-policy?ext=' + options.ext,
      dataType: 'json',
      success: function (result) {
        var data = result.data;
        if (data) {
          callback(data);
        } else {
          wx.showModal({
            title: '临时密钥获取失败',
            content: JSON.stringify(data),
            showCancel: false,
          });
        }
      },
      error: function (err) {
        wx.showModal({
          title: '临时密钥获取失败',
          content: JSON.stringify(err),
          showCancel: false,
        });
      },
    });
  };

  var postFile = function ({ prefix, filePath, key, formData }) {
    var requestTask = wx.uploadFile({
      url: prefix,
      name: 'file',
      filePath: filePath,
      formData: formData,
      success: function (res) {
        var url = prefix + '/' + camSafeUrlEncode(key).replace(/%2F/g, '/');
        if (res.statusCode === 200) {
          wx.showModal({ title: '上传成功', content: url, showCancel: false });
        } else {
          wx.showModal({
            title: '上传失败',
            content: JSON.stringify(res),
            showCancel: false,
          });
        }
        console.log(res.header['x-cos-request-id']);
        console.log(res.statusCode);
        console.log(url);
      },
      fail: function (res) {
        wx.showModal({
          title: '上传失败',
          content: JSON.stringify(res),
          showCancel: false,
        });
      },
    });
    requestTask.onProgressUpdate(function (res) {
      console.log('正在进度:', res);
    });
  };

  // 上传文件
  var uploadFile = function (filePath) {
    var extIndex = filePath.lastIndexOf('.');
    var fileExt = extIndex >= -1 ? filePath.substr(extIndex + 1) : '';
    getAuthorization({ ext: fileExt }, function (AuthData) {
      // 请求用到的参数
      var prefix = 'https://' + AuthData.cosHost;
      var key = AuthData.cosKey; // 让服务端来决定文件名更安全
      var formData = {
        key: key,
        success_action_status: 200,
        'Content-Type': '',
        'q-sign-algorithm': AuthData.qSignAlgorithm,
        'q-ak': AuthData.qAk,
        'q-key-time': AuthData.qKeyTime,
        'q-signature': AuthData.qSignature,
        policy: AuthData.policy,
      };
      if (AuthData.securityToken)
        formData['x-cos-security-token'] = AuthData.securityToken;
      postFile({ prefix, filePath, key, formData });
    });
  };

  // 选择文件
  wx.chooseMedia({
    count: 1, // 默认9
    sizeType: ['original'], // 可以指定是原图还是压缩图，这里默认用原图
    sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
    success: function (res) {
      uploadFile(res.tempFiles[0].tempFilePath);
    },
  });
};
```

#### 使用 PUT 上传

```js
var uploadFile = function () {
  // 对更多字符编码的 url encode 格式
  var camSafeUrlEncode = function (str) {
    return encodeURIComponent(str)
      .replace(/!/g, '%21')
      .replace(/'/g, '%27')
      .replace(/\(/g, '%28')
      .replace(/\)/g, '%29')
      .replace(/\*/g, '%2A');
  };

  // 获取签名
  var getAuthorization = function (options, callback) {
    wx.request({
      method: 'GET',
      // 替换为自己服务端地址 获取put上传签名
      url: 'http://127.0.0.1:3000/put-sign?ext=' + options.ext,
      dataType: 'json',
      success: function (result) {
        var data = result.data;
        if (data) {
          callback(data);
        } else {
          wx.showModal({
            title: '临时密钥获取失败',
            content: JSON.stringify(data),
            showCancel: false,
          });
        }
      },
      error: function (err) {
        wx.showModal({
          title: '临时密钥获取失败',
          content: JSON.stringify(err),
          showCancel: false,
        });
      },
    });
  };

  var putFile = function ({ prefix, filePath, key, AuthData }) {
    // put上传需要读取文件的真实内容来上传
    const wxfs = wx.getFileSystemManager();
    wxfs.readFile({
      filePath: filePath,
      success: function (fileRes) {
        var requestTask = wx.request({
          url: prefix + '/' + key,
          method: 'PUT',
          header: {
            Authorization: AuthData.authorization,
            'x-cos-security-token': AuthData.securityToken,
          },
          data: fileRes.data,
          success: function success(res) {
            var url = prefix + '/' + camSafeUrlEncode(key).replace(/%2F/g, '/');
            if (res.statusCode === 200) {
              wx.showModal({
                title: '上传成功',
                content: url,
                showCancel: false,
              });
            } else {
              wx.showModal({
                title: '上传失败',
                content: JSON.stringify(res),
                showCancel: false,
              });
            }
            console.log(res.statusCode);
            console.log(url);
          },
          fail: function fail(res) {
            wx.showModal({
              title: '上传失败',
              content: JSON.stringify(res),
              showCancel: false,
            });
          },
        });
        requestTask.onProgressUpdate(function (res) {
          console.log('正在进度:', res);
        });
      },
    });
  };

  // 上传文件
  var uploadFile = function (filePath) {
    var extIndex = filePath.lastIndexOf('.');
    var fileExt = extIndex >= -1 ? filePath.substr(extIndex + 1) : '';
    getAuthorization({ ext: fileExt }, function (AuthData) {
      const prefix = 'https://' + AuthData.cosHost;
      const key = AuthData.cosKey;
      putFile({ prefix, filePath, key, AuthData });
    });
  };

  // 选择文件
  wx.chooseMedia({
    count: 1, // 默认9
    sizeType: ['original'], // 可以指定是原图还是压缩图，这里默认用原图
    sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
    success: function (res) {
      uploadFile(res.tempFiles[0].tempFilePath);
    },
  });
};
```

## 相关文档

如需使用小程序 SDK，请参见小程序 SDK [快速入门](https://cloud.tencent.com/document/product/436/31953) 文档。
