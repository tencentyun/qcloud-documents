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
       For example: https://yun.tim.qq.com/v5/tlssmssvr/pullcallbackstatus?sdkappid=xxxxx&random=xxxx
      </td>
    </tr>
    <tr>
      <td>
        API description
      </td>
      <td>
      Pull the SMS report status in a certain period of time (the number of SMS messages submitted successfully, delivery reports, successful delivery reports, deleted delivery reports, and failure distribution)
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
    "begin_date": 2016090800, //Time to start pulling, which is accurate to hour. Format: yyyymmddhh
    "end_date": 2016090823 //Time to end pulling, which is accurate to hour. Format: yyyymmddhh
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
    "errmsg": "OK", //The specific error message when the "result" is not 0
    "data": { //It is valid when "result" is 0
        "success": 100, //SMS messages submitted successfully
        "status": 90, //Delivery reports
        "status_success": 80, //Successful delivery reports
        "status_fail": 10, //Deleted delivery report
        "status_fail_0": 2, //Operator's internal error
        "status_fail_1": 2, //Number is invalid or does not exist
        "status_fail_2": 2, //Out of service or powered off
        "status_fail_3": 2, //Blacklist
        "status_fail_4": 2 //Delivery frequency limit of operator
    }
}
```
