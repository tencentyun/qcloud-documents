## 1. API Description
 
This API (ModifyVpcAttribute) is used to modify VPCs.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

Currently, only modification to the name in the VPC attributes is supported.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyVpcAttribute.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |
| vpcName | Yes | String | VPC name. You can specify any name you like, but its length should be limited to 60 characters. VPC name must be unique under the same region.  |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please refer to <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
 
 ## 4. Error Code List
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
 | Error Code | Description |
|---------|---------|
| InvalidVpcName | Invalid VPC name. You can specify any name you like, but its length should be limited to 60 characters.  |
| InvalidVpcName.InUse | The VPC name is already in use. The VPC name of the same developer within the same region must be unique.  |
| InvalidVpc.NotFound | Invalid vpc. The vpc resource does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpcAttribute
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
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


