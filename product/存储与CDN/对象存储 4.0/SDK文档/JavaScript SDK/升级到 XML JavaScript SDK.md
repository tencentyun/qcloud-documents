如果您细心对比过  JSON  JavaScript SDK 和 XML  JavaScript SDK 的文档，您会发现并不是一个简单的增量更新。XML  JavaScript SDK 在架构、可用性和安全性上有了非常大的提升，而且在易用性、健壮性和性能上也做了非常大的改进。如果您想要升级到 XML  JavaScript SDK，请参考下面的指引，完成  JavaScript SDK 的升级工作。

## 功能对比

| 功能           |                     XML  JavaScript SDK                      |                     JSON  JavaScript SDK                     |
| -------------- | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 文件上传       | 支持本地文件、字符串内容<br>默认覆盖上传<br/>分片上传支持批量上传<br>智能判断上传模式：简单上传最大支持5GB<br>分块上传最大支持48.82TB（50,000GB） | 只支持本地文件上传<br>可选择是否覆盖<br/>小于等于20MB 使用简单上传、大于20MB 自动分片上传<br>简单上传最大支持20MB<br>分片上传最大支持64GB |
| 文件删除       |                         支持批量删除                         |                       只支持单文件删除                       |
| 存储桶基本操作 |            创建存储桶<br>查询存储桶<br>删除存储桶            |                            不支持                            |
| 存储桶ACL操作  |   设置存储桶ACL<br>获取设置存储桶ACL<br>删除设置存储桶ACL    |                            不支持                            |
| 存储桶生命周期 | 创建存储桶生命周期<br>查询存储桶生命周期<br>删除存储桶生命周期 |                            不支持                            |
| 目录操作       |                        不单独提供接口                        |               创建目录<br>查询目录<br>删除目录               |
| 使用临时密钥   |                     支持并推荐用临时密钥                     |                        不支持临时密钥                        |

## 升级步骤

#### 1. 更新 JavaScript SDK

