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
		举例：https://yun.tim.qq.com/v5/tlssmssvr/pullstatus?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        接口说明
      </td>
      <td>
		拉取短信状态（下发状态，短信回复等）。
		<br />
		拉取过的内容不会再重复返回，可以理解为消息队列机制。
		<br />
        此功能需要联系<a href="/doc/product/382/3773">sms helper</a>开通。
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
    "time": 1457336869, //unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会拉取失败
    "type": 1, //0 1分别代表 短信下发状态，短信回复
    "max": 10 //最大条数 最多100
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
    "errmsg": "ok", //result非0时的具体错误信息
    "count": 3, //result为0时有效，返回的信息条数
    "data": [... //具体内容见下注
    ]
}
```
注：  
请求type 0时 data字段内容同[短信下发状态通知](/doc/product/382/5807)  
请求type 1时 data字段内容同[短信回复](/doc/product/382/5809)