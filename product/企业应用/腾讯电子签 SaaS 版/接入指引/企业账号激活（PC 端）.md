本文档主要介绍如何在电脑端创建腾讯电子签企业账号，总体流程如下：
![](https://qcloudimg.tencent-cloud.cn/raw/b2050f761e008295b199846a7bc373ce.png)


## 操作步骤
### 步骤1：创建腾讯云账号并完成企业实名
- 如果您已有完成实名认证的腾讯云企业账号可跳过此步骤。
- 若您没有完成企业实名认证的腾讯云账号，您需要 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并完成 [企业实名认证](https://cloud.tencent.com/document/product/378/10496)。

### 步骤2：使用腾讯云账号登录电子签
1. 访问 [腾讯电子签登录页](https://ess.tencent.cn/)，单击腾讯云企业控制台入口（如下图所示），即可进入腾讯云账号登录页面。
2. 您可使用主账号或已授权电子签策略的子账号进行登录。本文档以主账号登录为例，子账号登录指引请参见 [如何使用子用户账号登录电子签](https://cloud.tencent.com/document/product/1323/58484#Q13)。
![](https://main.qcloudimg.com/raw/a07f2987c2078de9dc7117ed5bbcbfef.png)

#### 登录腾讯云账号
请您通过微信扫码，邮箱、QQ 等方式登录您的腾讯云账号。
<img style="width:400px; max-width: inherit;" src="https://main.qcloudimg.com/raw/a5909ec0434eb06d6d1cf594a0a2ce8a.png" />



### 步骤3：完成应用激活
登录成功后将进入应用激活流程，您完成企业名称确认，超级管理员设置及授权后，方可启用腾讯电子签的完整服务。

#### 1. 企业名称确认
- 请您在页面中确认企业名称，若信息无误可单击确认无误进入超级管理员设置流程。
- 若企业名称与实际不一致，需前往腾讯云官网进行企业更名操作，更名指引请参见 [变更企业认证信息](https://cloud.tencent.com/document/product/378/43087)。
<img style="width:700px; max-width: inherit;" src=https://qcloudimg.tencent-cloud.cn/raw/8ca130e4950874e4a6c2aa5e2a5a3ca5.png />


#### 2. 超级管理员设置[](id:smallStep2)
请您在页面中输入超级管理员的姓名、身份证号码以及手机号码，填写无误后单击下一步。
>?指定的超级管理员将拥有企业电子签合同管理的最高权限，请谨慎填写。

![](https://qcloudimg.tencent-cloud.cn/raw/00f1bb783db87e7f0746a58e69c73056.png)

#### 3. 授权方式设置[](id:smallStep3)
为保证企业合同数据的安全性，激活流程中需对超级管理员进行授权，允许超级管理员代表企业行使在腾讯电子签账号下的一切权力（如申请相关账号及数字证书、印章管理、组织管理等）。目前系统支持**上传授权书**和**法定代表人授权**两种授权方式，您可选择任意一种方式完成授权即可。

<dx-tabs>
::: 授权方式1：通过上传授权书完成授权
单击下载超级管理员授权书模板，按照模板要求填写相关信息签字并加盖企业公章后进行上传（请务必确保授权书信息的真实性与一致性。）
当前支持上传 JPG / PNG / PDF 的授权书文件格式，且文件大小不超过8M。确认企业及超级管理员信息（需与授权证书信息一致），确认无误后单击下一步完成授权操作。
![](https://qcloudimg.tencent-cloud.cn/raw/b981eff45de24695ba3bbaa6ef4eb7d5.png)
:::
::: 授权方式2：通过法定代表人授权
请在页面中输入企业社会统一信用代码、法定代表人姓名、法定代表人身份证号码以及法定代表人手机号码。输入后确认无误单击下一步。
![](https://qcloudimg.tencent-cloud.cn/raw/c23aaadd01a33d0886d7bc19f787e9a1.png)
<dx-alert infotype="explain" title="说明：">
- 输入的法定代表人信息需与企业注册的法定代表人信息一致，如不一致则无法提交成功。
- 当前仅支持企业或个体工商户的主体通过此方式进行授权，其他类型主体客户请使用授权书方式进行授权。
</dx-alert>

:::
</dx-tabs>

#### 4. 应用激活完成，等待超管完成激活及授权。
企业激活成功后，系统会向 [2](#smallStep2)、[3](#smallStep3) 步中设置的超级管理员与法定代表人发送短信（若步骤3选择通过授权书方式进行授权，则需等待人工审核）。
<dx-tabs>
::: 超管激活流程
1. 单击超级管理员手机中的**激活**短信，进入腾讯电子签小程序。
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/499a86c296f5f1cd95e6fcf28ea58c0c.png" />
2. 在小程序页面中，确认超级管理员实名信息正确后，单击**开始人脸核身**。 
![](https://qcloudimg.tencent-cloud.cn/raw/6c8d96c1ebf771250347bd8878b1593c.png)
3. 人脸核身通过后，即完成超级管理员激活操作。
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/47a103e4e5e7de6278e105414b4a7a69.png" />
4. 激活成功后，您可使用微信扫码登录 [腾讯电子签控制台](https://ess.tencent.cn/) 使用腾讯电子签服务。

:::
::: 法定代表人授权流程
1. 完成企业账号创建后，系统会给企业法定代表人发送一条短信，法定代表人需单击短信内**链接**进行授权。
![](https://qcloudimg.tencent-cloud.cn/raw/cae001ebac9659188092938f7198737d.png)
2. 单击**链接**后打开电子签小程序，法定代表人在页面中确认个人信息后即进入人脸核身环节。 
![](https://qcloudimg.tencent-cloud.cn/raw/46b6330a63a289b372b4524970c91489.png)
3. 人脸核身通过后，法定代表人将进入超级管理员授权书阅读页，授权书内容阅读完成并确认超管信息无误后单击**确认**，法定代表人即完成超级管理员的授权流程。 
![](https://qcloudimg.tencent-cloud.cn/raw/f2c942bc43807c55eba1c02fac929313.png)
:::
</dx-tabs>


### 步骤4：使用腾讯电子签服务
超级管理员通过短信完成激活并通过授权后，您即可体验腾讯电子签的所有功能，使用指引请参见 [操作指南](https://cloud.tencent.com/document/product/1323/58490)。

## 联系我们
如您按照文档进行操作的过程中遇到问题，您可通过 e-contract@tencent.com 联系我们，我们将竭诚为您服务！
