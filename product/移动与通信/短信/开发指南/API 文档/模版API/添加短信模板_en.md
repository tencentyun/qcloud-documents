## 1 Protocol Description
<table style="display:table;width:100%">
  <tbody>
    <tr>
      <td style="width:15%;">
        Protocol
      </td>
      <td>
        HTTP POST
        <br />
      </td>
    </tr>
    <tr>
      <td>
        Encoding format
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
       For example: https://yun.tim.qq.com/v5/tlssmssvr/add_template?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
      This API is used to add SMS text message (or voice message) templates.
		<br />
		Note: Replace "sdkappid" with the one you applied for on Tencent Cloud, and replace "random" with a random number.
      </td>
    </tr>
  </tbody>
</table>

## 2 Request Packet
```
{
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df", //app credential. For more information on how to calculate, please see below.
    "time": 1457336869, //The time at which the request is initiated. It is expressed as a Unix timestamp. A failure message is returned if the time difference between the Unix timestamp and the system time is greater than 10 minutes.
    "title": "xxxxx", //Template name (optional)
    "remark": "xxxxx", //Remarks for template, such as reason for application and usage scenarios. This field is optional.
    "text": "xxxxx", //Template content
    "type": 0 //0: general SMS message template; 1: marketing SMS message template; 2: SMS voice message template
}
```
Note:  
The "sig" field is generated based on the formula sha256(appkey=$appkey&random=$random&time=$time)
The pseudo code is as follows:
```
string strAppkey = "5f03a35d00ee52a21327ab048186a2c4"; //The appkey for the sdkappid, which must be kept confidential
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //The Unix timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869)
           = c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df;
```

## 3 Response Packet
```
{
    "result": 0, //0: Successful, Other values: Failed
    "msg": "", //The error message returned when "result" is not 0
    "data": {
        "id": 123, //Template ID
        "text": "xxxxx", //Template content
        "status": 1, //0: Approved; 1: Pending; 2: Rejected
        "type": 0 //0: general SMS message template; 1: marketing SMS message template; 2: SMS voice message template
    }
}
```
