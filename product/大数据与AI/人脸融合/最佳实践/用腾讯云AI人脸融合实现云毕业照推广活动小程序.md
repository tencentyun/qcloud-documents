近两年，经常在朋友圈、短视频平台刷到很多品牌的推广活动都融入了 AI 能力，形成裂变式传播，为品牌带来巨大的曝光量。特别是之前爆火的毕业照云写真活动，为很多因为疫情无法举行线下毕业活动的毕业生提供了毕业照换装的体验，不仅有趣，也挺有人文关怀。



作为一名小程序开发者，类似的玩法也激发了我的兴趣，想参考这个活动，研究一下如何实现相似的活动小程序。感兴趣的可以在微信搜索小程序【腾讯云 AI 体验中心】，直接访问小程序体验。

**活动流程如下：**

首先用户需要完成授权，因为这里涉及使用者人脸图片等隐私数据，需要谨慎对待。

<img src="https://qcloudimg.tencent-cloud.cn/raw/53405f88d891b5fd450db21bcc1a1944.png" width="300px">

然后上传或拍摄人脸图片，活动平台通过人脸融合服务，将用户上传图片与各种毕业造型进行融合，最终得到毕业照融合结果并展示。并且用户可以通过点击换造型，体验不同造型的融合效果，大大增加了趣味性。

<img src="https://qcloudimg.tencent-cloud.cn/raw/55c1514a376b3939e4bd579652aae769.png" length="606px">

## 一、准备工作
首先毕业照云写真是由腾讯云 AI 团队推出的小活动，今天我们同样选择腾讯云 AI 的人脸融合服务来实现相似的小程序。



