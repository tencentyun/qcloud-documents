## Error Codes
"message" field indicates errors related to modules.
Example:
"message": "(100004) incorrect projectId"
It consists of two parts - the string within () indicates the module error code, and the string following () is the error description.
Different modules may produce different errors. You can identify the cause of error based on error description.<font style="color:red">The common error codes are listed in the following table. Other error codes not listed here can be found in the specific API description of API document.</font>

## Common Error Codes

<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Module Error Code</b>
</th><th> <b>Error Message</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> 4000
</td><td> 10000
</td><td> invalid request parameters
</td><td> Request parameter is invalid. This is generally because the parameter is not specified according to the CMQ Cloud API description.
</td></tr>
<tr>
<td> 4000
</td><td> 10010
</td><td> lacked of required parameters
</td><td> Required parameter is missing. Find the missing required parameters by referring to the CMQ Cloud API description.
</td></tr>
<tr>
<td> 4100
</td><td> 10030
</td><td> authentication failed
</td><td> Authentication failed. The possible reasons are: (1) The secret key used in the generation of signature algorithm is incorrect; (2) <a hre="https://cloud.tencent.com/doc/api/431/5906">Signature algorithm</a> is incorrect (the signature algorithm implemented by users is used instead of official SDK).
</td></tr>
<tr>
<td> 4300
</td><td> 10040
</td><td> charge overdue
</td><td> Account is in arrears.
</td></tr>
<tr>
<td> 6000
</td><td> 10050
</td><td> server internal error
</td><td> Server internal error. Generally, requestId is returned to users, based on which users can submit a ticket to the technical support staff to locate the problem.
</td></tr>
<tr>
<td> 4100
</td><td> 10080
</td><td> secret id status error
</td><td>"secret id" status error. "secret id" may be disabled.
</td></tr>
<tr>
<td> 4000
</td><td> 10110
</td><td> request parameters error
</td><td> Incorrect request parameter. This is generally because the parameter is not specified according to the CMQ Cloud API description.
</td></tr>
<tr>
<td> 4420
</td><td> 10250
</td><td> qps throttling
</td><td> QPS is limited because it has reached the upper limit. To ensure backend stability and calling latency, the maximum QPS is 5k. Users with special requirements can submit a ticket to apply for more quota.
</td></tr>
<tr>
<td> 4100
</td><td> 10270
</td><td> secret id is not existed
</td><td> <a href="https://console.cloud.tencent.com/capi">The secret id </a>does not exist.
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
</td><td> Incorrect parameter format.
</td></tr>
<tr>
<td> 4000
</td><td> 10320
</td><td> no such parameter
</td><td> Such parameter does not exist.
</td></tr>
<tr>
<td> 4000
</td><td> 10330
</td><td> parameter is NOT a repeatable parameter
</td><td> The parameter is unique. In a batch API, such as BatchSendMessage, the parameter msgBody is repeatable. The parameter receiptHandle in BatchDeleteMessage is also repeatable. An error may occur if any parameter other than those specified to be repeatable in each API is passed as a repeatable parameter.
</td></tr>
<tr>
<td> 4000
</td><td> 10350
</td><td> parameter value or length is out of range
</td><td> The parameter value (Integer) or parameter length (String) exceeds the limit.
</td></tr>
<tr>
<td> 4000
</td><td> 10360
</td><td> parameter error type
</td><td> Incorrect parameter type. For example, a string is specified instead of an integer.
</td></tr>
<tr>
<td> 4000
</td><td> 10370
</td><td> parameter batch size is more than 16
</td><td> The batch value of batch API exceeds 16.
</td></tr>
<tr>
<td> 4000
</td><td> 10380
</td><td> parameter is not consequent
</td><td> The subscripts of repeatable parameters are not in sequential order.
</td></tr>
<tr>
<td> 4000
</td><td> 10390
</td><td> lacked of required parameter
</td><td> Required parameter is missing.
</td></tr>
<tr>
<td> 4000
</td><td> 10400
</td><td> cannot find parameter in uri
</td><td> Parameter cannot be found in URI.
</td></tr>
<tr>
<td> 4000
</td><td> 10410
</td><td> unexpected http method, only GET or POST is supported
</td><td> HTTP method is not supported. Currently, only GET and POST methods are supported. POST is recommended due to a limit on the length of GET request.
</td></tr>
<tr>
<td> 4000
</td><td> 10420
</td><td> cannot parse
</td><td> HTTP message cannot be resolved.
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
</td><td> Invalid account. It may be an assistant account. KMS does not support operations on an assistant account.
</td></tr>
<tr>
<td> 4000
</td><td> 10450
</td><td> secret id doesn't begin with AKID account
</td><td> The secret id does not start with AKID.
</td></tr>
<tr>
<td> 4480
</td><td> 10460
</td><td> exceed interface frequency limit, please slow down
</td><td> To protect the backend system, the call frequency limit of control class APIs (such as CreateQueue, DeleteQueue) is much lower than QPS. Therefore, when this error occurs, reduce the call frequency of control class APIs.
</td></tr>
<tr>
<td> 4200
</td><td> 10461
</td><td> no cam authorization
</td><td> The sub-account is not authorized by root account to access this API or resource.
</td></tr>
</tbody></table>

***

##SCF Error Code##

<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Module Error Code</b>
</th><th> <b>Error Message</b>
</th><th> <b>Description</b>
</th></tr>

<tr>
<td>      4400
</td><td> 9003
</td><td> InvalidParameter
</td><td> Parameter Error
</td></tr>

<tr>
<td>      5100
</td><td> 9000
</td><td> SystemError
</td><td> System Error
</td></tr>

<tr>
<td>      4102
</td><td> 9002
</td><td> SecretidNotAuthAccessResource
</td><td> Unauthorized access to the resource
</td></tr>

<tr>
<td>      4000
</td><td> 9305
</td><td> InsufficientBalance
</td><td> Insufficient Balance
</td></tr>

</tbody></table>


