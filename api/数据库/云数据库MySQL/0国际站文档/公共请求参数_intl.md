Common request parameters are the request parameters that are used by every API. Unless it is necessary, these parameters will not be described in the separate documents for each API. However, <font style="color:red">they need to be included in each request</font>. The first letter of common request parameters are capitalized, to distinguish them from API request parameters.

Common request parameters are listed below:

<table class="t">
<tbody><tr>
<th><b> Parameter </b>
</th><th width="50"><b>Required</b>
</th><th><b> Description </b>
</th><th><b> Type </b>
</th></tr>
<tr>
<td> Action
</td><td> Yes
</td> <td> The API name to be called. For example, if you want to call the <a href="/document/product/236/1266" title="DescribeInstances">DescribeCdbInstances</a> API, then the Action parameter is DescribeInstances.
</td><td> String
</td></tr>
<tr>
<td> Region
</td><td> No
</td><td> This parameter indicates the region you want to operate the instances. The values for the region parameter are: <br>Beijing:ap-beijing, Guangzhou:ap-guangzhou, Shanghai:ap-shanghai, Hong Kong:ap-hongkong, Toronto:na-toronto, Silicon Valley:na-siliconvalley, Singapore:ap-singapore, Shanghai Finance:ap-shanghai-fsi, Shenzhen Finance:ap-shenzhen-fsi, Guangzhou open zone: ap-guangzhou-open<br>Click to view all <a href="/doc/product/213/6091" title="Regions and Availability Zones">Regions and Availability Zones</a>，click to view <a href="/doc/api/213/9456" title="DescribeRegions">DescribeRegions</a> API introduce。<br><B> Note: 1. This parameter is required fot most cases. If it is not required, we will state that in the corresponding API doc. <br>2. Some regions are in trial period and only open for authorized users. </B>
</td><td> String
</td></tr>
<tr>
<td> Timestamp
</td><td> Yes
</td><td> Current UNIX timestamp, which records the time when an API request is originated.
</td><td> UInt
</td></tr>
<tr>
<td> Nonce
</td><td> Yes
</td><td> A random positive integer, used in conjunction with timestamp to prevent playback attacks.
</td><td> UInt
</td></tr>
<tr>
<td> SecretId
</td><td> Yes
</td><td> The SecretId that indicates the identity requested on the <a href="https://console.cloud.tencent.com/capi">Cloud API key</a>. A SecretId corresponds to a unique SecretKey, which is used to generate a request signature. For details, refer to the <a href="/doc/api/372/4214" title="签名方法">Signature Mode</a> page.
</td><td> String
</td></tr>
<tr>
<td> Signature
</td><td> Yes
</td><td> Request signature, used to verify the legitimacy of the request, the system automatically generated based on input parameters. For details, refer to the <a href="/doc/api/372/4214" title="签名方法">Signature Mode</a> page.
</td><td> String
</td></tr></tbody></table>

For example, if you want to query the CVM instance list in Guangzhou, the request link should be:

```
https://cdb.api.qcloud.com/v2/index.php?
Action=DescribeInstances
&SecretId=xxxxxxx
&Region=ap-guangzhou
&Timestamp=1465055529
&Nonce=59485
&Signature=mysignature
&<API request parameters>
```

A complete request requires two types of request parameters: public request parameters and API request parameters. Only the aforementioned six public request parameters are listed here. For more information about API request parameters, refer to the <a href="https://intl.cloud.tencent.com/document/product/236/6922" title="接口请求参数">API request parameters</a> section.
