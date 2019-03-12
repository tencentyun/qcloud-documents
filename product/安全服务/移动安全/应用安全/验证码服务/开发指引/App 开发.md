## 流程概览
App 开发流程如下图所示：
![](https://mc.qcloudimg.com/static/img/2257609feb6fb4c458c319aaf199fdb2/image.png)

## 步骤说明
1. 后台通过调用天御 CaptchIframeQuery 接口获取验证码的 JS 地址。
详情请参见 [后台获取验证码 JS 地址](https://cloud.tencent.com/document/product/283/33222)。
2. 把获取到的 JS 地址回传给网页客户端。
3. 依据获取到的回传 JS 地址加载和校验验证码。
 - [iOS 客户端 API](https://cloud.tencent.com/document/product/283/33219)
 - [Android 客户端 API](https://cloud.tencent.com/document/product/283/33218)
4. 用户验证完成后，将获取的用户验证票据到后台。
详情请参见 [后台验证票据 API](https://cloud.tencent.com/document/product/283/33223)。
5. 后台调用天御的 CaptchaCheck 接口来验证票据是否通过验证。

>!手机验证码页面要全屏显示，否则验证码会显示异常，影响用户使用。
