## 1. Common Error Code
The error code in the returned result indicates the result of user's call to the cloud API. code is common error code, which applies to APIs of all modules. A code of 0 means the call succeeded. Other values means the call failed. If the call fails, the user can find out the cause of the error based on the following table and take appropriate actions.

| Error Code | Error Type | Description |
|---|---|---|
| 4000 | Invalid request parameter | Mandatory parameters are missing, or the format of parameter values is incorrect. For more information on the error message, please see the message field in the error description. |
| 4100 | Authentication failed | Signature authentication failed. For more information, please see the Authentication section in the document. |
| 4200 | Request expired | Request has expired. For more information, please see the Request Validity section in the document. |
| 4300 | Access denied | The account is suspended or is not within the user range for the API. |
| 4400 | Quota exceeded | The number of requests has exceeded the quota limit. For more information, please see the Request Quota section in the document. |
| 4500 | Replay attack | The Nonce and Timestamp parameters of request can ensure that each request is executed only once on the server. Therefore, the Nonce should not be identical to the previous one. The time difference between the Timestamp and Tencent CVM should not be greater than 2 hours. |
| 4600 | Unsupported protocol | Protocol is not supported. Please refer to the document. |
| 5000 | Resource does not exist | The instance that the resource ID indicates does not exist, or the instance has been returned, or another user's resource is accessed. |
| 5100 | Resource operation failed | The operation performed on the resource failed. For more information on the error message, please see the message field in the error description. Try again later or contact customer service personnel for help. |
| 5200 | Failed to purchase resource | Failed to purchase resource. This may be caused by unsupported instance configuration, or insufficient resources. |
| 5300 | Failed to purchase resource | Failed to purchase resource because of insufficient balance. |
| 5400 | Part of operations performed successfully | Part of batch operations have been performed successfully. For more information, please see the returned value of the method. |
| 5500 | User failed to pass qualification verification | Failed to purchase resource, because user failed to pass the qualification verification. |
| 6000 | Internal error on the server | An internal error occurred on the server. Try again later or contact customer service personnel for help. |
| 6100 | Version is currently not supported | This API is not supported in this version or the API is under maintenance. Note: When this error occurs, first check whether the domain of the API is correct. Different modules may have different domains. |
| 6200 | API is temporarily unavailable | The API is being maintained. Please try again later. |

## 2. Module Error Code
Message field indicates a module-related error.
Example:
"message": "(100004) projectId is incorrect"
It consists of two parts - the string within () indicates the module error code, and the string following () is the error description.
Different modules may produce different errors. The user can identify the cause of error based on error description.
