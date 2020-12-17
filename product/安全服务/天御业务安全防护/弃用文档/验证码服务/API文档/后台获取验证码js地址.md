## 1.接口描述
协议：HTTPS 
域名：csec.api.qcloud.com 
接口名: CaptchaIframeQuery  
获取验证码的 JavaScript 连接，通过将验证码的 JavaScript 嵌入页面实现验证码的刷新和验证操作。

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 页面。<br> 其中，此接口的 Action 字段为 CaptchaIframeQuery。

| 参数        | 是否必选 | 类型 | 描述                                   |
| ---------------- | -------- | ------ | ---------------------------------------- |
| captchaType      | 是       | UInt   | [验证码类型](https://cloud.tencent.com/doc/product/295/6622#2.-.E5.A4.A9.E5.BE.A1.E9.AA.8C.E8.AF.81.E7.A0.81.E7.B1.BB.E5.9E.8B) |
| disturbLevel     | 是       | UInt   | [验证码干扰程度](https://cloud.tencent.com/document/product/295/6622#2.2-.E9.AA.8C.E8.AF.81.E7.A0.81.E5.8F.82.E6.95.B0) |
| isHttps          | 是       | UInt   | 返回的 JavaScript 中是否使用 HTTPS<br/>1：HTTPS   |
| clientType       | 是       | UInt   | 客户端类型<br/>1：手机 Web 页面<br/>2：PCWeb 页面<br/>4：App          |
| accountType      | 是       | UInt   | 用户账号类型<br/>0：其他账号<br/>1：QQ 开放帐号<br/>2：微信开放帐号 <br/>4：手机账号<br/>6：手机动态码<br/>7：邮箱账号 |
| appId            | 是       | String | accountType 是 QQ 或微信开放账号时，表示 QQ 或微信分配给给网站或应用的appId，用来唯一标识网站或应用 |
|                  |          |        |                                          |
| uid              | 建议       | String | 不同的用户 IDaccountType 对应不同的用户 ID。如果是 QQ 或微信用户则填入对应的 openId |
| businessId       | 建议       | UInt   | 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据        |
| registerTime     | 否       | UInt   | 注册时间戳，单位秒                                |
|                  |          |        |                                          |
| userIp           | 否       | String | 用户操作来源的外网 IP                              |
| xForwardedFor    | 否       | String | 用户 HTTP 请求中的 x_forward_for                  |
| macAddress       | 否       | String | Mac 地址或设备唯一标识                             |
| imei             | 否       | String | 手机设备号                                    |
| associateAccount | 否       | String | accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID |
| sceneId          | 否       | UInt   | 场景 ID 网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据     |

## 3.输出参数
| 参数名称 | 类型 | 描述                                  |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败<br/>详情请参见错误码页面的 [公共错误码](https://cloud.tencent.com/document/product/295/7285) |
| codeDesc | String | 业务侧错误码<br/>成功：返回 Success<br/>错误：返回具体业务错误原因       |
| message  | String | 模块错误信息描述，与接口相关                           |
| url      | String | 验证码 JavaScript 地址，该链接单次有效                  |

## 4.示例代码
代码下载： [java](https://mc.qcloudimg.com/static/archive/91612588f14dd8632dbb044d4a62061c/captcha_iframe_java%281%29.zip)、[php](https://mc.qcloudimg.com/static/archive/81a341051425904e44540a986f1a44a6/captcha_iframe_php.zip) 、[Python ](https://mc.qcloudimg.com/static/archive/caec2d56c3e4560eda138426bfd36492/captcha_iframe_python.zip)

 一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 小节。
```
请求示例 ：
https://csec.api.qcloud.com/v2/index.php?Action=CaptchaIframeQuery
&<公共请求参数>
&secretId=AKID*********2iBS8s2DCzazCD2g7OUq4Zw
&captchaType=1
&disturbLevel=1
&isHttps=1
&clientType=1
```
## 5.响应示例
```
{
"code":0,
"message":"No Error",
"url":"https://captcha.guard.qcloud.com/template/TCapIframeApi.js?appid=1251001047&clientype=1&lang=2052&asig=-DhJtUkDwLzJpmIfAmasXFn1Y6zCkRQUn8WERrs4lVNmUDcuoDiYYLmoKqd-Ev77Eogpq97Dpb69_MrwGjWXKmTGg9y9iW7wjdriTu_y6WBN4qGsHn6VRk0W1hLB6ZWvqHqw2E5IFCRUcGrHBzMF7A**"
}
```

