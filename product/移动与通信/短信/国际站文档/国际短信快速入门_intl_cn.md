## 开通国际/港澳台短信服务
 ### 注册腾讯云账号
 如果您还没有腾讯云账号，您需要先注册一个腾讯云账号，具体操作流程请参阅 [注册腾讯云](https://cloud.tencent.com/document/product/378/9603) 文档。
 如果您已有腾讯云账号，请直接进行下一步操作。

 ### 登录腾讯云短信控制台
 登录腾讯云短信 SMS【[控制台](https://console.cloud.tencent.com/sms)】，首次登录短信 SMS 控制台需要申请开通短信服务。
 ![](https://main.qcloudimg.com/raw/69894f4b9b1c722fdc4f462d7c645add.png)
 ### 申请开通国际/港澳台短信服务
 如果您的账号未实名认证，请到 [帐户信息中心](https://console.cloud.tencent.com/developer) 进行实名认证，具体操作参照 [实名认证指引](https://cloud.tencent.com/document/product/378/3629)。
 如果您已经实名认证通过，单击【开始接入】。

 >您需通过“企业认证”才能申请开通国际/港澳台短信服务。
 >若您为个人认证用户可提交工单修改认证信息。


 ## 发送前准备
 >1. 一个完整的短信由**短信签名**和**短信正文内容**两部分组成，您可以根据业务需求分别设置不同的短信正文内容模板，然后进行组合形成最终展示。**短信签名+短信正文内容=最终显示内容**；
 >2. 短信签名和模板提交后，我们会在半个工作日内完成审核，如有需求可设置常用手机和邮箱，用于即时接收该应用短信内容审核通知。

 ![](https://main.qcloudimg.com/raw/4b5fa1f8323d4cb4ce2a24e2e88fa756.png)
 最终用户收到的短信样式如下：
 ![](https://main.qcloudimg.com/raw/c8997824cf02cb1c9a65e1672e51863c.png)

 ### 添加应用
 添加应用获取 SDK AppID 和 App Key 。详细操作请参阅 [添加应用](https://cloud.tencent.com/document/product/382/18053#.E6.B7.BB.E5.8A.A0.E5.BA.94.E7.94.A8)。

 ### 创建签名
 一个完整的短信由短信签名和短信正文内容两部分组成，短信签名规则详见 [签名审核标准](https://cloud.tencent.com/document/product/382/13444#.E7.AD.BE.E5.90.8D.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86)，详细操作请参阅 [创建签名](https://cloud.tencent.com/document/product/382/18053#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。

 ### 创建正文模板
 短信正文模板规则详见 [普通短信审核标准](https://cloud.tencent.com/document/product/382/13444#.E6.99.AE.E9.80.9A.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86)，详细操作请参阅 [创建正文模板](https://cloud.tencent.com/document/product/382/18053#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E7.89.88)。


 ## 发送国际/港澳台短信
 正文模板和短信签名都通过审核后，就可以开始发送短信了。您通过控制台、云短信 API 或 SDK 发送短信。
 - 控制台发送文本短信详细流程请参阅 [发送文本短信](https://cloud.tencent.com/document/product/382/13481) 文档。
 - API 发送短信请参阅[ API 文档](https://cloud.tencent.com/document/product/382/13297)。



 ### 查看短信发送结果
 短信发送成功后，可在短信发送 [国际/港澳台短信统计分析](https://cloud.tencent.com/document/product/382/18054) 中查看短信发送结果和统计信息。
