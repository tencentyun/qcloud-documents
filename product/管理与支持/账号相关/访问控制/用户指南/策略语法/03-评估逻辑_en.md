When a Tencent Cloud user accesses cloud resource, CAM determines whether to allow or deny the request using the following evaluation logic.
    
1) All requests are denied by default.
    
2) CAM checks all policies associated with the current user.
     
a. Root accounts can access all resources under their names by default. Currently, cross-account resource access is only supported for COS products.
     
b. Certain general policies associate all CAM users by default. For more information, please see the General Policy table below.
     
c. Other policies need to be explicitly specified, including "allow" and "deny" policies.
    
3) If "deny" policy is matched, the result is determined as "deny", and the resource access request is denied.
    
4) If "allow" policy is matched, the result is determined as "allow", and the resource access request is allowed.
    
5) If no policy is matched, the result is determined as "deny", and the resource access request is denied.

![](https://mc.qcloudimg.com/static/img/b2bd42353bee28c55cc1bb1c3e8bb35d/395.png)


The following table contains general policies that are currently supported:

| Policy Description | Policy Definition |
|---|---|
| MFA verification is required for querying keys |{<br>"principal":"*",<br>"action":"name/account:QueryKeyBySecretId",<br>"resource":"*",<br>"condition":{"string_equal":{"mfa":"0"}}<br>}|
| MFA verification is required for sensitive configurations |{<br>"principal":"*",<br>"action":"name/account:SetSafeAuthFlag",<br>"resource":"*",<br>"condition":{"string_equal":{"mfa":"0"}}<br>}|
| MFA verification is required for binding tokens |{<br>"principal":"*",<br>"action":"name/account:BindToken",<br>"resource":"*",<br>"condition":{"string_equal":{"mfa":"0"}}<br>}|
| MFA verification is required for unbinding tokens |{<br>"principal":"*",<br>"action":"name/account:UnbindToken",<br>"resource":"*",<br>"condition":{"string_equal":{"mfa":"0"}}<br>}|
| MFA verification is required for modifying email address |{<br>"principal":"*",<br>"action":"name/account:ModifyMail",<br>"resource":"*",<br>"condition":{"string_equal":{"mfa":"0"}}<br>}|
| MFA verification is required for modifying phone number |{<br>"principal":"*",<br>"action":"name/account:ModifyPhoneNum",<br>"resource":"*",<br>"condition":{"string_equal":{"mfa":"0"}}<br>}|

