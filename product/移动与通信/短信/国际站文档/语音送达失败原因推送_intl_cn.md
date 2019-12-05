## 协议说明
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
		  举例：https://yun.tim.qq.com/voice/voicecallback
      </td>
    </tr>
    <tr>
      <td>
        接口说明
      </td>
      <td>
		   对语音验证码、语音通知下发失败的号码推送下发失败的原因。
      </td>
    </tr>
  </tbody>
</table>

## 请求包体
Json格式时，参数如下：
```
{
    "voice_failure_callback": {
        "callid": "xxxxxx", //标识本次发送id 
        "mobile": "13xxxxxxxxx", //手机号码  
        "nationcode": "86", //国家码
        "call_from": "075583763333", //呼入号码
        "failure_code": 8, //失败错误码
        "failure_reason": "空号" //失败原因
    }
}
```

## 应答包体
第三方业务收到回调请求下，需要按以下的格式给腾讯云短信业务应答
```
{ 
    "result": 0, //0表示成功，非0表示失败
    "errmsg": "OK" //result非0时的具体错误信息
}
```