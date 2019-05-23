In order to help you get started with auto scaling (AS) API quickly, we provide an example on how to use it.
To use auto scaling, you need at least one scaling group, where the maximum and minimum number of CVM instances as well as other information are defined. For the automatic expansion of the scaling group, you need to set scaling configuration, which is the template for automatically creating CVM instances by auto scaling. Finally, to control the scaling activity of the scaling group, you need to create its alarm triggering policy, which is used to automatically perform a scaling activity according to cloud monitoring metrics (such as CPU, memory and network traffic).
Here, we first create a new scaling configuration, and then create a scaling group, which is bound to the scaling configuration created previously; finally, we create an alarm triggering policy for this scaling group so as to perform scaling activities under specific conditions.
## 1. Creating a New Scaling Configuration
Before creating a scaling group, we first need to determine its scaling configuration, which defines the configuration of a CVM instance automatically created through auto scaling. For more information on creating a scaling configuration, refer to [Create Scaling Configuration](/doc/api/372/创建启动配置) page.
Here we create a new scaling configuration, named mytest. A public image with ID of img-50mr2ow7 is used for CVM instances defined by this scaling configuration, which have a one-core CPU, a memory of 1 GB, a local disk of 10 G, and support a public network bandwidth of 1 Mbps billed by traffic. The relevant API request parameters are as follows:

| Parameter Name | Description | Value |
|---------|---------|---------|
| scalingConfigurationName | Name of the scaling configuration set by users.  | mytest |
| imageType | Image type. Only two values are available: A value of 1 indicates that it is a private image; A value of 2 indicates that it is a public image.  | 2 |
| imageId | Image ID. Please fill in the unImgId (unified ID of image) field returned by <a href="/doc/api/229/查询可用的镜像列表" title="/doc/api/229/查询可用的镜像列表">Query Image</a> (DescribeImages) API.  | img-50mr2ow7 |
| cpu | the number of CPU cores. Optional number of CPU cores vary with different regions. For more information, refer to [Create Scaling Configuration](/doc/api/372/创建启动配置) page.  | 1 |
| mem | Memory size in GB. Optional memory size vary with different regions. For more information, [Create Scaling Configuration](/doc/api/372/创建启动配置) page. | 1 |
| storageType | Data disk type. Only two values are available: 1 indicating a local disks, and 2 indicating cloud disks.  | 1 |
| storageSize | Size of data disk in GB. For local disks, the optional range is 0-500 G; for cloud disks, the optional range is 0-4000 G.  | 10 |
| bandwidthType | Bandwidth type. Only two values are available: PayByHour indicating charge by bandwidth usage time and PayByTraffic indicating charge by traffic.  | PayByTraffic |
| bandwidth | Public network bandwidth (in Mbps). 0 means that public network bandwidth is not enabled.  | 1 |

By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://scaling.api.qcloud.com/v2/index.php?
Action=CreateScalingConfiguration
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&scalingConfigurationName=mytest
&imageType=2
&imageId=img-50mr2ow7
&cpu=1
&mem=1
&storageType=1
&storageSize=10
&bandwidthType=PayByTraffic
&bandwidth=1
```
The result of the above request is as follows. It shows that the ID of the newly created scaling configuration is asc-a19qoqq4.

```
{
    "code": 0,
    "message": "",
    "data": {
        "scalingConfigurationIdSet": [
            "asc-a19qoqq4"
        ]
    }
}
```

## 2. Creating a New Scaling Group
With the scaling configuration, we can now create a scaling group. For more information on creating a scaling group, refer to [Create Scaling Group](/doc/api/372/创建伸缩组) page.
Here we create a new scaling group, named mytest. The ID of the scaling configuration that we newly created in the previous step with ID of asc-a19qoqq4 is used by this scaling group; the number of CVM instances in the scaling group ranges from 1 to 10. Instances in the scaling group will be increased or decreased whenever its number is not in the range, so that the requirement for the maximum and minimum group size can be met. In addition, the policy for removing the oldest instance is used by the scaling group, which means the oldest instance in the scaling group will be removed first if necessary; as for the network, the basic network in Guangzhou Zone 1 is used. The relevant API request parameters are as follows:

| Parameter Name | Description | Value |
|---------|---------|---------|
| scalingGroupName | Scaling group name defined by the user | mytest |
| scalingConfigurationId | Scaling configuration ID, which specifies the template used when the CVM instance is automatically created by auto scaling. It can be queried by calling API <a href="/doc/api/372/查询启动配置" title="Query Scaling Configuration">Query Scaling Configuration</a> (DescribeScalingConfiguration).  | asc-a19qoqq4 |
| minSize | The minimum group size, that is, the minimum number of CVM instances in the scaling group, with the range of 0-30, no greater than maxSize. When the number of CVM instances in the scaling group is less than minSize, AS will automatically add CVM instance to make the current instance number in the scaling group equal to minSize.  | 1 |
| maxSize | The maximum group size, that is, the maximum number of CVM instances in the scaling group, with the range of 0-30, no less than minSize. When the number of CVM instances in the scaling group is larger than maxSize, AS will automatically remove CVM instance to make the current instance number in the scaling group equal to maxSize.  | 10 |
| removePolicy | Remove policy. Only two values are available: RemoveOldestInstance means removing the oldest instance in the scaling group, that is, the oldest CVM instance in the scaling group will be first removed if necessary; RemoveNewestInstance means removing the newest instance in the scaling group, that is, the newest CVM instance in the scaling group will be first removed if necessary.  | RemoveOldestInstance |
| vpcId | ID of VPC. The default is 0, representing a basic network. This can be queried via the <a href="/doc/api/245/1372" title="Query Virtual Private Cloud List">Query Virtual Private Cloud List</a>(DescribeVpcEx) API.** Note: This parameter supports only unVpcId, i.e. the "unified VPC ID" (unVpcId) field returned by the query of a VPC list.**  | 0 |
| zoneIds.0 | Region ID of the scaling group. If vpcId is 0, this parameter is required. This can be queried via the <a href="/doc/api/229/查询可用区" title="Query Availability Zones">Query Availability Zones</a>(DescribeAvailabilityZones) API.  | 100001 |

By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://scaling.api.qcloud.com/v2/index.php?
Action=CreateScalingGroup
&Region=gz
&Timestamp=1465751551
&Nonce=30253
&SecretId=AKIDxxxxugEY
&Signature=RfnIGpdebvtEQ%2BiL2CrXt%2Bpkirc%3D
&scalingGroupName=mytest
&scalingConfigurationId=asc-a19qoqq4
&minSize=1
&maxSize=10
&removePolicy=RemoveOldestInstance
&vpcId=0
&zoneIds_0=100001
```
The result of the above request is as follows. It shows that the ID of the newly created scaling group is asg-8r4dvrek.

