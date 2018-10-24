## 1. Service Address

Tencent Cloud APIs are divided into different function modules, with each module accessed using a different domain name. For the specific domain names, please see the documents of APIs.

## 2. Communication Protocol

All the Tencent Cloud APIs achieve communication over HTTPS to provide high-security channels.

## 3. Request Methods

Both POST and GET methods are supported, but they cannot be used together. If the GET method is used, the parameters are obtained from Querystring. If the POST method is used, the parameters are obtained from Request Body, and the parameters in the Querystring are ignored. The rules for parameter formats are the same for both methods. Generally, GET method is used. If parameter strings are too long, POST method is used. For more information, please see the relevant API description.

## 4. Character Encoding

UTF-8 encoding is always used.

## 5. API Request Structure

<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Description</b>
</th><th> <b>Remarks</b>
</th></tr>
<tr>
<td> API entry
</td><td>The WebService entry for calling API
</td><td> https://[APIdomain]/v2/index.php<br> For specific domain names (APIdomain), please see the descriptions of APIs.
</td></tr>
<tr>
<td> Common parameters
</td><td>The parameters common to all the APIs
</td><td>For more information, please see <a href="/document/api/213/11650" title="Common Parameters">Common Parameters</a>.
</td></tr>
<tr>
<td>Instruction name
</td><td>Name of the instruction to be executed by API, specified with Action.<br>
<p>For example, Action=CreateLoadBalancer
</p>
</td><td>For more information on complete instructions, please see <a href="/document/api/213/10015" title="API Overview">API Overview</a>.
</td></tr>
<tr>
<td>Instruction parameters
</td><td>Parameters required for each specific instruction
</td><td>For more information, please see the API document of each instruction.
</td></tr></tbody></table>


