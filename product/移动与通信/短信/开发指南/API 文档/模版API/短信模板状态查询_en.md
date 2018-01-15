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
       For example: https://yun.tim.qq.com/v5/tlssmssvr/get_template?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
      Query the status of the applied text SMS (or voice SMS) templates
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
    "tpl_id": [123, 124,...], //Query the ID of the specified template. It cannot appear together with the "tpl_page" field
    "tpl_page": //Query the information of all templates in pages. It cannot appear together with the "tpl_id" field. (The "total" field in the response package indicates the total number of templates)
        {
            "offset": 0, // Pull offset, whose initial value is 0. If you want to pull multiple times, the value must be the sum of the last offset and the value of the "max" field
            "max": 10 // Number of entries pulled at a time. The maximum: 50
        }
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
    "msg": "", //The specific error message when the "result" is not 0
    "total": 100, //The total number of templates in the App. It is valid when "result" is 0 
    "count": 3, //The number of returned information entries. The information content is in the "data" field. It is valid when "result" is 0
    "data": [
        {
            "id": 123, //Template ID
            "text": "xxxxx", //Template content
            "status": 0, //0: Approved; 1: Pending approval; 2: Rejected
            "reply": "xxxxx", //Approval information. If "status" is 2, the reason for rejection is provided
            "type": 0 //0: common SMS template; 1: marketing SMS template; 2: voice SMS template
        },...
    ]
}
```
