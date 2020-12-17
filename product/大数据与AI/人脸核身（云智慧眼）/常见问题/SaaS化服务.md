### SaaS 化服务中，如何获取 RuleId？

RuleId 在 SaaS 化服务调用中使用，您在申请开通腾讯云慧眼服务后，可在 [人脸核身控制台](https://console.cloud.tencent.com/faceid) 创建流程，审核通过后即可调用。详细生成具体方式可参考：[快速入门](https://cloud.tencent.com/product/faceid/getting-started)。

### SaaS 化服务中，如何获取验证信息结果？

在用户完成验证后，慧眼还提供 [获取实名核身结果信息](https://cloud.tencent.com/document/product/1007/41957) 接口，您可以通过调用这个接口，获取到用户验证过程数据，包括文本信息、识别分数、照片和视频，**为了保证用户的隐私，结果信息慧眼侧仅保留3天，请您及时拉取。若在未完成验证前调用该接口，数据可能为 null。**

### SaaS 化服务中， SDK 文件怎么获取？

您可以在 [人脸核身控制台-自助接入](https://console.cloud.tencent.com/faceid)，创建完流程并通过审核后，可以在控制台下载对应的 SDK。

### SaaS 化服务中，通用 H5 接口，是否和公众号绑定，其他公众号也要用这个接口，要重新申请吗？

支持多个公众号绑定。

### SaaS 化服务中，“ckv 数据有误”是什么问题?

ckv 数据有误，一般是 bizToken 错误。需要检查下 DetectAuth 生成的 bizToken 是否正确。
iOS App：拉起人脸核身时，initWithServerUrl 需要设置为`https:\\faceid.qq.com`。

>!不能是测试环境地址。

### SaaS 化服务中，单击实名核身鉴权接口返回的 url 会自动跳转到腾讯网是什么原因？

若客户未配置回调地址，完成验证后会默认跳转到腾讯网，需要客户在前置授权接口 DetectAuth 需要传入正确的回调地址 RedirectUrl， 且需要是 http:// 或 https:// 开头，慧眼会在用户验证完成后跳转相应的 Url。

### SaaS 获取验证结果信息，有很多字段为 null，是什么原因？

若在未完成验证前调用该接口，数据可能为 null，需要走完全流程后再去拉取。

### Biztoken 一直有效吗？
一次核身流程的标识，Biztoken 有效时间为7,200秒；完成认证后，三天内可用 Biztoken 多次获取验证结果信息。
