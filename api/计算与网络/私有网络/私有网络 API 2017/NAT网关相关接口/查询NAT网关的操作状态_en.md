## 1. API Description

This API (QueryNatGatewayProductionStatus) is used to query the production status of the NAT gateway
Domain for API request: vpc.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| billId | Yes | String | The order ID returned when creating the gateway.|


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded, other values: Failed |
| message | string | Error message |
| data.status | int | Production result: 0: Succeeded; 1: Failed; 2: In progress |
| data.errorCode | string | Error code |

## 4. Error Codes
 The API does not have a business error code. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>



## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=QueryNatGatewayProductionStatus
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&billId=2160000000
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
          "status":0,
          "errorCode":0
		}
}
```


