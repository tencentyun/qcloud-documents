As described in [Description of Return Structure](/doc/api/372/返回结构简介), a complete return result of an API consists of [Common Return Parameters](/doc/api/372/公共返回参数) and [Instruction Return Parameters](/doc/api/372/指令返回参数). The common return parameters are returned each time the API is called, while the instruction return parameters are specific to each API.

Take calling [View Scaling Group List](/doc/api/372/查看伸缩组列表 )(DescribeScalingGroup) API via [Final Request](https://intl.cloud.tencent.com/document/product/377/8939) as an example, the possible return results when the call succeeds and fails are as follows:

## 1. Return Parameters When API Call Succeeds

If the API call succeeds, the final return parameters will include both common return parameters and instructions return parameters, the error code will be 0, and the message field for error information will be empty.

```
{
    "code": 0,
    "message": "",
    "data": {
        "totalCount": 1,
        "scalingGroupSet": [
            {
                "scalingGroupId": "asg-d4hmoms6",
                "scalingGroupName": "test",
                "scalingConfigurationId": "asc-hq6jo6h4",
                "scalingConfigurationName": "test",
                "minSize": 0,
                "maxSize": 1,
                "createTime": "2016-06-04 23:58:03",
                "instanceNum": 0,
                "removePolicy": "RemoveOldestInstance",
                "loadBalancerIdSet": [],
                "vpcId": 0,
                "subnetIdSet": [],
                "zoneIdSet": [
                    {
                        "status": 1,
                        "owner": "1251707795",
                        "zoneId": 100002
                    }
                ],
                "projectId": 0
            }
        ]
    }
}
```

## 2. Return Parameters When API Call Fails

If the API call fails, the final return parameters will only include common return parameters, the error code will not be 0, and the message field will displays detailed error information.

```
{
    "code": XXXX,
    "message": "(XXXX)XXXXX",
}
```





