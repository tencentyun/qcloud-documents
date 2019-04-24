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
		   语音验证码下发给用户后，腾讯云短信服务可以通过回调业务url的方式，通知业务方语音验证码下发的状态。
      </td>
    </tr>
  </tbody>
</table>

## 请求包体
Json格式时，参数如下：
```
{
    "voicecode_callback": {
        "result": "0", //0:用户正常接听 1:用户未接听 2:呼叫异常
        "callid": "xxxxxx", //标识本次发送id
        "mobile": "13xxxxxxxxx", //手机号码
        "nationcode": "86", //国家码
        "call_from": "075583763333", //呼入号码
        "start_calltime": "1470196821", //开始发起语音验证呼叫时间
        "end_calltime": "1470196843", //结束语音验证呼叫时间
        "accept_time": "1470196835", //用户接听时间
        "fee": "1" //计费时长，分钟
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