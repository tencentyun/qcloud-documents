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
    "sign": "腾讯云", //短信签名，如果使用默认签名，该字段可缺省
    "tpl_id": 19, //业务在控制台审核通过的模板ID
     //假定这个模板为：您的{1}是{2}，请于{3}分钟内填写。如非本人操作，请忽略本短信。
    "params": [
        "验证码", 
        "1234", 
        "4"
    ], //参数，分别对应上面假定模板的{1}，{2}，{3}
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4", //app凭证，具体计算方式见下注
    "time": 1457336869, //unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会返回失败
    "extend": "", //通道扩展码，可选字段，默认没有开通(需要填空)。
    //在短信回复场景中，腾讯server会原样返回，开发者可依此区分是哪种类型的回复
    "ext": "" //用户的session内容，腾讯server回包中会原样返回，可选字段，不需要就填空。
}
```
注：  
1、"tpl_id"字段需填写审核通过的模板ID ，上面的请求参数组合后下发的内容为：  
"【腾讯云】您的验证码是1234，请于4分钟内填写。如非本人操作，请忽略本短信。"   
如果您有多个短信签名，请将需要的短信签名填入"sign"字段  
例如您有"【腾讯科技】"，"【腾讯云】"两个签名，但是想以"【腾讯云】"签名发送短信，则"sign"字段可赋值为："腾讯云"    
2、"extend"字段的配置请联系[腾讯云短信技术支持](/doc/product/382/3773)  
3、[sendisms](/document/product/382/8717)接口，"tel"字段为国际电话号码通用格式，如："+8613788888888"  
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