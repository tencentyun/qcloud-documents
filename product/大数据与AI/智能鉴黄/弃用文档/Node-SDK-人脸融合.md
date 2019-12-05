>!本 SDK 仅适用于2018年12月前发布的活动。
因引擎算法升级，请2018年12月1日后创建新活动的用户，使用 [新版 SDK](https://cloud.tencent.com/document/product/670/31061#SDK)。


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
* 信息认证
    - [身份证信息认证](https://cloud.tencent.com/document/product/641/13391) - authIdCard

* 人脸识别
    -  [多脸检索](https://cloud.tencent.com/document/product/867/17590) - faceMultiple
    -  [人脸检测与分析](https://cloud.tencent.com/document/product/867/17588) - faceDetect
    -  [五官定位](https://cloud.tencent.com/document/product/867/17585) - faceShape
    -  [个体信息管理-个体创建](https://cloud.tencent.com/document/product/867/17583#.E4.B8.AA.E4.BD.93.E5.88.9B.E5.BB.BA) - faceNewPerson
    -  [个体信息管理-删除个体](https://cloud.tencent.com/document/product/867/17583#.E5.88.A0.E9.99.A4.E4.B8.AA.E4.BD.93) - faceDelPerson
    -  [个体信息管理-增加人脸](https://cloud.tencent.com/document/product/867/17583#.E5.A2.9E.E5.8A.A0.E4.BA.BA.E8.84.B8) - faceAddFace
    -  [个体信息管理-删除人脸](https://cloud.tencent.com/document/product/867/17583#.E5.88.A0.E9.99.A4.E4.BA.BA.E8.84.B8) - faceDelFace
    -  [个体信息管理-设置信息](https://cloud.tencent.com/document/product/867/17583#.E8.AE.BE.E7.BD.AE.E4.BF.A1.E6.81.AF) - faceSetInfo
    -  [个体信息管理-获取信息](https://cloud.tencent.com/document/product/867/17583#.E8.8E.B7.E5.8F.96.E4.BF.A1.E6.81.AF) - faceGetInfo
    -  [个体信息管理-获取组列表](https://cloud.tencent.com/document/product/867/17583#.E8.8E.B7.E5.8F.96.E7.BB.84.E5.88.97.E8.A1.A8) - faceGetGpIds
    -  [个体信息管理-获取人列表](https://cloud.tencent.com/document/product/867/17583#.E8.8E.B7.E5.8F.96.E4.BA.BA.E5.88.97.E8.A1.A8) - faceGetPersonIds
    -  [个体信息管理-获取人脸列表](https://cloud.tencent.com/document/product/867/17583#.E8.8E.B7.E5.8F.96.E4.BA.BA.E8.84.B8.E5.88.97.E8.A1.A8) - faceGetFaceIds
    -  [个体信息管理-获取人脸信息](https://cloud.tencent.com/document/product/867/17583#.E8.8E.B7.E5.8F.96.E4.BA.BA.E8.84.B8.E4.BF.A1.E6.81.AF) - faceGetFaceInfo
    -  [个体信息管理-新增组信息](https://cloud.tencent.com/document/product/867/17583#person-.E6.96.B0.E5.A2.9E.E7.BB.84.E4.BF.A1.E6.81.AF) - faceAddGPIds
    -  [个体信息管理-删除组信息](https://cloud.tencent.com/document/product/867/17583#person-.E5.88.A0.E9.99.A4.E7.BB.84.E4.BF.A1.E6.81.AF) - faceDelGPIds
    -  [人脸验证](https://cloud.tencent.com/document/product/867/17589) - faceVerify
    -  [人脸检索](https://cloud.tencent.com/document/product/867/17586) - faceIdentify
    -  [人脸比对](https://cloud.tencent.com/document/product/867/17584) - faceCompare

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
    -  [图片标签](https://cloud.tencent.com/document/product/865/17592) - imgTagDetect
    -  [图片鉴黄](https://cloud.tencent.com/document/product/864/17609) - imgPornDetect

* 人脸核身
    -  [人脸静态活体检测](https://cloud.tencent.com/document/product/868/17575) - faceLiveDetectPic
    -  [唇语活体检测视频身份信息核验](https://cloud.tencent.com/document/product/868/17577) - faceIdCardLiveDetectFour
    -  [活体检测—获取唇语验证码](https://cloud.tencent.com/document/product/868/17579) - faceLiveGetFour
    -  [活体检测视频与用户照片的对比](https://cloud.tencent.com/document/product/868/17578) - faceLiveDetectFour
    -  [用户上传照片身份信息核验](https://cloud.tencent.com/document/product/868/17580) - faceIdCardCompare

* 人脸融合
    -  [人脸融合](https://cloud.tencent.com/document/product/670/14357) - faceFusion
