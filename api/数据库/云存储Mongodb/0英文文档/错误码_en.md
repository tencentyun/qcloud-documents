The error code included in the response packet provides the summary of results of calling and execution of Tencent Cloud APIs.
Any error code other than 0 indicates the request is not properly executed. An error message describes the error in details. Users can come up with the API execution result based on the error code.
On some terminals, such as browsers, message in Chinese is displayed in Unicode and needs to be decoded.

**The following table lists the error codes that may be returned by Tencent Cloud APIs:**
<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> 4000
</td><td> Invalid request parameter
</td><td> Required parameter is missing, or parameter value is not in a correct format. For relevant error message, please see the message field in error description.
</td></tr>
<tr>
<td> 4100
</td><td> Authentication failed
</td><td> Signature authentication failed. Please see the Authentication section in the document.
</td></tr>
<tr>
<td> 4200
</td><td> Request expired
</td><td> The request has expired. Please see the Request Validity Period section in the document.
</td></tr>
<tr>
<td> 4300
</td><td> Access denied
</td><td> Account is blocked or not within the user range of the API.
</td></tr>
<tr>
<td> 4400
</td><td> Quota exceeded
</td><td> The number of requests exceeds the quota. For more information, please see the Request Quota section in the document.
</td></tr>
<tr>
<td> 4500
</td><td> Replay attack
</td><td> The Nonce and Timestamp parameters can ensure that each request will be executed only once on the server. Therefore, the Nonce value cannot be the same as last one, and the difference between Timestamp and Tencent server time cannot be greater than 2 hours.
</td></tr>
<tr>
<td> 4600
</td><td> Protocol not supported
</td><td> The protocol is not supported. For more information, please see the relevant document.
</td></tr>
<tr>
<td> 5000
</td><td> Resource not found
</td><td> The instance corresponding to resource ID does not exist, or the instance has been returned, or another user's resource is accessed.
</td></tr>
<tr>
<td> 5100
</td><td> Resource operation failed
</td><td> The operation performed on the resource failed. For relevant error message, please see the message field in error description. Try again later or contact customer service personnel for help.
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
</td><td> Identity verification failed
</td><td> Unable to purchase resource as the user failed to pass identity verification.
</td></tr>
<tr>
<td> 6000
</td><td> Internal server error
</td><td> An internal error occurred on the server. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> 6100
</td><td> Not supported by the version
</td><td> This API is not supported in this version or the API is under maintenance. Note: When this error occurs, first check whether the domain of the API is correct. Different modules may have different domains.
</td></tr>
<tr>
<td> 6200
</td><td> API temporarily unavailable
</td><td> The API is unavailable due to maintenance. Try again later.
</td></tr></tbody></table>
