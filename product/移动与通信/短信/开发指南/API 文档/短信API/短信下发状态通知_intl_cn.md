## 1 协议说明
<table style="display:table;width:100%">
  <tbody>
    <tr>
      <td style="width:15%;">
        协议
      </td>
      <td>
        HTTP JSON
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
		举例：https://yun.tim.qq.com/sms/smscallback
      </td>
    </tr>
    <tr>
      <td>
        接口说明
      </td>
      <td>
		短信下发给用户后，腾讯云短信服务可以通过回调业务url的方式，通知业务方短信下发的状态。
      </td>
    </tr>
  </tbody>
</table>

## 2	请求包体
Json格式时，参数如下：
```
[
    {
        "user_receive_time": "2015-10-17 08:03:04", //用户实际接收到短信的时间
        "nationcode": "86", //国家码
        "mobile": "13xxxxxxxxx", //手机号码
        "report_status": "SUCCESS", //实际是否收到短信接收状态。SUCCESS（成功）、FAIL（失败）
        "errmsg": "DELIVRD", //用户接收短信状态码
        "description": "用户短信送达成功", //用户接收短信状态描述
        "sid": "xxxxxxx" //标识本次发送id
    }, 
    { }…
]
```
注：  
1、一次回调请求里可能有多次的短信请求结果  
2、"errmsg"详见[状态回执错误码](/doc/product/382/3771#2-.E7.8A.B6.E6.80.81.E5.9B.9E.E6.89.A7.E9.94.99.E8.AF.AF.E7.A0.81)说明

## 3 应答包体
第三方业务收到回调请求下，需要按以下的格式给腾讯云短信业务应答
```
{ 
    "result": 0, //0表示成功，非0表示失败
    "errmsg": "OK" //result非0时的具体错误信息
}
```