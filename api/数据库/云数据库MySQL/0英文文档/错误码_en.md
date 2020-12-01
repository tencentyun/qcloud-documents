## 1. Common Error Codes
The error codes returned represent the results for calling the cloud API. Code represents a common error code, which applies to all module APIs. 0 indicates successful calling and other values for calling failure. For calling failure, you can determine error causes according to the following table and take corresponding measures.

<table class="t">
<tbody><tr>
<th><b> Error Code </b>
</th><th><b> Error Type </b>
</th><th><b> Description </b>
</th></tr>
<tr>
<td> 4000
</td><td> Invalid request parameters
</td><td> Required parameters are missing, or parameter values are not in the correct format. See the message field of error description for specific error information.
</td></tr>
<tr>
<td> 4100
</td><td> Authentication failed
</td><td> Signature authentication failed. Refer to the authentication section in the document.
</td></tr>
<tr>
<td> 4200
</td><td> Request expired
</td><td> The request has expired. Refer to the validity request section in the document.
</td></tr>
<tr>
<td> 4300
</td><td> Access denied
</td><td> The account is blocked, or not in the user range of the API.
</td></tr>
<tr>
<td> 4400
</td><td> Quota exceeded
</td><td> The number of requests exceeded the quota. Refer to the request quota section of the document.
</td></tr>
<tr>
<td> 4500
</td><td> Playback attack
</td><td> The Nonce and Timestamp parameters of a request ensure that the request will be executed only once on the server, so two Nonce parameters cannot be repeated, and the Timestamp parameter cannot have a time difference of more than 2 hours from Tencent server.
</td></tr>
<tr>
<td> 4600
</td><td> Protocol not supported
</td><td> The protocol is not supported. Currently the API only supports the HTTPS protocol, but not HTTP.
</td></tr>
<tr>
<td> 5000
</td><td> Resource not existed
</td><td> The instance corresponding to the resource ID does not exist, or the instance has been returned, or the resource belong to other users.
</td></tr>
<tr>
<td> 5100
</td><td> Resource operation failed
</td><td> The resource operation failed. See the message field of error description for specific error information. Try again later or contact customer service personnel for help.
</td></tr>
<tr>
<td> 5200
</td><td> Resource purchase failed
</td><td> Failed to purchase the resource. Possible causes may be instance configuration not supported, insufficient resources and so on.
</td></tr>
<tr>
<td> 5300
</td><td> Insufficient balance
</td><td> Your account has insufficient balance to complete the purchase or upgrade.
</td></tr>
<tr>
<td> 5400
</td><td> Partial operations succeeded
</td><td> The batch operation is partially successful. See return values for details.
</td></tr>
<tr>
<td> 5500
</td><td> User qualification review failed
</td><td> The resources purchase failed, for you do not pass user qualification review.
</td></tr>
<tr>
<td> 6000
</td><td> Server error
</td><td> A server error occurred. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> 6100
</td><td> Version not supported
</td><td> The API is not supported on this version or is under maintenance. Note:  When this error occurs, make sure that the domain name of the API is correct. Different modules may have different domain names.
</td></tr>
<tr>
<td> 6200
</td><td> API inaccessible
</td><td> The current API is under maintenance. Please try again later.
</td></tr></tbody></table>

## 2. Module Error Codes
The message field indicates module-related errors.
Example:
"message": "(100004) projectId is incorrect"
It consists of two parts: the module error code is in () and specific error description after ().
Different modules may produce different errors. You can determine errors based on the specific error description.