```
{
    "code": 0,
    "message": "",
    "data": {
        "scalingGroupIdSet": [
            "asg-8r4dvrek"
        ]
    }
}
```
## 3. Creating Alarm Triggering Policies for a Scaling Group
After creating the scaling group, you need to set its alarm triggering policy, to specify under which conditions it will automatically scale up or down so as to increase or decrease its CVM instances. For more information, refer to the [Create Alarm Triggering Policy](/doc/api/372/创建告警触发策略) page.
Here, we create an alarm triggering policy for the scaling group created above with ID of asg-8r4dvrek, and name it as mytest. The specific scaling policy is that when CPU usage is greater than or equal to 50%, auto scaling is triggered and 10 CVM instances are added. In addition, the alarm policy has a cooldown time of 300s, so that the scaling group cannot perform other scaling activities within 300s after one scaling activity is performed. The relevant API request parameters are as follows:

| Parameter Name | Description | Value |
|---------|---------|---------|
| scalingGroupId | ID of the scaling group for which the alarm triggering policy is to be created.  | asg-8r4dvrek |
| scalingPolicyName | Name of the user-defined alarm policy. | mytest |
|metric| Scaling policy, specific scaling policy taken. |{"dimensionName":"cpu_usage",<br>"comparisonOperator":"EqualOrGreater",<br>"threshold":50}|
| adjustmentType | Adjustment method of the scaling rule. Only 3 values are available:<br>TotalCapacity: Adjusting the number of instances in the current scaling group to the specified number. <br>QuantityChangeInCapacity: Increasing or decreasing the instances by specified number. <br>PercentChangeInCapacity: Increasing or decreasing instances by specified percentage. |QuantityChangeInCapacity|
| adjustmentValue | Adjustment value for the scaling rule. If it is negative, it means decreasing instances.  The value ranges of adjustmentValue are as follows:<br>TotalCapacity: 0-30<br>QuantityChangeInCapacity: -30-30<br>PercentChangeInCapacity: -100-100. |10|
| cooldown | Cooldown period (in seconds), a period of time when the corresponding scaling group is locked after a scaling activity is completed. During this period, this scaling group cannot execute other scaling activities. |300|

The metric here represents a scaling policy that when CPU usage is greater than or equal to 50%, auto scaling is triggered to increase or decrease corresponding CVMs.

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://scaling.api.qcloud.com/v2/index.php?
Action=CreateScalingPolicy
&Region=gz
&Timestamp=1465753286
&Nonce=45428
&SecretId=AKIDxxxx8ugEY
&Signature=rPKej10n%2BAW5%2FlM9P%2FsTyhrlFIk%3D
&scalingGroupId=asg-8r4dvrek
&scalingPolicyName=mytest
&adjustmentType=QuantityChangeInCapacity
&adjustmentValue=10
&cooldown=300
&metric=%7B%22dimensionName%22%3A%22cpu_usage%22%2C%22comparisonOperator%22%3A%22EqualOrGreater%22%2C%22threshold%22%3A50%7D
```
**Note: since Cloud APIs apply the GET request method by default, URL encoding needs to be performed on all parameters when the URL is generated.**
The result of the above request is as follows. It shows that the ID of the newly created alarm policy is asp-ofalm43w.

```
{
    "code": 0,
    "message": "",
    "data": {
        "scalingPolicyIdSet": [
            "asp-ofalm43w"
        ]
    }
}
```
Now, we have an auto scaling group. Its ID is asg-8r4dvrek, where the number of CVM instances can retain between 1 and 10. Its scaling configuration has the ID of asc-a19qoqq4. That means when the scaling group automatically scales up, CVM instances (which have a one-core CPU, a memory of 1 GB, a local disk of 10 G, and support a public network bandwidth of 1 Mbps billed by traffic) set by this scaling configuration will be increased. Its alarm policy has the ID of asp-ofalm43w so that when the overall CPU usage of the scaling group is greater than or equal to 50%, auto scaling is triggered and 10 CVM instances are added.


