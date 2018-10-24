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
       举例：https://yun.tim.qq.com/v5/tlssmssvr/mod_sign?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        接口说明
      </td>
      <td>
      修改短信签名
		<br />
		注：sdkappid请填写您在腾讯云上申请到的，random请填成随机数。
      </td>
    </tr>
  </tbody>
</table>

## 2	请求包体
```
{
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df", //app凭证，具体计算方式见下注
    "time": 1457336869, //unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会返回失败
    "remark": "xxxxx", //新的签名备注，比如申请原因，使用场景等，可选字段
    "text": "xxxxx", //新的签名内容，不带【】，例如：改为【腾讯科技】这个签名，这里填"腾讯科技"
    "sign_id": 123 //待修改的签名对应的签名id
    "pic":"xxxxx" //请把签名内容相关的证件截图base64格式字符串添到该字段，可选择字段。base64格式工具:http://base64.xpcha.com/indexie.php 
}
```
注：  
"sig"字段根据公式sha256(appkey=$appkey&random=$random&time=$time)生成
伪代码如下：
```
string strAppkey = "5f03a35d00ee52a21327ab048186a2c4"; //sdkappid对应的appkey，需要业务方高度保密
string strRand = "7226249334"; //url中的random字段的值
string strTime = "1457336869"; //unix时间戳
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869)
           = c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df;
```

## 3 应答包体
```
{
    "result": 0, //0表示成功，非0表示失败
    "msg": "", //result非0时的具体错误信息
    "data": {
        "id": 123, //签名id
        "text": "xxxxx", //签名内容
        "status": 1, //0：已通过；1：待审核；2：已拒绝
    }
}
```