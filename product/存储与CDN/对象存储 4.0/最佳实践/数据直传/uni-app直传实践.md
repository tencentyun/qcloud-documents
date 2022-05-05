## 简介
本文档介绍如何不依赖 SDK，使用简单的代码，在 uni-app 直传文件到对象存储（Cloud Object Storage，COS）的存储桶。

>? 本文档内容基于 XML API 的 [PostObject 接口](https://cloud.tencent.com/document/product/436/14690)。
>

## 方案说明

### 执行过程

1. 在前端选择文件，前端将后缀发送给服务端。
2. 服务端根据后缀，生成带时间的随机 COS 文件路径，并计算对应的 PostObject policy 签名，返回 URL 和签名信息给前端。
3. 前端调用 [PostObject 接口](https://cloud.tencent.com/document/product/436/14690)，直传文件到 COS。

### 方案优势

- 权限安全：使用 PostObject policy 签名可以有效限定安全的权限范围，只能用于上传指定的一个文件路径。
- 路径安全：由服务端决定随机的 COS 文件路径，可以有效避免已有文件被覆盖的问题和安全风险。
- 兼容多端：使用 uni-app 提供的选文件、上传接口，可以一份代码多端可兼容（Web/小程序/App）。


## 前提条件

1. 登录  [COS 控制台](https://console.cloud.tencent.com/cos5) 并创建存储桶，得到 Bucket（存储桶名称） 和 Region（地域名称），详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
2. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)， 获取您的项目 SecretId 和 SecretKey。
3. 进入刚创建的存储桶详情页面，在**安全管理 > 跨域访问CORS设置**页面，单击**添加规则**。配置示例如下图，详情请参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318) 文档。
![](https://main.qcloudimg.com/raw/86dc77bee6d3da13a91ab378c79d8a53.jpg)


## 实践步骤

>! 正式部署前，建议您在服务端加一层对网站本身的权限检验。
>

### 前端上传

1. 参考 [post-policy 示例](https://github.com/tencentyun/cos-demo/tree/main/server/post-policy/) 实现一个服务端接口，用于生成随机文件路径、计算签名，并返回给前端。
2. 使用 HBuildX 默认模板创建 uni-app 应用。
创建后，该应用为一个基于 Vue 的项目。
3. 复制以下代码替换 pages/index/index.vue 文件内容，并修改调用的 post-policy 接口链接，将其指向自己的服务端地址（即步骤1的服务端接口）。
```html
<template>
   <view class="content">
      <button type="default" @click="selectUpload">选择文件上传</button>
      <image v-if="fileUrl" class="image" :src="fileUrl"></image>
   </view>
</template>

<script>
   export default {
      data() {
         return {
            title: 'Hello',
            fileUrl: ''
         };
      },
      onLoad() {

      },
      methods: {
         selectUpload() {

            var vm = this;

            // 对更多字符编码的 url encode 格式
            var camSafeUrlEncode = function (str) {
               return encodeURIComponent(str)
                       .replace(/!/g, '%21')
                       .replace(/'/g, '%27')
                       .replace(/\(/g, '%28')
                       .replace(/\)/g, '%29')
                       .replace(/\*/g, '%2A');
            };

            // 获取上传路径、上传凭证L
            var getUploadInfo = function (extName, callback) {
               // 传入文件后缀，让后端生成随机的 COS 对象路径，并返回上传域名、PostObject 接口要用的 policy 签名
               // 参考服务端示例：https://github.com/tencentyun/cos-demo/server/post-policy/
               uni.request({
                  url: 'http://127.0.0.1:3000/post-policy?ext=' + extName,
                  success: (res) => {
                     callback && callback(null, res.data.data);
                  },
                  error(err) {
                     callback && callback(err);
                  },
               });
            };

            // 发起上传请求，上传使用 PostObject 接口，使用 policy 签名保护
            // 接口文档：https://cloud.tencent.com/document/product/436/14690#.E7.AD.BE.E5.90.8D.E4.BF.9D.E6.8A.A4
            var uploadFile = function (opt, callback) {
               var formData = {
                  key: opt.cosKey,
                  policy: opt.policy, // 这个传 policy 的 base64 字符串
                  success_action_status: 200,
                  'q-sign-algorithm': opt.qSignAlgorithm,
                  'q-ak': opt.qAk,
                  'q-key-time': opt.qKeyTime,
                  'q-signature': opt.qSignature,
               };
               // 如果服务端用了临时密钥计算，需要传 x-cos-security-token
               if (opt.securityToken) formData['x-cos-security-token'] = formData.securityToken;
               uni.uploadFile({
                  url: 'https://' + opt.cosHost, //仅为示例，非真实的接口地址
                  filePath: opt.filePath,
                  name: 'file',
                  formData: formData,
                  success: (res) => {
                     if (![200, 204].includes(res.statusCode)) return callback && callback(res);
                     var fileUrl = 'https://' + opt.cosHost + '/' + camSafeUrlEncode(opt.cosKey).replace(/%2F/g, '/');
                     callback && callback(null, fileUrl);
                  },
                  error(err) {
                     callback && callback(err);
                  },
               });
            };

            // 选择文件
            uni.chooseImage({
               success: (chooseImageRes) => {
                  var file = chooseImageRes.tempFiles[0];
                  if (!file) return;
                  // 获取要上传的本地文件路径
                  var filePath = chooseImageRes.tempFilePaths[0];
                  // 获取上传的文件后缀，然后后端生成随机 COS 路径地址
                  var fileName = file.name;
                  var lastIndex = fileName.lastIndexOf('.');
                  var extName = lastIndex > -1 ? fileName.slice(lastIndex + 1) : '';
                  // 获取预上传用的域名、路径、凭证
                  getUploadInfo(extName, function (err, info) {
                     // 上传文件
                     info.filePath = filePath;
                     uploadFile(info, function (err, fileUrl) {
                        vm.fileUrl = fileUrl;
                     });
                  });
               }
            });
         },
      }
   }
</script>

<style>
   .content {
      padding: 20px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
   }

   .image {
      margin-top: 20px;
      margin-left: auto;
      margin-right: auto;
   }
</style>
```
4. 在 HBuilderX 上，选择**运行 > 运行到浏览器 > Chrome**，即可在浏览器选择文件进行上传。
执行效果如下图所示：
 - 创建项目：
![uni-app 创建项目](https://qcloudimg.tencent-cloud.cn/raw/a11738411f47e1d1df51b1246ad92104.jpg)
 - 直传效果：
![uni-app 直传效果](https://qcloudimg.tencent-cloud.cn/raw/01fd87f664cff606f9dfbad7783a06f8.jpg)

##  Demo 代码地址

示例 Demo 下载地址：[upload-demo](https://github.com/tencentyun/cos-demo/tree/main/uni-app/upload-demo)

