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
        举例：https://yun.tim.qq.com/v5/tlssmssvr/querysms4mobile?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        接口说明
      </td>
      <td>
		拉取单个手机的短信下发记录。
		<br />
		注：sdkappid请填写您在腾讯云上申请到的，random请填成随机数。
      </td>
    </tr>
  </tbody>
</table>

## 2	请求包体
```
{
    "sig": "30db206bfd3fea7ef0db929998642c8ea54cc7042a779c5a0d9897358f6e9505", //app凭证，具体计算方式见下注
    "time": 1457336869, //unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会拉取失败
    "nationcode": "86", //国家码
    "mobile": "13788888888", //手机号码
    "begin_time": 1486396800, //unix时间戳，需要拉取的起始时间
    "end_time": 1486483200 //unix时间戳，需要拉取的截止时间
}
```
注：  
"sig"字段根据公式sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile)生成 
伪代码如下：
```
string strMobile = "13788888888"; //tel的mobile字段的内容
string strAppKey = "dffdfd6029698a5fdf4"; //sdkappid对应的appkey，需要业务方高度保密
string strRand = "7226249334"; //url中的random字段的值
string strTime = "1457336869"; //unix时间戳
string sig = sha256(appkey=$strAppKey&random=$strRand&time=$strTime&mobile=$strMobile);
```

## 3 应答包体
```
{
    "result": 0, //0表示成功，非0表示失败
    "errmsg": "OK", //result非0时的具体错误信息
    "real_count": 2, //实际查询到的结果数，当结果数超过100条时，data里面返回前100条并且truncated会被设置为1
    "truncated": 0, //0表示未截断，1表示截断
    "data": [
        {
            "nationcode": "86", //国家码
            "mobile": "13788888888", //手机号码
            "sign": "腾讯科技", //短信签名
            "text": "【腾讯科技】测试验证码1**4", //短信内容，超过100个字符的部分会用...替代
            "send_time": "2017-01-04 20:02:44", //短信下发的时间
            "type": 0, //0:普通短信;1:营销短信
            "result": 0, //下发结果，0表示成功(计费依据)，非0表示失败
            "errmsg": "OK", //result非0时的具体错误信息
            "sid": "8:aIt9bcbZHdse7kBZuqi20170104", //发送id，标识一次短信下发记录
            "user_receive_time": "2017-01-04 20:02:46", //用户实际接收到短信的时间
            "report_status": "SUCCESS", //实际是否收到短信接收状态。SUCCESS（成功）、FAIL（失败）
            "status": "DELIVRD", //用户接收短信状态码
            "description": "用户短信接收成功" //用户接收短信状态描述
        }, 
        {
            "nationcode": "86", //国家码
            "mobile": "13788888888", //手机号码
            "sign": "腾讯科技", //短信签名
            "text": "【腾讯科技】测试验证码2**4", //短信内容，超过100个字符的部分会用...替代
            "send_time": "2017-01-04 20:02:50", //短信下发的时间
            "type": 1, //0:普通短信;1:营销短信
            "result": 1008, //下发结果，0表示成功(计费依据)，非0表示失败
            "errmsg": "请求下发短信/语音超时。" //result非0时的具体错误信息
        }
    ]
}
```
注：  
result非0的时候表示下发失败，此时无"sid"，"user_receive_time"，"report_status"，"status"，"description"这些字段
