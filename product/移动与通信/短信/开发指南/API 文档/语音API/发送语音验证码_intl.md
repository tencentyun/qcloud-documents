## Protocol Descriptions
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
		For example: https://yun.tim.qq.com/v5/tlsvoicesvr/sendvoice?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
		Send voice verification codes to domestic users (consisting of letters, numbers or a combination of both)
		<br />
		Note: Enter the applied SDKAppID as sdkappid, and a random number as random.
      </td>
    </tr>
  </tbody>
</table>

## Request Packet
The packet is a JSON string with the following parameters:
```
{
    "tel": {
        "nationcode": "86", //Country code
        "mobile": "13788888888" //Mobile number
    }, 
    "msg": "1234", //A verification code can contain letters, numbers or a combination of both. A voice prompt "Your verification code is" is added before the voice verification code when it is sent to a user.
    "playtimes": 2, //The number of playbacks (optional). Maximum is 3. Default is 2.
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4", //App credential. For more information on the calculation, please see the following
    "time": 1457336869, //UNIX timestamp, i.e. the time to initiate the request. A failure message will be returned if the time difference between the UNIX timestamp and the system time is greater than 10 minutes
    "ext": "" //User's session content (optional). The Tencent server returns it as is. You can leave it empty if it is not needed.
}
```
Note:  
1. The "sig" field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile).  
The pseudo codes are as follows:
```
string strMobile = "13788888888"; //Content of the mobile field of tel
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //The corresponding appkey of sdkappid, which must be kept confidential at the business side.
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //UNIX timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&mobile=13788888888)
           = ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4;
```

## Response Packet
```
{
    "result": 0, //0: Successful. Other values: Failed
    "errmsg": "OK", //The specific error message when the "result" is not 0
    "ext": "", //User's session content. The Tencent server returns it as is.
    "callid": "xxxx" //Indicate the ID of this delivery as well as a delivery record
}
```
