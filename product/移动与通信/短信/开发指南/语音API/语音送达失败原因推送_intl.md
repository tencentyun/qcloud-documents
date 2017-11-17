## Protocol Descriptions
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
		  For example: https://yun.tim.qq.com/voice/voicecallback
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
		   Send the reasons why it is unable to deliver the voice verification code or voice notification to the target mobile number.
      </td>
    </tr>
  </tbody>
</table>

## Request Packet
The packet is in JSON format with the following parameters:
```
{
    "voice_failure_callback": {
        "callid": "xxxxxx", //Indicate the ID of this delivery 
        "mobile": "13xxxxxxxxx", //Mobile number  
        "nationcode": "86", //Country code
        "call_from": "075583763333", //Calling number
        "failure_code": 8, //Error code
        "failure_reason": "Invalid number" //Reason of failure
    }
}
```

## Response Packet
When receiving a callback request, the third party needs to give a response to Tencent Cloud SMS service in the following format:
```
{ 
    "result": 0, //0: Successful. Other values: Failed
    "errmsg": "OK" //The specific error message when the "result" is not 0
}
```
