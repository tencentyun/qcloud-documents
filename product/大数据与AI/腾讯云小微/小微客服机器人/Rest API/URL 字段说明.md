### 请求 URL 字段说明
Rest API 是一种灵活、安全、通用的接入解决方案，同时 Rest API 读写简单，请求 body 信息直观，业务可以快速完成功能集成，实现产品上线。小微客服机器人 Rest 请求格式如下所示：  

<pre>
https://yun.tim.qq.com/v3/prophet/$command?
appid=$appid
&sdkappid=$sdkappid
&identifier=$identifier
&usersig=$usersig
&random=999999
&contenttype=json
</pre>

字段详细说明如下：

|字段名称|	描述|
|-----|--------|
|v3	|协议版本号|
|command	|命令字，与 servicename 组合用来标识具体的业务功能|
|appid	|用户的 APPID 信息，在控制台中可以获取。|
|sdkappid	|业务 SDK_ID，用户开通业务时获取到的信息。|
|identifier	|用户名，为第三方用户帐号 ID 信息, 需要管理员权限的操作必须填管理员。|
|usersig	|用户名对应的签名，第三方后台使用腾讯工具结合用户 identifier 信息生成。 |
|random	|标识当前请求的整数随机数参数。|

### AppID 获取方式
如果您还没有腾讯云账号，您需要先注册腾讯云账号；
如果您已有腾讯云账号，登录腾讯云小微机器人控制台就能看到 AppID 信息和业务 SDK_ID 信息了。
![](//mc.qcloudimg.com/static/img/49f6d25112eacb7373a1f850629a4ec1/image.png)
