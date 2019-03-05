## 1. Service Address

The domain name of the Tencent Cloud LVB service is live.api.qcloud.com.

## 2. Communication Protocol
All the Tencent Cloud APIs achieve communication over HTTPS to provide high-security channels.

## 3. Request Methods
The POST and GET methods are both supported, but cannot be mixed. If the GET method is used, parameters are obtained from the Querystring. If the POST method is used, parameters are obtained from the Request Body, and the parameters in the Querystring are ignored. Generally, GET method is used if the rules for parameter formats are the same for both methods. POST method is used if the parameter strings are too long. For more information, please see corresponding API description.

## 4. Character Encoding
UTF-8 encoding is used.


## 5. API Request Structure
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Description</b>
</th><th> <b>Note</b>
</th></tr>
<tr>
<td> API entry
</td><td> The WebService entry for API calling
</td><td> https://live.api.qcloud.com/v2/index.php<br> 
</td></tr>
<tr>
<td> Common parameters
</td><td> Common parameters included in each API
</td><td> For more information, please see section 6 "Common Parameters"
</td></tr>
<tr>
<td> Instruction name
</td><td> Name of the instruction to be executed by API, which is specified by Action.<br>
<p>For example, Action=CreateLVBChannel
</p>
</td><td> For more information on complete instructions, please see <a href="https://cloud.tencent.com/document/product/267/5664" title="API概览">API Overview</a>
</td></tr>
<tr>
<td> Instruction parameters
</td><td> Parameters required for each specific instruction
</td><td> For more information, please see the API document of each instruction.
</td></tr></tbody></table>

## 6. Common Parameters
Common parameters are used for user identification and API authentication. Unless necessary, these parameters are not discussed in each API document. A request must contain these parameters to be initiated successfully.

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
</td><td> Region parameter, which is used to identify the region to which the instance you want to work with belongs. Available values: <br>bj:Beijing<br>gz:Guangzhou<br>sh:Shanghai<br>hk:Hong Kong<br>ca:North America<br>

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
</td><td> A random positive integer, which is used in conjunction with Timestamp to prevent replay attacks
</td><td> Yes
</td></tr>
<tr>
<td> SecretId
</td><td> String
</td><td> SecretId and SecretKey used for identification and applied for through the Tencent Cloud platform. SecretKey can be used to generate a Signature. <br>For more information, please see <a href="/doc/api/258/接口鉴权" title="API Authentication">API Authentication</a> page.
</td><td> Yes
</td></tr>
<tr>
<td> Signature
</td><td> String
</td><td> Request signature, which is used to verify the validity of a request. <br>For more information, please see <a href="/doc/api/258/接口鉴权" title="API Authentication">API Authentication</a> page
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

