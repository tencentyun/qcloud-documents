## 1 协议说明
<table style="display:table;width:100%">
  <tbody>
    <tr>
      <td style="width:15%;">
        协议
      </td>
      <td>
        HTTP POST
        <br />
      </td>
    </tr>
    <tr>
      <td>
        编码格式
      </td>
      <td>
        UTF8
      </td>
    </tr>
    <tr>
      <td>
        URL
      </td>
      <td>
        举例：https://yun.tim.qq.com/v5/tlssmssvr/sendsms?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        接口说明
      </td>
      <td>
        给用户发短信验证码、短信通知，营销短信（内容长度不超过450字）。
        <br />
        注：sdkappid请填写您在腾讯云上申请到的，random请填成随机数。
      </td>
    </tr>
  </tbody>
</table>

## 	2	请求包体
包体为json字符串，参数如下：
```
{
    "tel": { //如需使用国际电话号码通用格式，如："+8613788888888" ，请使用sendisms接口见下注
        "nationcode": "86", //国家码
        "mobile": "13788888888" //手机号码
    }, 
    "type": 0, //0:普通短信;1:营销短信（强调：要按需填值，不然会影响到业务的正常使用）
    "msg": "你的验证码是1234", //utf8编码 
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4", //app凭证，具体计算方式见下注
    "time": 1457336869, //unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会返回失败
    "extend": "", //通道扩展码，可选字段，默认没有开通(需要填空)。
     //在短信回复场景中，腾讯server会原样返回，开发者可依此区分是哪种类型的回复
    "ext": "" //用户的session内容，腾讯server回包中会原样返回，可选字段，不需要就填空。
}
```
注：  
1、"msg"字段需要匹配审核通过的模板内容  
如果您的模板是"你的验证码是{1}"，则"msg"字段可赋值为："你的验证码是xxxx"。（其中"xxxx"为下发的验证码）  
如果您有多个短信签名，请将需要的短信签名放在短信内容前面  
例如您有"【腾讯科技】"，"【腾讯云】"两个签名，但是想以"【腾讯云】"签名发送短信，  
则"msg"字段可赋值为："【腾讯云】你的验证码是xxxx"。（其中"xxxx"为下发的验证码）  
2、"extend"字段的配置请联系[腾讯云短信技术支持](/doc/product/382/3773)  
3、[sendisms](/document/product/382/8716)接口，"tel"字段为国际电话号码通用格式，如："+8613788888888"  
4、"sig"字段根据公式sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile)生成 
伪代码如下：
```
string strMobile = "13788888888"; //tel的mobile字段的内容
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //sdkappid对应的appkey，需要业务方高度保密
string strRand = "7226249334"; //url中的random字段的值
string strTime = "1457336869"; //unix时间戳
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&mobile=13788888888)
           = ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4;
```

## 3	应答包体
```
{
    "result": 0, //0表示成功(计费依据)，非0表示失败
    "errmsg": "OK", //result非0时的具体错误信息
    "ext": "", //用户的session内容，腾讯server回包中会原样返回
    "sid": "xxxxxxx", //标识本次发送id，标识一次短信下发记录
    "fee": 1 //短信计费的条数
}
```
注：  
["fee"字段计费说明](/doc/product/382/3772#2-.E7.9F.AD.E4.BF.A1.E9.95.BF.E5.BA.A6)  
[result对应的错误码](/doc/product/382/3771)

## 4 SDK
我们为开发者封装了多个平台的 API 供开发者直接使用，以节省开发时间，点击[这里](/doc/product/382/5804)查看。