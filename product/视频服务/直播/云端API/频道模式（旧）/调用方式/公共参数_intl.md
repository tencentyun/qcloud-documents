Common parameters are used for user identification and API authentication. Unless necessary, these parameters will not be discussed in each API document. A request that comes with these parameters can be initiated successfully.

<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th><th width="50"> <b>Required</b>
</th></tr>
<tr>
<td> Action
</td><td> String
</td><td> Name of API instruction, for example: DescribeDomains
</td><td> Yes
</td></tr>
<tr>
<td> Region
</td><td> String
</td><td> Region parameter, which is used to identify the region to which the instance you want to work with belongs. Available values: <br>bj: Beijing<br>gz: Guangzhou<br>sh: Shanghai<br>hk: Hong Kong<br>ca: North America<br>

</td><td> Yes
</td></tr>
<tr>
<td> Timestamp
</td><td> UInt
</td><td> Current UNIX timestamp
</td><td> Yes
</td></tr>
<tr>
<td> Nonce
</td><td> UInt
</td><td> A random positive integer, which is used in conjunction with Timestamp to prevent replay attacks.
</td><td> Yes
</td></tr>
<tr>
<td> SecretId
</td><td> String
</td><td> SecretId and SecretKey used for identification and applied for through the Tencent Cloud platform. SecretKey is used to generate a Signature. <br>For more information, please see <a href="/doc/api/258/API Authentication" title="API Authentication">API Authentication</a> page.
</td><td> Yes
</td></tr>
<tr>
<td> Signature
</td><td> String
</td><td>Request signature, which is used to verify the validity of the request. <br>For more information, please see <a href="/doc/api/258/API Authentication" title="API Authentication">API Authentication</a> page.
</td><td> Yes
</td></tr></tbody></table>

The following shows a typical API request. "Action=DescribeInstance" indicates a query for the details of the CVM instance.

```
https://domain/v2/index.php?Action=DescribeInstances
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1402992826
&Nonce=345122
&Signature=mysignature
&instanceId=101
```
instanceId is an instruction parameter, and others are common parameters.

