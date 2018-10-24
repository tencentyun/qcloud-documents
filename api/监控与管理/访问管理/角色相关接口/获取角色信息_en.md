## API Description
This API (GetRole) is used to obtain the details of a specified role.
Domain for API request: cam.api.qcloud.com

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| roleId | No | String | Role ID used to specify a role. Either roleId or roleName can be used as the input parameter. |
| roleName | No | String | Role name used to specify a role. Either roleId or roleName can be used as the input parameter. |

 ## Output Parameters
 
| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| roleId | String | Role ID |
| roleName | String | Role name |
| policyDocument | String | Trust policy of the role |
| description | String | Role description |
| addTime | String | Creation time of the role |
| updateTime | String | Time when the role was last modified |

## Example
Input
```
https://domain/v2/index.php?Action=GetRole&roleName=testroleName323&<Common request parameters>
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "roleId": "4611686018427397919",
        "roleName": "testroleName323",
        "policyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"qcs\":[\"qcs::cam::uin/2385420691:root\"]}}]}",
        "description": "",
        "addTime": "2017-09-26 11:02:21",
        "updateTime": "2017-09-26 11:02:21"
    }
}

````