XML  JavaScript SDK 发布在 [npm](https://www.npmjs.com/package/cos-js-sdk-v5) 仓库，推荐您使用 npm 安装依赖包。

```js
npm install cos-js-sdk-v5
```

您也可以在 github 源码中下载 js 文件 [dist/cos-js-sdk-v5.min.js](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/dist) ，通过 script 标签加入页面 html。

```html
<script src="./cos-js-sdk-v5.min.js"></script>
```

#### 2. 更改存储桶名称和可用区域简称

XML  JavaScript SDK 的存储桶名称和可用区域简称与 JSON  JavaScript SDK 的不同，需要您进行相应的更改。

#### 存储桶 Bucket

XML  JavaScript SDK  存储桶名称由两部分组成：用户自定义字符串和 APPID，两者以中划线“-”相连。
例如 `examplebucket-1250000000`，其中 `examplebucket` 为用户自定义字符串，`1250000000` 为 APPID。

> ?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。您可通过腾讯云控制台，在 [账号信息](https://console.cloud.tencent.com/developer) 查看 APPID。

设置 Bucket，请参考以下上传示例代码：

```js
cos.getBucket({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
}, function (err, data) {
    console.log(err || data);
});
```

#### 存储桶可用区域简称 Region

XML  JavaScript SDK  的存储桶可用区域简称发生了变化，不同区域在 JSON  JavaScript SDK 和 XML  JavaScript SDK  中的对应关系请查看下表：

| 地域             | XML SDK 地域简称      | JSON SDK 地域简称 |
| ---------------- | ---------------- | ----------- |
| 北京一区（华北） | ap-beijing-1     | tj          |
| 北京             | ap-beijing       | bj          |
| 上海（华东）     | ap-shanghai      | sh          |
| 广州（华南）     | ap-guangzhou     | gz          |
| 成都（西南）     | ap-chengdu       | cd          |
| 重庆             | ap-chongqing     | 无          |
| 中国香港             | ap-hongkong      | hk          |
| 新加坡           | ap-singapore     | sgp         |
| 多伦多           | na-toronto       | ca          |
| 法兰克福         | eu-frankfurt     | ger         |
| 孟买             | ap-mumbai        | 无          |
| 首尔             | ap-seoul         | 无          |
| 硅谷             | na-siliconvalley | 无          |
| 弗吉尼亚         | na-ashburn       | 无          |
| 曼谷             | ap-bangkok       | 无          |
| 莫斯科           | eu-moscow        | 无          |

您也可以参考 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 文档。

在调用每个方法时，请将存储桶所在区域的简称设置到参数 `Region` 中：

```java
cos.headBucket({
    Bucket: 'examplebucket-1250000000,
    Region: 'ap-beijing',
}, function (err, data) {
    console.log(err || data);
});
```

#### 3. 更改 API

升级到 XML  JavaScript SDK 之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。

同时我们做了封装让 SDK 更加易用，具体请参考我们的 [示例代码](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/demo) 和 [快速入门](https://cloud.tencent.com/document/product/436/11459)。

API 变化主要有以下变化：

**1）没有单独的目录接口**

在 XML SDK 中，不再提供单独的目录接口。对象存储中本身是没有文件夹和目录的概念的，对象存储不会因为上传对象`project/a.txt` 而创建一个 project 文件夹。为了满足用户使用习惯，对象存储在控制台、COSBrowser 等图形化工具中模拟了「文件夹」或「目录」的展示方式，具体实现是通过创建一个键值为`project/`，内容为空的对象，在展示方式上模拟了传统文件夹。

例如：上传对象`project/doc/a.txt`，分隔符`/`会模拟「文件夹」的展示方式，于是可以看到控制台上出现「文件夹」project 和 doc，其中 doc 是 project 下一级「文件夹」，并包含 a.txt 文件。

因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。使用场景里面有文件夹的概念，则需要提供创建文件夹的功能，您可以上传一个路径以`/`结尾的0KB 文件。这样在您调用 GetBucket 接口时，就可以将该文件当做文件夹。

**2）使用临时密钥鉴权**

由于密钥放在前端代码有安全风险，后端计算签名给前端权限不好控制，XML  JavaScript SDK 推荐您使用临时密钥的方式。具体代码参考以下完整上传示例：

```js
var Bucket = 'examplebucket-1250000000';
var Region = 'ap-beijing';
var cos = new COS({
    getAuthorization: function (options, callback) {
        var url = 'http://example.com/sts.php';
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onload = function (e) {
            try {
                var data = JSON.parse(e.target.responseText);
                var credentials = data.credentials;
            } catch (e) {
            }
            callback({
                TmpSecretId: credentials.tmpSecretId,
                TmpSecretKey: credentials.tmpSecretKey,
                XCosSecurityToken: credentials.sessionToken,
                ExpiredTime: data.expiredTime,
            });
        };
        xhr.send();
    }
});
cos.putObject({
    Bucket: Bucket,
    Region: Region,
    Key: file.name,
    Body: file,
    onProgress: function (progressData) {
        console.log('上传中', JSON.stringify(progressData));
    },
}, function (err, data) {
    console.log(err, data);
});
```

如果您仍然采用后台手动计算签名，再返回前端使用的方式，请注意我们的签名算法发生了改变。签名不再区分单次和多次签名，而是通过设置签名的有效期来保证安全性。请参考 [XML 请求签名](https://cloud.tencent.com/document/product/436/7778) 文档更新您签名的实现。

**3）参数和返回统一格式**

参数是一个对象，除了一些工具方法，接口格式都是通过一个回调返回错误信息或成功结果，如下示例：

```js
cos.putObject({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.txt',
}, function (err, data) {
    console.log(err || data);
});
```

**4）新增 API**

XML  JavaScript SDK 新增 API，您可根据需求进行调用。包括：

- 存储桶的操作，如 getService 、putBucket、getBucket 等。
- 存储桶 ACL 的操作，如 getBucketAcl、putBucketAcl 等。
- 存储桶 Policy 的操作，putBucketPolicy、getBucketPolicy、 deleteBucketPolicy。
- 存储桶生命周期的操作，如 putBucketLifecycle、getBucketLifecycle、 deleteBucketLifecycle。
- 对象 ACL 操作：getObjectAcl、putObjectAcl。
- 对象复制操作：putObjectCopy、sliceCopyFile。
- 工具方法：getObjectUrl。
- 对象上传队列：pauseTask、restartTask、cancelTask、getTaskList 方法以及 list-update 事件。

了解更多请参见 JavaScript SDK [快速入门](https://cloud.tencent.com/document/product/436/11459) 文档。
