## 1 协议说明
<table style="display:table;width:100%">
  <tbody>
    <tr>
      <td style="width:15%;">
        协议
      </td>
      <td>
        HTTP POST/GET/JSON
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
		用户向腾讯提交上行短信，腾讯云短信服务可以通过回调业务url的方式，通知业务方用户发送的短信内容。
      </td>
    </tr>
  </tbody>
</table>

## 2 请求包体
Json格式时，参数如下：
```
{
    "mobile": "13xxxxxxxxx", 
    "time": 1457336869, //unix时间戳
    "text": "用户回复的内容"，
    "port": "106901333914",
    "extend": "扩展码" //可选字段，通道扩展码，在发送短信的接口中，如果填写了"extend"字段，
			//在短信回复时，腾讯server会原样返回，开发者可依此区分是哪种类型的回复
}
```

## 3 应答包体
第三方业务收到回调请求下，需要按以下的格式给腾讯云短信业务应答
```
{ 
    "result": 0, //0表示成功，非0表示失败
    "errmsg": "OK" //result非0时的具体错误信息
}
```