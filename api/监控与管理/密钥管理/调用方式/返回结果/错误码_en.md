# **Error Codes**
"message" field indicates errors related to modules.
Example:
"message": "(100004) incorrect projectId"
It consists of two parts - the string within () indicates the module error code, and the string following () is the error description.
Different modules may produce different errors. You can identify the cause of error based on error description.<font style="color:red">The common error codes are listed in the following table. Other error codes not listed here can be found in the specific API description of API document.</font>


## Common Error Codes##


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
</td><td> Request parameter is invalid. This is generally because the parameter is not specified according to the KMS Cloud API description.
</td></tr>
<tr>
<td> 4000
</td><td> 10010
</td><td> lacked of required parameters
</td><td> Required parameter is missing. Find the missing required parameters by referring to the KMS Cloud API description.
</td></tr>
<tr>
<td> 4100
</td><td> 10030
</td><td> authentication failed
</td><td> Authentication failed. The possible reasons are: 1) the secret key used in the generation of signature algorithm is incorrect; 2) <a hre="https://cloud.tencent.com/doc/api/431/5906">Signature algorithm</a> is incorrect (the signature algorithm implemented by user is used instead of official SDK).
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
</td><td> Server internal error. Generally, requestId is returned to a user, based on which the user can submit a ticket to the technical support staff to locate the problem.
</td></tr>
<tr>
<td> 4100
</td><td> 10080
</td><td> secret id status error
</td><td> "secret id" status error. "secret id" may be disabled.
</td></tr>
<tr>
<td> 4000
</td><td> 10110
</td><td> request parameters error
</td><td> Incorrect request parameter. This is generally because the parameter is not specified according to the KMS Cloud API description.
</td></tr>
<tr>
<td> 4420
</td><td> 10250
</td><td> qps throttling
</td><td> QPS is limited because it has reached the upper limit. To ensure backend stability and calling latency, the maximum QPS is 5,000. Users with special requirements can submit a ticket to apply for more quota.
</td></tr>
<tr>
<td> 4100
</td><td> 10270
</td><td> key agent secret id is not exist
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
</td><td> The parameter must be unique.
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
</td><td> Incorrect parameter type. For example, integer is specified instead of a string.
</td></tr>
<tr>
<td> 4000
</td><td> 10370
</td><td> batch size of parameter is too large
</td><td> The batch value of batch API exceeds the upper limit.
</td></tr>
<tr>
<td> 4000
</td><td> 10380
</td><td> index of parameter is not consequent
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
</td><td> Parameter cannot be resolved.
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
</td><td> Invalid account. It may be an assistant account. Currently, KMS does not support the operations of assistant account.
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
</td><td> To protect the backend system, the call frequency limit of control APIs (such as ListKey, etc.) is much lower than QPS. Therefore, when you see this error, reduce the call frequency of control APIs.
</td></tr>
<tr>
<td> 4530
</td><td> 10630
</td><td> key is not existed
</td><td> The key does not exist, which means that CMK is not used. Check whether the key exists.
</td></tr>

<tr>
<td> 4550
</td><td> 10650
</td><td> key is disabled
</td><td> The key is disabled. Check whether the key is enabled.
</td></tr>
</tbody></table>

***


