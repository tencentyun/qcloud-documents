## 1. API Description
This API (CreateScalingGroup) is used to create new scaling groups.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) Scaling group and cloud load balancer instances must be in the same region and the same project.

2) A maximum of 20 scaling groups can be created for each project.

3) A scaling group can only correspond to one scaling configuration.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/Common Request Parameters" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is CreateScalingGroup.

| Parameter Name | Required | Type | Description | 
|---------|---------|---------|---------|
| scalingConfigurationId | Yes | String | The scaling configuration ID used by the scaling group to be created, which specifies the template used when the CVM instance is automatically created by auto scaling. It can be queried by calling API <a href="/doc/api/372/查询启动配置" title="Query Scaling Configuration">Query Scaling Configuration</a> (DescribeScalingConfiguration). |
| scalingGroupName | Yes | String | Scaling group name defined by the user. |
| minSize | Yes | Int | The minimum group size, that is, the minimum number of CVM instances in the scaling group, with the range of 0-30, no greater than maxSize. When the number of CVM instances in the scaling group is less than minSize, AS will automatically add CVM instance to make the current instance number in the scaling group equal to minSize.  |
| maxSize | Yes | Int | The maximum group size, that is, the maximum number of CVM instances in the scaling group, with the range of 0-30, no less than minSize. When the number of CVM instances in the scaling group is larger than maxSize, AS will automatically remove CVM instance to make the current instance number in the scaling group equal to maxSize. |
| removePolicy | Yes | String | Remove policy. Only two values are available: RemoveOldestInstance means removing the oldest instance in the scaling group, that is, the oldest CVM instance in the scaling group will be first removed if necessary; RemoveNewestInstance means removing the newest instance in the scaling group, that is, the newest CVM instance in the scaling group will be first removed if necessary. |  
| vpcId | Yes | String | VPC ID. 0 means basic network. To specify a VPC network, please fill in the unVpcId (unified ID of VPC) field returned in the API <a href="/doc/api/245/1372" title="Query VPC List">Query VPC List</a> (DescribeVpcEx). |
| zoneIds.n | No | String | Region ID of the scaling group. If vpcId is 0, this parameter is required. It can be queried by calling API [Query Availability Zone](https://cloud.tencent.com/document/api/213/1286) (DescribeAvailabilityZones). |
| loadBalancerIds.n | No | String | An array of IDs of cloud load balancers bound to the scaling group. You can call API <a href="/doc/api/244/查询云服务器关联的负载均衡实例" title="Query Cloud Load Balancer Instances">Query Cloud Load Balancer Instances</a> (DescribeLoadBalancersByInstances) to query. |
| subnetIds.n  | No | String |Subnet ID of scaling group. If vpcId is not 0, this parameter is required. It can be queried by calling API [Query Subnet List](https://cloud.tencent.com/document/api/215/1371) (DescribeSubnetEx). |
| projectId | No | String | Project ID. If not specified, 0 means default project. To specify other projects, you can call API <a href="/doc/api/403/4400" title="Query Project List">Query Project List </a>(DescribeProject) to query. |
| desiredCapacity | No | Int | Initial number of instances, that is, the number of CVMs when the scaling group is created|


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | Output result, displaying the information of newly created scaling group.  |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingGroupIdSet | Array | ID of the newly created scaling group.  | 

scalingGroupIdSet is a set that contains IDs of all the newly created scaling groups.
## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

| Error Code | Description |
|---------|---------|
| Conflict.MaxsizeLessMinsize | maxsize must be greater than minsize |
| InvalidParameter.ZoneIdError | Incorrect zoneId |
| InvalidParameter.VpcIdOrSubnetIdError | Incorrect vpcId or subnetId |
| Conflict.VpcIdVszoneId | vpc and zone cannot both specified |
| InvalidParameter.LoadBalancerIdError | Incorrect LbId |
| QuotaExceeded.ScalingGroup | Number of scaling groups allowed to be added has been exceeded |
| QuotaExceeded.ZoneId | Number of zoneId allowed to be added has been exceeded |
| QuotaExceeded.SubnetId | Number of subnetId allowed to be added has been exceeded |
| QuotaExceeded.LoadBalancerId | Number of lbId allowed to be added has been exceeded |
| NameDuplicate.ScalingGroup | The scaling group name already exists |
| Conflict.InsufficientBalance | Unable to create the scaling group due to insufficient balance |

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupName=xxxxx
&scalingConfigurationId=xxxxxx
&minSize=1
&maxSize=10
&vpcId=0
&removePolicy=RemoveOldestInstance
&zoneIds.0=100001
&loadBalancerIds.0=qlbxxxxx
```

Example of returned result is as follows. Only one scaling group is created, so the scalingGroupIdSet contains only one element.
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
    "data":{
        "scalingGroupIdSet":[
            "asg-hz5v140t"
        ]
    }
}
```


