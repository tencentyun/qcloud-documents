## 1 Protocol Descriptions
<table style="display:table;width:100%">
  <tbody>
    <tr>
      <td style="width:15%;">
        Protocol
      </td>
      <td>
        HTTP JSON
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
		After an SMS is sent to a user, Tencent Cloud SMS service notifies the business side of the delivery status of the SMS by calling back the service URL.
      </td>
    </tr>
  </tbody>
</table>

## 2 Request Packet
The packet is in JSON format with the following parameters:
```
[
    {
        "user_receive_time": "2015-10-17 08:03:04", //The time the user actually received the message
        "nationcode": "86", //Country code
        "mobile": "13xxxxxxxxx", //Mobile number
        "report_status": "SUCCESS", //The actual SMS receiving status. SUCCESS: successful, FAIL: failed
        "errmsg": "DELIVRD", //Code that defines the SMS receiving status
        "description": "The SMS message is successfully sent ", //Description of the SMS receiving status
        "sid": "xxxxxxx" //Indicate the ID of this delivery
    }, 
    { }…
]
```
Notes:  
1. A callback request may have results of multiple SMS requests returned.  
2. For more information on "errmsg", see [Error Codes for Status Report](/doc/product/382/3771).

## 3 Response Packet
When receiving a callback request, the third party needs to give a response to Tencent Cloud SMS service in the following format:
```
{ 
    "result": 0, //0: Successful. Other values: Failed
    "errmsg": "OK" //The specific error message when the "result" is not 0
}
```
