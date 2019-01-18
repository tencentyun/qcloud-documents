Common parameters are used for user identification and API authentication. Unless necessary, these parameters are not discussed in each API document. A request must contain these parameters to be initiated successfully.

<table class="t">
<tbody><tr>
<th> <b>Parameter name</b>
</th><th width="50"> <b>Required</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> Action
</td><td> Yes
</td><td> The name of the API for the desired operation. For example, if you want to call API<a href="/document/api/213/9388" title="Query List of Instances">Query List of Instances</a>, the Action parameter is DescribeInstances.
</td><td> String
</td></tr>
<tr>
<td> Region
</td><td> No
</td><td> Region parameter, which is used to identify the region to which the instance you want to work with belongs. The values for the region parameter are: <br>Beijing: ap-beijing, Guangzhou: ap-guangzhou, Shanghai: ap-shanghai, Hongkong: ap-hongkong, Toronto: na-toronto, Silicon Valley: na-siliconvalley, Singapore: ap-singapore, Shanghai Finance: ap-shanghai-fsi, Shenzhen Finance: ap-shenzhen-fsi, Guangzhou Open zone: ap-guangzhou-open. <br>Click to view all <a href="/doc/product/213/6091" title="Regions and Availability Zones">Regions and Availability Zones</a>. Click to view API <a href="/doc/api/213/9456" title="Query Region List">Query Region List</a>.<br><B>Notes: 1. TUnless otherwise specified in the API document, this parameter is required generally. <br>2. Some of the regions are under internal trial and are only available to certain users.</B>
</td><td> String
</td></tr>
<tr>
<td> Timestamp
</td><td> Yes
</td><td> The current UNIX timestamp that records the time at which the API request was initiated.
</td><td> UInt
</td></tr>
<tr>
<td> Nonce
</td><td> Yes
</td><td> A random positive integer that is used in conjunction with Timestamp to prevent replay attacks.
</td><td> UInt
</td></tr>
<tr>
<td> SecretId
</td><td> Yes
</td><td> The SecretId which is used for identifying identity and applied for on <a href="https://console.cloud.tencent.com/capi">Cloud API Key</a>. A SecretId corresponds to a unique SecretKey, which is used to generate the request Signature. For more information, please see <a href="/doc/api/372/4214" title="Signature Method">Signature Method</a>.
</td><td> String
</td></tr>
<tr>
<td> Signature
</td><td> Yes
</td><td> Request signature, which is used to verify the validity of the request. The signature must be calculated according to input parameters. For more information, please see <a href="/doc/api/372/4214" title="Signature Method">Signature Method</a>.
</td><td> String
</td></tr><tr>
<td> SignatureMethod
</td><td> No
</td><td> Signature method. Currently supported methods are HmacSHA256 and HmacSHA1. HmacSHA256 method is used only when the parameter is specified as HmacSHA256, otherwise HmacSHA1 is used to verify signatures. For more information, please see <a href="/doc/api/372/4214" title="Signature Method">Signature Method</a>.
</td><td> String
</td></tr><tr>
<td> Token
</td><td> No
</td><td> Token used for the temporary certificate. The token must be used together with the temporary key. A long-term key does not require a Token.
</td><td> String
</td></tr></tbody></table>

For example, if a user wants to query the CVM instance list for Guangzhou, the request link may be as follows:

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstances
&SecretId=xxxxxxx
&Region=ap-guangzhou
&Timestamp=1402992826
&Nonce=345122
&Signature=xxxxxxxx
&Version=2017-03-12
</pre>

Version is the required parameter for the version of the API DescribeInstances.

