## 开发准备
### SDK 获取

智能图像的 Node SDK 下载地址：[node-SDK-V2.0](https://github.com/TencentCloudBase/image-node-sdk) 。


## 快速入门
### 在腾讯云申请业务的授权

授权包括： APPID 、SecretId 、 SecretKey 及存储桶名（可参考 [域名管理](https://cloud.tencent.com/document/product/460/6937) ）。


### 安装使用

```javascript
npm i -save image-node-sdk-v2
```
以 OCR-身份证识别 为例，一般支持外链 url 或者本地读取图片文件，两种方式。

* 外链 url

```javascript
const {
    ImageClient
} = require('image-node-sdk');

let AppId = ''; // 腾讯云 AppId
let SecretId = ''; // 腾讯云 SecretId
let SecretKey = ''; // 腾讯云 SecretKey

let idCardImageUrl = 'http://images.cnitblog.com/blog/454646/201306/07090518-029ff26fac014d72a7786937e8319c78.jpg';
let imgClient = new ImageClient({ AppId, SecretId, SecretKey });
imgClient.ocrIdCard({
    data: {
        url_list: [idCardImageUrl]
    }
}).then((result) => {
    console.log(result.body)
}).catch((e) => {
    console.log(e);
});
```
* 读取本地文件

```javascript
const fs = require('fs');
const path = require('path');
const {
    ImageClient
} = require('image-node-sdk');

let AppId = ''; // 腾讯云 AppId
let SecretId = ''; // 腾讯云 SecretId
let SecretKey = ''; // 腾讯云 SecretKey

let imgClient = new ImageClient({ AppId, SecretId, SecretKey });
imgClient.ocrIdCard({
    formData: {
        card_type: 0,
        image: fs.createReadStream(path.join(__dirname, './idcard.jpg'))
    },
    headers: {
        'content-type': 'multipart/form-data'
    }
}).then((result) => {
    console.log(result.body)
}).catch((e) => {
    console.log(e);
});
```

如果想运行，[example/index.js](./example/index.js) 下面的例子，请先在项目根目录新建 config/index.js 文件，并按以下格式写下配置

```javascript
    const ProxyUrl = ''; // 可填公司代理
    const AppId = ''; // 腾讯云 AppId
    const SecretId = ''; // 腾讯云  SecretId
    const SecretKey = ''; // 腾讯云 SecretKey

    exports.ProxyUrl = ProxyUrl;
    exports.AppId = AppId;
    exports.SecretId = SecretId;
    exports.SecretKey = SecretKey;
```

然后运行

```javascript
npm run example
```

