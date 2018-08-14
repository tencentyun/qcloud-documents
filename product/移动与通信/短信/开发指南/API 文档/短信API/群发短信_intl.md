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
        For example: https://yun.tim.qq.com/v5/tlssmssvr/sendmultisms2?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
        Send notification or marketing SMS messages to a group of users.
		<br />
		This API is only available for bulk/single SMS messages to mobile phones in China (no more than 200 mobile numbers and 450 characters per time).
        <br />
        Note: Enter the applied SDKAppID as sdkappid, and a random number as random.
      </td>
    </tr>
  </tbody>
</table>

## 2 Request Packet
The packet is a JSON string with the following parameters:
```
{
    "tel": [
        {
            "nationcode": "86", //Country code
            "mobile": "13788888888" //Mobile number
        }, 
        {
            "nationcode": "86", //Country code
            "mobile": "13788888889" //Mobile number
        }
    ], 
    "type": 0, //0: common SMS; 1: marketing SMS (note: Enter the value as needed, otherwise the normal business will be affected)
    "msg": "Your verification code is 1234 ", //UTF8 encoding 
    "sig": "be66bb4aeb54701ed0637d0996a0b75111d5b8eda9b3a71bdc579a3d26f3edfb", //App credential. For more information on the calculation, please see the following
    "time": 1457336869, //UNIX timestamp, i.e. the time to initiate the request. A failure message will be returned if the time difference between the UNIX timestamp and the system time is greater than 10 minutes
    "extend": "", //The extended code of the channel (optional). Disabled by default. (A value must be specified.)
    //In the SMS reply scenario, the Tencent server returns it as is for developers to distinguish the specific reply type
    "ext": "" //User's session content (optional). The Tencent server returns it as is. You can leave it empty if it is not needed.
}
```
Note:   
1. A maximum of 200 mobile numbers are allowed per time for group messaging.  
2. The "msg" field must match the contents of the approved template.  
If the template is "Your verification code is {1}", the "msg" field can be "Your verification code is xxxx", where "xxxx" is the issued verification code.  
If you have multiple SMS signatures, place the needed SMS signature in the front of the message.      
For example, if you have two signatures of "[Tencent Technology]" and "[Tencent Cloud]", and you want to send an SMS message with "[Tencent Cloud]",  
the "msg" field can be "[Tencent Cloud]. Your verification code is xxxx", where "xxxx" is the issued verification code.  
3. To configure the "extend" field, [contact SMS Helper](/doc/product/382/3773).  
4. The "sig" field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile).  
The pseudo codes are as follows:
```
string strMobile = "13788888888,13788888889"; //The parameter value of tel's "mobile" field is separated with ","
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //The corresponding appkey of sdkappid, which must be kept confidential at the business side.
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //UNIX timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&mobile=13788888888,13788888889)
           = be66bb4aeb54701ed0637d0996a0b75111d5b8eda9b3a71bdc579a3d26f3edfb;
```

## 3 Response Packet
```
{
    "result": 0, //0: Successful. Other values: Failed (no detail list)
    "errmsg": "OK", //The specific error message when the "result" is not 0
    "ext": "", //User's session content. The Tencent server returns it as is.
    "detail": [
        {
            "result": 0, //0: Successful (the basis for billing). Other values: Failed
            "errmsg": "OK", //The specific error message when the "result" is not 0
            "mobile": "13788888888", //Mobile number
            "nationcode": "86", //Country code
            "sid": "xxxxxxx", //Indicate the ID of this delivery as well as an SMS delivery record
            "fee": 1 //Number of SMS messages billed
        }, 
        {
            "result": 0, //0: Successful (the basis for billing). Other values: Failed
            "errmsg": "OK", //The specific error message when the "result" is not 0
            "mobile": "13788888889", //Mobile number
            "nationcode": "86", //Country code
            "sid": "xxxxxxx", //Indicate the ID of this delivery as well as an SMS delivery record
            "fee": 1 //Number of SMS messages billed
        }
    ]
}
```
Note:  
[Billing](/document/product/382/18051)  
[Error Codes](/doc/product/382/3771)

## 4 SDK
We provide APIs of multiple platforms for developers to save the development time. Click [here](/doc/product/382/5804) to view details.
