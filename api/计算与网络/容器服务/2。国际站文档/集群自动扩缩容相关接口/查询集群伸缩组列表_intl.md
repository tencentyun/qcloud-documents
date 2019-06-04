## API Description
 
This API (DescribeClusterAsg) is used to query the information of a cluster scaling group.

Domain name for API request:
```
ccs.api.qcloud.com
```
## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Description | Required | Type |
|---------|---------|---------|---------|
| clusterId | Cluster ID. Enter the clusterId field returned by the API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448) | No | String |
| autoScalingGroupId | Scaling group ID | No | String |
| status | Scaling group status. For more information, please see the status list. | No | String |
| offset | Offset. Default is 0. | No | Int |
| limit | The maximum number of entries outputted. Default is 20. | No | Int |

#### Status List

| Status | Description |
|---------|---------|
| disabled | Disabled |
| disabling | Disabling |
| enabled | Enabled |
| enabling | Enabling |
| updating | Updating |

## Output Parameters
 
| Parameter Name | Description | Type |
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int |
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |
| data | Scaling group information. Details are shown below. | Array |

"data" is composed as follows:

| Parameter Name | Description | Type |
|---------|---------|---------|
| totalCount | Total number of results | Int |
| asgInfo | List of scaling groups. Details are shown below. | Array |

Each scaling group in asgInfo is composed as follows:

| Field | Description | Type |
|---------|---------|---------|
| autoScalingGroupId | Scaling group ID | String |
| autoScalingGroupName | Scaling group name | String |
| clusterId | Cluster ID | String |
| status | Scaling group status | String |
| scaleDownEnabled | Whether to enable scale-down | Bool |
| minSize | The minimum size of a scaling group | Int |
| maxSize | The maximum size of a scaling group | Int |
| instanceNum | The number of CVMs in a scaling group | Int |
| desiredCapacity | The desired number of CVMs in a scaling group | Int |
| label | The label of the CVM in the scaling group | Array |
| launchConfigurationId | Launch configuration ID | String |
| launchConfigurationName | Launch configuration name | String |


## Example

### Input

```
  https://domain/v2/index.php?Action=DescribeClusterAsg
  &clusterId=cls-xxxxxxxx
  &autoScalingGroupId=asg-xxxxxxxx
  &status=enabled
  &offset=0
  &limit=20
  &other common parameters
```
### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCount": 1,
        "asgInfo": [
            {
                "autoScalingGroupId": "asg-xxxxxxxx",
                "autoScalingGroupName": "cls-xxxxxxxx-g1867619587",
                "clusterId": "cls-xxxxxxxx",
                "status": "enabled",
                "scaleDownEnabled": false,
                "label": [],
                "minSize": 0,
                "maxSize": 5,
                "instanceNum": 0,
                "desiredCapacity": 1,
                "launchConfigurationId": "asc-xxxxxxxx",
                "launchConfigurationName": "cls-xxxxxxxx-c123109984"
            }
        ]
    }
}

```

