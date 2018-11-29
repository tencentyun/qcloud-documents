__1. API Description__ 
This API (DescribeRoleList) is used to obtain the details of a specified role.
Request domain: cam.api.qcloud.com

__2. Input Parameters__ 
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| page | Yes | int | Page number, starting from 1 |
| rp | Yes | int | Page size, cannot be greater than 200 |


 __3. Output Parameters__ 

| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| totalNum | int | Total number of roles under this owner |
| list | Array | Role list |

The following information is displayed for each role in the `list` field 
 
| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| roleId | string | Role ID |
| roleName | String | Role name |
| policyDocument | String | Trust policy of the role |
| description | String | Role description |
| roleId | string | Role ID |
| addTime | String | Creation time of the role |
| updateTime | String | Time when the role was last modified |


 __4. Example__ 
Input
```
https://domain/v2/index.php?Action=DescribeRoleList&page=1&rp=10&<Common request parameters>
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalNum": 2,
        "list": [
            {
                "roleId": "4611686018427397919",
                "roleName": "testroleName001",
                "policyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"qcs\":[\"qcs::cam::uin/888888888:root\"]}}]}",
                "description": "",
                "addTime": "2017-09-26 11:02:21",
                "updateTime": "2017-09-26 11:02:21"
            },
            {
                "roleId": "4611686018427397919",
                "roleName": "testroleName002",
                "policyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"qcs\":[\"qcs::cam::uin/12345678:root\"]}}]}",
                "description": "",
                "addTime": "2017-09-25 15:19:29",
                "updateTime": "2017-09-25 15:19:29"
            }
        ]
    }
}
````
