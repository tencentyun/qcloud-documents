## 1. Service Address

The domain name for the Tencent Cloud LVB service is live.api.qcloud.com.

## 2. Communication Protocol
All the Tencent Cloud APIs communicate over HTTPS to provide high-security channels.

## 3. Request Methods
POST and GET requests are both supported, but cannot be used at the same time. If the GET method is used, the parameters are obtained from Querystring. If the POST method is used, the parameters are obtained from Request Body, and the parameters in the Querystring are ignored. The request parameters are organized in the same way in both types of requests. Generally, GET method is used. If the parameter strings are too long, POST method is used. For more information, please see the relevant API description.

## 4 Character Encoding
UTF-8 encoding is always used.


## 5. API Request Structure
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Description</b>
</th><th> <b>Notes</b>
</th></tr>
<tr>
<td> API entry
</td><td>The WebService entry for calling API
</td><td> https://live.api.qcloud.com/v2/index.php<br> 
</td></tr>
<tr>
<td> Common parameters
</td><td>The parameters common to all the APIs
</td><td>For more information, please see "6. Common Parameters" section in this document.
</td></tr>
<tr>
<td>Instruction name
</td><td>Name of the instruction to be executed by API, specified with Action.<br>
<p>For example, Action=CreateLVBChannel
</p>
</td><td>For more information on complete instructions, please see <a href="https://cloud.tencent.com/document/product/267/5664" title="API Overview">API Overview</a>
</td></tr>
<tr>
<td>Instruction parameters
</td><td>Parameters required for each specific instruction
</td><td>For more information, please see the API document of each instruction.
</td></tr></tbody></table>

## 6. Common Parameters
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
</td><td> Current Unix timestamp
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

