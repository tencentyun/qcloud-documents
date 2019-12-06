## 开发准备
### SDK 获取
智能图像的 Node SDK 下载地址：[Node-SDK](https://github.com/TencentCloudBase/image-node-sdk) 。

## 快速入门
### 在腾讯云申请业务的授权

授权包括： APPID 、SecretId 、 SecretKey ，目前只支持主账号及密钥进行调用。


### 安装使用

```javascript
npm i --save image-node-sdk
```
以 OCR-身份证识别 为例，一般支持外链 url 或者本地读取图片文件这两种方式。

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

如果想运行，[example/index.js](https://github.com/TencentCloudBase/image-node-sdk/tree/master/example/index.js) 下面的例子，请先在项目根目录新建 config/index.js 文件，并按以下格式写下配置：

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

然后运行：

```javascript
npm run example
```

## 支持功能

* 文字识别 OCR
    -  [手写体识别](https://cloud.tencent.com/document/product/866/17596) - ocrHandWriting
    -  [身份证识别](https://cloud.tencent.com/document/product/866/17597) - ocrIdCard
    -  [营业执照识别](https://cloud.tencent.com/document/product/866/17598) - ocrBizLicense
    -  [行驶证驾驶证识别](https://cloud.tencent.com/document/product/866/17599) - ocrDrivingLicence
    -  [车牌号识别](https://cloud.tencent.com/document/product/866/17601) - ocrPlate
    - [通用印刷体识别](https://cloud.tencent.com/document/product/866/17600) - ocrGeneral
    -  [银行卡识别](https://cloud.tencent.com/document/product/866/17602) - ocrBankCard
    - [名片识别（V2)](https://cloud.tencent.com/document/product/866/17595) - ocrBizCard

* 图片识别
    -  [图片分析](https://cloud.tencent.com/document/product/865/17592) - imgTagDetect
    -  [图片鉴黄](https://cloud.tencent.com/document/api/865/35473) - imgPornDetect

