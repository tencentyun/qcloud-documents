## API Description
This API (DetachRolePolicy) is used to unbind a policy from a role.
Domain for API request: cam.api.qcloud.com

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| policyId | No | Int | Policy ID. Either policyId or policyName can be used as the input parameter. |
| policyName | No | String | Policy name. Either policyId or policyName can be used as the input parameter. |
| roleId | No | String | Role ID used to specify a role. Either roleId or roleName can be used as the input parameter. |
| roleName | No | String | Role name used to specify a role. Either roleId or roleName can be used as the input parameter. |

## Output Parameters
 
| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API.|
| codeDesc | String | Error description |

## Example 
Input
```
https://domain/v2/index.php?Action=DetachRolePolicy&policyId=296232
&roleId=4611686018427397919&<Common request parameters>
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

````

