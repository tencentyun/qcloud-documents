## API Description

This API (ListPolicies) is used to query policy list.

Request domain name:

```
cam.api.qcloud.com 
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ------ | ---- | ------------------------------------------------------------ |
| page | int | No | Page number, which starts from 1 and cannot be greater than 200. Default is 1. |
| rp | int | No | Number of items on each page, which must be greater than 0 and less than or equal to 200. Default is 20. |
| scope | string | No | Available values: 'All', 'QCS' and 'Local'. 'All': All policies; 'QCS': Only preset policies; 'Local': Only custom policies. Default is 'All'. |
| keyword | string | No | Query by policy name |

## Output Parameters

| Parameter Name | Type | Description |
| -------- | ----- | ------------------------------------------------------------ |
| totalNum | int | Total number of policies |
| list | array | Policy array, of which each member contains the following fields: policyId, policyName, addTime, type, description and createMode. <br>policyId: Policy ID <br>policyName: Policy name <br>addTime: Time when a policy is created<br> type: 1: Custom policy; 2: Preset policy <br>description: Policy description <br>createMode: 1 indicates a policy created according to business permissions, while other values indicate you can view policy syntax and update a policy through the policy syntax. |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?page=1
&rp=20
&SignatureMethod=HmacSHA256
&Action=ListPolicies
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=6796
&Timestamp=1508485689
&RequestClient=SDK_PHP_1.1
&Signature=nq490ytZEB6hb6dFc%2BA1A56qDe743T%2FOEuuCctmXY08%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "list": [
            {
                "policyId": 1,
                "policyName": "AdministratorAccess",
                "addTime": "2016-06-02 19:40:09",
                "type": 2,
                "description": "This policy allows you to manage all users under your account and their permissions, financial information and Cloud assets.",
                "createMode": 2
            },
            {
                "policyId": 400411,
                "policyName": "ReadOnlyAccess",
                "addTime": "2017-09-01 15:57:54",
                "type": 2,
                "description": "This policy authorizes you with the read-only access to all Cloud assets in your account.",
                "createMode": 2
            },
            {
                "policyId": 2,
                "policyName": "QCloudResourceFullAccess",
                "addTime": "2016-06-02 19:40:23",
                "type": 2,
                "description": "This policy allows you to manage all Cloud assets in your account.",
                "createMode": 2
            },
            {
                "policyId": 3,
                "policyName": "QCloudFinanceFullAccess",
                "addTime": "2016-06-02 19:40:37",
                "type": 2,
                "description": "This policy allows you to manage all financial items in your account, such as making payment and issuing invoices.",
                "createMode": 2
            },
            {
                "policyId": 524252,
                "policyName": "QcloudAVCFullAccess",
                "addTime": "2017-10-20 10:59:24",
                "type": 2,
                "description": "Full read-write access to AVC",
                "createMode": 2
            },
            {
                "policyId": 439285,
                "policyName": "QcloudBeianFullAccess",
                "addTime": "2017-09-14 14:33:47",
                "type": 2,
                "description": "Full read-write access to ICP licensing",
                "createMode": 2
            },
            {
                "policyId": 399353,
                "policyName": "QcloudBMFullAccess",
                "addTime": "2017-09-01 11:55:26",
                "type": 2,
                "description": "Full read-write access to BM",
                "createMode": 2
            },
            {
                "policyId": 399424,
                "policyName": "QcloudBMReadOnlyAccess",
                "addTime": "2017-09-01 12:05:01",
                "type": 2,
                "description": "Read-only access to BM",
                "createMode": 2
            },
            {
                "policyId": 219186,
                "policyName": "QcloudCASFullAccess",
                "addTime": "2017-06-06 12:42:37",
                "type": 2,
                "description": "Full read-write access to CAS",
                "createMode": 2
            },
            {
                "policyId": 244866,
                "policyName": "QcloudCASReadOnlyAccess",
                "addTime": "2017-06-21 15:32:48",
                "type": 2,
                "description": "Read-only access to CAS",
                "createMode": 2
            },
            {
                "policyId": 419076,
                "policyName": "QcloudCCBFullAccess",
                "addTime": "2017-09-07 14:13:10",
                "type": 2,
                "description": "Full read-write access to CCB",
                "createMode": 2
            },
            {
                "policyId": 419081,
                "policyName": "QcloudCCBReadOnlyAccess",
                "addTime": "2017-09-07 14:13:36",
                "type": 2,
                "description": "Read-only access to CCB",
                "createMode": 2
            },
            {
                "policyId": 419082,
                "policyName": "QcloudCCRFullAccess",
                "addTime": "2017-09-07 14:14:12",
                "type": 2,
                "description": "Full read-write access to CCR",
                "createMode": 2
            },
            {
                "policyId": 419084,
                "policyName": "QcloudCCRReadOnlyAccess",
                "addTime": "2017-09-07 14:14:30",
                "type": 2,
                "description": "Read-only access to CCR",
                "createMode": 2
            },
            {
                "policyId": 304652,
                "policyName": "QcloudCCSFullAccess",
                "addTime": "2017-07-31 19:45:45",
                "type": 2,
                "description": "Full read-write access to CCS, including CCS access and relevant access to CVM, CLB, VPC and Cloud Monitor",
                "createMode": 2
            },
            {
                "policyId": 296232,
                "policyName": "QcloudCCSInnerFullAccess",
                "addTime": "2017-07-26 19:48:14",
                "type": 2,
                "description": "Full access to CCS",
                "createMode": 2
            },
            {
                "policyId": 296233,
                "policyName": "QcloudCCSReadOnlyAccess",
                "addTime": "2017-07-26 19:51:19",
                "type": 2,
                "description": "Read-only access to CCS",
                "createMode": 2
            },
            {
                "policyId": 450021,
                "policyName": "QcloudCLBFinanceAccess",
                "addTime": "2017-09-18 15:35:17",
                "type": 2,
                "description": "Access to financial items of CLB",
                "createMode": 2
            },
            {
                "policyId": 219850,
                "policyName": "QcloudCLBFullAccess",
                "addTime": "2017-06-07 11:51:54",
                "type": 2,
                "description": "Full read-write access to CLB",
                "createMode": 2
            },
            {
                "policyId": 219851,
                "policyName": "QcloudCLBReadOnlyAccess",
                "addTime": "2017-06-07 11:53:45",
                "type": 2,
                "description": "Read-only access to CLB",
                "createMode": 2
            }
        ],
        "totalNum": 71
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

