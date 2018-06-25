__1. API Description__ 
This API (ListAttachedRolePolicies) is used to obtain the list of policies associated to a role.
Request domain: cam.api.qcloud.com

__2. Input Parameters__ 
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| roleId | No | string | Role ID used to specify a role. Either roleId or roleName can be used as the input parameter. |
| roleName | No | string | Role name used to specify a role. Either roleId or roleName can be used as the input parameter. |
| page | Yes | int | Page number, starting from 1 |
| rp | Yes | int | Page size, cannot be greater than 200 |


 __3. Output Parameters__ 
 
| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| totalNum | int | Total number of policies |
| list | array | Policy array, of which each policy has the following fields: policyId (ID of the policy), policyName (name of the policy), addTime (time when the policy was created), description (descriptions of the policy), and createMode (1 indicates the policy is created according to business permissions, while other values indicate you can view policy syntax and update the policy through the policy syntax) |


 __4. Example__ 
Input
```
https://domain/v2/index.php?Action=ListAttachedRolePolicies&roleName=testRole&page=1&rp=10&<Common request parameters>
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalNum": 3,
        "list": [
            {
                "policyId": 524497,
                "policyName": "testpppName323",
                "addTime": "2017-10-20 17:26:16",
                "createMode": 2
            },
            {
                "policyId": 296232,
                "policyName": "QcloudCCSInnerFullAccess",
                "addTime": "2017-10-20 17:11:19",
                "createMode": 2
            },
            {
                "policyId": 219851,
                "policyName": "QcloudCLBReadOnlyAccess",
                "addTime": "2017-09-04 16:40:15",
                "createMode": 2
            }
        ]
    }
}

````
