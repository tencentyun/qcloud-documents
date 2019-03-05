## 操作场景
该任务指导您在购买人脸核身-云智慧眼服务后，通过 API 3.0 Explorer 在线接口调试页面调用人脸核身-云智慧眼接口，并将该接口对应语言的 SDK 集成到项目。

## 前提条件
在调用人脸核身接口前，您需要先 [申请开通人脸核身服务](https://cloud.tencent.com/apply/p/shcgszvmppc)，并通过审核。
审核成功后，进入云智慧眼 [API 3.0 Explorer 在线接口调试页面](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=DetectAuth&SignVersion=)，按照下面的操作流程调用接口。
![step](https://main.qcloudimg.com/raw/6a91e6088815af344eb5b1519341a4c0.png)
## 操作步骤
1. 在左侧导航栏，选择需要调用的接口。
![step_1.png](https://main.qcloudimg.com/raw/fd9409baaf6dff028e92f2d06a9e2b23.png)
2. 填写个人密钥和输入参数中的必填参数。
![step_2.png](https://main.qcloudimg.com/raw/f236395d825670f15939a2e81929e753.png)
 - Region 参数说明： 域名中的地域信息，该参数决定访问的接入点，例如 faceid.ap-shanghai.tencentcloudapi.com 就是要访问上海这个接入点。公共参数 Region 决定的是要访问业务资源所在区，例如 Region=ap-beijing 就是要操作北京区的资源，如果域名中不指定地域信息则默认就近接入。就近接入可能会存在问题。如果解析不到 IP 会默认到广州地域里面。另外域名地域和公共参数 Region 可以不一致，但是可能会增加耗时。建议域名和公共参数 Region 选择相同的地域：华南地区(广州)，ap-guangzhou。
 - RuleId 参数：需要添加云智慧眼小助手微信号（faceid001）获取。

3. 选择语言生成对应代码。
您需要先填好左侧的参数值，再生成代码，生成代码里面的一些字段和填写的信息是关联的。如需调整传入参数，要在左侧修改参数值后重新生成代码。

4. 集成 SDK 到项目。
参考右上角的 SDK 使用说明，将 SDK 引入到项目，通过上步骤3生成的代码即可调用对应的接口。
![step_3.png](https://main.qcloudimg.com/raw/91e62297edf04a9ce16f6ac6a6e29112.png)

## 注意事项
- SDK 调用方式公共参数时只需要关注 Region 字段，建议域名和 Region 统一使用 "ap-guangzhou"。
- SecretId/SecretKey 生成地址：`https://console.cloud.tencent.com/cam/capi`
- 图片/视频转 Base64时，需要去掉相关前缀`data:image/jpg;base64,`和换行符`\n`。
- 如果请求结果提示如下，  需要手动设置签名类型：
 ```
[TencentCloudSDKException]message:AuthFailure.SignatureFailure-The provided credentials
could not be validated because of exceeding request size limit, please use new signature 
method `TC3-HMAC-SHA256`. requestId:719970d4-5814-4dd9-9757-a3f11ecc9b20
```
设置签名类型：
``` js
  clientProfile.setSignMethod("TC3-HMAC-SHA256"); // 指定签名算法(默认为HmacSHA256)
```
- 如果接口请求内容超过1M，只能使用 V3 鉴权（TC3-HMAC-SHA256），API3.0 SDK 支持语言：Node、Python、Java、PHP、Go。其他语言如 .net、C# 暂时不支持 SDK 方式调用，需要自行实现 [V3鉴权](https://cloud.tencent.com/document/product/1007/31324) 进行接口调用, 建议使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=GetActionSequence) 中签名串生成工具进行核验签名有效性。
![签名调试参考图](https://main.qcloudimg.com/raw/7edfaae5e0453765606691d7d3eddb35.png)

 

## Saas化相关接口(集成UI功能版本)
### 实名核身鉴权
接口文档: https://cloud.tencent.com/document/product/1007/31816
调用时注意事项:
- RuleId参数为腾讯侧线下分配，需要填写对应checklist文档，配置好相关权限后提供
- 图片/视频转Base64时，需要去掉相关前缀"data:image/jpg;base64,"，去掉换行符(\n)

### 获取实名核身结果信息
接口文档: https://cloud.tencent.com/document/product/1007/31331
调用时注意事项：
- 需要先调用前置授权接口获取BizToken后进行验证，验证完成后再调用该接口，否则数据可能为null
- InfoType建议选1判断验证结果，如果需要视频或身份信息留底，再用234去拉取。3天内可多次拉取

## Paas化相关接口(纯API模式)
### 获取动作顺序
接口文档: https://cloud.tencent.com/document/product/1007/31822
调用时注意事项：
- 除了地域信息，不需要传其他参数，在需要活体人脸核身或活体人脸比对的动作活体时需要调用

### 获取数字验证码 
接口文档: https://cloud.tencent.com/document/product/1007/31821
调用时注意事项：
- 除了地域信息，不需要传其他参数，在需要活体人脸核身或活体人脸比对的数字活体时需要调用

### 照片人脸核身 
接口文档: https://cloud.tencent.com/document/product/1007/31820
调用时注意事项：
- 图片/视频转Base64时，需要去掉相关前缀"data:image/jpg;base64,"，去掉换行符(\n)

### 活体人脸比对 
接口文档: https://cloud.tencent.com/document/product/1007/31819
调用时注意事项：
- 图片/视频转Base64时，需要去掉相关前缀"data:image/jpg;base64,"，去掉换行符(\n)
- 当某种活体类型感觉成功率不高时，可以换一种动作活体尝试，小程序录制的非压缩视频，不建议使用静默活体

### 活体人脸核身 
接口文档: https://cloud.tencent.com/document/product/1007/31818
调用时注意事项：
- 图片/视频转Base64时，需要去掉相关前缀"data:image/jpg;base64,"，去掉换行符(\n)
- 当某种活体类型感觉成功率不高时，可以换一种动作活体尝试，小程序录制的非压缩视频，不建议使用静默活体
