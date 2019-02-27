## 流程概览
PC  页面开发流程如下图所示：
![](https://mc.qcloudimg.com/static/img/3cabdc2a3af7369cd05eca73ce5517bb/image.png)

## 步骤说明
1. 后台通过调用天御 CaptchIframeQuery 接口获取验证码的 JS 地址。
详情请参见 [后台获取验证码 JS 地址](https://cloud.tencent.com/document/product/283/33222)。
2. 把获取到的 JS 地址回传给网页客户端。
3. 依据获取到的回传 JS 地址加载和校验验证码。
详情请参见 [PC 网页 API](https://cloud.tencent.com/document/product/283/33221)。
4. 用户验证完成后，将获取的用户验证票据到后台。
```js
function cbfn(retJson){
　　if(retJson.ret==0) 　　{
　　　//用户验证成功
　　　retJson.ticket://用户票据
　　} 　　else
　　｛
　　　//用户关闭验证码页面，没有验证
　　｝
｝
```
5. 后台调用天御的 CaptchaCheck 接口来验证票据是否通过验证。
详情请参见 [后台验证票据 API](https://cloud.tencent.com/document/product/283/33223)。
>!
- 请不要使用 iframe 页面嵌入验证码。验证码弹出的 iframe 框大小会变化，如果业务使用 iframe 会导致验证码 iframe 页面显示不全。
- PC 预留给验证码展示的地方尺寸不能小于300px（宽）\* 310px（高），否则会导致验证码显示异常而影响用户使用。
- PC 页面必须设置验证码显示页面初始宽高。
- 手机验证码页面要全屏显示，否则验证码页面会显示异常，影响用户使用。
