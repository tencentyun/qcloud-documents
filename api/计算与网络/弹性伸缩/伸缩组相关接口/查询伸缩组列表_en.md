## 1. API Description
This API (DescribeScalingGroup) is used to query the scaling group details. You can filter the results by scaling group ID, scaling group name, scaling configuration ID, etc.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeScalingGroup.

| Parameter Name | Required | Type | Description  
|---------|---------|---------|---------|
| scalingGroupIds.n  | No | String | An array of scaling group IDs to be queried. The array subscript starts from 0. If left empty, it means all scaling groups will be displayed. |
| scalingGroupName | No | String | The scaling group name to be queried. Passing the array of scaling group names is currently not supported.  | 
| scalingConfigurationId | No | String | The scaling configuration ID used by the scaling group to be queried, which specifies the template used when the CVM instance is automatically created by auto scaling. It can be queried by calling API <a href="/doc/api/372/查询启动配置" title="Query Scaling Configuration">Query Scaling Configuration</a> (DescribeScalingConfiguration). |
| offset | No | Int | Offset; default is 0.  | 
| limit | No | Int | The maximum number of scaling groups that can be queried at a time. Default is 20. |
| vpcId | No | String | VPC ID. If it is left empty, all the network scaling groups will be queried; 0 means basic network. To specify a VPC network, please fill in the unVpcId (unified ID of VPC) field returned in the API <a href="/doc/api/245/1372" title="Query VPC List">Query VPC List</a> (DescribeVpcEx). |
| projectId | No | String | Project ID. If it is left empty, the scaling groups of all projects will be queried. 0 means default project. To specify other projects, you can call API <a href="/doc/api/403/4400" title="Query Project List">Query Project List</a> (DescribeProject) to query. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | Output results. Scaling group list information returned for the query.  |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Number of scaling groups returned for the query.  |
| scalingGroupSet | Array | Set of scaling group information returned for the query.  |

scalingGroupSet contains information about a number of scaling groups, and the information about each scaling group is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingGroupId | String | Scaling group ID returned for the query.  | 
| scalingGroupName | String | Scaling group name returned for the query. | 
| scalingConfigurationId | String | Scaling configuration ID corresponding to the scaling group. | 
| scalingConfigurationName | String | Scaling configuration name corresponding to the scaling group. | 
| minSize | Int | The minimum size of the scaling group, that is, the minimum number of CVM instances in the scaling group. | 
| maxSize | Int | The maximum size of the scaling group, that is, the maximum number of CVM instances in the scaling group. | 
| createTime | String | Creation time of the scaling group. | 
| instanceNum | Int | The number of existing CVM instances of the scaling group. | 
| removePolicy | String | Remove policy for the scaling group <br>1. RemoveOldestInstance means removing the oldest instance in the scaling group. The oldest CVM instance in the scaling group will be first removed to scale down the group.  <br>2. RemoveNewestInstance means removing the newest instance in the scaling group. The newest CVM instance in the scaling group will be first removed to scale down the group. | 
| loadBalancerIdSet | Array | Information of the cloud load balancers bound to the scaling group. | 
| vpcId | Int | ID of the VPC to which the scaling group belongs. | 
| subnetIdSet | Array | Subnet information of scaling group. | 
| zoneIdSet | Array | Region information of scaling group. | 
| projectId | Int | Project ID of scaling group.  | 
| bInScalingActivity | Int | Whether the scaling group has scaling activity being performed (0: no scaling activity being performed; 1: scaling activity being performed)<br> Scaling up, scaling down, binding and unbinding the CVM will trigger the scaling activity, and the scaling group can only have one scaling activity in progress at the same time.

loadBalancerIdSet indicates Cloud Load Balancer information of the scaling group, and is composed of the following parameters: Empty parameter means Cloud Load Balancer is not used.

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Cloud Load Balancer status. | 
| loadBalancerId | String | ID of Cloud Load Balancer. | 
| owner | String | Account of Cloud Load Balancer owner. | 
| zoneId | Int | Region of Cloud Load Balancer. | 

subnetIdSet indicates subnet information of the scaling group, and is composed of the following parameters. Empty parameter means subnet is not used.

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Subnet status. | 
| subnetId | String | Subnet ID. | 
| owner | String | Account of subnet owner. | 
| zoneId | Int | Region of subnet. | 

zoneIdSet indicates zone information of the scaling group, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Status information. | 
| owner | String | Owner account. | 
| zoneId | Int | Region.  |

## 4. Error Codes
For common errors on this API, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupIds.0=asg-d4hmoms6
```

The following results will be returned:
```
{
    "code": 0,
    "message": "",
    "codeDesc":"Success",      
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
                "projectId": 0,
                "bInScalingActivity": 1
            }
        ]
    }
}
```