在开始之前，需要先了解腾讯云 AI 人脸融合服务，下一步在腾讯云控制台开通服务并创建专属的活动以及上传活动模板图片。
1. 了解腾讯云人脸融合服务以及 API 使用方式：
	- [人脸融合](https://cloud.tencent.com.cn/product/facefusion)
	- [人脸融合 API 概览](https://cloud.tencent.com.cn/document/product/670/31052)
2. 访问人脸融合控制台：[登录 - 腾讯云](https://console.cloud.tencent.com/facefusion) 开通人脸融合服务。
3. 新建活动，上传模板图片。
![](https://qcloudimg.tencent-cloud.cn/raw/3eb740caf0a52123fcdfc49cee79845f.png)
![](https://qcloudimg.tencent-cloud.cn/raw/9de04d9d8070723b1b41a878719f7b4b.png)
>! 新活动有500次免费调用，后续可以购买资源包或者走后付费结算。
4. 获取 API 访问密钥 [登录 - 腾讯云](https://console.cloud.tencent.com/cam/capi)，这个访问密钥十分重要，是每个用户请求腾讯云请求的标识，一旦泄漏，可能被拿去刷量从而产生高额费用，要谨慎保管。其次，需要学习小程序开发的基础知识：[微信开放文档](https://developers.weixin.qq.com/miniprogram/dev/framework/)，充分了解这两个内容后，就可以开始开发。

## 二、开发过程
1. 前端页面
以毕业照活动为例，总共包括：开始页、上传页以及结果页。
![](https://qcloudimg.tencent-cloud.cn/raw/df25916552fdc2d0f81385d52b4fa745.png)
	- 开始页：点击进入上传页
	- 上传页：用户可上传或拍摄带有人脸的图片，作为毕业照的换脸图使用
	- 结果页：将换脸图与活动设定的随机模板图，通过腾讯云人脸融合服务，请求并获得换脸结果展示出来。当前活动主题是毕业季云写真，因此模板图都是毕业照相关的内容，如果需要展示其他主题内容，可更换模板图达到效果。
2. 前端开发
	- 开始页：简单的页面跳转不赘述
	- 上传页：**（仅为主要逻辑，非完整代码）**
		主要完成点击相册、点击拍摄两个操作逻辑，其中相册跟拍摄都可以使用微信小程序集成的接口：wx.chooseMedia，通过 sourceType 区分场景
		需要注意的是处理 chooseMedia 的回调，成功获取临时图片数据之后，将图片上传到云存储，方便后面其他场景使用。上传云存储使用接口：**wx.cloud.uploadFile**，完成后即可跳转到下一页。
		```
		Page({
  data: {},
  async chooseMediaSuccessCB({ tempFiles }) {
    const tempFile = tempFiles[0];
    // 将临时图片上传到云存储
    const { fileID } = await wx.cloud.uploadFile({
      // 可设置随机字符串作为存储名称存储
      cloudPath: 'xxxxxx.jpg',
      filePath: tempFile,
    });
    // 完成后，将图片结果作为参数传递到结果页
    wx.navigateTo({
      url: 'result?userImage=' + fileID, // 结果页地址
    });
  },
  // 相册按钮响应事件
  tapAlbum() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album'],
      sizeType: ['compressed'],
      success: this.chooseMediaSuccessCB,
    });
  },
  // 拍摄按钮响应事件
  async tapShoot() {
    const { authSetting } = await wx.getSetting({});
    const shoot = () => {
      wx.chooseMedia({
        count: 1,
        mediaType: ['image'],
        sourceType: ['camera'],
        // 默认使用前置摄像头
        camera: 'front',
        sizeType: ['compressed'],
        success: this.chooseMediaSuccessCB,
      });
    };
    // 拍摄前需要咨询摄像头权限
    if (!authSetting['scope.camera']) {
      wx.authorize({
        scope: 'scope.camera',
        success() {
          shoot();
        },
      })
    } else {
      shoot();
    }
  },
})
```
	- 结果页：**（仅为主要逻辑，非完整代码）**
结果页需要完成上传图片与模板图片的融合，以及换造型的逻辑。
为了提升整个换造型的体验，可以将融合结果跟模板id映射并缓存起来，节省请求发起！最重要的是省钱！<br>
腾讯云 API 的实现，我们是使用了小程序的云开发，下一段落再详细描述，这里前端直接请求封装好的请求函数即可，参考人脸融合API文档，将入参填入发起请求，逻辑本身并不复杂。请求小程序云函数使用函数：**wx.cloud.callFunction**。
```
Page({
  data: {
    userImage: '',
    resultImage: '',
  },
  async onLoad(option) {
    const userImage = option.userImage;
    this.setData({
      userImage,
    });
    // 默认进行一次人脸融合请求，获取结果并展示
    await this.fuseFace(userImage);
  },
  // 换造型按钮响应事件
  async tapReplace() {
    await this.fuseFace(this.data.userImage);
  },
  async fuseFace(userImage) {
    // 获取随机模板ID
    const modelId = this.getModelId();
    let resultImage = this.getResult(modelId);
    // 如果该模板ID在缓存中有结果，直接拿缓存结果返回
    if (resultImage) {
      this.setData({
        resultImage,
      });
      return;
    }
    // 请求腾讯云人脸融合服务获取结果
    // 此处使用小程序云开发，可另行在服务端实现腾讯云请求
    const { result: res } = await wx.cloud.callFunction({
      name: 'TencentCloudAI',
      data: {
        method: 'facefusion/FuseFace',
        data： {
          ProjectId: 'xxxx', // 在控制台创建的活动ID
          ModelId: modelId,
          RspImgType: 'url',
          MergeInfos: [{
            Url: userImage,
          }],
        }，
      },
    });
    if (res && res.Response && res.Response.FusedImage) {
      resultImage = res.Response.FusedImage;
      this.setData({
        resultImage,
      });
      // 将modelID与融合结果配对存进缓存
      this.saveResult(modelId, resultImage);
    }
  },
  // 随机返回在腾讯云人脸融合控制台上传的模板id
  getModelId() {}，
  // 根据modelId返回缓存结果，没有结果返回null
  getResult(modelId) {},
  // 将modelID与融合结果配对存进缓存
  saveResult(modelId, resultImage);
})
```
3. 云函数开发（仅为主要逻辑，非完整代码）

接上，本次开发使用了云函数实现腾讯云函数请求，请求逻辑参考以下代码：requestYunApi.js，大家有需要复制粘贴使用即可。通过密钥完成鉴权，由于涉及腾讯云密钥使用，强烈建议将密钥放到云函数存放，不要明文写在前端代码里。
```
/* requestYunApi.js */
// 引入腾讯云服务SDK
const tencentcloud = require('tencentcloud-sdk-nodejs');
const { Credential } = tencentcloud.common;
const { ClientProfile } = tencentcloud.common;
const { HttpProfile } = tencentcloud.common;
// 密钥信息，妥善保管
const secretId = '';
const secretKey = '';
function requestAPI({
  endpoint, // 请求域名 (可选)
  service, // 服务前缀
  action, // 接口名称
  version, // 版本号
  region, // 地域 (可选)
  data, // 请求数据
}) {
  const { Client } = tencentcloud[service][version];
  const { Models } = tencentcloud[service][version];
  const cred = new Credential(secretId, secretKey);
  const httpProfile = new HttpProfile();
  httpProfile.endpoint = endpoint || `${service}.tencentcloudapi.com`;
  const clientProfile = new ClientProfile();
  clientProfile.httpProfile = httpProfile;
  const client = new Client(cred, region || 'ap-guangzhou', clientProfile);
  const req = new Models[`${action}Request`]();
  const reqParams = JSON.stringify({ ...data });
  req.from_json_string(reqParams);
  return new Promise((resolve, reject) => {
    client[action](req, (errMsg, response) => {
      if (errMsg) {
        reject(errMsg);
        return;
      }
      resolve(JSON.parse(response.to_json_string() || {}));
    });
  });
}
module.exports = requestAPI;
```
处理前端请求，需要注意的是，前端传入的图片文件地址，是云存储的地址，需要将云存储换成真实的文件地址，通过 cloud.getTempFileURL 完成转换逻辑。
```
/* 云函数TencentCloudAI */
const cloud = require('wx-server-sdk');
// 腾讯云API请求函数
const requestAPI = require('./requestYunApi');
cloud.init();
function getFileUrl(url) {
  // 如果是 cloud:// 则，换取云文件真实链接
  if (/^cloud:\/\//.test(url)) {
    const { fileList } = await cloud.getTempFileURL({
      fileList: [url],
    }); 
    if (!fileList || !fileList[0]) {
      throw new Error('无法获取文件');
    } 
    return fileList[0].tempFileURL;
  }
  return url;
}
// 云函数入口函数
exports.main = async (event) => {
  // 有云存储fileID则将其转换为http url
  if (event.data.MergeInfos) {
    const mergeInfos = event.data.MergeInfos;
    event.data.MergeInfos = await Promise.all(mergeInfos.map(mergeInfo => {
      ...mergeInfo,
      Url: await getFileUrl(cloud, e.Url),
    }));
  }
  // 请求参数，可以配置不同腾讯云请求参数
  const configs = {
    'facefusion/FuseFace': {
      service: 'facefusion',
      action: 'FuseFace',
      version: 'v20181201',
    },
  };
  // 发起请求
  const requestRes = {
    Response: await requestAPI({
      ...configs[event.method],
      data: event.data,
    }),
  };
  return requestRes;
}
```

## 三、发布
开发完成并完成测试验证后，即可通过小程序管理平台发布线上供用户访问。

至此整个毕业照活动的主要逻辑就介绍完成了，这个逻辑可以复用到类似的主题活动小程序里面。如果有兴趣的同学可以加入一起开发尝试哦～

