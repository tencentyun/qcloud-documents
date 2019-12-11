## 1. 接口描述
本接口（DescribeAvailableCvmInstanceTypes）查看批量计算可用的CVM机型配置信息。
接口请求域名：batch.api.qcloud.com

## 2. 输入参数
| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| Version | String | 是 | API版本号 |
| Filters.N | array of Filter objects | 否 | 过滤条件，详见实例过滤条件表。 |

实例过滤条件表

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| zone | String | 否 | （过滤条件）按照可用区过滤。 |
| instance-family | String | 否 | （过滤条件）按照实例机型系列过滤。实例机型系列形如：S1、I1、M1等。 |

## 3. 输出参数
| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回RequestId。当用户调用接口失败找后台研发人员处理时需提供该RequestId。 |-|
| InstanceTypeConfigSet | array of InstanceTypeConfig objects | 实例机型配置列表。 |-|

```
# 输出样例
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM4",
                "CPU": 2,
                "Memory": 4
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM8",
                "CPU": 2,
                "Memory": 8
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM16",
                "CPU": 2,
                "Memory": 16
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.LARGE8",
                "CPU": 4,
                "Memory": 8
            }
        ],
        "RequestId": "2f1fd71e-95ab-4f10-8adb-895e99d33ff5"
    }
}
```

## 4. 错误码
错误码 | 描述
-----|------
CallCvmException | 调用CVM异常。
InvalidZoneMismatchRegion | 非法的zone名称。
InternalServerError | 内部服务错误。
