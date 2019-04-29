## Common Error Codes
The error codes in the returned result indicate the result of the call to a cloud API. "code" is common error code, which applies to APIs of all modules. A code of 0 means the call is successful. Other values mean the call fails. If a call fails, you can find out the cause of the error and take appropriate actions based on the following table.

<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> 4000
</td><td> Invalid request parameter
</td><td> Required parameter is missing, or parameter value is in an incorrect format. For relevant error message, please see the "message" field in error description.
</td></tr>
<tr>
<td> 4100
</td><td> Authentication failed
</td><td> Signature authentication failed. For more information, please see the "Authentication" section in the document.
</td></tr>
<tr>
<td> 4200
</td><td> Request expired
</td><td> The request has expired. For more information, please see the "Request Validity Period" section in the document.
</td></tr>
<tr>
<td> 4300
</td><td> Access denied
</td><td> Account is blocked or not within the user range of the API.
</td></tr>
<tr>
<td> 4400
</td><td> Quota exceeded
</td><td> The number of requests exceeds the quota limit. For more information, please see the "Request Quota" section in the document.
</td></tr>
<tr>
<td> 4500
</td><td> Replay attack
</td><td> The Nonce and Timestamp parameters ensure that each request is executed only once on the server. Therefore, the Nonce value cannot be the same as last one, and the difference between Timestamp and Tencent server time cannot be greater than 2 hours.
</td></tr>
<tr>
<td> 4600
</td><td> Unsupported protocol
</td><td> The protocol is not supported. For more information, please see the relevant document.
</td></tr>
<tr>
<td> 5000
</td><td> Resource does not exist
</td><td> The instance corresponding to the resource ID does not exist, or the instance has been returned, or another user's resource is accessed.
</td></tr>
<tr>
<td> 5100
</td><td> Operation on the resource failed
</td><td> The operation performed on the resource failed. For error message, please see the "message" field in error description. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> 5200
</td><td> Failed to purchase the resource
</td><td> The resource purchase failed. This may be caused by unsupported instance configuration or insufficient resource.
</td></tr>
<tr>
<td> 5300
</td><td> Failed to purchase the resource
</td><td> The resource purchase failed because of insufficient balance.
</td></tr>
<tr>
<td> 5400
</td><td> Some of operations successful
</td><td> Some of the batch operations were successful. For more information, please see the returned value of method.
</td></tr>
<tr>
<td> 5500
</td><td> User failed to pass identity verification
</td><td> Resource purchase failed because the user failed to pass identity verification.
</td></tr>
<tr>
<td> 6000
</td><td> Internal error with the server
</td><td> An internal error occurred with the server. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> 6100
</td><td> Not supported by the version
</td><td> This API is not supported in this version or is under maintenance. Note: When this error occurs, check whether the domain name for the API is correct. Domain name may vary with different modules.
</td></tr>
<tr>
<td> 6200
</td><td> API is unavailable
</td><td> The API is under maintenance and is unavailable. Try again later.
</td></tr></tbody></table>

## Module Error Codes
"message" field indicates errors related to modules.
Example:
"message": "(100004) incorrect projectId"
It consists of two parts - the string within () indicates the module error code, and the string following () is the error description.
Different modules may produce different errors. You can identify the cause of error based on error description.

