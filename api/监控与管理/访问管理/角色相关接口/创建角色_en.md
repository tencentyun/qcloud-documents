## API Description
This API (CreateRole) is used to create a role.
Domain for API request: cam.api.qcloud.com

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| policyDocument | Yes | String | Trust policy of the role |
| description | No | String | Role description |
| roleName | Yes | String | Role name |

## Output Parameters
 
| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| roleId | String | Role ID |

## Example
Input
```
https://domain/v2/index.php?Action=CreateRole&roleName=testroleName
&policyDocument=%7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22action%22%3A%22name%2Fsts%3AAssumeRole%22%2C%22effect%22%3A%22allow%22%2C%22principal%22%3A%7B%22qcs%22%3A%5B%22qcs%3A%3Acam%3A%3Auin%12345678%3Aroot%22%5D%7D%7D%5D%7D&<Common request parameters>
```
The value of parameter policyDocument is: 
{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"qcs":["qcs::cam::uin/12345678:root"]}}]}

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "roleId": "4611686018427397919"
    }
}

````

