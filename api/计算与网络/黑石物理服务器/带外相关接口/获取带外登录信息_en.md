## 1. API Description

This API (GetDeviceOutBandInfo) is used to get the out-of-band information of CPMs.
Domain for API request:<font style="color:red">bm.api.qcloud.com</font>

Get the out-of-band information of CPMs: Out-of-band username, password, and out-of-band IP information. This information is used for the out-of-band system for logging into CPMs.


## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> appId
<td> Yes
<td> Int
<td> Developer's appId
<tr>
<td> instanceId
<td> Yes
<td> String
<td> Unique ID of CPM instance
</tbody></table>


## 3. Output Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> data
<td> Object
<td> outbandInfo. For more information on its composition, please see below.
</tbody></table>

</b></th>Parameter outbandInfo is composed as follows:</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> dhcp_ip
<td> String
<td> Out-of-band IP.
<tr>
<td> password
<td> String
<td> Password of out-of-band system.
<tr>
<td> userName
<td> String
<td> Username of out-of-band system.
<tr>
<td> sn
<td> String
<td> Unique series No. of CPM.
</tbody></table>


## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |
| 10004 | OperationDenied | No permission for the operation |
| 10100 | InternalError.ObAuthAccessError | An error occurred when accessing the authentication module |
| 10101 |InternalError.ObAuthError| An error is returned by authentication module |
| 10105 |InvalidResource.ObAuthNoConfig| Operation error. No VPN configuration information exists in the system for the user |
| 10106 | InternalError.TocQueryError | Query for TOC out-of-band information failed |
| 11041 | InvalidInstanceId | No device information on this appId and instanceId can be found in the system |


## 5. Example
Input
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=GetDeviceOutBandInfo
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "outbandInfo": {
            "dhcp_ip": "100.68.134.36",
            "password": "h4vBbEz9ocn8h8",
            "sn": "2102311HMK10G4000008",
            "username": "albert"
        }
    }
}
```


