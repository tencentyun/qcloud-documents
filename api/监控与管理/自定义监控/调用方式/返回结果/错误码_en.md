## 1. Common Error Codes
The error codes in the returned result indicate the result of the call to the cloud API. "code" is common error code, which applies to APIs of all modules. A code of 0 means the call succeeded. Other values means the call failed. If a call fails, you can find out the cause of the error and take appropriate actions based on the following table.

<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> 4000
</td><td> Invalid request parameter
</td><td> Required parameter is missing, or parameter value is not in a correct format. For relevant error message, please see the "message" field in error description.
</td></tr>
<tr>
<td> 4100
</td><td> Authentication failed
</td><td> Signature authentication failed. For more information, please see the Authentication section in the document.
</td></tr>
<tr>
<td> 4200
</td><td> Request expired
</td><td> The request has expired. For more information, please see the Request Validity Period section in the document.
</td></tr>
<tr>
<td> 4300
</td><td> Access denied
</td><td> Account is blocked or not within the user range of the API.
</td></tr>
<tr>
<td> 4400
</td><td> Quota is exceeded
</td><td> The number of requests exceeds the quota. For more information, please see the Request Quota section in the document.
</td></tr>
<tr>
<td> 4500
</td><td> Replay attack
</td><td> The Nonce and Timestamp parameters can ensure that each request is executed only once on the server. Therefore, the Nonce value cannot be the same as last one, and the difference between Timestamp and Tencent server time cannot be greater than 2 hours.
</td></tr>
<tr>
<td> 4600
</td><td> Protocol is not supported
</td><td> The protocol is not supported. For more information, please see the relevant document.
</td></tr>
<tr>
<td> 5000
</td><td> Resource does not exist
</td><td> The instance corresponding to resource ID does not exist, or the instance has been returned, or another user's resource is accessed.
</td></tr>
<tr>
<td> 5100
</td><td> Resource operation failed
</td><td> The operation performed on the resource failed. For detailed error message, please see the "message" field in error description. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> 5200
</td><td> Failed to purchase resource
</td><td> The resource purchase failed. This is may be caused by unsupported instance configuration or insufficient resource.
</td></tr>
<tr>
<td> 5300
</td><td> Failed to purchase resource
</td><td> The resource purchase failed because of insufficient balance.
</td></tr>
<tr>
<td> 5400
</td><td> Part of operations performed successfully
</td><td> Part of the batch operations have been performed successfully. For more information, please see the returned value of method.
</td></tr>
<tr>
<td> 5500
</td><td> User failed to pass identity verification
</td><td> Resource purchase failed because the user failed to pass identity verification.
</td></tr>
<tr>
<td> 6000
</td><td> Internal error on the server
</td><td> An internal error occurred on the server. Try again later or contact customer service personnel for help.
</td></tr>
<tr>
<td> 6100
</td><td> Not supported by the version
</td><td> This API is not supported in this version or the API is under maintenance. Note:  When this error occurs, first check whether the domain of the API is correct. Different modules may have different domains.
</td></tr>
<tr>
<td> 6200
</td><td> API is temporarily unavailable
</td><td> The API is under maintenance and is unavailable. Please try again later.
</td></tr></tbody></table>

## 2. Module Error Codes
"message" field indicates errors related to modules.
Example:
"message": "(- 514) Resource already exists"
It consists of two parts - the string within () indicates the module error code, and the string following () is the error description.
Different modules may produce different errors. You can identify the cause of error based on error description.


| Error Code | Error Description    | Error Message                                 |
| ---- | ---------- | ------------------------------------ |
| -503 | Incorrect request parameter     | InvalidParameter                     |
| -507 | Limit is exceeded       | OperationDenied.ExceedLimit          |
| -513 | DB operation failed     | InternalError.DBoperationFail        |
| -514 | Resource already exists       | OperationDenied.SourceAlreadyExists  |
| -509 | Incorrect combination of dimensions    | InvalidParameter.DimensionGroupError |
| -502 | Resource does not exist      | OperationDenied.SourceNotExists      |
| -515 | Operation is impossible because a sub-resource exists | OperationDenied.SubresourceExist     |
| -505 | Parameter is missing       | InvalidParameter.MissingParameter    |
