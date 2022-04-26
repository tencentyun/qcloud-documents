## 业务请求流程
验证码请求流程涉及客户网站客户端（前端）、客户网站后端、验证码 Captcha 服务端三端交互。以用户登录时调用验证码服务为例，请求流程图如下：
![](https://qcloudimg.tencent-cloud.cn/raw/1d3e8bf833d685eec0183a4079429006.png)
为保障验证码 Captacha 服务端异常时不阻塞客户网站正常业务流程，针对以上三次请求（加载 TCaptcha.js、交互验证、票据校验），提供验证码业务容灾方案如下。
> !容灾方案中生成的所有容灾票据，在请求后端票据校验时，均不会产生计费。

## 加载 TCaptcha.js 请求容灾方案
在 html 中引入验证码 TCaptcha.js 文件时，建议参考如下示例进行方式接入。
1. 定义错误处理函数
``` javascript
// 在脚本加载或初始化错误时 需手动绑定button元素的事件确保流程正常
// 函数定义需在script加载前
function TCaptchaLoadError(){
  // CaptchaAppId   String  验证码应用ID，登录验证码控制台，在验证列表的【密钥】列，即可查看到CaptchaAppId
  var CaptchaAppId=''
  document.getElementById('TencentCaptcha').addEventListener('click', function () {
    var CaptchaAppId = ''
    /* 生成票据或自行做其它处理 */
    var ticket = 'terror_1001_' + CaptchaAppId + '_' + Math.floor(new Date().getTime()/1000)
    window.callback({
      ret: 0,
      randstr: '@'+Math.random().toString(36).substr(2),
     ticket: ticket,
      errorCode: 1001,
      errorMessage: 'jsload_error'
    })
  }, false)
}
```
2. 在 html 中加入以下代码引入验证 JS 文件。
``` javascript
<!-- 如果script是在head中引入 onerror的函数需等domready再绑定元素事件 在body中加载无需等待 -->
<script src="https://ssl.captcha.qq.com/TCaptcha.js" onerror="TCaptchaLoadError()"></script>
```

基于以上步骤接入后，如果加载 TCaptcha.js 时出现异常，将会自动生成 `terror_1001` 格式的容灾票据（防止无法生成票据导致后端票据校验流程阻塞）。

## 交互验证请求容灾方案
用户与验证码交互时，验证码会调用业务传入的回调函数， 并在第一个参数中传入回调结果。

#### 结果字段说明

| 字段名       | 值类型 | 说明                                                       |
| :----------- | ------ | ---------------------------------------------------------- |
| ret          | Int    | 验证结果。0：验证成功；2：用户主动关闭验证码。             |
| ticket       | String | 验证成功的票据，当且仅当 ret = 0 时 ticket 有值。          |
| CaptchaAppId | String | 验证码应用 ID。                                            |
| bizState     | Any    | 自定义透传参数。                                           |
| randstr      | String | 本次验证的随机串，请求后台接口时需带上。                   |
| errorCode    | Number | 错误 code，详情请参见 [回调函数 errorCode 说明](#errCode)。|
| errorMessage | String | 错误信息。                                                  |

#### 回调函数 errorCode 说明[](id:errCode)

| errorCode | 说明                    |
| :-------- | ----------------------- |
| 1001      | TCaptcha.js 加载错误    |
| 1002      | 调用 show 方法超时      |
| 1003      | 中间 js 加载超时        |
| 1004      | 中间 js 加载错误        |
| 1005      | 中间 js 运行错误        |
| 1006      | 拉取验证码配置错误/超时 |
| 1007      | iframe 加载超时         |
| 1008      | iframe 加载错误         |
| 1009      | jquery 加载错误         |
| 1010      | 滑块 js 加载错误        |
| 1011      | 滑块 js 运行错误        |
| 1012      | 刷新连续错误3次         |
| 1013      | 验证网络连续错误3次     |
> !为保障不阻塞后端票据校验流程，当验证码服务端出现异常时，会命中容灾逻辑，回调结果中 ticket 字段将自动返回 `terror_` 前缀的票据。

#### 交互验证请求发生异常时回调返回结果示例
```json
{
    "bizState": "data-biz-state",
    "appid": "123456",
    "ret": 0,
    "randstr": "@bwvwg7d4e3q",
    "ticket": "terror_1006_2031483705_1649302812",
    "errorCode": 1006,
    "errorMessage": "get_captcha_config_request_error"
}
```

#### 自定义容灾示例
正常情况，配置交互验证容灾时，直接带着回调函数生成的容灾票据进行后端票据校验即可，但如果需要自定义容灾方案（例如跳过这次验证，不进行后台校验），则可根据 errorCode 的不同值定义不同的容灾处理。

在回调函数中，根据 ticket 和 errorCode 自定义容灾处理如下所示：
``` 
window.callback = function(res){
	if (res.ticket){
    	//上传票据 可根据errorCode和errorMessage做特殊处理或统计
		if(res.errorCode === xxxxx){
       	//自定义容灾逻辑（例如跳过这次验证，不进行后台校验）
		}
  	}
}
```


## 票据校验容灾方案
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
