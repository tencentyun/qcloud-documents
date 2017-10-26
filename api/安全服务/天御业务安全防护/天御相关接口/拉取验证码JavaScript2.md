## 1. 接口描述
 
域名：csec.api.qcloud.com
接口名: CaptchaQuery

获取验证码的JavaScript代码，通过JavaScript代码实现验证码的刷新和验证

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> accountType
</td><td> 可选
</td><td> UInt
</td><td>用户账号类型<br>0：其他账号<br>1：QQ开放帐号<br>2：微信开放帐号<br>4：手机账号<br>6：手机动态码<br>7：邮箱账号
</td></tr>
<tr>
<td> appId
</td><td> 可选
</td><td> string
</td><td> accountType是QQ或微信开放账号时，该参数必填，表示QQ或微信分配给给网站或应用的appId，用来唯一标识网站或应用
</td></tr>
<tr>
<td> uid
</td><td> 可选
</td><td> string
</td><td> 用户ID，accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
</td></tr>
<tr>
<td> associateAccount
</td><td> 可选
</td><td> string
</td><td> accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
</td></tr>
<tr>
<td> registerTime
</td><td> 必选
</td><td> UInt
</td><td> 注册时间戳，单位秒
</td></tr>
<tr>
<td> userIp <td> 必选 <td> String <td> 用户操作来源的外网IP
<tr>
<td> xForwardedFor
</td><td> 可选
</td><td> string
</td><td> 用户Http请求中的x_forward_for
</td></tr>
<tr>
<td> captchaType <td> 必选   <td> Int <td> 验证码图片的类型,参考验证码类型说明
<tr>
<td> script <td> 必选   <td> Int    <td> 1：直接返回JavaScript代码 <br>0：返回json数据，script字段的值是JavaScript代码
<tr>
<td> callBack <td> 可选   <td> String   <td> 当script为1的时候，接口错误的回调函数
<tr>
<td> macAddress
</td><td> 可选
</td><td> string
</td><td> mac地址或设备唯一标识
</td></tr>
<tr>
<td> imei
</td><td> 可选
</td><td> string
</td><td> 手机设备号
</td></tr>
<tr>
<td> businessId <td> 必选  <td> UInt <td> 业务ID，网站或应用在多个业务中使用此服务，通过此ID区分统计数据
<tr>
<td> sceneId <td> 可选   <td> UInt    <td> 场景ID，网站或应用的业务下有多个场景使用此服务，通过此ID区分统计数据
<tr>
</tbody></table>

## 3.验证码类型说明
验证码有以下8种类型，在接口中设置不同的参数值即可获得不同类型的验证码。
<table class="t">
<tbody><tr>
<th width="150"><b>验证码类型</b>
</th><th> <b>验证码样例</b>
</th><th> <b>说明</b>
</th></tr>
<tr>
<td> 1
</td><td> <img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/anquanAPIjieru_02.png" alt="anquanAPIjieru_02.png">
</td><td> 清晰4位字母
</td></tr>
<tr>
<td> 2
</td><td> <img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/anquanAPIjieru_03.png" alt="anquanAPIjieru_03.png">
</td><td> 清晰5位字母
</td></tr>
<tr>
<td> 3
</td><td> <img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/anquanAPIjieru_04.png" alt="anquanAPIjieru_04.png">
</td><td> 清晰6位字母
</td></tr>
<tr>
<td> 4
</td><td> 以上3中随机出现
</td><td> 清晰随机4~6位字母
</td></tr>
<tr>
<td> 5
</td><td> <img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/anquanAPIjieru_05.png" alt="anquanAPIjieru_05.png">
</td><td> 干扰4 位字母
</td></tr>
<tr>
<td> 6
</td><td> <img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/anquanAPIjieru_06.png" alt="anquanAPIjieru_06.png">
</td><td> 干扰5位字母
</td></tr>
<tr>
<td> 7
</td><td> <img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/anquanAPIjieru_07.png" alt="anquanAPIjieru_07.png">
</td><td> 干扰6位字母
</td></tr>
<tr>
<td> 8
</td><td> 以上3中随机出现
</td><td> 干扰随机4~6位字母
</td></tr></tbody></table>

## 4. 输出参数
<table class="t">
<tbody><tr>
<th width="100"> <b>参数名称</b>
</th><th width="100"> <b>类型</b>
</th><th width="300"> <b>描述</b>
</th></tr>
<tr>
<td> code       </td><td> Int    </td><td> 错误码, 0: 成功, 其他值: 失败
</td></tr>
<tr>
<td> message    </td><td> String </td><td> 错误信息
</td></tr>
<tr>
<td> script </td><td> String </td><td> 验证码功能的 JavaScript 代码
</td></tr></tbody></table>
说明: 
1) 参数 script=1 时, 接口直接返回 JavaScript 代码, script=0 时返回 Json 格式的字符串。 Javascript结构见实例输出。
2) JavaScript的使用参考验证码页面部署参考示例
3) 用户输入验证码后, 会返回一个ticket(票据)用于调用 CaptchaCheck 接口验证验证码的有效性
4) JavaScript代码有时效性，用户每次请求页面的时候需要重新拉取JavaScript。

## 5. 示例
输入

<pre>
https://domain/v2/index.php?Action=CaptchaQuery
 &userIp=121.14.96.121
 &businessId=1
 &captchaType=1
 &uid=1
 &script=1
 &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出

```
{
   "code" : 0,
   "message" : "No Error",
   "script" : 参考下面的JavaScript样例
}
```

## 6. JavaScript样例
![](//mccdn.qcloud.com/img5693ad9809b39.png)

## 7. JavaScript使用参考
![](//mccdn.qcloud.com/img5693adaad4352.png)

代码下载链接：http://url.cn/f5F9ix