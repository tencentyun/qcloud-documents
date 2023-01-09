## 业务请求流程
验证码请求流程涉及业务客户端（前端）、业务服务端（后端）、验证码服务端三端交互。调用时序图如下：

![](https://qcloudimg.tencent-cloud.cn/raw/8932466a9ac61639f24b447bfb6f8f01.png)

为保障验证码服务端异常时不阻塞客户正常业务流程，提供验证码业务容灾方案如下。

> !容灾方案中生成的所有容灾票据，在请求后端票据校验时，均不会产生计费。

## 业务客户端（前端）容灾
1. 定义错误处理函数。
``` javascript
// 错误处理函数作用：在脚本加载或初始化错误时，保障事件流程正常
// 定义验证码js加载错误处理函数
    function loadErrorCallback() {
    var appid = '您的CaptchaAppId';
    // 生成容灾票据或自行做其它处理
    var ticket = 'terror_1001_' + appid + '_' + Math.floor(new Date().getTime() / 1000);
    callback({
     ret: 0,
     randstr: '@'+ Math.random().toString(36).substr(2),
     ticket: ticket,
     errorCode: 1001,
     errorMessage: 'jsload_error'
    });
 }
```

2. 验证码返回错误时，调用错误处理函数。
```javascript
try {
	// 生成一个验证码对象
	var captcha = new TencentCaptcha('你的验证码CaptchaAppId', callback, {});
	// 调用方法，显示验证码
	captcha.show(); 
} catch (error) {
	// 加载异常，调用验证码js加载错误处理函数
	loadErrorCallback();
}
```

3. 回调函数根据 ticket 和 errorCode （而非 ret）的情况做处理。
```javascript
function callback(res) {
	// res（用户主动关闭验证码）= {ret: 2, ticket: null}
	// res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
	// res（请求验证码发生错误，验证码自动返回terror_前缀的容灾票据） = {ret: 0, ticket: "String", randstr: "String",  errorCode: Number, errorMessage: "String"}
	if (res.ticket){
		//根据errorCode情况做特殊处理
        if(res.errorCode === xxxxx){
           //自定义容灾逻辑（例如跳过这次验证）
        }
      }
}
```


## 业务服务端（后端）容灾
当请求**验证码票据校验接口**发生异常时，客户服务端需做出相应的业务异常处理（例如跳过这次验证），保证不会因为接口返回结构异常，请求超时或服务未响应而阻碍业务流程。**如下为几种异常返回的情况，需要客户侧进行容灾。**
- 请求超时或服务未响应。
- 返回异常，Code为InternalError，接口返回举例如下：
```php
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "xxxxxxxxxxx"
    }
}
```
- 服务内部错误，CaptchaCode 为26，接口返回举例如下：
``` 
{
    "Response": {
        "CaptchaCode": 26,
        "CaptchaMsg": "system busy 详情请参考：腾讯云-天御验证码-产品文档，搜索关键字“DescribeCaptchaResult”，查看输出参数中CaptchaCode字段的具体描述",
        "EvilLevel": 0,
        "GetCaptchaTime": 0,
        "RequestId": "xxxxxxxxxxx"
    },
    "retcode": 0,
    "retmsg": "ok"
}
```

## 更多信息
您可以登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**，了解更多详细信息。
