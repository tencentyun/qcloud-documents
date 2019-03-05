Instruction return parameters are specific to each API. Different APIs support different instruction return parameters. Take <a href="/doc/api/372/查询伸缩组列表" title="查询伸缩组列表">Query Scaling Group List</a>(DescribeScalingGroup) as an example, the instruction return parameters are listed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code; 0: Succeeded; other values: Failed. For more information, refer to <a href="/doc/api/372/错误码" title="错误码">Error Code</a> page.
| message | String | Error message description depending on API |
| data | Array | Output result, scaling group list information queried |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Number of scaling groups returned for the query |
| scalingGroupSet | Array | Set containing scaling group information |

scalingGroupSet contains information about a number of scaling groups, and the information about each scaling group is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingGroupId | String | Scaling group ID | 
| scalingGroupName | String | Scaling group name | 
| scalingConfigurationId | String | Scaling configuration ID | 
| scalingConfigurationName | String | Scaling configuration name | 
| minSize | Int | Minimum group size | 
| maxSize | Int | Maximum group size | 
| createTime | String | Creation time of scaling group | 
| instanceNum | Int | Number of hosts | 
| removePolicy | String | Remove policy <br>1. RemoveOldestInstance means the oldest policy will be removed <br>2. RemoveNewestInstance means the latest policy will be removed | 
| loadBalancerIdSet | Array | Cloud Load Balancer information of scaling group | 
| vpcId | int | ID of the VPC to which the scaling group belongs | 
| subnetIdSet | Array | Subnet information of scaling group | 
| zoneIdSet | Array | Region information of scaling group | 
| projectId | Int | Project ID of scaling group | 

loadBalancerIdSet indicates Cloud Load Balancer information of the scaling group, and is composed of the following parameters: Empty parameter means Cloud Load Balancer is not used.

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Cloud Load Balancer status | 
| loadBalancerId | String | ID of Cloud Load Balancer | 
| owner | String | Account of Cloud Load Balancer owner | 
| zoneId | Int | Region of Cloud Load Balancer | 

subnetIdSet indicates subnet information of the scaling group, and is composed of the following parameters. Empty parameter means subnet is not used.

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Subnet status | 
| subnetId | String | Subnet ID | 
| owner | String | Account of subnet owner | 
| zoneId | Int | Region of subnet | 

zoneIdSet indicates zone information of the scaling group, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Status information | 
| owner | String | Owner account | 
| zoneId | Int | Region |


Take calling API via [Final Request](/doc/api/372/最终请求形式) as an example, the possible instruction return parameters when the call succeeds and fails are as follows:

## 1. Instruction Return Parameters When API Call Succeeds

If the API Call succeeds, the instruction return parameters will be in the following format:
```
{
	<Common return parameters>,
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

## 2. Instruction Return Parameters When API Call Fails
If the API call fails, no instruction return parameters will be included in the return result:
```
{
	<Common return parameters>,
}
```



