## 1 Protocol Descriptions
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
        For example: https://yun.tim.qq.com/v5/tlssmssvr/pullstatus4mobile?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
		Pull the SMS status of a mobile phone, such as SMS delivery status and SMS reply.
		<br />
		Note: Enter the applied SDKAppID as sdkappid, and a random number as random.
      </td>
    </tr>
  </tbody>
</table>

## 2 Request Packet
```
{
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df", //App credential. For more information on the calculation, please see the following
    "time": 1457336869, //UNIX timestamp, i.e. the time to initiate the request. A failure message will be returned if the time difference between the UNIX timestamp and the system time is greater than 10 minutes
    "type": 1, //0: SMS delivery status. 1: SMS reply
    "max": 10, //The maximum number of entries. The maximum: 100
    "begin_time": 1464624000, //UNIX timestamp. The time to start pulling
    "end_time": 1464706800, //UNIX timestamp. The time to end pulling
    "nationcode": "86", //Country code
    "mobile": "13788888888" //Mobile number
}
```
Note:  
The "sig" field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time).
The pseudo codes are as follows:
```
string strAppkey = "5f03a35d00ee52a21327ab048186a2c4"; //The corresponding appkey of sdkappid, which must be kept confidential at the business side.
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //UNIX timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869)
           = c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df;
```

## 3 Response Packet
```
{
    "result": 0, //0: Successful. Other values: Failed
    "errmsg": "ok", //The specific error message when the "result" is not 0
    "count": 3, //The number of returned information entries. It is valid when "result" is 0
    "data": [... //For more information, please see the following
    ]
}
```
Notes:  
If the request type is 0, the content of the "data" field is same as [SMS Delivery Status Notification](/doc/product/382/5807)  
If the request type is 1, the content of the "data" field is same as [SMS Reply](/doc/product/382/5809)
