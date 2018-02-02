## API Description 
This API (UpdateAssumeRolePolicy) is used to modify the trust policy of a role.
Domain for API request: cam.api.qcloud.com

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| policyDocument | Yes | String | Trust policy of the role |
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
https://domain/v2/index.php?Action=UpdateAssumeRolePolicy&roleName=testroleName
&policyDocument=%7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22action%22%3A%22name%2Fsts%3AAssumeRole%22%2C%22effect%22%3A%22allow%22%2C%22principal%22%3A%7B%22qcs%22%3A%5B%22qcs%3A%3Acam%3A%3Auin%2F909619400%3Aroot%22%5D%7D%7D%5D%7D&<Common request parameters>
```
The value of parameter policyDocument is: 
{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"qcs":["qcs::cam::uin/909619400:root"]}}]}

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

````

