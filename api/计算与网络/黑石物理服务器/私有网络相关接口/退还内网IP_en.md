## 1. API Description
 
The API (ReturnIps) is used to release the private IP of BM VPC.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>



 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is ReturnIps.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |
| ips | Yes | Array | Released IP arrays.  |


 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |



  ## 4. Error Codes
 
 | Error Code | Error Message | Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. The VPC resource does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmVpcEx
	&<Common request parameters>
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


