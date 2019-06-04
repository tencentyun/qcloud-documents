Common return parameters are the parameters that will be returned each time the cloud API is called. These parameters are discussed in the document for each API. Here's a list of common return parameters:

<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code when calling cloud API. A code of 0 means the API call succeeded. Other values means the call failed. For information, refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Error Codes">Error Codes</a> page.
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Detailed error message, which varies depending on different APIs.
</td></tr>
</tbody></table>

Take <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a>(DescribeScalingGroup) as an example, the possible common return parameters when the API call succeeds or fails are as follows:

## 1. Common Return Parameters When API Call Succeeds
If the API call succeeds, the common return parameters will be in the following format:
```
{
    "code":"0",
    "message":"",
		<Instruction return parameters>
}
```
An error code of 0 means the API call succeeded. In addition, since the API call succeeded, the message field for error information will be empty.

## 2. Common Return Parameters When API Call Fails
If the API call fails, the common return parameters will be in the following format:
```
{
    "code":"XXXX",
    "message":"(XXXX)XXXXX",
		<Instruction return parameters>
}
```
The error code is not 0, which means the API call failed. In addition, since the API call failed, the message field will display detailed error information.

