## 协议说明
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
        举例：https://yun.tim.qq.com/v5/tlsvoicesvr/sendvoiceprompt?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        接口说明
      </td>
      <td>
      给国内用户发语音通知（支持中文、英文字母、数字及组合，内容长度不超过100字）。
		<br />
		注：sdkappid请填写您在腾讯云上申请到的，random请填成随机数。
      </td>
    </tr>
  </tbody>
</table>

## 请求包体
包体为json字符串，参数如下：
```
{
    "tel": {
        "nationcode": "86", //国家码
        "mobile": "13788888888" //手机号码
    }, 
    "prompttype": 2, //语音类型，目前固定为2
    "promptfile": "语音内容文本", //通知内容，utf8编码，支持中文英文、数字及组合，需要和语音内容模版相匹配
    "playtimes": 2, //播放次数，可选，最多3次，默认2次
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4", //app凭证，具体计算方式见下注
    "time": 1457336869, //unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会返回失败
    "ext": "" //用户的session内容，腾讯server回包中会原样返回，可选字段，不需要就填空。
}
```
注：  
1、"sig"字段根据公式sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile)生成  
伪代码如下：
```
string strMobile = "13788888888"; //tel的mobile字段的内容
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //sdkappid对应的appkey，需要业务方高度保密
string strRand = "7226249334"; //url中的random字段的值
string strTime = "1457336869"; //unix时间戳
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&mobile=13788888888)
           = ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4;
```

## 应答包体
```
{
    "result": 0, //0表示成功，非0表示失败
    "errmsg": "OK", //result非0时的具体错误信息
    "ext": "", //用户的session内容，腾讯server回包中会原样返回
    "callid": "xxxx" //标识本次发送id，标识一次下发记录
}
```