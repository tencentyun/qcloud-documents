## 1. API Description
 
This API (ReturnIps) is used to release IPs of subnets in BM VPC.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>



 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is ReturnIps.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Both vpcId before the upgrade and unVpcId after the upgrade are supported.  |
| ips | Yes | Array | Array of released IPs.  |


 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |



  ## 4. Error Codes
 
 | Error Code | Error Message | Description |
|---------|---------|---------|
| -3047 |InvalidBmVpc.NotFound| Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct.  |

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=ReturnIps
	&<Public Request Parameters>
	&vpcId=vpc-2ari9m7h
	&ips.0=1.1.1.1&ips.1=2.2.2.2
	&count=1
```

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

```


