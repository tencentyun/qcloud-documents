## 1. Service Address

The domain for the Tencent Cloud Redis Store (CRS) is vod.api.qcloud.com.

## 2. Communication Protocol
All the Tencent Cloud APIs achieve communication over HTTPS to provide high-security channels.

## 3. Request Methods
POST and GET requests are both supported, but cannot be used at the same time. If GET method is used, parameters are obtained from the Querystring. If POST method is used, parameters are obtained from the Request Body, and the parameters in the Querystring will be ignored. The rules for parameter formats are the same for both methods. Generally, GET method is used. If the parameter strings are too long, POST method is used. For more information, please see the relevant API description.

## 4. Character Encoding
UTF-8 encoding is always used.


## 5. API Request Structure
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Description</b>
</th><th> <b>Note</b>
</th></tr>
<tr>
<td> API entry
</td><td> The WebService entry for API call
</td><td> https://redis.api.qcloud.com/v2/index.php<br> 
</td></tr>
<tr>
<td> Common parameters
</td><td> Common parameters included in each API
</td><td> For more information, please see <a href="/doc/api/260/公共参数" title="Common Parameters">Common Parameters</a> page
</td></tr>
<tr>
<td> Instruction name
</td><td> Name of the instruction to be executed by API, which is specified by Action.<br>
<p>For example, Action = DescribeRedis
</p>
</td><td> For more information on complete instructions, please see <a href="/doc/api/260/API概览" title="API Overview">API Overview</a>
</td></tr>
<tr>
<td> Instruction parameters
</td><td> Parameters required for each specific instruction
</td><td> For more information, please see the API document of each instruction.
</td></tr></tbody></table>
