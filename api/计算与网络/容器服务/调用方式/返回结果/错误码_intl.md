## Error Codes

Message field indicates a module-related error.
Example:
"message": "(100004) projectId is incorrect"
It consists of two parts - the string within () indicates the module error code, and the string following () is the error description.
Different modules may produce different errors. The user can identify the cause of error based on error description. <font style="color:red">The following table lists a number of common error codes. If you do not find the error code you want, please refer to the specific API description in API document.</font>


## Common Error Code ##


<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Module Error Code</b>
</th><th> <b>Error Message</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> 4000
</td><td> 10,000
</td><td> invalid request parameters
</td><td> The request parameters are invalid. This error is usually caused by the fact that the parameters are not set according to the API descriptions of CMQ Cloud API.
</td></tr>
<tr>
<td> 4000
</td><td> 10010
</td><td> lacked of required parameters
</td><td> Lacked of required parameters. Users should refer to the API descriptions of CMQ Cloud API to find which required parameters are missing.
</td></tr>
<tr>
<td> 4100
</td><td> 10030
</td><td> authentication failed
</td><td> Authentication failed. Possible reasons are as follows 1) The secret key that generated the signature algorithm is incorrect; 2) The <a hre="https://cloud.tencent.com/doc/api/431/5906">signature algorithm</a> is incorrect (users try to implement the signature algorithm by themselves instead of using the official sdk).
</td></tr>
<tr>
<td> 4300
</td><td> 10040
</td><td> charge overdue
</td><td> Charge overdue.
</td></tr>
<tr>
<td> 6000
</td><td> 10050
</td><td> server internal error
</td><td> Internal server error. Generally, there will be a requestId returned to the user. Users can submit a ticket according to requestId to the technicians to locate the problem.
</td></tr>
<tr>
<td> 4100
</td><td> 10080
</td><td> secret id status error
</td><td> Secret id status error. The secret id may be disabled.
</td></tr>
<tr>
<td> 4000
</td><td> 10110
</td><td> request parameters error
</td><td> Request parameters error. This error is usually caused by the fact that the parameters are not set according to the API descriptions of CMQ Cloud API.
</td></tr>
<tr>
<td> 4420
</td><td> 10250
</td><td> qps throttling
</td><td> The qps reaches the maximum value, so it is restricted. In order to ensure the stability of background and call latency, the current maximum number of messages per second is 5,000. For customers with special requirements, customers can can submit a ticket for a larger one.
</td></tr>
<tr>
<td> 4100
</td><td> 10270
</td><td> secret id is not existed
</td><td> <a href="https://console.cloud.tencent.com/capi">The secret id</a> does not exist.
</td></tr>
<tr>
<td> 4000
</td><td> 10280
</td><td> action is not existed
</td><td> The parameter Action does not exist.
</td></tr>
<tr>
<td> 4000
</td><td> 10310
</td><td> error: parameter key format error"
</td><td> The parameter format is incorrect.
</td></tr>
<tr>
<td> 4000
</td><td> 10320
</td><td> no such parameter
</td><td> There is no such parameter.
</td></tr>
<tr>
<td> 4000
</td><td> 10330
</td><td> parameter is NOT a repeatable parameter
</td><td> The parameter is not a repeatable parameter. For example, in the batch APIs, BatchSendMessage and msgBody are repeatable parameters. In BatchDeleteMessage, receiptHandle is a repeatable parameter. If a parameter other than the repeatable parameters specified by each API is passed in the form of repeatable parameters, it will be treated as an error.
</td></tr>
<tr>
<td> 4000
</td><td> 10350
</td><td> parameter value or length is out of range
</td><td> Parameter value or length is out of range. For integers, this is usually a value error. For String parameters, it is a length error.
</td></tr>
<tr>
<td> 4000
</td><td> 10360
</td><td> parameter error type
</td><td> The parameter type is incorrect. For example, fill the integer as a string.
</td></tr>
<tr>
<td> 4000
</td><td> 10370
</td><td> parameter batch size is more than 16
</td><td> The batch value of batch API is more than 16.
</td></tr>
<tr>
<td> 4000
</td><td> 10380
</td><td> parameter is not consequent
</td><td> The subscripts of repeatable parameters are not consequent.
</td></tr>
<tr>
<td> 4000
</td><td> 10390
</td><td> lacked of required parameter
</td><td> Lacked of required parameter.
</td></tr>
<tr>
<td> 4000
</td><td> 10400
</td><td> cannot find parameter in uri
</td><td> Cannot find parameter in uri.
</td></tr>
<tr>
<td> 4000
</td><td> 10410
</td><td> unexpected http method, only GET or POST is supported
</td><td> Unexpected http method. Only GET or POST is supported. Due to the length restriction of GET, it is recommended to use POST.
</td></tr>
<tr>
<td> 4000
</td><td> 10420
</td><td> cannot parse
</td><td> Cannot parse http message.
</td></tr>
<tr>
<td> 4000
</td><td> 10430
</td><td> action name is not existed
</td><td> The API name specified by Action does not exist.
</td></tr>
<tr>
<td> 4000
</td><td> 10440
</td><td> account illegal, it may be an assistant account
</td><td> Account illegal. It may be an assistant account. Currently, CMQ does not support the operations of assistant account.
</td></tr>
<tr>
<td> 4000
</td><td> 10450
</td><td> secret id doesn't begin with AKID account
</td><td> The secret id doesn't begin with AKID account.
</td></tr>
<tr>
<td> 4480
</td><td> 10460
</td><td> exceed interface frequency limit, please slow down
</td><td> To protect the back-end system, the call frequency limit of control APIs (such as CreateQueue, DeleteQueue, etc.) is much lower than QPS. Therefore, when you see this error, please reduce the call frequency of control APIs.
</td></tr>
</tbody></table>

***
