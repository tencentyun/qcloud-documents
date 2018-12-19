## 1. Common Error Codes


If Error key exists in the returned result, it means the call to the API failed. The Code field under the Error indicates the error code. When the call fails, you can determine the cause of error and take appropriate actions based on the following table.

<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> InvalidParameter
</td><td>Invalid request parameter
</td><td>Required parameter is missing, or parameter value is in an incorrect format. For relevant error message, please see the "message" field in error description.
</td></tr>
<tr>
<td> InvalidParameter.SignatureFailure
</td><td> Authentication failed
</td><td> The failure of authentication is usually caused by signature computing error. Please see <a href="/document/api/213/6984" title="Signature Method">Signature Method</a> section in the document.
</td></tr>
<tr>
<td> AuthFailure
</td><td> Unauthorized access to the API
</td><td> The sub-account is not authorized by the main account to access the API. Contact the main account administrator to enable the permission for API.
</td></tr>
<tr>
<td> AuthFailure
</td><td> Unauthorized access to the resource
</td><td> The sub-account is not authorized by the main account to access the specific resource. Contact the main account administrator to enable the permission for resource.
</td></tr>
<tr>
<td> AuthFailure
</td><td> Unauthorized access to the resource the current API is working with.
</td><td> The sub-account is not authorized by the main account to access the specific resource the current API is working with. Contact the main account administrator to enable the permission for resource.
</td></tr>
<tr>
<td> InvalidParameter.SecretIdNotFound
</td><td> Key does not exist.
</td><td> The key used for the request does not exist. Please verify it and try again.
</td></tr>
<tr>
<td> InvalidRequest.TokenCheckFailed
</td><td> token error
</td><td> token error.
</td></tr>
<tr>
<td> InvalidRequest.MFACheckFailed
</td><td> MFA verification failed
</td><td> MFA verification failed.
</td></tr>
<tr>
<td> InternalError.CAMInnerError
</td><td> Other CAM authentication failed
</td><td> Other CAM authentication failed.
</td></tr>
<tr>
<td> InvalidRequest.Forbidden
</td><td>Access denied
</td><td>Account is blocked or not within the user range of the API.
</td></tr>
<tr>
<td> InvalidRequest.LimitExceeded
</td><td>Quota is exceeded
</td><td>The number of requests exceeds the quota limit. For more information, please see the Request Quota section in the document.
</td></tr>
<tr>
<td> InvalidRequest.ReplayAttack
</td><td>Replay attack
</td><td>The Nonce and Timestamp parameters can ensure that each request is executed only once on the server. Therefore, the Nonce value cannot be the same as last one, and the difference between Timestamp and Tencent server time cannot be greater than 5 hours.
</td></tr>
<tr>
<td> InvalidRequest.UnsupportedProtocol
</td><td> Unsupported protocol
</td><td> The protocol is not supported. The current API only supports HTTPS protocol and does not support HTTP protocol.
</td></tr>
<tr>
<td> InternalError.ResourceOpFailed
</td><td> Operation on the resource failed
</td><td>The operation performed on the resource failed. For error message, please see the "message" field in error description. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> InternalError
</td><td>Internal error on the server
</td><td>An internal error occurred with the server. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> InvalidAction.NotFound
</td><td>Not supported by the version
</td><td>The API is not supported by this version or is under maintenance. Note: When this error occurs, first check whether the domain name of the API is correct. Different modules may have different domain names.
</td></tr>
<tr>
<td> InvalidAction.ActionUnavailable
</td><td>API is temporarily unavailable
</td><td>The API is under maintenance and is unavailable. Please try again later.
</td></tr>
<tr>
<td> InvalidRequest.RequestConcurrencyExceeded
</td><td> Number of requests for the API exceeds the concurrency limit
</td><td> The number of requests for the current API exceeds the qps limit. Please try again later.
</td></tr>
</tbody></table>

