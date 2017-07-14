## 1. API Description

This API (SetOutBandVPNAuthPwd) is used to set the password for the authenticated user of out-band VPN.
Domain for API request: bm.api.qcloud.com


This API has two logics, creation of a VPN authenticated user and setting of password for an authenticated user. Two calls involving different parameter values are needed for the execution of the two logics.

Creating a VPN authenticated user: You can first call API <a href="/doc/api/386/6679" title="Get Out-of-band VPN Information">Get Out-of-band VPN Information (GetOutBandVPNAuthInfo)</a> to obtain VPN information. If the returned value of GetOutBandVPNAuthInfo is "be_first = true", this API must be called and value of the input parameter CreateOrUpdate should be "create".

Setting password for an authenticated user: After creating a VPN authenticated user using this API, you can directly call this API to set a password.


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
<td> password
<td> Yes
<td> String
<td> VPN authentication password set by user. The password should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, and special characters (!, #, $, %, &, ^, *, ())


<tr>
<td> createOrUpdate
<td> Yes
<td> String
<td> The value is a string "create" or "update". <br>create: Create a VPN account for this appId. The creation is only needed when "be_first = true" is returned by <a href="/doc/api/386/6679" title="Get Out-of-Band VPN Information">GetOutBandVPNAuthInfo</a> API. <br>
update: Modify the password for the VPN authenticated account. This is on the condition that this API has been called for the creation of a VPN authenticated user
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
<td> null
<td> 
</tbody></table>


## 4. Error Codes

| Code | codeDesc | Description |
|------|------|------|
| 10004 | OperationDenied | No permission for the operation |
| 10100 | InternalError.ObAuthAccessError | An error occurred when accessing the authentication module |
| 10101 |InternalError.ObAuthError| An error is returned by authentication module |




## 5. Example
Input
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=SetOutBandVPNAuthPwd
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&password=tencent89
&createOrUpdate=update
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}
```


