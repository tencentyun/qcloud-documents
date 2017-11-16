## Rest API接口说明

Rest API 是一种灵活、安全、通用的接入解决方案，同时 Rest API 写一个是简单，请求 body 信息直观，业务可以快速完成功能集成，实现产品上线。小微客服机器人 Rest 请求格式如下所示：
```
https://yun.tim.qq.com/v3/prophet/$command?appid=$appid&sdkappid=$sdkappid&identifier=$identifier&usersig=$usersig&random=999999&contenttype=json
``` 
(如无特别注明，都使用该 URL 格式)

## 字段说明
| 字段名称 | 字段说明 | 
|---------|---------|
| v3 | 协议版本号 | 	
|command|	命令字，与 servicename 组合用来标识具体的业务功能。|
|appid|	用户的 appid 信息，在页面中可以获取。|
|sdkappid|	业务 sdkappid，用户开通业务时获取到的信息。|
|identifier|	用户名，为第三方用户帐号 ID 信息。|
|usersig	|用户名对应的签名，第三方后台使用腾讯工具结合用户 identifier 信息生成生成。生成方法详情见附件1。|
|random	|标识当前请求的整数随机数参数。|

示例图：
![](//mc.qcloudimg.com/static/img/fb90d7986993e0469a181bf2693bc00f/image.png)

### 帐号登录
usersig 字段使用登录服务(Tencent Login Service，TLS)生成，TLS 是腾讯为开发者快速完成帐号集成接入云通讯服务而提供的一套通用帐号登录组件。实现包括QQ、微信、新浪微博、人人在内的多种帐号类型登录校验功能。开发者可以通过简单工具集成，或便捷的接口调用，即可实现原本复杂的登录验证服务，使代码量急剧减少。



