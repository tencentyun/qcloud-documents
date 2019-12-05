## 1. Common Error Code
The error code in the returned result indicates the result of user's call to the cloud API. `code` is common error code, which applies to APIs of all modules. If the code is 0, it means the call succeeds. If not, it means the call fails. If the call fails, the user can find out the cause of the error based on the following table and take appropriate actions.

<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> 4000
</td><td> Invalid request parameter
</td><td> Required parameters are missing, or parameter values​are not in the correct format. For specific error message, please see the message field in error description.
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
</td><td> Account is suspended or not within the user range of the API.
</td></tr>
<tr>
<td> 4400
</td><td> Quota exceed
</td><td> The number of requests exceeds the quota. For more information, please see the Request Quota section in the document.
</td></tr>
<tr>
<td> 4500
</td><td> Replay attack
</td><td> The Nonce and Timestamp parameters can ensure that each request will be executed only once on the server. Therefore, the Nonce value cannot be the same as last one, and the difference between Timestamp and Tencent server time cannot be greater than 2 hours.
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
</td><td> The operation performed on the resource failed. For specific error message, please see the message field in error description. Try again later or contact customer service personnel for help.
</td></tr>
<tr>
<td> 5200
</td><td> Failed to purchase resource
</td><td> Resource purchase failed. This may be caused by unsupported instance configuration or insufficient resource.
</td></tr>
<tr>
<td> 5300
</td><td> Failed to purchase resource
</td><td> Resource purchase failed because of insufficient balance.
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
</td><td> This API is not supported in this version or the API is under maintenance. Note: When this error occurs, first check whether the domain of the API is correct. Different modules may have different domains.
</td></tr>
<tr>
<td> 6200
</td><td> API is temporarily unavailable
</td><td> The API is under maintenance and is unavailable. Please try again later.
</td></tr></tbody></table>

## 2. Module Error Code
message field indicates errors related to modules.
Example:
"message": "(-514) Resource already exists"
It consists of two parts - the string within () indicates the module error code, and the string following () is the error description.
Different modules may produce different errors. The user can identify the cause of error based on error description.

| Error Code | Meaning       | Description                                 |
| ---- | ---------- | ------------------------------------ |
| -503 | Incorrect request parameter     | InvalidParameter                     |
| -507 | Limit has been exceeded       | OperationDenied.ExceedLimit          |
| -513 | DB operation failed     | InternalError.DBoperationFail        |
| -514 | Resource already exists       | OperationDenied.SourceAlreadyExists  |
| -509 | Incorrect combination of dimensions    | InvalidParameter.DimensionGroupError |
| -502 | Resource does not exist      | OperationDenied.SourceNotExists      |
| -515 | Unable to operate because a sub-resource exists | OperationDenied.SubresourceExist     |
| -505 | Parameter is missing       | InvalidParameter.MissingParameter    |


