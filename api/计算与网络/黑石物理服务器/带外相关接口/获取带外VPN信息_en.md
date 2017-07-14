## 1. API Description

This API (GetOutBandVPNAuthInfo) is used to get authentication information of out-of-band VPN.
Domain for API request: <font style="color:red">bm.api.qcloud.com</font>


When you log in to VPN from the out-of-band SSL VPN client, you can enter the acquired information at the VPN client.


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
<td> Returned authInfo instance. For more information on its composition, please see below.
</tbody></table>

</b></th>authInfo is composed as follows:</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> vpnGwAddr
<td> String
<td> Gateway IP of out-of-band SSL VPN.
<tr>
<td> userName
<td> String
<td> Authenticated user name of out-of-band SSL VPN.
<tr>
<td> userGroup
<td> String
<td> The user group to which the authenticated user of out-of-band SSL VPN belongs. This corresponds to the domain information to be input at the out-of-band SSL VPN client.
<tr>
<td> be_first
<td> Bool
<td> Whether the userName returned in this API is used for the first time. 
 The value "True" indicates it is used for the first time. In this case, you need to call the API SetOutBandVPNAuthPwd with the input parameter createOrUpdate equaling "create" to create VPN authentication account for this appId; 
 The value "False" indicates SetOutBandVPNAuthPwd has been called for the creation of a VPN authentication account.
</tbody></table>


## 4. Error Codes

| Code |codeDesc| Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |
| 10004 | OperationDenied | No permission for the operation |
| 10100 | InternalError.ObAuthAccessError | An error occurred when accessing the authentication module |
| 10101 |InternalError.ObAuthError| An error is returned by authentication module |
| 10105 |InvalidResource.ObAuthNoConfig| Operation error. No VPN configuration information exists in the system for the user |


## 5. Example
Input
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=GetOutBandVPNAuthInfo
&<<a href="https://www.qcloud.com/doc/api/229/6976">common request parameters</a>>
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "authInfo": {
            "vpnGwAddr": "115.159.242.100:443",
            "userName": "1251001002",
            "userGroup": "bm1251001002",
            "be_first": false
        }
    }
}
```


