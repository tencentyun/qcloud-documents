## 1 Protocol Descriptions
<table style="display:table;width:100%">
  <tbody>
    <tr>
      <td style="width:15%;">
        Protocol
      </td>
      <td>
        HTTP POST/GET/JSON
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
		For example: https://yun.tim.qq.com/sms/smscallback
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
		After a user receives an SMS message and replies to it, Tencent Cloud SMS service notifies the business side of the SMS reply by calling back the service URL.
      </td>
    </tr>
  </tbody>
</table>

## 2 Request Packet
The packet is in JSON format with the following parameters:
```
{
    "nationcode": "86", //Country code
    "mobile": "13xxxxxxxxx", //Mobile number
    "text": "User's reply",
    "sign": "SMS signature",
    "time": 1457336869, //UNIX timestamp
    "extend": "Extended code" //The extended code of the channel (optional). If the "extend" field is specified in the API for sending SMS messages, 
			//when a user replies to an SMS message, Tencent server returns it as is for developers to distinguish the specific reply type.
}
```

## 3 Response Packet
When receiving a callback request, the third party needs to give a response to Tencent Cloud SMS service in the following format:
```
{ 
    "result": 0, //0: Successful. Other values: Failed
    "errmsg": "OK" //The specific error message when the "result" is not 0
}
```
