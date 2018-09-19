## 1. API Description
 
This API (ModifyVpcAttribute) is used to modify VPCs.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

Currently, only modification to the name in the VPC attributes is supported.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyVpcAttribute.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |
| vpcName | Yes | String | VPC name. It should be within  60 characters. |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: success； other values: failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a>. |
| message | String | Module error message description depending on API. |
 
## 4. Error Codes
 The following error code list only provides the error codes for this API. For common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
 | Error Code | Description |
|---------|---------|
| InvalidVpcName | Invalid VPC name. It should be within  60 characters.  |
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered. |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpcAttribute
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-2ari9m7h
  &vpcName=vpcName1
</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


