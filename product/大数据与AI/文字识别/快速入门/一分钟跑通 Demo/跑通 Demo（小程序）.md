本文主要介绍如何快速运行腾讯云 文字识别 OCR Demo。


### 前提条件

- 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629) 。
- 进入 [文字识别控制台](https://console.cloud.tencent.com/ocr/general)，即可开通相应服务，并在 [账号中心](https://console.cloud.tencent.com/cam/capi) 获取 API 密钥。
- 并将 [OcrDemo](https://github.com/TencentCloud/tc-ocr-sdk/tree/master/MiniProgram/OcrDemo) 文件下载到本地。


### 环境要求

- 开发工具使用微信开发者工具，基础库 2.12.2 或以上版本
- 建议使用真机体验（开发者工具中无法体验自动识别模式）


### 操作步骤

#### 步骤1：导入工程

打开微信开发者工具，导入 OcrDemo 项目工程

#### 步骤2：若使用真机调试，请在开发者工具中登录您的微信开发者账号


#### 步骤3: 修改配置信息

修改项目中的 secretId secretKey 值，填入您在腾讯云控制台的 API 密钥。
修改文件的路径 'demo/config.js'

```
module.exports = {
  secretId: '**************', // 此处修改为您的 secretId
  secretKey: '**************', // 此处修改为您的 secretKey
}
```

>! 
> 
> 本文提到的将 secretId、secretKey 直接配置到小程序中的方式，使用固定密钥计算签名，一旦您的密钥泄密，攻击者可以使用您的 secretId、secretKey 信息进行 OCR 识别请求，给您造成损失。因此该方法**仅适用于本地跑通 Demo 和功能调试**
> 
> 我们建议您将 secretId、secretKey 配置到服务器端，同时小程序使用临时密钥兑换的方式进行 OCR 识别。



#### 步骤4:编译运行

完成配置之后，选择您的运行机器（模拟器&真机）。
