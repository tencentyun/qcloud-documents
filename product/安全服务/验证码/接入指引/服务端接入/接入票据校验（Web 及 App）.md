服务端需调用票据校验 API，对客户端验证结果进行二次校验。 

> !未接入票据校验，会导致黑产轻易伪造验证结果，失去验证码人机对抗效果。

## 接入步骤
### 步骤1：安装对应语言 SDK
腾讯云提供多语言 SDK，您可以基于业务需求，安装对应语言的 SDK，详情请参见：[SDK中心](https://cloud.tencent.com/document/sdk/Description)。

### 步骤2：获取云 API 密钥
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)，左侧导航栏选择**访问秘钥** > **API 密钥管理**。
2. 在 API 密钥管理页面，如已创建密钥，在该页面查看即可；如未创建密钥，单击**新建密钥**，即可生成所需密钥。
![](https://qcloudimg.tencent-cloud.cn/raw/c4ccd1b9a4450d1130d3898dc29aef65.png)

>!建议使用子账号密钥，并遵循最小权限控制的原则（仅赋予子账号“QcloudCaptchaFullAccess”权限），降低使用风险。子账号密钥获取可参见 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。


### 步骤3：调用 DescribeCaptchaResult 接口
建议使用 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=captcha&Version=2019-07-22&Action=DescribeCaptchaResult&SignVersion=) ，在线生成代码。API 详情参见：[核查验证码票据结果（Web 及 APP）](https://cloud.tencent.com/document/product/1110/36926)。
> !不同客户端需调用对应客户端的票据校验 API，不可混用，否则会导致接口报错。

## 常见问题
详情请参见 [接入相关问题](https://cloud.tencent.com/document/product/1110/36828)。

## 更多信息
您可以登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**，了解更多详细信息。
